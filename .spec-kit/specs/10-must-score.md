# Spec 10: MUST Score (Malnutrition Universal Screening Tool)

## Status
- [x] Specify
- [ ] Plan
- [ ] Tasks
- [ ] Implement

## Clinical Context
The Malnutrition Universal Screening Tool (MUST) is a five-step screening tool to identify adults who are malnourished, at risk of malnutrition, or obese. It's a mandatory assessment in NHS hospitals and care homes.

## Clinical Requirements

### Assessment Tool
- **Name**: MUST (Malnutrition Universal Screening Tool)
- **Total Range**: 0-6+ (higher score = higher risk)
- **Risk Categories**:
  - 0: Low risk
  - 1: Medium risk
  - 2+: High risk
- **Frequency**: On admission, weekly, and when condition changes

### SNOMED Coding
- **Main Code**: `870431003` - Malnutrition Universal Screening Tool score
- **Alternative**: `108331000000102` - Malnutrition screening using MUST

### Components (5 Steps)
1. **BMI Score**: 0-2 points
   - BMI >20 (>30 obese) = 0
   - BMI 18.5-20 = 1
   - BMI <18.5 = 2

2. **Weight Loss Score**: 0-2 points
   - <5% unplanned weight loss = 0
   - 5-10% = 1
   - >10% = 2

3. **Acute Disease Effect**: 0-2 points
   - No acute disease = 0
   - Acutely ill with no nutritional intake for >5 days = 2

4. **Overall Risk Score**: Sum of steps 1-3 (0-6)

5. **Management Plan**: Based on risk category

### Validation Rules
1. **Total Score**: Must be integer 0-6
2. **Component Scores**: Each 0-2
3. **Status**: Must be 'final', 'amended', or 'corrected'
4. **All three components required** for valid assessment

### Clinical Safety
- **Risk stratification**: Determines nutritional intervention level
- **Component validation**: Each factor within valid range
- **Clinical actions**:
  - Low risk (0): Routine clinical care
  - Medium risk (1): Observe, document intake for 3 days
  - High risk (2+): Refer to dietitian, improve intake

## FHIR Structure
```json
{
  "resourceType": "Observation",
  "status": "final",
  "code": {
    "coding": [{
      "system": "http://snomed.info/sct",
      "code": "870431003",
      "display": "Malnutrition Universal Screening Tool score"
    }]
  },
  "subject": {
    "reference": "Patient/example"
  },
  "effectiveDateTime": "2025-12-26T00:00:00Z",
  "valueQuantity": {
    "value": 2,
    "unit": "{score}",
    "system": "http://unitsofmeasure.org"
  },
  "component": [
    {
      "code": {
        "coding": [{
          "system": "http://snomed.info/sct",
          "code": "846931000000101",
          "display": "Malnutrition Universal Screening Tool BMI score"
        }]
      },
      "valueQuantity": {
        "value": 0,
        "unit": "{score}"
      }
    },
    {
      "code": {
        "coding": [{
          "system": "http://snomed.info/sct",
          "code": "846941000000105",
          "display": "Malnutrition Universal Screening Tool weight loss score"
        }]
      },
      "valueQuantity": {
        "value": 1,
        "unit": "{score}"
      }
    },
    {
      "code": {
        "coding": [{
          "system": "http://snomed.info/sct",
          "code": "846951000000107",
          "display": "Malnutrition Universal Screening Tool acute disease effect score"
        }]
      },
      "valueQuantity": {
        "value": 1,
        "unit": "{score}"
      }
    }
  ]
}
```

## Success Metrics
- Valid MUST scores (0-6) pass validation
- Risk categories correctly identified
- All three components present and within valid ranges
- Clear error messages for invalid input
