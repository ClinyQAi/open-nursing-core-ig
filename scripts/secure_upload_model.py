"""
Secure Model Upload to Hugging Face
This script will upload your nursing model using your HF token
"""

import os
from huggingface_hub import HfApi, login

# =============================================================================
# IMPORTANT: Set your token as an environment variable for security
# =============================================================================
# In PowerShell, run: $env:HF_TOKEN = "your_actual_token_here"
# Or paste it when prompted below

HF_TOKEN = os.getenv("HF_TOKEN") or input("Paste your HF token: ")

# Login
print("🔐 Logging in to Hugging Face...")
login(token=HF_TOKEN)

# =============================================================================
# WHERE IS YOUR MODEL?
# =============================================================================
print("\n📍 Where is your trained model saved?")
print("1. Google Colab (/content/...)")
print("2. Google Drive (mounted in Colab)")
print("3. Local computer")
print("4. I don't have the model files")

choice = input("\nEnter choice (1-4): ")

if choice == "4":
    print("\n⚠️  You need to locate or re-train the model first.")
    print("Check your Colab notebooks or Google Drive for:")
    print("  - nursing-llama-3-8b-fons/")
    print("  - Any folder with model.safetensors or pytorch_model.bin")
    exit()

model_path = input("\nEnter the full path to your model folder: ")

# Verify files exist
if not os.path.exists(model_path):
    print(f"❌ Path not found: {model_path}")
    exit()

# =============================================================================
# UPLOAD
# =============================================================================
print(f"\n🚀 Uploading from: {model_path}")
print(f"📤 Destination: NurseCitizenDeveloper/nursing-llama-3-8b-fons")

api = HfApi()

try:
    api.upload_folder(
        folder_path=model_path,
        repo_id="NurseCitizenDeveloper/nursing-llama-3-8b-fons",
        repo_type="model",
        token=HF_TOKEN
    )
    print("\n✅ Upload successful!")
    print("🔗 https://huggingface.co/NurseCitizenDeveloper/nursing-llama-3-8b-fons")
except Exception as e:
    print(f"\n❌ Upload failed: {e}")
    print("\n💡 If you see 'permission denied', you need a WRITE token:")
    print("   1. Go to https://huggingface.co/settings/tokens")
    print("   2. Create a new token with 'Write' access")
    print("   3. Run this script again with the new token")
