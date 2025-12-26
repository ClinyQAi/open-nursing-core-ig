# Spec 14: Mini Mental State Examination (MMSE)

## Status
- [x] Specify
- [ ] Plan
- [ ] Tasks
- [ ] Implement

## Clinical Context
The Mini Mental State Examination (MMSE) is a widely used test of cognitive function among the elderly. It's used to screen for dementia and assess cognitive impairment.

## Clinical Requirements

### Assessment Tool
- **Name**: MMSE (Mini Mental State Examination)
- **Total Range**: 0-30 points
- **Cognitive Impairment Levels**:
  - 24-30: No cognitive impairment
  - 18-23: Mild cognitive impairment
  - 0-17: Severe cognitive impairment
- **Frequency**: On admission, periodically for at-risk patients

### LOINC Coding
- **Main Code**: `72106-8` - Mini-Mental State Examination (MMSE)

### Components (5 Domains)
1. **Orientation** (10 points): Time and place
2. **Registration** (3 points): Immediate recall of 3 words
3. **Attention & Calculation** (5 points): Serial 7s or spelling backwards
4. **Recall** (3 points): Delayed recall of 3 words
5. **Language** (9 points): Naming, repetition, comprehension, reading, writing, drawing

### Validation Rules
1. **Total Score**: Must be 0-30
2. **Status**: Must be 'final', 'amended', or 'corrected'
3. **Clinical significance**: Score <24 suggests cognitive impairment

### Clinical Safety
- **Screening tool**: Not diagnostic, requires follow-up assessment
- **Age/education adjusted**: Interpretation varies by demographics
- **Clinical actions**:
  - 24-30: Routine monitoring
  - 18-23: Further cognitive assessment
  - <18: Comprehensive dementia evaluation

## FHIR Structure
```json
{
  "resourceType": "Observation",
  "status": "final",
  "code": {
    "coding": [{
      "system": "http://loinc.org",
      "code": "72106-8",
      "display": "Mini-Mental State Examination (MMSE)"
    }]
  },
  "subject": {"reference": "Patient/example"},
  "effectiveDateTime": "2025-12-26T00:00:00Z",
  "valueQuantity": {
    "value": 26,
    "unit": "{score}",
    "system": "http://unitsofmeasure.org"
  }
}
```

## Success Metrics
- Valid MMSE scores (0-30) pass validation
- Cognitive impairment levels correctly identified
- Clear error messages for invalid scores
