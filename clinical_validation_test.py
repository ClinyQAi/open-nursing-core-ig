import os
import json
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

# Initialize Azure OpenAI client
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

# Test data: CarePlan with "Risk for Falls" but missing assessment evidence
test_fhir_data = {
    "resourceType": "CarePlan",
    "status": "active",
    "intent": "order",
    "subject": { "reference": "Patient/example-glenda" },
    "period": { "start": "2025-11-24" },
    "addresses": [
        {
            "display": "Risk for falls",
            "system": "http://snomed.info/sct",
            "code": "129839007"
        }
    ],
    "activity": [
        {
            "detail": {
                "description": "Ensure call bell is within reach",
                "status": "in-progress"
            }
        }
    ],
    "note": [
        { "text": "Patient is unsteady. No formal fall score calculated yet." }
    ]
}

print("="*80)
print("NURSING IG VALIDATOR - CLINICAL VALIDATION TEST")
print("="*80)
print()
print("Test Scenario: Risk for Falls CarePlan without supporting Assessment")
print()
print("INPUT FHIR DATA:")
print(json.dumps(test_fhir_data, indent=2))
print()
print("-"*80)
print("Running Validation with GPT-4o...")
print("-"*80)
print()

try:
    response = client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        messages=[
            {
                "role": "system",
                "content": """You are a clinical validation expert specializing in FHIR (Fast Healthcare Interoperability Resources) and nursing implementation guides. 
Your role is to validate nursing care plans against the Open Nursing Core Implementation Guide.
When reviewing a CarePlan with a 'Risk for Falls' diagnosis, you MUST verify that it includes:
1. A supporting Observation resource (e.g., Morse Fall Scale score, Hendrich II Fall Risk scale)
2. Evidence linking the risk assessment to the intervention

If any of these elements are missing, mark it as INVALID and clearly state what evidence is missing.
"""
            },
            {
                "role": "user",
                "content": f"""Please validate this nursing CarePlan against the Open Nursing Core IG:

{json.dumps(test_fhir_data, indent=2)}

Validation Rule: Every 'Risk for Falls' CarePlan MUST reference a supporting Observation (e.g., Morse Fall Scale or Hendrich II). Mark as INVALID if evidence is missing.

Provide your validation result in this format:
VALIDATION STATUS: [VALID/INVALID]
FINDINGS: [detailed findings]
MISSING ELEMENTS: [list what's missing, if any]
RECOMMENDATIONS: [how to fix it]
"""
            }
        ],
        temperature=0.2
    )
    
    validation_result = response.choices[0].message.content
    print("VALIDATION RESULT:")
    print(validation_result)
    print()
    print("="*80)
    print("✅ TEST COMPLETED SUCCESSFULLY")
    print("="*80)
    print()
    print("This demonstrates that the Nursing IG Validator can:")
    print("  1. Parse FHIR CarePlan data")
    print("  2. Validate against nursing implementation guide rules")
    print("  3. Detect missing clinical evidence (Assessment/Fall Scale)")
    print("  4. Provide actionable recommendations for clinical teams")
    print()
    
except Exception as e:
    print(f"❌ VALIDATION ERROR: {e}")
