"""
Phase 2.1: Database Integration - Streamlit App with PostgreSQL Backend

Supports both JSON (fallback) and PostgreSQL database storage.
Uses database for production, JSON for development/testing.
"""

import os
import logging
from typing import Optional, Dict, List, Any

import streamlit as st
# AI/ML Imports (Optional for basic platform run)
try:
    from langchain_openai import AzureOpenAI
    from langchain.chains import RetrievalQA
    AI_AVAILABLE = True
except ImportError:
    AI_AVAILABLE = False
    logging.warning("LangChain/AI modules not available (running in non-AI mode)")

# Core imports
from core.settings import settings
from core.logging_config import configure_logging
from core.safe_logging import mask_identifier
from core.validator import (
    authenticate_user,
    load_vector_db,
    save_chat_message,
    load_chat_history,
    audit_log,
    analytics_log,
    hash_password,
    DB_AVAILABLE
)
from core.analytics_dashboard import render_dashboard

# Optional Imports with new paths
try:
    from db.database import (
        init_database,
        add_user,
        get_user,
    )
    from db.db_migrations import run_migrations
except ImportError:
    pass # DB_AVAILABLE handled in core/validator.py

# Import visualization module
try:
    from visualizations.visualizations import (
        display_care_plan_dashboard,
        display_problem_assessment,
        display_intervention_analysis,
        display_health_indicators,
    )
    VISUALIZATIONS_AVAILABLE = True
except ImportError:
    VISUALIZATIONS_AVAILABLE = False

# Import ML modules
try:
    from ml.ml_dashboards import display_ml_analytics_dashboard
    from ml.ml_predictive import PatientOutcomePredictor
    from ml.ml_anomaly_detection import VitalSignsAnomalyDetector
    ML_AVAILABLE = True
except ImportError:
    ML_AVAILABLE = False
    logging.getLogger(__name__).warning("ML modules not available")


# ============================================
# LOGGING SETUP
# ============================================
configure_logging()
logger = logging.getLogger(__name__)

# ============================================
# STREAMLIT CONFIG
# ============================================
st.set_page_config(
    page_title="NHS Unified Nursing Validator (Phase 2.1 - DB)",
    page_icon="🔒",
    layout="wide",
)

logger.info(
    f"Starting NHS Nursing Validator - "
    f"Environment: {settings.APP_ENV}, Database: {settings.USE_DATABASE}"
)

# Constants
ROLE_PERMISSIONS = {
    "admin": ["validate", "view_history", "export", "manage_users", "analytics"],
    "nurse": ["validate", "view_history", "export", "analytics"],
    "clinician": ["validate", "view_history"],
}


def init_database_if_needed():
    """Initialize database on first run."""
    if settings.USE_DATABASE and DB_AVAILABLE:
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
            from core.safe_logging import log_exception_safe
            log_exception_safe(logger, "Database initialization failed", e)
            st.warning("Database connection failed - using local storage")


