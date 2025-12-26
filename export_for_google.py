
import json
import os
import sys

# Configuration
INPUT_FILE = r'c:\Users\g0226\OneDrive\Desktop\fhir-git\open-nursing-core-ig\chroma_db_fons_simple\database.json'
OUTPUT_FILE = r'c:\Users\g0226\OneDrive\Desktop\fhir-git\open-nursing-core-ig\fons_knowledge_google.jsonl'

def convert_to_google_format():
    """Reads the database.json and writes a Google Vertex AI compatible JSONL file."""
    
    if not os.path.exists(INPUT_FILE):
        print(f"Error: Input file not found at {INPUT_FILE}")
        return

    print(f"Reading from {INPUT_FILE}...")
    try:
        with open(INPUT_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error reading JSON: {e}")
        return

    documents = data.get("documents", [])
    print(f"Found {len(documents)} documents to process.")

    print(f"Writing to {OUTPUT_FILE}...")
    count = 0
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as out_f:
        for doc in documents:
            # Vertex AI Vector Search Format:
            # {
            #   "id": "...", 
            #   "embedding": [ ... ], 
            #   "restricts": [ { "namespace": "...", "allow": [ "..." ] } ]
            # }
            
            # Map metadata to restricts
            restricts = []
            if "metadata" in doc and doc["metadata"]:
                for key, value in doc["metadata"].items():
                    # Vertex AI restricts must be strings
                    restricts.append({
                        "namespace": key,
                        "allow": [str(value)]
                    })
            
            # Construct entry
            entry = {
                "id": doc.get("id", str(count)),
                "embedding": doc.get("embedding", []),
                "restricts": restricts
            }
            
            # Optional: Include original content/metadata for reference if allowed by schema, 
            # but strictly Vector Search consumes the above. 
            # We can also add a "crowding_tag" if needed.
            # For now, we stick to the core requirements. 
            # If the user wants to use this for hybrid search, they might need the content separate.
            # We will ADD 'original_content' and 'original_metadata' fields. 
            # Vertex AI might ignore unknown fields or we might need them for payload.
            # To be safe for *import*, standard Vector Search JSONL usually only contains the vector data.
            # However, let's keep it clean standard format first.
            
            json.dump(entry, out_f)
            out_f.write('\n')
            count += 1
            
            if count % 1000 == 0:
                print(f"Processed {count} documents...")

    print(f"Successfully exported {count} documents to {OUTPUT_FILE}")

if __name__ == "__main__":
    convert_to_google_format()
