import os
import json
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

OUTPUT_FILE = "fons-relational-care-synthetic-v1.jsonl"
NUM_EXAMPLES_TO_GENERATE = 50 

CORE_PRINCIPLES = [
    "SBAR for Pain Management", "SBAR for Fall Risk", "SBAR for Sepsis Alert",
    "Documenting Relational Care", "Documenting Patient Education", "Handling Family Conflict",
    "Health Equity in Wound Care (Monk Scale)", "Safe Discharge Planning",
]

def generate_synthetic_data():
    print("?? Starting Synthetic Data Factory...")
    
    try:
        client = AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        )
        model_name = os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4o")
    except Exception as e:
        print(f"? Azure Connection Error: {e}")
        return

    generated_examples = []
    
    system_prompt = """You are a Clinical Educator creating a training dataset for an AI scribe.
Generate a JSON object with two keys: "transcript" (a messy clinical conversation) and "sbar" (a perfect, structured SBAR note).
The scenario must be unique and based on the requested clinical principle.
"""

    print(f"?? Generating {NUM_EXAMPLES_TO_GENERATE} examples...")
    
    for i in range(NUM_EXAMPLES_TO_GENERATE):
        principle = CORE_PRINCIPLES[i % len(CORE_PRINCIPLES)]
        print(f"   [{i+1}/{NUM_EXAMPLES_TO_GENERATE}] Generating: {principle}...", end="\r")

        try:
            response = client.chat.completions.create(
                model=model_name,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Generate a new, unique scenario for: '{principle}'"}
                ],
                response_format={"type": "json_object"},
                temperature=0.8
            )
            
            data = json.loads(response.choices[0].message.content)
            
            # --- THE FIX: VALIDATION STEP ---
            # Ensure both keys are strings before creating the example
            transcript_str = str(data.get('transcript', ''))
            sbar_str = str(data.get('sbar', ''))

            finetune_example = {
                "messages": [
                    {"role": "user", "content": f"Transcript: {transcript_str}"},
                    {"role": "model", "content": sbar_str}
                ]
            }
            generated_examples.append(finetune_example)

        except Exception as e:
            print(f"\n   ?? Error on example {i+1}: {e}")
            continue

    with open(OUTPUT_FILE, 'w') as f:
        for item in generated_examples:
            f.write(json.dumps(item) + "\n")
            
    print(f"\n\n? SUCCESS! Created '{OUTPUT_FILE}' with {len(generated_examples)} clean examples.")

if __name__ == "__main__":
    generate_synthetic_data()
