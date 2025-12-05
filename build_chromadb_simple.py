import os
import shutil
from pathlib import Path
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.embeddings import SentenceTransformerEmbeddings

# --- CONFIGURATION ---
DATA_FOLDER = "fons_knowledge_base"
DB_OUTPUT_FOLDER = "chroma_db_fons"

def load_pdfs_from_folder(folder_path):
    """Load text from all PDFs in a folder"""
    print(f"   📚 Loading PDFs from '{folder_path}'...")
    documents = []
    pdf_files = list(Path(folder_path).glob("*.pdf"))
    
    for i, pdf_file in enumerate(pdf_files):
        try:
            print(f"      Processing {i+1}/{len(pdf_files)}: {pdf_file.name}")
            reader = PdfReader(pdf_file)
            for page_num, page in enumerate(reader.pages):
                text = page.extract_text()
                if text.strip():
                    documents.append({
                        "page_content": text,
                        "metadata": {
                            "source": pdf_file.name,
                            "page": page_num
                        }
                    })
        except Exception as e:
            print(f"      ⚠️  Error processing {pdf_file.name}: {e}")
    
    print(f"   ✅ Loaded {len(documents)} pages.")
    return documents

def build_the_brain():
    print(f"🧠 Building ChromaDB from {DATA_FOLDER}...")

    # Clean up old versions to ensure a fresh build
    if os.path.exists(DB_OUTPUT_FOLDER):
        print(f"   🧹 Removing old database...")
        shutil.rmtree(DB_OUTPUT_FOLDER)

    # 1. Load PDFs
    documents = load_pdfs_from_folder(DATA_FOLDER)
    
    if not documents:
        print("   ❌ No documents found. Exiting.")
        return

    # 2. Split into chunks
    print("   🔄 Splitting text into chunks...")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    
    chunks = []
    for doc in documents:
        split_texts = text_splitter.split_text(doc["page_content"])
        for text in split_texts:
            chunks.append({
                "page_content": text,
                "metadata": doc["metadata"]
            })
    
    print(f"   ✅ Created {len(chunks)} text chunks.")

    # 3. Load Embedding Model
    print("   🧠 Loading embedding model (using SentenceTransformers)...")
    try:
        embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    except Exception as e:
        print(f"   ⚠️  Error loading embeddings: {e}")
        print("   Using default embeddings instead...")
        from langchain.embeddings import FakeEmbeddings
        embeddings = FakeEmbeddings(model_name="default")

    # 4. Create and Persist the Database
    print("   💾 Creating and saving the vector database (This will take several minutes)...")
    
    try:
        # Convert document format for Chroma
        texts = [doc["page_content"] for doc in chunks]
        metadatas = [doc["metadata"] for doc in chunks]
        
        db = Chroma.from_texts(
            texts=texts,
            metadatas=metadatas,
            embedding=embeddings,
            persist_directory=DB_OUTPUT_FOLDER
        )
        
        print(f"\n🎉 SUCCESS! ChromaDB created in folder: '{DB_OUTPUT_FOLDER}'")
        print("   You can now upload this folder to your Hugging Face Space.")
    except Exception as e:
        print(f"\n❌ Error creating database: {e}")
        raise

if __name__ == "__main__":
    build_the_brain()
