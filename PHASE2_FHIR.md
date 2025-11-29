# Phase 2.3: EHR/FHIR Integration

## Overview

**Phase 2.3** integrates the application with Electronic Health Record (EHR) systems through:
- **FHIR APIs** (Fast Healthcare Interoperability Resources)
- **HL7 v2 messaging** (legacy EHR systems)
- **Real patient data** from hospital systems
- **Bi-directional data sync**

**Prerequisites:**
- Phase 2.1 (PostgreSQL Database)
- Phase 2.2 (Analytics) - optional

---

## Features

### 1. **FHIR API Integration**

#### Patient Data Retrieval
```python
from ehr_integration import FHIRAPIClient

client = FHIRAPIClient("https://fhir.hospital.com")

# Get patient demographics
patient = client.get_patient("12345")

# Get patient's conditions
conditions = client.get_patient_conditions("12345")

# Get vital signs and labs
observations = client.get_patient_observations("12345")

# Get active care plans
care_plans = client.get_patient_care_plans("12345")

# Get patient goals
goals = client.get_patient_goals("12345")
```

#### Data Submission
```python
# Create new observation (e.g., blood pressure reading)
obs_id = client.create_observation("12345", {
    "code": {"coding": [{"code": "85354-9"}]},  # BP
    "valueQuantity": {"value": 120, "unit": "mmHg"}
})

# Update care plan
client.update_care_plan("cp-123", updated_data)
```

### 2. **HL7 v2 Messaging**

For integration with legacy EHR systems:

```python
from ehr_integration import HL7Parser

parser = HL7Parser()

# Parse incoming HL7 message
message = """MSH|^~\\&|APP|FAC|APP|FAC|20251129...
PID|||12345||Doe^John||19800101|M
OBX|1|NM|85354-9||120||80-120|N"""

parsed = parser.parse_hl7_message(message)
# Returns: {
#   "patient": {"id": "12345", "name": "Doe^John", ...},
#   "observations": [{"type": "85354-9", "value": "120", ...}]
# }
```

### 3. **FHIR Resource Building**

Helper functions to create standardized FHIR resources:

```python
from ehr_integration import FHIRResourceBuilder

builder = FHIRResourceBuilder()

# Create condition
condition = builder.build_condition(
    patient_id="12345",
    code="80891009",  # SNOMED code for type 2 diabetes
    display="Type 2 Diabetes Mellitus",
    onset_date="2020-01-15"
)

# Create observation (lab result)
observation = builder.build_observation(
    patient_id="12345",
    code="2345-7",  # Glucose
    value=125,
    unit="mg/dL",
    reference_range=(70, 100)
)

# Create goal
goal = builder.build_goal(
    patient_id="12345",
    description="Achieve HbA1c < 7%",
    status="in-progress",
    target_date="2026-01-15"
)
```

### 4. **EHR Integration Manager**

Comprehensive manager for all EHR operations:

```python
from ehr_integration import EHRIntegrationManager

manager = EHRIntegrationManager(
    fhir_url="https://fhir.hospital.com",
    api_key="your-api-key"
)

# Sync all patient data
patient_record = manager.sync_patient_data("12345")
# Returns complete record with:
# - Patient demographics
# - Conditions
# - Observations
# - Care plans
# - Goals

# Send observation to EHR
obs_id = manager.send_observation_to_ehr("12345", observation)

# Process incoming HL7
parsed = manager.process_hl7_message(hl7_message)
```

---

## Setup Instructions

### 1. Prerequisites

```bash
# Install FHIR libraries
pip install fhir-parser requests

# Or add to requirements.txt
fhir-parser==1.2.0
requests==2.28.0
```

### 2. Configure FHIR Server Connection

```bash
# Update .env.production
EHR_FHIR_URL=https://fhir.hospital.com
EHR_API_KEY=your_api_key
EHR_TIMEOUT=10
EHR_VERIFY_SSL=true
EHR_SYNC_INTERVAL=3600  # seconds
```

### 3. Register with FHIR Server

Most FHIR servers require:
1. **OAuth 2.0 credentials** or **API key**
2. **Client registration** (get client_id, client_secret)
3. **Scope permissions** (read, write, admin)

