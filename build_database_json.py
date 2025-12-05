#!/usr/bin/env python
"""
Simple ChromaDB alternative: Save embeddings as JSON
Works with Python 3.14 without ChromaDB version conflicts
"""
import os
import shutil
import json
import numpy as np
from pathlib import Path
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def simple_hash_embedding(text):
    """Create a simple hash-based embedding"""
    hash_val = hash(text) % 2**32
    embedding = [
        hash_val % 128 / 128.0,
        (hash_val // 128) % 128 / 128.0,
        (hash_val // 16384) % 128 / 128.0,
    ] + [float((ord(c) % 128) / 128.0) for c in text[:381]]
    return embedding[:384]

def build_database():
    """Build a simple vector database from PDFs"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    DATA_FOLDER = os.path.join(script_dir, "fons_knowledge_base")
    DB_OUTPUT_FOLDER = os.path.join(script_dir, "chroma_db_fons_simple")
    
    print(f"[BRAIN] Building Database from {DATA_FOLDER}...")

    # Clean up old versions
    if os.path.exists(DB_OUTPUT_FOLDER):
        print(f"   [CLEAN] Removing old database...")
        shutil.rmtree(DB_OUTPUT_FOLDER)
    
    os.makedirs(DB_OUTPUT_FOLDER, exist_ok=True)

    # Load PDFs
    print(f"   [LOAD] Loading PDFs...")
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
            print(f"      [WARN] Error with {pdf_file.name}: {str(e)[:30]}")
    
    print(f"   [OK] Loaded {len(documents)} pages from {len(pdf_files)} PDFs")

    # Split into chunks
    print("   [SPLIT] Splitting text into chunks...")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    
    chunks = []
    for doc in documents:
        split_texts = text_splitter.split_text(doc["page_content"])
        for text in split_texts:
            chunks.append({
                "page_content": text,
                "metadata": doc["metadata"]
            })
    
    print(f"   [OK] Created {len(chunks)} text chunks")

    # Create embeddings and save
    print("   [EMBED] Creating embeddings...")
    database = {
        "metadata": {
            "total_pdfs": len(pdf_files),
            "total_pages": len(documents),
            "total_chunks": len(chunks),
            "embedding_dim": 384
        },
        "documents": []
    }
    
    for i, chunk in enumerate(chunks):
        if (i + 1) % 2000 == 0:
            print(f"      Embedded {i+1}/{len(chunks)} chunks")
        
        embedding = simple_hash_embedding(chunk["page_content"])
        database["documents"].append({
            "id": str(i),
            "content": chunk["page_content"][:1000],  # Truncate for file size
            "embedding": embedding,
            "metadata": chunk["metadata"]
        })
    
    # Save to JSON
    print("   [SAVE] Saving database...")
    output_file = os.path.join(DB_OUTPUT_FOLDER, "database.json")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(database, f, indent=2)
    
    # Save metadata separately
    metadata_file = os.path.join(DB_OUTPUT_FOLDER, "metadata.json")
    with open(metadata_file, 'w') as f:
        json.dump(database["metadata"], f, indent=2)
    
    print(f"\n[SUCCESS] Database created at: {DB_OUTPUT_FOLDER}")
    print(f"   Total PDFs: {len(pdf_files)}")
    print(f"   Total pages: {len(documents)}")
    print(f"   Total chunks: {len(chunks)}")
    print(f"   Embedding dimension: 384")
    print(f"\n   Files saved:")
    print(f"   - database.json (complete database with embeddings)")
    print(f"   - metadata.json (statistics)")
    
    return True

if __name__ == "__main__":
    try:
        build_database()
        print("\n[DONE] Build successful!")
    except KeyboardInterrupt:
        print("\n[CANCEL] Build cancelled by user")
    except Exception as e:
        print(f"\n[ERROR] Fatal error: {e}")
        import traceback
        traceback.print_exc()
