# Spec 13: Barthel Index

## Status
- [x] Specify
- [ ] Plan
- [ ] Tasks
- [ ] Implement

## Clinical Context
The Barthel Index measures performance in activities of daily living (ADL). It's widely used in rehabilitation to assess functional independence.

## Clinical Requirements

### Assessment Tool
- **Name**: Barthel Index
- **Total Range**: 0-100 points
- **Independence Levels**:
  - 0-20: Total dependency
  - 21-60: Severe dependency
  - 61-90: Moderate dependency
  - 91-99: Slight dependency
  - 100: Independent
- **Frequency**: On admission, weekly, at discharge

### LOINC Coding
- **Main Code**: `83254-5` - Barthel Index

### Components (10 Activities)
Each scored 0, 5, 10, or 15 depending on activity

1. Feeding (0-10)
2. Bathing (0-5)
3. Grooming (0-5)
4. Dressing (0-10)
5. Bowel control (0-10)
6. Bladder control (0-10)
7. Toilet use (0-10)
8. Transfers (0-15)
9. Mobility (0-15)
10. Stairs (0-10)

### Validation Rules
1. **Total Score**: Must be 0-100
2. **Components**: Must match valid values for each activity
3. **Increments of 5**: Total always divisible by 5

## FHIR Structure
```json
{
  "resourceType": "Observation",
  "status": "final",
  "code": {
    "coding": [{
      "system": "http://loinc.org",
      "code": "83254-5",
      "display": "Barthel Index"
    }]
  },
  "subject": {"reference": "Patient/example"},
  "effectiveDateTime": "2025-12-26T00:00:00Z",
  "valueQuantity": {
    "value": 85,
    "unit": "{score}",
    "system": "http://unitsofmeasure.org"
  }
}
```
