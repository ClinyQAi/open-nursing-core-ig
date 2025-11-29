"""Fast Ingestion Script for FoNS Knowledge Base
Builds a ChromaDB vector store from downloaded FoNS articles.
"""
import os
import glob
from pathlib import Path
from langchain_openai import AzureOpenAIEmbeddings
from langchain_chroma import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain.schema import Document

# Configuration
AZURE_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
KNOWLEDGE_BASE_DIR = "fons_knowledge_base"
CHROMA_DB_PATH = "chroma_db_fons"

def load_documents(knowledge_dir: str) -> list[Document]:
    """Load all documents from the knowledge base directory."""
    documents = []
    
    # Get all text files
    txt_files = glob.glob(os.path.join(knowledge_dir, "**/*.txt"), recursive=True)
    for file_path in txt_files:
        try:
            loader = TextLoader(file_path, encoding="utf-8")
            docs = loader.load()
            for doc in docs:
                doc.metadata["source"] = Path(file_path).name
                doc.metadata["type"] = "text"
            documents.extend(docs)
            print(f"  Loaded: {file_path}")
        except Exception as e:
            print(f"  Error loading {file_path}: {e}")
    
    # Get all PDF files
    pdf_files = glob.glob(os.path.join(knowledge_dir, "**/*.pdf"), recursive=True)
    for file_path in pdf_files:
        try:
            loader = PyPDFLoader(file_path)
            docs = loader.load()
            for doc in docs:
                doc.metadata["source"] = Path(file_path).name
                doc.metadata["type"] = "pdf"
            documents.extend(docs)
            print(f"  Loaded: {file_path}")
        except Exception as e:
            print(f"  Error loading {file_path}: {e}")
    
    # Get all markdown files
    md_files = glob.glob(os.path.join(knowledge_dir, "**/*.md"), recursive=True)
    for file_path in md_files:
        try:
            loader = TextLoader(file_path, encoding="utf-8")
            docs = loader.load()
            for doc in docs:
                doc.metadata["source"] = Path(file_path).name
                doc.metadata["type"] = "markdown"
            documents.extend(docs)
            print(f"  Loaded: {file_path}")
        except Exception as e:
            print(f"  Error loading {file_path}: {e}")
    
    return documents

def split_documents(documents: list[Document]) -> list[Document]:
    """Split documents into smaller chunks for embedding."""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        separators=["\n\n", "\n", ". ", " ", ""]
    )
    return text_splitter.split_documents(documents)

def create_vectorstore(chunks: list[Document]) -> Chroma:
    """Create and persist a ChromaDB vector store."""
    print(f"\nCreating embeddings for {len(chunks)} chunks...")
    
    embeddings = AzureOpenAIEmbeddings(
        azure_endpoint=AZURE_ENDPOINT,
        api_key=AZURE_API_KEY,
        azure_deployment="text-embedding-3-small"
    )
    
    # Create vector store with persistence
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DB_PATH
    )
    
    return vectorstore

def main():
    print("="*60)
    print("FoNS Knowledge Base Ingestion")
    print("="*60)
    
    # Check for environment variables
    if not AZURE_ENDPOINT or not AZURE_API_KEY:
        print("ERROR: Azure OpenAI credentials not set.")
        print("Set AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_API_KEY environment variables.")
        return
    
    # Check for knowledge base directory
    if not os.path.exists(KNOWLEDGE_BASE_DIR):
        print(f"ERROR: Knowledge base directory not found: {KNOWLEDGE_BASE_DIR}")
        print("Run harvest_fons.py first to download articles.")
        return
    
    # Load documents
    print(f"\nLoading documents from {KNOWLEDGE_BASE_DIR}...")
    documents = load_documents(KNOWLEDGE_BASE_DIR)
    
    if not documents:
        print("No documents found. Exiting.")
        return
    
    print(f"\nLoaded {len(documents)} documents.")
    
    # Split into chunks
    print("\nSplitting documents into chunks...")
    chunks = split_documents(documents)
    print(f"Created {len(chunks)} chunks.")
    
    # Create vector store
    print("\nBuilding vector store (this may take a few minutes)...")
    vectorstore = create_vectorstore(chunks)
    
    # Verify
    doc_count = vectorstore._collection.count()
    print(f"\nVector store created successfully!")
    print(f"Total documents in ChromaDB: {doc_count}")
    print(f"Stored at: {CHROMA_DB_PATH}")
    print("\n" + "="*60)
    print("Ready to run: streamlit run app.py")
    print("="*60)

if __name__ == "__main__":
    main()
