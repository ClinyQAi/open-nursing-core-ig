# Spec 11: Morse Fall Scale

## Status
- [x] Specify
- [ ] Plan
- [ ] Tasks
- [ ] Implement

## Clinical Context
The Morse Fall Scale is a rapid and simple method of assessing a patient's likelihood of falling. It's widely used in acute care, long-term care, and rehabilitation settings.

## Clinical Requirements

### Assessment Tool
- **Name**: Morse Fall Scale
- **Total Range**: 0-125 points
- **Risk Categories**:
  - 0-24: No risk
  - 25-50: Low risk
  - ≥51: High risk
- **Frequency**: On admission, after fall, and when condition changes

### LOINC Coding
- **Main Code**: `73830-2` - Morse Fall Scale panel

### Components (6 Risk Factors)
1. **History of falling**: No=0, Yes=25
2. **Secondary diagnosis**: No=0, Yes=15
3. **Ambulatory aid**: None/bedrest/nurse assist=0, Crutches/cane/walker=15, Furniture=30
4. **IV/Heparin lock**: No=0, Yes=20
5. **Gait**: Normal/bedrest/wheelchair=0, Weak=10, Impaired=20
6. **Mental status**: Oriented=0, Overestimates/forgets limitations=15

### Validation Rules
1. **Total Score**: Must be 0-125
2. **Each component**: Must match valid values
3. **Status**: Must be 'final', 'amended', or 'corrected'

## FHIR Structure
```json
{
  "resourceType": "Observation",
  "status": "final",
  "code": {
    "coding": [{
      "system": "http://loinc.org",
      "code": "73830-2",
      "display": "Morse Fall Scale panel"
    }]
  },
  "subject": {"reference": "Patient/example"},
  "effectiveDateTime": "2025-12-26T00:00:00Z",
  "valueQuantity": {
    "value": 45,
    "unit": "{score}",
    "system": "http://unitsofmeasure.org"
  }
}
```
