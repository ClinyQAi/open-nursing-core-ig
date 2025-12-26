"""
Core validation logic module.
Contains authentication, RAG setup, and common validation routines.
"""
import os
import shutil
import hashlib
import logging
from typing import Optional, List, Dict, Any, Union

import streamlit as st
try:
    from langchain_openai import AzureOpenAI
    from langchain_openai import AzureOpenAIEmbeddings
    from langchain_chroma import Chroma
    from langchain.chains import RetrievalQA
    AI_AVAILABLE = True
except ImportError:
    AI_AVAILABLE = False
    # Define dummy classes or None to prevent NameError if used in type hints or default args
    AzureOpenAI = None
    AzureOpenAIEmbeddings = None
    Chroma = None
    RetrievalQA = None

from core.settings import settings

# Attempt to import DB modules
try:
    from db.database import (
        get_user,
        update_last_login,
        save_chat_message as db_save_chat_message,
        get_chat_history as db_get_chat_history,
        log_audit_event,
        log_analytics_event
    )
    DB_AVAILABLE = True
except ImportError:
    DB_AVAILABLE = False

logger = logging.getLogger(__name__)

def hash_password(password: str) -> str:
    """Hash a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def get_default_users() -> Dict[str, Dict[str, str]]:
    """Return default users from settings (in-memory)."""
    return {
        "admin": {
            "password": settings.ADMIN_PASSWORD,
            "role": "admin"
        },
        "nurse": {
            "password": settings.NURSE_PASSWORD,
            "role": "nurse"
        },
        "clinician": {
            "password": settings.CLINICIAN_PASSWORD,
            "role": "clinician"
        },
    }

def authenticate_user(username: str, password: str) -> Optional[str]:
    """
    Authenticate user against database (if enabled) or default in-memory users.
    Returns the role if successful, None otherwise.
    """
    if not username or not password:
        logger.warning("Invalid authentication attempt - empty credentials")
        return None

    # 1. Try Database
    if settings.USE_DATABASE and DB_AVAILABLE:
        try:
            user = get_user(username)
            if user:
                password_hash = hash_password(password)
                if user["password_hash"] == password_hash and user["is_active"]:
                    logger.info(f"User authenticated from database: {username}")
                    update_last_login(user["id"])
                    return user["role"]
                else:
                    logger.warning(
                        f"Failed auth for DB user: {username} "
                        "(invalid password or inactive)"
                    )
                    return None
        except Exception as e:
            from core.safe_logging import log_exception_safe
            log_exception_safe(logger, "Database authentication error", e)
            # Fall through to defaults if DB fails (optional behavior, strictly speaking should fail closed,
            # but legacy app.py allowed fallback. For security, maybe we should stop here if DB is configured.)
            # However, prompt implies 'Phase 2' supports fallback. I will keep fallback logic but log it.

    # 2. Fallback to Default Users
    defaults = get_default_users()
    if username in defaults:
        if defaults[username]["password"] == password:
            logger.info(f"User authenticated from defaults: {username}")
            return defaults[username]["role"]
        else:
            logger.warning(f"Failed auth for default user: {username}")
            return None

    logger.warning(f"User not found: {username}")
    return None

@st.cache_resource
def load_vector_db():
    """Load and cache ChromaDB vector database."""
    if not AI_AVAILABLE:
        logger.warning("AI modules not available - vector DB disabled")
        return None

    vector_db_path = settings.VECTOR_DB_PATH
    local_db_path = settings.LOCAL_DB_PATH

    if not os.path.exists(vector_db_path):
        logger.warning(f"Vector database not found at {vector_db_path}")
        return None

    if not os.path.exists(local_db_path):
        try:
            logger.info(f"Copying vector DB to {local_db_path}")
            shutil.copytree(vector_db_path, local_db_path, dirs_exist_ok=True)
        except Exception as e:
            from core.safe_logging import log_exception_safe
            log_exception_safe(logger, "Failed to copy vector DB", e)
            return None

    try:
        logger.debug("Loading embeddings...")
        embeddings = AzureOpenAIEmbeddings(
            azure_deployment=settings.EMBEDDING_MODEL,
            api_key=settings.AZURE_OPENAI_API_KEY,
            azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
            api_version=settings.AZURE_OPENAI_API_VERSION
        )
        logger.debug("Loading ChromaDB...")
        db = Chroma(persist_directory=local_db_path, embedding_function=embeddings)
        logger.info("Vector DB loaded successfully")
        return db
    except Exception as e:
        from core.safe_logging import log_exception_safe
        log_exception_safe(logger, "Failed to load vector DB", e)
        return None

def save_chat_message(username: str, role: str, content: str, chat_history_file: str = ".chat_history.json") -> bool:
    """Save chat message to database or JSON file."""
    # 1. Try Database
    if settings.USE_DATABASE and DB_AVAILABLE:
        try:
            user = get_user(username)
            if user:
                db_save_chat_message(user["id"], role, content)
                return True
        except Exception as e:
            from core.safe_logging import log_exception_safe
            log_exception_safe(logger, "Failed to save to database", e, level="warning")

    # 2. Fallback to JSON
    try:
        history_data = {}
        if os.path.exists(chat_history_file):
            import json
            with open(chat_history_file, "r") as f:
                history_data = json.load(f)

        if username not in history_data:
            history_data[username] = []

        history_data[username].append({"role": role, "content": content})

        import json
        with open(chat_history_file, "w") as f:
            json.dump(history_data, f, indent=2)
        return True
    except Exception as e:
        from core.safe_logging import log_exception_safe
        log_exception_safe(logger, "Failed to save chat history to file", e)
        return False

def load_chat_history(username: str, chat_history_file: str = ".chat_history.json") -> List[Dict[str, Any]]:
    """Load chat history from database or JSON."""
    # 1. Try Database
    if settings.USE_DATABASE and DB_AVAILABLE:
        try:
            user = get_user(username)
            if user:
                messages = db_get_chat_history(user["id"], limit=100)
                return [
                    {"role": msg["role"], "content": msg["content"]}
                    for msg in messages
                ]
        except Exception as e:
            from core.safe_logging import log_exception_safe
            log_exception_safe(logger, "Failed to load from database", e, level="warning")

    # 2. Fallback to JSON
    try:
        import json
        if os.path.exists(chat_history_file):
            with open(chat_history_file, "r") as f:
                history_data = json.load(f)
                return history_data.get(username, [])
    except Exception as e:
        from core.safe_logging import log_exception_safe
        log_exception_safe(logger, "Failed to load chat history from file", e, level="warning")

    return []

def audit_log(username: str, action: str, details: Optional[Dict] = None):
    """Log user action to database if available, otherwise just logger."""
    if settings.USE_DATABASE and DB_AVAILABLE:
        try:
            user = get_user(username)
            if user:
                log_audit_event(user["id"], action, changes=details)
        except Exception as e:
            from core.safe_logging import log_exception_safe
            log_exception_safe(logger, "Failed to log audit event to DB", e, level="warning")

    logger.info(f"AUDIT - User: {username}, Action: {action}, Details: {details}")

def analytics_log(username: str, event_type: str, event_name: str, data: Optional[Dict] = None):
    """Log analytics event."""
    if settings.USE_DATABASE and DB_AVAILABLE:
        try:
            user = get_user(username)
            if user:
                log_analytics_event(user["id"], event_type, event_name, data)
        except Exception as e:
            from core.safe_logging import log_exception_safe
            log_exception_safe(logger, "Failed to log analytics to DB", e, level="warning")
