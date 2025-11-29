import os
import shutil
import json
import logging
from datetime import datetime
import streamlit as st
from dotenv import load_dotenv

from langchain_openai import AzureOpenAI
from langchain_openai import AzureOpenAIEmbeddings
from langchain_chroma import Chroma
from langchain.chains import RetrievalQA

# Import visualization module
try:
    from visualizations import (
        display_care_plan_dashboard,
        display_problem_assessment,
        display_intervention_analysis,
        display_health_indicators
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
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(
            os.getenv("LOG_FILE", "/tmp/nursing_validator.log")
        )
    ]
)
logger = logging.getLogger(__name__)

# ============================================
# STREAMLIT CONFIG
# ============================================
st.set_page_config(
    page_title="NHS Unified Nursing Validator (PRO)",
    page_icon="🔒",
    layout="wide"
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

logger.info(f"Starting NHS Nursing Validator - Environment: {APP_ENV}")

# Default credentials (in production, use a proper auth system)
DEFAULT_USERS = {
    "admin": {"password": "admin2025", "role": "admin"},
    "nurse": {"password": "nurse2025", "role": "nurse"},
    "clinician": {"password": "clinician2025", "role": "clinician"}
}

ROLE_PERMISSIONS = {
    "admin": ["validate", "view_history", "export", "manage_users"],
    "nurse": ["validate", "view_history", "export"],
    "clinician": ["validate", "view_history"]
}


@st.cache_resource
def load_vector_db():
    if not os.path.exists(VECTOR_DB_PATH):
        logger.warning(
            f"Vector database not found at {VECTOR_DB_PATH}"
        )
        return None
    if not os.path.exists(LOCAL_DB_PATH):
        try:
            logger.info(f"Copying vector DB to {LOCAL_DB_PATH}")
            shutil.copytree(
                VECTOR_DB_PATH,
                LOCAL_DB_PATH,
                dirs_exist_ok=True
            )
        except Exception as e:
            logger.error(f"Failed to copy vector DB: {e}", exc_info=True)
            return None
    try:
        logger.debug("Loading embeddings...")
        embeddings = AzureOpenAIEmbeddings(
            azure_deployment=EMBEDDING_MODEL
        )
        logger.debug("Loading Chroma database...")
        return Chroma(
            persist_directory=LOCAL_DB_PATH,
            embedding_function=embeddings
        )
    except Exception as e:
        logger.error(f"Failed to load vector DB: {e}", exc_info=True)
        return None


def load_chat_history(username):
    """Load chat history for a specific user."""
    try:
        if os.path.exists(CHAT_HISTORY_FILE):
            with open(CHAT_HISTORY_FILE, 'r') as f:
                all_history = json.load(f)
                logger.debug(f"Loaded chat history for {username}")
                return all_history.get(username, [])
    except json.JSONDecodeError as e:
        logger.error(
            f"Failed to parse chat history: {e}",
            exc_info=True
        )
    except Exception as e:
        logger.error(
            f"Failed to load chat history: {e}",
            exc_info=True
        )
    return []


def save_chat_history(username, history):
    """Save chat history for a specific user."""
    try:
        all_history = {}
        if os.path.exists(CHAT_HISTORY_FILE):
            with open(CHAT_HISTORY_FILE, 'r') as f:
                all_history = json.load(f)
        all_history[username] = history
        with open(CHAT_HISTORY_FILE, 'w') as f:
            json.dump(all_history, f, indent=2)
        logger.debug(f"Saved chat history for {username}")
    except Exception as e:
        logger.warning(f"Could not save chat history: {e}")
        st.warning(f"Could not save chat history: {e}")


def authenticate_user(username, password):
    """Authenticate user and return role if successful."""
    if not isinstance(username, str) or not isinstance(password, str):
        logger.warning(
            "Invalid authentication attempt - invalid types"
        )
        return None
    if username in DEFAULT_USERS:
        user = DEFAULT_USERS[username]
        if user["password"] == password:
            logger.info(f"User authenticated: {username}")
            return user["role"]
    logger.warning(f"Authentication failed for username: {username}")
    return None


def init_session_state():
    """Initialize session state variables."""
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    if "username" not in st.session_state:
        st.session_state.username = None
    if "role" not in st.session_state:
        st.session_state.role = None
    if "messages" not in st.session_state:
        st.session_state.messages = []


def login_page():
    """Display login interface."""
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.title("🔐 NHS Nursing Validator")
        st.markdown("---")

        username = st.text_input("Username:", key="login_username")
        password = st.text_input(
            "Password:",
            type="password",
            key="login_password"
        )

        if st.button("Login", use_container_width=True):
            role = authenticate_user(username, password)
            if role:
                st.session_state.authenticated = True
                st.session_state.username = username
                st.session_state.role = role
                st.session_state.messages = load_chat_history(username)
                st.success(f"Welcome, {username}!")
                st.rerun()
            else:
                st.error("Invalid username or password")

        st.markdown("---")
        st.markdown(
            "**Demo Credentials:**\n"
            "- Username: `nurse` | Password: `nurse2025`\n"
            "- Username: `clinician` | Password: `clinician2025`\n"
            "- Username: `admin` | Password: `admin2025`"
        )


def logout():
    """Logout user."""
    if st.session_state.username:
        save_chat_history(
            st.session_state.username,
            st.session_state.messages
        )
    st.session_state.authenticated = False
    st.session_state.username = None
    st.session_state.role = None
    st.session_state.messages = []
    st.success("You have been logged out")
    st.rerun()


def check_permission(action):
    """Check if current user has permission for action."""
    role = st.session_state.role
    if role in ROLE_PERMISSIONS:
        return action in ROLE_PERMISSIONS[role]
    return False


def main_app():
    """Main application interface."""
    db = load_vector_db()

    # Sidebar with user info and controls
    with st.sidebar:
        st.markdown(f"**👤 Logged in as:** {st.session_state.username}")
        st.markdown(f"**Role:** {st.session_state.role.capitalize()}")
        st.markdown("---")

        if db:
            st.success("📚 FoNS Knowledge Base: Active")
        else:
            st.error("⚠️ Knowledge Base Offline")

        if st.button("🚪 Logout", use_container_width=True):
            logout()

        st.markdown("---")
        st.markdown("### About")
        st.markdown(
            "This tool uses Retrieval-Augmented Generation (RAG) "
            "to provide evidence-based nursing knowledge from the "
            "Foundation of Nursing Studies."
        )

    # Main content
    st.title("🏥 NHS Unified Nursing Validator (PRO)")

    if not db:
        st.error(
            "⚠️ Knowledge Base Offline - "
            "Please run ingest_fast.py to initialize the database"
        )
        return

    # Navigation tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "💬 Assistant",
        "📊 Care Plan",
        "🔍 Problems",
        "💊 Interventions",
        "📈 Indicators"
    ])

    with tab1:
        st.subheader("💬 Clinical Knowledge Assistant")

        # Display chat history
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Chat input
        if query := st.chat_input(
            "Ask about nursing practice, clinical guidance, or "
            "care planning..."
        ):
            st.session_state.messages.append({
                "role": "user",
                "content": query
            })

            with st.chat_message("user"):
                st.markdown(query)

            # Generate response
            with st.chat_message("assistant"):
                with st.spinner("📚 Consulting Knowledge Base..."):
                    try:
                        llm = AzureOpenAI(
                            temperature=0,
                            deployment_name=os.getenv(
                                "AZURE_OPENAI_DEPLOYMENT"
                            )
                        )

                        qa_chain = RetrievalQA.from_chain_type(
                            llm=llm,
                            chain_type="stuff",
                            retriever=db.as_retriever(
                                search_kwargs={"k": 5}
                            )
                        )

                        response = qa_chain.run(query)
                        st.markdown(response)

                        st.session_state.messages.append({
                            "role": "assistant",
                            "content": response
                        })

                    except Exception as e:
                        error_msg = f"Error generating response: {e}"
                        st.error(error_msg)

            # Save chat history
            save_chat_history(
                st.session_state.username,
                st.session_state.messages
            )

    with tab2:
        if VISUALIZATIONS_AVAILABLE:
            display_care_plan_dashboard()
        else:
            st.warning("Visualization module not available")

    with tab3:
        if VISUALIZATIONS_AVAILABLE:
            display_problem_assessment()
        else:
            st.warning("Visualization module not available")

    with tab4:
        if VISUALIZATIONS_AVAILABLE:
            display_intervention_analysis()
        else:
            st.warning("Visualization module not available")

    with tab5:
        if VISUALIZATIONS_AVAILABLE:
            display_health_indicators()
        else:
            st.warning("Visualization module not available")

    # Quick action buttons
    st.divider()
    st.subheader("🎯 Quick Actions")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📋 Clear History", use_container_width=True):
            st.session_state.messages = []
            save_chat_history(st.session_state.username, [])
            st.success("Chat history cleared")
            st.rerun()

    with col2:
        if check_permission("export"):
            if st.button("💾 Export Chat", use_container_width=True):
                chat_json = json.dumps(
                    st.session_state.messages,
                    indent=2
                )
                st.download_button(
                    label="Download as JSON",
                    data=chat_json,
                    file_name=(
                        f"chat_{st.session_state.username}_"
                        f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
                    ),
                    mime="application/json"
                )

    with col3:
        if check_permission("view_history"):
            if st.button("📊 View Stats", use_container_width=True):
                st.metric("Messages in Chat", len(st.session_state.messages))
                user_msgs = sum(
                    1 for m in st.session_state.messages
                    if m["role"] == "user"
                )
                st.metric("Questions Asked", user_msgs)


def admin_panel():
    """Admin panel for user management."""
    st.subheader("⚙️ Admin Panel")

    if st.session_state.role != "admin":
        st.error("Access denied. Admin role required.")
        return

    st.write("User Management:")
    with st.expander("Manage Users"):
        st.info(
            "In production, integrate with a proper user database "
            "(e.g., Auth0, Azure AD, Okta)"
        )

        col1, col2, col3 = st.columns(3)
        with col1:
            st.write("**Current Users:**")
            for user, data in DEFAULT_USERS.items():
                st.write(f"- {user} ({data['role']})")


if __name__ == "__main__":
    init_session_state()

    if not st.session_state.authenticated:
        login_page()
    else:
        if st.session_state.role == "admin":
            # Admin can access both main app and admin panel
            page = st.sidebar.radio(
                "Navigation",
                ["Assistant", "Admin Panel"],
                key="admin_nav"
            )
            if page == "Assistant":
                main_app()
            else:
                admin_panel()
        else:
            main_app()
