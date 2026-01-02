"""
Upload Nursing LLM Model to Hugging Face
Run this script from wherever your trained model is saved (Colab, local machine, etc.)
"""

from huggingface_hub import HfApi, login, create_repo
import os

# =============================================================================
# CONFIGURATION
# =============================================================================
MODEL_NAME = "NurseCitizenDeveloper/nursing-llama-3-8b-fons"
LOCAL_MODEL_PATH = "./nursing-llama-3-8b-fons"  # Update this to your model's location

# Common locations to check:
# - Google Colab: "/content/nursing-llama-3-8b-fons"
# - Google Drive: "/content/drive/MyDrive/nursing-llama-3-8b-fons"
# - Local: "C:/Users/g0226/path/to/model"

# =============================================================================
# STEP 1: Login to Hugging Face
# =============================================================================
print("🔐 Logging in to Hugging Face...")
login()  # This will prompt for your token or use HF_TOKEN env variable

# =============================================================================
# STEP 2: Verify Model Files Exist
# =============================================================================
print(f"\n📁 Checking for model files in: {LOCAL_MODEL_PATH}")

required_files = [
    "config.json",
    "tokenizer_config.json", 
    "tokenizer.json",
    "special_tokens_map.json"
]

# Model weights (at least one should exist)
weight_files = [
    "pytorch_model.bin",
    "model.safetensors",
    "adapter_model.safetensors",  # If using LoRA
    "adapter_config.json"  # If using LoRA
]

missing_files = []
for file in required_files:
    if not os.path.exists(os.path.join(LOCAL_MODEL_PATH, file)):
        missing_files.append(file)

has_weights = any(os.path.exists(os.path.join(LOCAL_MODEL_PATH, f)) for f in weight_files)

if missing_files:
    print(f"⚠️  Missing required files: {missing_files}")
if not has_weights:
    print(f"❌ No model weight files found! Need one of: {weight_files}")
    print("\n💡 If you trained with LoRA, make sure adapter files are present.")
    exit(1)

print("✅ Model files verified!")

# =============================================================================
# STEP 3: Upload to Hugging Face
# =============================================================================
print(f"\n🚀 Uploading model to {MODEL_NAME}...")

api = HfApi()

# Create repo if it doesn't exist
try:
    create_repo(MODEL_NAME, exist_ok=True, repo_type="model")
    print(f"✅ Repository ready: https://huggingface.co/{MODEL_NAME}")
except Exception as e:
    print(f"ℹ️  Repository already exists or error: {e}")

# Upload all files
print("\n📤 Uploading files...")
api.upload_folder(
    folder_path=LOCAL_MODEL_PATH,
    repo_id=MODEL_NAME,
    repo_type="model",
    commit_message="Upload trained nursing LLM model"
)

print(f"\n✅ Upload complete!")
print(f"🔗 Model URL: https://huggingface.co/{MODEL_NAME}")
print(f"🔗 Space URL: https://huggingface.co/spaces/NurseCitizenDeveloper/relational-ai-nursing")
print("\n⏳ The Space should automatically restart and work now!")
