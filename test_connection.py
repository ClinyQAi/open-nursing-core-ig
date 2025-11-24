import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

try:
    client = AzureOpenAI(
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
    )
    print("🩺 Connecting to Nursing AI Judge...")
    response = client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        messages=[{"role": "user", "content": "Are you ready to validate FHIR data?"}]
    )
    print(f"✅ SUCCESS: {response.choices[0].message.content}")
except Exception as e:
    print(f"❌ ERROR: {e}")
