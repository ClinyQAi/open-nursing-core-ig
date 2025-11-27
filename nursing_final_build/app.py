import os
import shutil
import streamlit as st
from dotenv import load_dotenv
from openai import AzureOpenAI
from langchain_openai import AzureOpenAIEmbeddings
from langchain_community.vectorstores import Chroma

load_dotenv()
st.set_page_config(page_title="NHS Unified Nursing Validator (PRO)", page_icon="🔒", layout="wide")

VECTOR_DB_PATH = "chroma_db_fons"
LOCAL_DB_PATH = "/tmp/chroma_db_fons_fast"
EMBEDDING_MODEL = "text-embedding-ada-002"

mst_colors = {"MST-01": "#f6ede4", "MST-02": "#f3e7db", "MST-03": "#f7ead0", "MST-04": "#eadaba", "MST-05": "#d7bd96", "MST-06": "#a07e56", "MST-07": "#825c43", "MST-08": "#604134", "MST-09": "#3a312a", "MST-10": "#292420"}

def check_password():
    def password_entered():
        if st.session_state["password"] == os.getenv("APP_PASSWORD"):
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else: st.session_state["password_correct"] = False
    if "password_correct" not in st.session_state:
        st.header("🔒 NHS Wisdom Engine")
        st.text_input("Enter License Key:", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        st.text_input("Enter License Key:", type="password", on_change=password_entered, key="password")
        st.error("🚫 Access Denied.")
        return False
    else: return True

@st.cache_resource
def load_vector_db():
    if not os.path.exists(VECTOR_DB_PATH): return None
    if not os.path.exists(LOCAL_DB_PATH):
        try: shutil.copytree(VECTOR_DB_PATH, LOCAL_DB_PATH, dirs_exist_ok=True)
        except: return None
    try:
        embeddings = AzureOpenAIEmbeddings(azure_deployment=EMBEDDING_MODEL, openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"), azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"), api_key=os.getenv("AZURE_OPENAI_API_KEY"))
        return Chroma(persist_directory=LOCAL_DB_PATH, embedding_function=embeddings)
    except: return None

db = load_vector_db()

def sidebar_equity_check():
    st.sidebar.header("💙 Standards of Care")
    st.sidebar.success("**Project Lead:** Lincoln Gombedza")
    st.sidebar.info("**Clinical Leadership:**\n\n**Equity:** Kumbi Kariwo (BCHC)\n**Relational:** Prof. Bosanquet & Dr. Cable")
    st.sidebar.markdown("---")
    if db: st.sidebar.success(f"📚 FoNS Knowledge Base: Active")
    else: st.sidebar.warning("⚠️ Knowledge Base Offline")
    st.sidebar.markdown("---")
    st.sidebar.subheader("🧑🏽‍⚕️ Health Equity")
    selected_mst = st.sidebar.select_slider("Patient Skin Tone", options=list(mst_colors.keys()), value="MST-05")
    st.sidebar.markdown(f'<div style="background-color: {mst_colors[selected_mst]}; width: 100%; height: 30px; border-radius: 5px; border: 1px solid #ddd; margin-bottom: 20px;"></div>', unsafe_allow_html=True)
    return selected_mst

def main():
    st.title("🏥 NHS Unified Nursing Validator (PRO)")
    st.caption("Proprietary Validation Engine | Powered by Azure OpenAI + FoNS Library")
    current_skin_tone = sidebar_equity_check()
    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("1. Input Data")
        manual_text = st.text_area("Clinical Note:", height=300)
    with col2:
        st.subheader("2. Analysis")
        if st.button("🚀 Run Validation"):
            if not manual_text: st.warning("Enter text first.")
            else:
                evidence_text = ""
                if db:
                    with st.spinner("📚 Consulting Knowledge Graph..."):
                        try:
                            results = db.similarity_search(manual_text, k=3)
                            evidence_text = "\n\n".join([f"SOURCE ({doc.metadata.get('source', 'Unknown')}): {doc.page_content[:300]}..." for doc in results])
                        except: evidence_text = "Search failed."
                system_prompt = f"""You are the Nursing Validator.
GLOBAL SETTING: Skin Tone {current_skin_tone}.
EVIDENCE (FoNS): {evidence_text}
RULES:
1. Relational Care (Check Patient Voice).
2. Equity (Reject Redness for MST-06+).
3. Logic (ADPIE).
OUTPUT: Status, Score, Findings, Citations."""
                try:
                    client = AzureOpenAI(api_key=os.getenv("AZURE_OPENAI_API_KEY"), api_version=os.getenv("AZURE_OPENAI_API_VERSION"), azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"))
                    deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4o")
                    with st.spinner("🤖 Analyzing..."):
                        response = client.chat.completions.create(model=deployment_name, messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": manual_text}], temperature=0)
                    st.success("Complete")
                    st.markdown(response.choices[0].message.content)
                    if "WARNING" in response.choices[0].message.content or "INVALID" in response.choices[0].message.content:
                         if st.button("✍️ Suggest Better Documentation"):
                            st.info("AI Suggestion loading...")
                except Exception as e: st.error(f"AI Error: {e}")

if __name__ == "__main__":
    if check_password(): main()
