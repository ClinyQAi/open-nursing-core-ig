import os
import shutil
import streamlit as st
from dotenv import load_dotenv

from langchain_openai import AzureOpenAI
from langchain_openai import AzureOpenAIEmbeddings
from langchain_chroma import Chroma
from langchain.chains import RetrievalQA

load_dotenv()
st.set_page_config(
    page_title="NHS Unified Nursing Validator (PRO)",
    page_icon="🔒",
    layout="wide"
)

VECTOR_DB_PATH = "chroma_db_fons"
LOCAL_DB_PATH = "/tmp/chroma_db_fons_fast"
EMBEDDING_MODEL = "text-embedding-ada-002"


@st.cache_resource
def load_vector_db():
    if not os.path.exists(VECTOR_DB_PATH):
        return None
    if not os.path.exists(LOCAL_DB_PATH):
        try:
            shutil.copytree(
                VECTOR_DB_PATH,
                LOCAL_DB_PATH,
                dirs_exist_ok=True
            )
        except Exception:
            return None
    try:
        embeddings = AzureOpenAIEmbeddings(
            azure_deployment=EMBEDDING_MODEL
        )
        return Chroma(
            persist_directory=LOCAL_DB_PATH,
            embedding_function=embeddings
        )
    except Exception:
        return None


db = load_vector_db()


def main():
    st.title("🏥 NHS Unified Nursing Validator (PRO)")
    if db:
        st.sidebar.success("📚 FoNS Knowledge Base: Active")
    else:
        st.sidebar.warning("⚠️ Knowledge Base Offline")
    manual_text = st.text_area("Clinical Note:", height=300)

    if st.button("🚀 Run Validation"):
        if manual_text and db:
            with st.spinner("📚 Consulting Knowledge Graph..."):
                llm = AzureOpenAI(
                    temperature=0,
                    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT")
                )

                qa_chain = RetrievalQA.from_chain_type(
                    llm=llm,
                    chain_type="stuff",
                    retriever=db.as_retriever()
                )

                query = (
                    f"You are a Nursing Validator. Analyze this note: "
                    f"'{manual_text}'. "
                    "Check for Relational Care and Equity. "
                    "Cite your sources."
                )

                response = qa_chain.run(query)

            st.success("Analysis Complete")
            st.markdown(response)


if __name__ == "__main__":
    main()
