"""
Phase 2.1: Database Integration - Streamlit App with PostgreSQL Backend

Supports both JSON (fallback) and PostgreSQL database storage.
Uses database for production, JSON for development/testing.
"""

import os
import shutil
import json
import logging
import hashlib
from datetime import datetime
from typing import Optional, Dict, List, Any

import streamlit as st
from dotenv import load_dotenv

from langchain_openai import AzureOpenAI
from langchain_openai import AzureOpenAIEmbeddings
from langchain_chroma import Chroma
from langchain.chains import RetrievalQA

# Try to import database modules (optional for fallback)
try:
    from database import (
        init_database,
        add_user,
        get_user,
        update_last_login,
        save_chat_message,
        get_chat_history,
        clear_chat_history,
        log_audit_event,
        log_analytics_event,
    )
    from db_migrations import run_migrations

    DB_AVAILABLE = True
except ImportError:
    DB_AVAILABLE = False
    logging.warning("Database modules not available - using JSON fallback")

# Import visualization module
try:
    from visualizations import (
        display_care_plan_dashboard,
        display_problem_assessment,
        display_intervention_analysis,
        display_health_indicators,
    )

    VISUALIZATIONS_AVAILABLE = True
except ImportError:
    VISUALIZATIONS_AVAILABLE = False

load_dotenv()

# ============================================
# LOGGING SETUP
# ============================================
log_level = os.getenv("LOG_LEVEL", "info").upper()
logging.basicConfig(
    level=getattr(logging, log_level, logging.INFO),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(os.getenv("LOG_FILE", "/tmp/nursing_validator.log")),
    ],
)
logger = logging.getLogger(__name__)

# ============================================
# STREAMLIT CONFIG
# ============================================
st.set_page_config(
    page_title="NHS Unified Nursing Validator (Phase 2.1 - DB)",
    page_icon="🔒",
    layout="wide",
)

# ============================================
# CONFIGURATION
# ============================================
VECTOR_DB_PATH = "chroma_db_fons"
LOCAL_DB_PATH = "/tmp/chroma_db_fons_fast"
EMBEDDING_MODEL = "text-embedding-ada-002"
CHAT_HISTORY_FILE = ".chat_history.json"
APP_ENV = os.getenv("APP_ENV", "development")
IS_PRODUCTION = APP_ENV == "production"
USE_DATABASE = os.getenv("USE_DATABASE", "true").lower() == "true"

logger.info(
    f"Starting NHS Nursing Validator - "
    f"Environment: {APP_ENV}, Database: {USE_DATABASE}"
)

# Default credentials (in production, migrate to database)
DEFAULT_USERS = {
    "admin": {"password": "admin2025", "role": "admin"},
    "nurse": {"password": "nurse2025", "role": "nurse"},
    "clinician": {"password": "clinician2025", "role": "clinician"},
}

ROLE_PERMISSIONS = {
    "admin": ["validate", "view_history", "export", "manage_users", "analytics"],
    "nurse": ["validate", "view_history", "export", "analytics"],
    "clinician": ["validate", "view_history"],
}


def hash_password(password: str) -> str:
    """Hash a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()


def init_database_if_needed():
    """Initialize database on first run."""
    if USE_DATABASE and DB_AVAILABLE:
        try:
            if not st.session_state.get("db_initialized", False):
                logger.info("Initializing database schema...")
                init_database()
                run_migrations()
                st.session_state.db_initialized = True
                logger.info("Database initialized successfully")

                # Seed default users into database
                _seed_default_users()
        except Exception as e:
            logger.error(f"Database initialization failed: {e}", exc_info=True)
            st.warning("Database connection failed - using local storage")


def _seed_default_users():
    """Seed default users into database if they don't exist."""
    if not DB_AVAILABLE:
        return

    for username, creds in DEFAULT_USERS.items():
        try:
            user = get_user(username)
            if user is None:
                password_hash = hash_password(creds["password"])
                add_user(username, password_hash, creds["role"])
                logger.info(f"Seeded user: {username}")
        except Exception as e:
            logger.warning(f"Could not seed user {username}: {e}")


