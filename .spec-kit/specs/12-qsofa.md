# Spec 12: qSOFA (Quick Sequential Organ Failure Assessment)

## Status
- [x] Specify
- [ ] Plan
- [ ] Tasks
- [ ] Implement

## Clinical Context
qSOFA is a bedside prompt to identify patients with suspected infection who are at greater risk for poor outcome. It's simpler than full SOFA and doesn't require lab tests.

## Clinical Requirements

### Assessment Tool
- **Name**: qSOFA (Quick SOFA)
- **Total Range**: 0-3 points
- **Risk Threshold**: ≥2 indicates high risk of poor outcome
- **Frequency**: With any suspected infection

### LOINC Coding
- **Main Code**: `96790-1` - Quick Sequential Organ Failure Assessment panel

### Components (3 Criteria)
1. **Respiratory rate**: ≥22/min = 1 point
2. **Altered mentation**: GCS <15 = 1 point
3. **Systolic BP**: ≤100 mmHg = 1 point

### Validation Rules
1. **Total Score**: Must be 0-3
2. **Each component**: 0 or 1
3. **Clinical action**: Score ≥2 requires urgent assessment

## FHIR Structure
```json
{
  "resourceType": "Observation",
  "status": "final",
  "code": {
    "coding": [{
      "system": "http://loinc.org",
      "code": "96790-1",
      "display": "Quick Sequential Organ Failure Assessment panel"
    }]
  },
  "subject": {"reference": "Patient/example"},
  "effectiveDateTime": "2025-12-26T00:00:00Z",
  "valueQuantity": {
    "value": 2,
    "unit": "{score}",
    "system": "http://unitsofmeasure.org"
  }
}
```
