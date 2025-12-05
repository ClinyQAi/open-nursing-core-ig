import os
import shutil
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

# --- CONFIGURATION ---
DATA_FOLDER = "fons_knowledge_base" # Your 378 PDFs
DB_OUTPUT_FOLDER = "chroma_db_fons"
# Using basic default embeddings that work with Python 3.14

def build_the_brain():
    print(f"🧠 Building ChromaDB from {DATA_FOLDER}...")

    # Clean up old versions to ensure a fresh build
    if os.path.exists(DB_OUTPUT_FOLDER):
        print(f"   🧹 Removing old database...")
        shutil.rmtree(DB_OUTPUT_FOLDER)

    # 1. Load PDFs
    print(f"   📚 Loading PDFs from '{DATA_FOLDER}'...")
    loader = PyPDFDirectoryLoader(DATA_FOLDER)
    documents = loader.load()
    print(f"   ✅ Loaded {len(documents)} pages.")

    # 2. Split into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = text_splitter.split_documents(documents)
    print(f"   ✅ Created {len(chunks)} text chunks.")

    # 3. Load Embedding Model
    print("   🧠 Loading embedding model (this may download the model)...")
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_ID)

    # 4. Create and Persist the Database
    # This is the heavy step. It converts all chunks to vectors.
    print("   💾 Creating and saving the vector database (This will take several minutes)...")
    db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=DB_OUTPUT_FOLDER
    )

    print(f"\n🎉 SUCCESS! ChromaDB created in folder: '{DB_OUTPUT_FOLDER}'")
    print("   You can now upload this folder to your Hugging Face Space.")

if __name__ == "__main__":
    build_the_brain()