@st.cache_resource
def load_vector_db():
    """Load and cache ChromaDB vector database."""
    if not os.path.exists(VECTOR_DB_PATH):
        logger.warning(f"Vector database not found at {VECTOR_DB_PATH}")
        return None

    if not os.path.exists(LOCAL_DB_PATH):
        try:
            logger.info(f"Copying vector DB to {LOCAL_DB_PATH}")
            shutil.copytree(VECTOR_DB_PATH, LOCAL_DB_PATH, dirs_exist_ok=True)
        except Exception as e:
            logger.error(f"Failed to copy vector DB: {e}", exc_info=True)
            return None

    try:
        logger.debug("Loading embeddings...")
        embeddings = AzureOpenAIEmbeddings(azure_deployment=EMBEDDING_MODEL)
        logger.debug("Loading ChromaDB...")
        db = Chroma(persist_directory=LOCAL_DB_PATH, embedding_function=embeddings)
        logger.info("Vector DB loaded successfully")
        return db
    except Exception as e:
        logger.error(f"Failed to load vector DB: {e}", exc_info=True)
        return None


def authenticate_user(username: str, password: str) -> Optional[str]:
    """Authenticate user against database or defaults."""
    if not username or not password:
        logger.warning("Invalid authentication attempt - empty credentials")
        return None

    try:
        # Try database first
        if USE_DATABASE and DB_AVAILABLE:
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

        # Fallback to default users
        if username in DEFAULT_USERS:
            if DEFAULT_USERS[username]["password"] == password:
                logger.info(f"User authenticated from defaults: {username}")
                return DEFAULT_USERS[username]["role"]
            else:
                logger.warning(f"Failed auth for default user: {username}")
                return None

        logger.warning(f"User not found: {username}")
        return None

    except Exception as e:
        logger.error(f"Authentication error: {e}", exc_info=True)
        return None


def load_chat_history(username: str) -> List[Dict[str, Any]]:
    """Load chat history from database or JSON."""
    if USE_DATABASE and DB_AVAILABLE:
        try:
            user = get_user(username)
            if user:
                logger.debug(f"Loading chat history from database for {username}")
                messages = get_chat_history(user["id"], limit=100)
                return [
                    {"role": msg["role"], "content": msg["content"]}
                    for msg in messages
                ]
        except Exception as e:
            logger.warning(f"Failed to load from database: {e}")

    # Fallback to JSON
    try:
        if os.path.exists(CHAT_HISTORY_FILE):
            with open(CHAT_HISTORY_FILE, "r") as f:
                history_data = json.load(f)
                return history_data.get(username, [])
    except Exception as e:
        logger.warning(f"Failed to load chat history: {e}")

    return []


def save_chat_message(username: str, role: str, content: str) -> bool:
    """Save chat message to database or JSON."""
    if USE_DATABASE and DB_AVAILABLE:
        try:
            user = get_user(username)
            if user:
                logger.debug(f"Saving message to database for {username}")
                save_chat_message(user["id"], role, content)
                return True
        except Exception as e:
            logger.warning(f"Failed to save to database: {e}")

    # Fallback to JSON
    try:
        history_data = {}
        if os.path.exists(CHAT_HISTORY_FILE):
            with open(CHAT_HISTORY_FILE, "r") as f:
                history_data = json.load(f)

        if username not in history_data:
            history_data[username] = []

        history_data[username].append({"role": role, "content": content})

        with open(CHAT_HISTORY_FILE, "w") as f:
            json.dump(history_data, f, indent=2)
        return True
    except Exception as e:
        logger.error(f"Failed to save chat history: {e}", exc_info=True)
        return False


def log_user_action(
    username: str, action: str, details: Optional[Dict] = None
) -> bool:
    """Log user action for audit trail."""
    if USE_DATABASE and DB_AVAILABLE:
        try:
            user = get_user(username)
            if user:
                log_audit_event(user["id"], action, changes=details)
                logger.debug(f"Logged action for {username}: {action}")
                return True
        except Exception as e:
            logger.warning(f"Failed to log action: {e}")

    logger.info(f"User action - {username}: {action}")
    return False


