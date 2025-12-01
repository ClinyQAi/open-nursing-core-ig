import os
import json
import logging
from datetime import datetime
import streamlit as st

from langchain_openai import AzureOpenAI
from langchain.chains import RetrievalQA

# Core Imports
from core.settings import settings
from core.logging_config import configure_logging
from core.validator import (
    authenticate_user,
    load_vector_db,
    save_chat_message,
    load_chat_history,
)

# Import visualization module
try:
    from visualizations.visualizations import (
        display_care_plan_dashboard,
        display_problem_assessment,
        display_intervention_analysis,
        display_health_indicators
    )
    VISUALIZATIONS_AVAILABLE = True
except ImportError:
    VISUALIZATIONS_AVAILABLE = False


# ============================================
# LOGGING SETUP
# ============================================
configure_logging()
logger = logging.getLogger(__name__)

# ============================================
# STREAMLIT CONFIG
# ============================================
st.set_page_config(
    page_title="NHS Unified Nursing Validator (PRO)",
    page_icon="🔒",
    layout="wide"
)

logger.info(f"Starting NHS Nursing Validator - Environment: {settings.APP_ENV}")

ROLE_PERMISSIONS = {
    "admin": ["validate", "view_history", "export", "manage_users"],
    "nurse": ["validate", "view_history", "export"],
    "clinician": ["validate", "view_history"]
}

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
                # For app.py legacy, we load full history into memory session state
                st.session_state.messages = load_chat_history(username)
                st.success(f"Welcome, {username}!")
                st.rerun()
            else:
                st.error("Invalid username or password")

        st.markdown("---")
        st.markdown(
            "**Demo Credentials:**\n"
            "- Username: `nurse` | Check .env\n"
            "- Username: `clinician` | Check .env\n"
            "- Username: `admin` | Check .env"
        )


def logout():
    """Logout user."""
    if st.session_state.username:
        # Save last state (though we save per message usually, this is good practice in legacy app)
        # However, save_chat_message saves one by one.
        # app.py's save_chat_history saved whole list.
        # We'll rely on the fact that we should save messages as they come in.
        # But for compatibility, let's just clear state.
        pass

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
                # Persist message
                save_chat_message(st.session_state.username, "user", query)

            # Generate response
            with st.chat_message("assistant"):
                with st.spinner("📚 Consulting Knowledge Base..."):
                    try:
                        llm = AzureOpenAI(
                            temperature=0,
                            deployment_name=settings.AZURE_OPENAI_DEPLOYMENT,
                            api_version=settings.AZURE_OPENAI_API_VERSION,
                            api_key=settings.AZURE_OPENAI_API_KEY,
                            azure_endpoint=settings.AZURE_OPENAI_ENDPOINT
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
                        # Persist response
                        save_chat_message(st.session_state.username, "assistant", response)

                    except Exception as e:
                        error_msg = f"Error generating response: {e}"
                        st.error(error_msg)


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
            # Note: Logic to clear history in DB/File is in db module or needs helper in validator
            # For now, just clear session.
            st.success("Chat history cleared (session only)")
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

        # We can't easily display default users dict anymore as it is dynamic or DB based
        st.write("Users are managed via Database or Environment Variables.")


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
