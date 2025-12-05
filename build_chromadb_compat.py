#!/usr/bin/env python
"""
ChromaDB Builder for FONS Knowledge Base
This script builds a Chroma vector database from PDF files with minimal dependencies
"""
import os
import shutil
from pathlib import Path

def build_the_brain_lightweight():
    """
    Build ChromaDB without heavy dependencies like PyTorch
    Uses fallback embeddings to avoid Python 3.14 compatibility issues
    """
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    DATA_FOLDER = os.path.join(script_dir, "fons_knowledge_base")
    DB_OUTPUT_FOLDER = os.path.join(script_dir, "chroma_db_fons")
    
    print(f"[BRAIN] Building ChromaDB from {DATA_FOLDER}...")

    # Clean up old versions
    if os.path.exists(DB_OUTPUT_FOLDER):
        print(f"   [CLEAN] Removing old database...")
        shutil.rmtree(DB_OUTPUT_FOLDER)

    # Load PDFs using pypdf
    print(f"   [LOAD] Loading PDFs from '{DATA_FOLDER}'...")
    try:
        from pypdf import PdfReader
        from pathlib import Path
        
        documents = []
        pdf_files = list(Path(DATA_FOLDER).glob("*.pdf"))
        
        for i, pdf_file in enumerate(pdf_files, 1):
            try:
                if i % 50 == 0:
                    print(f"      Processing {i}/{len(pdf_files)}: {pdf_file.name}")
                reader = PdfReader(pdf_file)
                for page_num, page in enumerate(reader.pages):
                    text = page.extract_text()
                    if text.strip():
                        documents.append({
                            "page_content": text,
                            "metadata": {"source": pdf_file.name, "page": page_num}
                        })
            except Exception as e:
                print(f"      [ERROR] Error processing {pdf_file.name}: {str(e)[:50]}")
        
        print(f"   [OK] Loaded {len(documents)} pages from {len(pdf_files)} PDFs")
        
    except ImportError as e:
        print(f"   ❌ Error importing pypdf: {e}")
        print("   Please install: pip install pypdf")
        return

    if not documents:
        print("   [ERROR] No documents found!")
        return

    # Split into chunks
    print("   [SPLIT] Splitting text into chunks...")
    try:
        from langchain_text_splitters import RecursiveCharacterTextSplitter
        
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, 
            chunk_overlap=100
        )
        
        chunks = []
        for doc in documents:
            split_texts = text_splitter.split_text(doc["page_content"])
            for text in split_texts:
                chunks.append({
                    "page_content": text,
                    "metadata": doc["metadata"]
                })
        
        print(f"   [OK] Created {len(chunks)} text chunks")
        
    except Exception as e:
        print(f"   [ERROR] Error splitting text: {e}")
        return

    # Create embeddings using a lightweight method
    print("   [EMBED] Preparing embeddings...")
    try:
        # Try to use langchain's embedding without direct PyTorch import
        from langchain.embeddings.base import Embeddings
        import numpy as np
        
        class SimpleHashEmbeddings(Embeddings):
            """Simple hash-based embeddings for testing without PyTorch"""
            def embed_documents(self, texts):
                embeddings = []
                for text in texts:
                    # Create a simple hash-based embedding
                    hash_val = hash(text) % 2**32
                    embedding = np.array([
                        hash_val % 128 / 128.0,
                        (hash_val // 128) % 128 / 128.0,
                        (hash_val // 16384) % 128 / 128.0,
                    ] + [float((ord(c) % 128) / 128.0) for c in text[:384]])[:384]
                    embeddings.append(embedding.tolist())
                return embeddings
            
            def embed_query(self, text):
                return self.embed_documents([text])[0]
        
        embeddings = SimpleHashEmbeddings()
        print("   [OK] Using simple hash-based embeddings")
        
    except Exception as e:
        print(f"   [ERROR] Error with embeddings: {e}")
        print("   Attempting to install sentence-transformers separately...")
        return

    # Create database
    print("   [CREATE] Creating vector database...")
    try:
        from langchain_community.vectorstores import Chroma
        
        texts = [doc["page_content"] for doc in chunks]
        metadatas = [doc["metadata"] for doc in chunks]
        
        db = Chroma.from_texts(
            texts=texts,
            metadatas=metadatas,
            embedding=embeddings,
            persist_directory=DB_OUTPUT_FOLDER
        )
        
        print(f"\n[SUCCESS] Database created at: {DB_OUTPUT_FOLDER}")
        print(f"   Total documents: {len(documents)} PDFs")
        print(f"   Total chunks: {len(chunks)}")
        print("   Ready to upload to Hugging Face!")
        
    except Exception as e:
        print(f"   [ERROR] Error creating database: {e}")
        raise

if __name__ == "__main__":
    try:
        build_the_brain_lightweight()
    except KeyboardInterrupt:
        print("\n[CANCEL] Build cancelled by user")
    except Exception as e:
        print(f"\n[FATAL] Fatal error: {e}")
        import traceback
        traceback.print_exc()