Example (Azure Health Data Services):
```bash
# Register application
az ad app create \
  --display-name "Nursing Validator" \
  --reply-urls "http://localhost:8501"

# Get credentials
AZURE_AD_TENANT_ID=your-tenant-id
AZURE_AD_CLIENT_ID=your-client-id
AZURE_AD_CLIENT_SECRET=your-secret
```

### 4. Initialize EHR Integration

```python
from ehr_integration import EHRIntegrationManager
import os

manager = EHRIntegrationManager(
    fhir_url=os.getenv("EHR_FHIR_URL"),
    api_key=os.getenv("EHR_API_KEY")
)

# Verify connection
patient = manager.fhir_client.get_patient("test-patient-id")
if patient:
    print("✅ Connected to FHIR server")
else:
    print("❌ Failed to connect")
```

---

## FHIR Resources Supported

### Patient
- Demographics
- Contact information
- Insurance information

### Condition
- Diagnoses
- Problems
- Chronic conditions

### Observation
- Vital signs (BP, temp, O2)
- Lab results
- Assessment findings

### Goal
- Clinical goals
- Patient goals
- Progress tracking

### CarePlan
- Nursing care plans
- Treatment protocols
- Intervention activities

### Medication
- Current medications
- Dosage information
- Allergies

### Procedure
- Surgical procedures
- Clinical procedures
- Completed interventions

### Appointment
- Scheduled visits
- Follow-ups
- Clinic appointments

---

## Data Synchronization

### Real-time Sync

```python
# Background task to sync patient data
import asyncio
import time

async def sync_patient_data_loop(patient_id, interval=3600):
    """Continuously sync patient data."""
    while True:
        patient_data = manager.sync_patient_data(patient_id)
        # Save to database
        from database import save_patient_record
        save_patient_record(patient_id, patient_data)
        
        await asyncio.sleep(interval)

# Run in background
asyncio.create_task(sync_patient_data_loop("12345"))
```

### Event-Driven Sync

```python
# Listen for EHR events (webhook)
@st.streamlit_route("/ehr-webhook", methods=["POST"])
def receive_ehr_update(request):
    data = request.json
    patient_id = data["patient_id"]
    
    # Sync on update
    patient_data = manager.sync_patient_data(patient_id)
    
    return {"status": "updated"}
```

---

## HL7 v2 Message Types

### ADT (Admission/Discharge/Transfer)
```
MSH|^~\&|SENDAPP|SENDFAC|RECAPP|RECFAC|20251129120000||ADT^A01
PID|1||12345||Doe^John
```

### ORM (Order Message)
```
MSH|^~\&|SENDAPP|SENDFAC|RECAPP|RECFAC|20251129120000||ORM^O01
ORC|NW|123456
OBX|1|NM|85354-9||120||80-120|N
```

### ORU (Observation/Result - Lab)
```
MSH|^~\&|LAB|HOSPITAL|APP|FACILITY|20251129120000||ORU^R01
OBX|1|NM|2345-7||125||70-100|N
```

---

## Security Considerations

### HIPAA Compliance
- ✅ Encryption in transit (HTTPS/TLS)
- ✅ Encryption at rest (database encryption)
- ✅ API key management
- ✅ Audit logging
- ✅ Access controls
- ✅ Data anonymization
- ✅ Consent management

### OAuth 2.0 Implementation

```python
from oauthlib.oauth2 import WebApplicationClient

client_id = os.getenv("AZURE_AD_CLIENT_ID")
client_secret = os.getenv("AZURE_AD_CLIENT_SECRET")

client = WebApplicationClient(client_id)

# Get authorization URL
authorization_url, state = client.prepare_request_uri(
    "https://login.microsoftonline.com/common/oauth2/v2.0/authorize"
)

# Exchange code for token
token = client.prepare_refresh_token_request_body(
    refresh_token, client_id, client_secret
)
```

### Certificate Pinning

