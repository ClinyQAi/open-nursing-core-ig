
import os
import argparse
from huggingface_hub import login, HfApi

def upload_to_hub(dataset_path: str, repo_name: str, token: str = None, private: bool = True):
    """
    Uploads a local dataset (JSONL) to Hugging Face Hub using HfApi.
    
    Args:
        dataset_path: Path to the local .jsonl file.
        repo_name: Name of the repository on HF (e.g., 'username/dataset-name').
        token: HF API Token (optional if logged in via CLI).
        private: Whether the dataset should be private.
    """
    print(f"📦 Preparing to upload '{dataset_path}' to '{repo_name}'...")
    
    # 1. Login if token provided
    if token:
        print("🔑 Logging in to Hugging Face...")
        login(token=token)
    
    # 2. Check if file exists
    if not os.path.exists(dataset_path):
        raise FileNotFoundError(f"Dataset file not found: {dataset_path}")

    api = HfApi()
    
    # 3. Create Repo if it doesn't exist
    try:
        print(f"🔨 Creating/Checking repository '{repo_name}'...")
        api.create_repo(repo_id=repo_name, repo_type="dataset", private=private, exist_ok=True)
    except Exception as e:
        print(f"⚠️  Repo creation check failed (might already exist or permission issue): {e}")

    # 4. Upload File
    print(f"🚀 Uploading file to Hugging Face Hub...")
    try:
        api.upload_file(
            path_or_fileobj=dataset_path,
            path_in_repo=os.path.basename(dataset_path),
            repo_id=repo_name,
            repo_type="dataset"
        )
        print(f"✨ Success! Your dataset is live at: https://huggingface.co/datasets/{repo_name}")
        print("ℹ️  Note: On Colab, load it using: load_dataset('json', data_files='fons-relational-care-synthetic-v1.jsonl', split='train')")
    except Exception as e:
        print(f"❌ Failed to upload dataset: {e}")
        print("Tip: Check your token permissions and repo name.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upload Nursing Dataset to Hugging Face")
    parser.add_argument("--file", type=str, default="fons-relational-care-synthetic-v1.jsonl", help="Path to local JSONL file")
    parser.add_argument("--repo", type=str, required=True, help="Target HF Repo (e.g. 'your-username/nursing-sbar-instruct')")
    parser.add_argument("--token", type=str, help="Hugging Face Write Token (optional)")
    parser.add_argument("--public", action="store_true", help="Make dataset public (default is private)")
    
    args = parser.parse_args()
    
    upload_to_hub(args.file, args.repo, args.token, not args.public)