def log_analytics(
    username: str, event_type: str, event_name: str, data: Optional[Dict] = None
) -> bool:
    """Log analytics event."""
    if USE_DATABASE and DB_AVAILABLE:
        try:
            user = get_user(username)
            if user:
                log_analytics_event(user["id"], event_type, event_name, data)
                return True
        except Exception as e:
            logger.warning(f"Failed to log analytics: {e}")

    return False


def login_page():
    """Display login interface."""
    st.markdown(
        """
    <style>
    .login-container { max-width: 400px; margin: 100px auto; }
    .welcome-text { text-align: center; color: #1f77b4; }
    </style>
    """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.markdown("# 🔐 NHS Nursing Validator")
        st.markdown("### Secure Clinical Decision Support")

        username = st.text_input(
            "Username",
            key="login_username",
            help="Enter your username",
        )
        password = st.text_input(
            "Password", type="password", key="login_password", help="Enter password"
        )

        if st.button("🔓 Login", use_container_width=True):
            if not username or not password:
                st.error("Please enter both username and password")
                return

            role = authenticate_user(username, password)
            if role:
                st.session_state.authenticated = True
                st.session_state.username = username
                st.session_state.role = role
                log_user_action(username, "login")
                logger.info(f"User logged in: {username} ({role})")
                st.success(f"Welcome back, {username}!")
                st.rerun()
            else:
                st.error("❌ Invalid credentials")
                log_user_action(username, "failed_login")

        st.markdown("---")
        st.markdown("### 📋 Demo Credentials")
        st.info(
            """
        **Nurse:**
        - Username: `nurse`
        - Password: `nurse2025`

        **Clinician:**
        - Username: `clinician`
        - Password: `clinician2025`

        **Admin:**
        - Username: `admin`
        - Password: `admin2025`
        """
        )


def main_app():
    """Main application interface."""
    init_database_if_needed()

    # Sidebar
    with st.sidebar:
        st.markdown("### 👤 Current User")
        st.info(
            f"**{st.session_state.username}**\n\n"
            f"Role: *{st.session_state.role.upper()}*"
        )

        if st.button("🚪 Logout", use_container_width=True):
            log_user_action(st.session_state.username, "logout")
            st.session_state.authenticated = False
            st.session_state.username = None
            st.session_state.role = None
            logger.info("User logged out")
            st.rerun()

        st.markdown("---")
        st.markdown("### ⚙️ Settings")

        if "admin" in st.session_state.get("role", ""):
            if st.button("🔧 Admin Panel"):
                st.session_state.show_admin = True

    # Main content
    st.markdown("# 🔐 NHS Unified Nursing Validator")
    st.markdown("### Phase 2.1: Database Integration")

    # Check if vector DB is available
    vector_db = load_vector_db()
    if vector_db is None:
        st.warning(
            "⚠️ Vector database not found. Please run: "
            "`python harvest_fons.py && python ingest_fast.py`"
        )

    # Tab interface
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
        [
            "💬 Chat Assistant",
            "📋 Care Plan",
            "🔍 Problems",
            "💊 Interventions",
            "📈 Health Indicators",
            "⚙️ Admin" if st.session_state.role == "admin" else "ℹ️ Info",
        ]
    )

    with tab1:
        st.markdown("## Chat with Clinical Assistant")
        st.markdown(
            "Ask questions about nursing care, clinical guidance, "
            "and best practices."
        )

        if "chat_history" not in st.session_state:
            st.session_state.chat_history = load_chat_history(
                st.session_state.username
            )

        # Display chat history
        for message in st.session_state.chat_history:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Chat input
        user_input = st.chat_input("Ask a clinical question...")

        if user_input:
            log_analytics(
                st.session_state.username,
                "chat",
                "user_message",
                {"length": len(user_input)},
            )

            st.session_state.chat_history.append(
                {"role": "user", "content": user_input}
            )
            save_chat_message(
                st.session_state.username, "user", user_input
            )

            with st.chat_message("user"):
                st.markdown(user_input)

            with st.chat_message("assistant"):
                if vector_db:
                    try:
                        qa = RetrievalQA.from_chain_type(
                            llm=AzureOpenAI(),
                            chain_type="stuff",
                            retriever=vector_db.as_retriever(),
                        )
                        response = qa.run(user_input)
                    except Exception as e:
                        logger.error(f"QA error: {e}", exc_info=True)
                        response = (
                            f"Unable to process your question. "
                            f"Error: {str(e)}"
                        )
                else:
                    response = (
                        "Vector database not available. "
                        "Please set up the knowledge base."
                    )

                st.markdown(response)
                st.session_state.chat_history.append(
                    {"role": "assistant", "content": response}
                )
                save_chat_message(
                    st.session_state.username, "assistant", response
                )
                log_analytics(
                    st.session_state.username,
                    "chat",
                    "assistant_response",
                    {"length": len(response)},
                )

            st.rerun()

    with tab2:
        st.markdown("## Care Plan Management")
        if VISUALIZATIONS_AVAILABLE and "admin" in st.session_state.get("role", ""):
            display_care_plan_dashboard()
        elif VISUALIZATIONS_AVAILABLE:
            st.info("Care Plan visualizations available for admin users")
        else:
            st.warning("Visualizations module not available")

    with tab3:
        st.markdown("## Problem Assessment")
        if VISUALIZATIONS_AVAILABLE:
            display_problem_assessment()
        else:
            st.warning("Visualizations module not available")

    with tab4:
        st.markdown("## Intervention Analysis")
        if VISUALIZATIONS_AVAILABLE:
            display_intervention_analysis()
        else:
            st.warning("Visualizations module not available")

    with tab5:
        st.markdown("## Health Indicators")
        if VISUALIZATIONS_AVAILABLE:
            display_health_indicators()
        else:
            st.warning("Visualizations module not available")

    with tab6:
        if st.session_state.role == "admin":
            st.markdown("## 🔧 Admin Panel")
            admin_option = st.selectbox(
                "Select Admin Function",
                ["User Management", "System Status", "Database Info", "Backups"],
            )

            if admin_option == "User Management":
                st.subheader("User Management")
                if DB_AVAILABLE:
                    st.success("✅ Database Available")
                    st.info(
                        "Add/edit users through database migration"
                        " or command line"
                    )
                else:
                    st.warning("⚠️ Database not available")

            elif admin_option == "System Status":
                st.subheader("System Status")
                st.write(
                    f"**Environment:** {APP_ENV}"
                )
                st.write(
                    f"**Database:** {'Enabled' if USE_DATABASE else 'Disabled'}"
                )
                st.write(
                    f"**Vector DB:** "
                    f"{'Loaded' if vector_db else 'Not Available'}"
                )

            elif admin_option == "Database Info":
                st.subheader("Database Information")
                if DB_AVAILABLE and USE_DATABASE:
                    st.code(
                        f"""
HOST: {os.getenv('DB_HOST', 'localhost')}
PORT: {os.getenv('DB_PORT', '5432')}
NAME: {os.getenv('DB_NAME', 'nursing_validator')}
USER: {os.getenv('DB_USER', 'nursing_admin')}
                    """
                    )
                else:
                    st.info("Database not configured")

            elif admin_option == "Backups":
                st.subheader("Database Backups")
                if DB_AVAILABLE:
                    st.info("Backup functionality available via db_migrations.py")
                    st.code(
                        """
# Create backup
from db_migrations import create_backup
backup_path = create_backup()

# List backups
from db_migrations import list_backups
backups = list_backups()

# Restore backup
from db_migrations import restore_backup
restore_backup(backup_path)
                    """
                    )
        else:
            st.markdown("## ℹ️ Application Information")
            st.info(
                """
            ### NHS Unified Nursing Validator
            #### Phase 2.1: PostgreSQL Database Integration

            **Features:**
            - Multi-user authentication with role-based access
            - PostgreSQL backend with connection pooling
            - Chat history persistence in database
            - Comprehensive audit logging
            - Analytics event tracking

            **Your Role Permissions:**
            """
                + ", ".join(ROLE_PERMISSIONS.get(st.session_state.role, []))
            )


def main():
    """Main entry point."""
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        login_page()
    else:
        main_app()


if __name__ == "__main__":
    main()