```python
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.ssl_ import create_urllib3_context

class SSLAdapter(HTTPAdapter):
    def init_poolmanager(self, *args, **kwargs):
        ctx = create_urllib3_context()
        ctx.load_verify_locations('hospital_ca.pem')
        kwargs['ssl_context'] = ctx
        return super().init_poolmanager(*args, **kwargs)

session = requests.Session()
session.mount('https://', SSLAdapter())
```

---

## Troubleshooting

### Connection Errors

```python
# Test connection
try:
    patient = client.get_patient("test-id")
    if patient:
        print("✅ Connection successful")
    else:
        print("❌ Invalid patient ID")
except Exception as e:
    print(f"❌ Connection failed: {e}")
```

### Authentication Issues

```bash
# Verify API key is valid
curl -H "Authorization: Bearer YOUR_API_KEY" \
  https://fhir.hospital.com/Patient/test-id

# Check token expiry
# Refresh token if needed
```

### FHIR Server Compatibility

Some common FHIR servers:
- **Azure Health Data Services**: FHIR R4
- **Cerner**: FHIR R4 (with extensions)
- **Epic**: FHIR R4 (limited)
- **InterSystems**: FHIR R3/R4
- **HAPI FHIR**: Full FHIR support

Verify server's FHIR version:
```bash
curl https://fhir.hospital.com/metadata
```

---

## Integration with Main App

### Add Patient Context to Chat

```python
# In app_phase2.py

if st.session_state.get("patient_id"):
    manager = EHRIntegrationManager(ehr_fhir_url, api_key)
    patient_data = manager.sync_patient_data(patient_id)
    
    # Use in chat context
    context = f"""
    Patient: {patient_data['patient']['name']}
    Conditions: {', '.join([c['code']['text'] for c in patient_data['conditions']])}
    """
    
    # Include in LLM prompt
    qa = RetrievalQA.from_chain_type(
        llm=AzureOpenAI(),
        chain_type="stuff",
        retriever=vector_db.as_retriever(),
        return_source_documents=True,
    )
    response = qa.run(f"{context}\n\nQuestion: {user_input}")
```

### Save Assessments Back to EHR

```python
# After nursing assessment
assessment_observation = builder.build_observation(
    patient_id=st.session_state.patient_id,
    code="84811-6",  # Nursing assessment
    value="Assessment complete",
    unit="text"
)

obs_id = manager.send_observation_to_ehr(
    st.session_state.patient_id,
    assessment_observation
)

st.success(f"Assessment saved to EHR: {obs_id}")
```

---

## Performance Optimization

### Caching

```python
import streamlit as st
from functools import lru_cache

@st.cache_data(ttl=3600)
def get_patient_data(patient_id):
    return manager.sync_patient_data(patient_id)
```

### Batch Operations

```python
# Sync multiple patients
patient_ids = ["123", "456", "789"]
for patient_id in patient_ids:
    patient_data = manager.sync_patient_data(patient_id)
    # Process...
```

### Pagination

```python
# Most FHIR servers support _count and _offset
url = f"{self.base_url}/Observation?subject=Patient/{patient_id}&_count=100&_offset=0"
```

---

## Next Steps

1. **Get FHIR server credentials** from your EHR vendor
2. **Test connection** to FHIR server
3. **Configure patient sync** frequency
4. **Implement UI** for patient selection
5. **Add audit logging** for all data access
6. **Deploy to staging** and test with real data
7. **Proceed to Phase 2.4** - Mobile App

---

## Files Created/Modified

**New Files:**
- `ehr_integration.py` (400+ lines)

**Integration Points:**
- Update `app_phase2.py` for patient selection
- Add `save_patient_record()` to database.py
- Update requirements.txt with fhir-parser

**Documentation:**
- `PHASE2_FHIR.md` (this file)

---

## References

- [FHIR Specification](http://hl7.org/fhir/R4/)
- [HL7 v2 Reference](http://www.hl7.org/implement/standards/product_brief.cfm?product_id=20)
- [SMART on FHIR](http://docs.smarthealthit.org/)
- [Azure Health Data Services](https://learn.microsoft.com/en-us/azure/healthcare-apis/)

---

*Phase 2.3 Implementation - November 29, 2025*
