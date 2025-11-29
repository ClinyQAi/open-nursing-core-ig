"""NHS Unified Nursing Validator - Relational Intelligence Coach
A Streamlit-based RAG application for nursing knowledge validation and coaching.
"""
import os
import streamlit as st
from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings
from langchain_chroma import Chroma
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

# --- Configuration ---
AZURE_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4o")
APP_PASSWORD = os.getenv("APP_PASSWORD", "nurse2025")
CHROMA_DB_PATH = "chroma_db_fons"

# --- Page Configuration ---
st.set_page_config(
    page_title="NHS Nursing Validator",
    page_icon="🏥",
    layout="wide"
)

# --- Authentication ---
def check_password():
    """Simple password check for app access."""
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    
    if not st.session_state.authenticated:
        st.title("🔐 NHS Unified Nursing Validator")
        password = st.text_input("Enter access password:", type="password")
        if st.button("Login"):
            if password == APP_PASSWORD:
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Incorrect password. Please try again.")
        return False
    return True

# --- RAG System Prompt ---
SYSTEM_PROMPT = """You are a Relational Intelligence Coach for NHS nursing professionals.
You combine evidence-based nursing knowledge from the Foundation of Nursing Studies (FoNS)
with person-centred care principles to support clinical decision-making.

When answering:
1. Draw from the provided context to give evidence-based responses
2. If the context doesn't contain relevant information, say so clearly
3. Always encourage reflection and critical thinking
4. Relate concepts to real-world nursing practice
5. Be supportive, encouraging, and professional

Context from FoNS Knowledge Base:
{context}

Question: {question}

Provide a thoughtful, evidence-based response that supports nursing professional development:"""

# --- Initialize Components ---
@st.cache_resource
def initialize_rag_chain():
    """Initialize the RAG chain with Azure OpenAI and ChromaDB."""
    try:
        # Initialize embeddings
        embeddings = AzureOpenAIEmbeddings(
            azure_endpoint=AZURE_ENDPOINT,
            api_key=AZURE_API_KEY,
            azure_deployment="text-embedding-3-small"
        )
        
        # Initialize vector store
        vectorstore = Chroma(
            persist_directory=CHROMA_DB_PATH,
            embedding_function=embeddings
        )
        
        # Initialize LLM
        llm = AzureChatOpenAI(
            azure_endpoint=AZURE_ENDPOINT,
            api_key=AZURE_API_KEY,
            azure_deployment=AZURE_DEPLOYMENT,
            temperature=0.7
        )
        
        # Create prompt template
        prompt = PromptTemplate(
            template=SYSTEM_PROMPT,
            input_variables=["context", "question"]
        )
        
        # Create retrieval chain
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=vectorstore.as_retriever(search_kwargs={"k": 5}),
            chain_type_kwargs={"prompt": prompt},
            return_source_documents=True
        )
        
        return qa_chain, vectorstore
    except Exception as e:
        st.error(f"Failed to initialize RAG system: {e}")
        return None, None

# --- Main Application ---
def main():
    if not check_password():
        return
    
    st.title("🏥 NHS Unified Nursing Validator")
    st.markdown("**Relational Intelligence Coach** - Evidence-based nursing knowledge at your fingertips")
    
    # Check for required environment variables
    if not AZURE_ENDPOINT or not AZURE_API_KEY:
        st.error("⚠️ Azure OpenAI credentials not configured. Please set environment variables.")
        st.info("Required: AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_API_KEY")
        return
    
    # Check for ChromaDB
    if not os.path.exists(CHROMA_DB_PATH):
        st.warning("⚠️ Knowledge base not found. Please run the ingestion script first.")
        st.code("python ingest_fast.py", language="bash")
        return
    
    # Initialize RAG
    with st.spinner("Loading knowledge base..."):
        qa_chain, vectorstore = initialize_rag_chain()
    
    if qa_chain is None:
        return
    
    # Sidebar
    with st.sidebar:
        st.header("📚 About")
        st.markdown("""
        This tool uses Retrieval-Augmented Generation (RAG) to provide
        evidence-based nursing knowledge from the Foundation of Nursing Studies.
        
        **Features:**
        - Person-centred care guidance
        - Practice development support
        - Evidence-based recommendations
        - Reflective practice coaching
        """)
        
        st.divider()
        
        # Knowledge base stats
        try:
            doc_count = vectorstore._collection.count()
            st.metric("Documents in Knowledge Base", doc_count)
        except:
            pass
    
    # Main chat interface
    st.subheader("💬 Ask the Coach")
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if question := st.chat_input("Ask about nursing practice, person-centred care, or professional development..."):
        # Display user message
        st.session_state.messages.append({"role": "user", "content": question})
        with st.chat_message("user"):
            st.markdown(question)
        
        # Generate response
        with st.chat_message("assistant"):
            with st.spinner("Consulting the knowledge base..."):
                try:
                    result = qa_chain.invoke({"query": question})
                    response = result["result"]
                    
                    st.markdown(response)
                    
                    # Show sources
                    if result.get("source_documents"):
                        with st.expander("📖 View Sources"):
                            for i, doc in enumerate(result["source_documents"], 1):
                                source = doc.metadata.get("source", "Unknown")
                                st.markdown(f"**Source {i}:** {source}")
                                st.markdown(f"*{doc.page_content[:200]}...*")
                                st.divider()
                    
                    st.session_state.messages.append({"role": "assistant", "content": response})
                
                except Exception as e:
                    error_msg = f"Error generating response: {e}"
                    st.error(error_msg)
                    st.session_state.messages.append({"role": "assistant", "content": error_msg})
    
    # Quick prompts
    st.divider()
    st.subheader("🎯 Quick Prompts")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("What is person-centred care?", use_container_width=True):
            st.session_state.quick_prompt = "What is person-centred care and how can I implement it in my daily nursing practice?"
            st.rerun()
    
    with col2:
        if st.button("Practice development tips", use_container_width=True):
            st.session_state.quick_prompt = "What are the key principles of practice development in nursing?"
            st.rerun()
    
    with col3:
        if st.button("Reflective practice", use_container_width=True):
            st.session_state.quick_prompt = "How can I develop my reflective practice skills as a nurse?"
            st.rerun()

if __name__ == "__main__":
    main()