def _seed_default_users():
    """Seed default users into database if they don't exist."""
    if not DB_AVAILABLE:
        return

    # Get defaults from core settings/validator logic?
    # Or just use the env vars directly here since it's admin logic.
    users_to_seed = {
        "admin": {"password": settings.ADMIN_PASSWORD, "role": "admin"},
        "nurse": {"password": settings.NURSE_PASSWORD, "role": "nurse"},
        "clinician": {"password": settings.CLINICIAN_PASSWORD, "role": "clinician"}
    }

    for username, creds in users_to_seed.items():
        try:
            user = get_user(username)
            if user is None:
                password_hash = hash_password(creds["password"])
                add_user(username, password_hash, creds["role"])
                logger.info(f"Seeded user: {mask_identifier(username, 'user')}")
        except Exception as e:
            from core.safe_logging import log_exception_safe
            log_exception_safe(logger, "Could not seed user", e, level="warning")


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
                audit_log(username, "login")
                logger.info(f"User logged in: {username} ({role})")
                st.success(f"Welcome back, {username}!")
                st.rerun()
            else:
                st.error("❌ Invalid credentials")
                audit_log(username, "failed_login")

        st.markdown("---")
        st.markdown("### 📋 Credentials")
        if settings.is_production():
            st.info("Contact your administrator for credentials.")
        else:
            # Show hints in dev
            st.info(
                f"""
            **Nurse:**
            - Username: `nurse`
            - Password: Check `.env` (default: `{settings.NURSE_PASSWORD}`)

            **Clinician:**
            - Username: `clinician`
            - Password: Check `.env` (default: `{settings.CLINICIAN_PASSWORD}`)

            **Admin:**
            - Username: `admin`
            - Password: Check `.env` (default: `{settings.ADMIN_PASSWORD}`)
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
            audit_log(st.session_state.username, "logout")
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
            "`python scripts/harvest_fons.py && python scripts/ingest_fast.py`"
        )

    # Tab interface
    tabs = [
        "💬 Chat Assistant",
        "📋 Care Plan",
        "🔍 Problems",
        "💊 Interventions",
        "📈 Health Indicators",
    ]

    if ML_AVAILABLE:
        tabs.append("🔮 ML Analytics")
        
    if st.session_state.role == "admin":
        tabs.append("📊 Analytics")

    tabs.append("⚙️ Admin" if st.session_state.role == "admin" else "ℹ️ Info")

    selected_tabs = st.tabs(tabs)

    # ... [Existing Tabs] ...

    # Analytics Tab (Before Admin/Info)
    if "📊 Analytics" in tabs:
        # Find index dynamically or just check constraint
        idx = tabs.index("📊 Analytics")
        with selected_tabs[idx]:
            render_dashboard()

    # Chat Assistant (Tab 1)
    with selected_tabs[0]:
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
            analytics_log(
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
                if vector_db and AI_AVAILABLE:
                    try:
                        # Use AzureOpenAI with settings handled implicitly or explicitly if needed
                        # LangChain's AzureOpenAI usually picks up env vars if not passed,
                        # but we can pass them from settings if we want to be explicit.
                        # For now, relying on Env vars or what validator set up if possible,
                        # but RetrievalQA creates a new LLM instance usually.
                        llm = AzureOpenAI(
                            deployment_name=settings.AZURE_OPENAI_DEPLOYMENT,
                            api_version=settings.AZURE_OPENAI_API_VERSION,
                            api_key=settings.AZURE_OPENAI_API_KEY,
                            azure_endpoint=settings.AZURE_OPENAI_ENDPOINT
                        )
                        qa = RetrievalQA.from_chain_type(
                            llm=llm,
                            chain_type="stuff",
                            retriever=vector_db.as_retriever(),
                        )
                        response = qa.run(user_input)
                    except Exception as e:
                        from core.safe_logging import log_exception_safe
                        log_exception_safe(logger, "QA error", e)
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
                analytics_log(
                    st.session_state.username,
                    "chat",
                    "assistant_response",
                    {"length": len(response)},
                )

            st.rerun()

    # Care Plan (Tab 2)
    with selected_tabs[1]:
        st.markdown("## Care Plan Management")
        if VISUALIZATIONS_AVAILABLE and "admin" in st.session_state.get("role", ""):
            display_care_plan_dashboard()
        elif VISUALIZATIONS_AVAILABLE:
            st.info("Care Plan visualizations available for admin users")
        else:
            st.warning("Visualizations module not available")

    # Problem Assessment (Tab 3)
    with selected_tabs[2]:
        st.markdown("## Problem Assessment")
        if VISUALIZATIONS_AVAILABLE:
            display_problem_assessment()
        else:
            st.warning("Visualizations module not available")

    # Intervention Analysis (Tab 4)
    with selected_tabs[3]:
        st.markdown("## Intervention Analysis")
        if VISUALIZATIONS_AVAILABLE:
            display_intervention_analysis()
        else:
            st.warning("Visualizations module not available")

    # Health Indicators (Tab 5)
    with selected_tabs[4]:
        st.markdown("## Health Indicators")
        if VISUALIZATIONS_AVAILABLE:
            display_health_indicators()
        else:
            st.warning("Visualizations module not available")

    # ML Analytics (Tab 6, if available)
    if ML_AVAILABLE:
        with selected_tabs[5]:
            display_ml_analytics_dashboard()

    # Admin / Info (Last Tab)
    with selected_tabs[-1]:
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
                    f"**Environment:** {settings.APP_ENV}"
                )
                st.write(
                    f"**Database:** {'Enabled' if settings.USE_DATABASE else 'Disabled'}"
                )
                st.write(
                    f"**Vector DB:** "
                    f"{'Loaded' if vector_db else 'Not Available'}"
                )

            elif admin_option == "Database Info":
                st.subheader("Database Information")
                if DB_AVAILABLE and settings.USE_DATABASE:
                    st.code(
                        f"""
HOST: {settings.DB_HOST}
PORT: {settings.DB_PORT}
NAME: {settings.DB_NAME}
USER: {settings.DB_USER}
                    """
                    )
                else:
                    st.info("Database not configured")

            elif admin_option == "Backups":
                st.subheader("Database Backups")
                if DB_AVAILABLE:
                    st.info("Backup functionality available via db.db_migrations")
                    st.code(
                        """
# Create backup
from db.db_migrations import create_backup
backup_path = create_backup()

# List backups
from db.db_migrations import list_backups
backups = list_backups()

# Restore backup
from db.db_migrations import restore_backup
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
