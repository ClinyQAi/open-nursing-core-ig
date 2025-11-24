import streamlit as st
import os
from dotenv import load_dotenv
from openai import AzureOpenAI
import json

load_dotenv()

# Initialize Azure OpenAI client
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

st.set_page_config(page_title="Nursing IG Validator", layout="wide")
st.title("🩺 Nursing IG Validator")
st.markdown("Validate and evaluate FHIR (Fast Healthcare Interoperability Resources) data for nursing implementations.")

# Sidebar for options
with st.sidebar:
    st.header("Settings")
    validation_type = st.radio(
        "Select validation type:",
        ["Schema Validation", "Data Type Check", "Required Fields", "Custom Validation"]
    )

# Main content area
col1, col2 = st.columns(2)

with col1:
    st.subheader("Input Data")
    fhir_data = st.text_area(
        "Enter FHIR JSON data to validate:",
        height=300,
        placeholder='{"resourceType": "Patient", "id": "example"}'
    )

with col2:
    st.subheader("Validation Results")
    if st.button("Validate", key="validate_btn"):
        if fhir_data.strip():
            with st.spinner("Validating FHIR data..."):
                try:
                    response = client.chat.completions.create(
                        model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
                        messages=[
                            {"role": "system", "content": "You are a FHIR data validator. Analyze the provided FHIR data and provide validation results."},
                            {"role": "user", "content": f"Please validate this FHIR data:\n\n{fhir_data}"}
                        ]
                    )
                    result = response.choices[0].message.content
                    st.success("Validation completed!")
                    st.markdown(result)
                except json.JSONDecodeError:
                    st.error("❌ Invalid JSON format. Please check your input.")
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
        else:
            st.warning("⚠️ Please enter FHIR data to validate.")

st.divider()
st.footer("Nursing IG Validator - Powered by Azure OpenAI GPT-4")
