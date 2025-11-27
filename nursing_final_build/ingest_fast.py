import os
import shutil
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import AzureOpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv

load_dotenv()
DATA_FOLDER = "fons_knowledge_base"
DB_FOLDER = "chroma_db_fons"
EMBEDDING_MODEL = "text-embedding-ada-002"

def ingest():
    print("🧠 Building Knowledge Graph...")
    if os.path.exists(DB_FOLDER): shutil.rmtree(DB_FOLDER)
    embeddings = AzureOpenAIEmbeddings(azure_deployment=EMBEDDING_MODEL, openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"), azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"), api_key=os.getenv("AZURE_OPENAI_API_KEY"))
    vector_store = Chroma(persist_directory=DB_FOLDER, embedding_function=embeddings)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    files = [f for f in os.listdir(DATA_FOLDER) if f.endswith('.pdf')]
    print(f"   Processing {len(files)} PDFs...")
    for i, f in enumerate(files):
        try:
            loader = PyPDFLoader(os.path.join(DATA_FOLDER, f))
            pages = loader.load()
            if pages:
                chunks = text_splitter.split_documents(pages)
                vector_store.add_documents(chunks)
                if (i+1) % 10 == 0: print(f"   [{i+1}/{len(files)}] Indexed...", end="\r")
        except: pass
    print("\n🎉 Database Rebuilt Successfully!")
if __name__ == "__main__": ingest()
