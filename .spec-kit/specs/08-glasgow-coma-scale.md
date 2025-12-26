# Spec 08: Glasgow Coma Scale (GCS) Profile

## Status
- [x] Specify
- [ ] Plan
- [ ] Tasks
- [ ] Implement

## Clinical Context
The Glasgow Coma Scale (GCS) is the most widely used scoring system for quantifying level of consciousness following traumatic brain injury. It's a critical assessment in emergency, neurology, and intensive care settings.

## Clinical Requirements

### Assessment Tool
- **Name**: Glasgow Coma Scale (GCS)
- **Total Range**: 3-15 (sum of three components)
- **Frequency**: Continuous monitoring for head injuries, altered consciousness
- **Components**:
  - Eye Response: 1-4
  - Verbal Response: 1-5
  - Motor Response: 1-6

### LOINC Coding
- **Total Score**: `9269-2` - Glasgow coma score total
- **Eye Response**: `9267-6` - Glasgow coma score eye opening
- **Verbal Response**: `9270-0` - Glasgow coma score verbal
- **Motor Response**: `9268-4` - Glasgow coma score motor

### Validation Rules
1. **Total Score**: Must be integer 3-15 (sum of components)
2. **Eye Response**: 1-4 (1=None, 2=To pain, 3=To sound, 4=Spontaneous)
3. **Verbal Response**: 1-5 (1=None, 2=Incomprehensible, 3=Inappropriate, 4=Confused, 5=Oriented)
4. **Motor Response**: 1-6 (1=None, 2=Extension, 3=Flexion, 4=Withdrawal, 5=Localizing, 6=Obeys)
5. **Status**: Must be 'final', 'amended', or 'corrected'
6. **All three components required** for a valid GCS assessment

### Clinical Safety
- **Score validation**: Total must equal sum of components
- **Component ranges**: Each component must be within valid range
- **Clinical interpretation**:
  - 13-15: Mild brain injury
  - 9-12: Moderate brain injury
  - 3-8: Severe brain injury

## FHIR Structure
```json
{
  "resourceType": "Observation",
  "status": "final",
  "code": {
    "coding": [{
      "system": "http://loinc.org",
      "code": "9269-2",
      "display": "Glasgow coma score total"
    }]
  },
  "subject": {
    "reference": "Patient/example"
  },
  "effectiveDateTime": "2025-12-26T00:00:00Z",
  "valueQuantity": {
    "value": 13,
    "unit": "{score}",
    "system": "http://unitsofmeasure.org"
  },
  "component": [
    {
      "code": {
        "coding": [{
          "system": "http://loinc.org",
          "code": "9267-6",
          "display": "Glasgow coma score eye opening"
        }]
      },
      "valueQuantity": {
        "value": 4,
        "unit": "{score}",
        "system": "http://unitsofmeasure.org"
      }
    },
    {
      "code": {
        "coding": [{
          "system": "http://loinc.org",
          "code": "9270-0",
          "display": "Glasgow coma score verbal"
        }]
      },
      "valueQuantity": {
        "value": 4,
        "unit": "{score}",
        "system": "http://unitsofmeasure.org"
      }
    },
    {
      "code": {
        "coding": [{
          "system": "http://loinc.org",
          "code": "9268-4",
          "display": "Glasgow coma score motor"
        }]
      },
      "valueQuantity": {
        "value": 5,
        "unit": "{score}",
        "system": "http://unitsofmeasure.org"
      }
    }
  ]
}
```

## Success Metrics
- Valid GCS scores (3-15) pass validation
- Invalid scores (outside range, incorrect component sum) are rejected
- All three components are present and within valid ranges
- Clear error messages guide users to correct input
