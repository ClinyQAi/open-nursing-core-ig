# Spec 09: Waterlow Score Profile

## Status
- [x] Specify
- [ ] Plan
- [ ] Tasks
- [ ] Implement

## Clinical Context
The Waterlow Score is a pressure ulcer risk assessment tool widely used in the NHS and UK healthcare settings. It's complementary to the Braden Scale but uses different risk factors and scoring methodology.

## Clinical Requirements

### Assessment Tool
- **Name**: Waterlow Pressure Ulcer Risk Assessment
- **Total Range**: 0-64+ (higher score = higher risk)
- **Risk Categories**:
  - 10-14: At risk
  - 15-19: High risk
  - 20+: Very high risk
- **Frequency**: On admission, weekly, and when condition changes

### SNOMED Coding
- **Main Code**: `443846001` - Waterlow score (observable entity)
- **Risk Assessment**: `225358003` - Pressure ulcer risk assessment

### Risk Factors (Components)
1. **Build/Weight for Height**: 0-3 points
2. **Visual Skin Type**: 0-3 points
3. **Sex/Age**: 0-5 points
4. **Continence**: 0-3 points
5. **Mobility**: 0-5 points
6. **Appetite**: 0-3 points
7. **Special Risks** (multiple selections possible):
   - Tissue Malnutrition: 0-8 points
   - Neurological Deficit: 0-6 points
   - Major Surgery/Trauma: 0-5 points
   - Medication: 0-4 points

### Validation Rules
1. **Total Score**: Must be integer ≥ 0
2. **Status**: Must be 'final', 'amended', or 'corrected'
3. **All core components required** (Build, Skin, Sex/Age, Continence, Mobility, Appetite)
4. **Special risks optional** but commonly assessed

### Clinical Safety
- **Risk stratification**: Score determines intervention level
- **Component validation**: Each factor must be within valid range
- **Clinical interpretation guides care planning**

## FHIR Structure
```json
{
  "resourceType": "Observation",
  "status": "final",
  "code": {
    "coding": [{
      "system": "http://snomed.info/sct",
      "code": "443846001",
      "display": "Waterlow score"
    }]
  },
  "subject": {
    "reference": "Patient/example"
  },
  "effectiveDateTime": "2025-12-26T00:00:00Z",
  "valueQuantity": {
    "value": 12,
    "unit": "{score}",
    "system": "http://unitsofmeasure.org"
  },
  "component": [
    {
      "code": {
        "coding": [{
          "system": "http://snomed.info/sct",
          "code": "248326004",
          "display": "Body build"
        }]
      },
      "valueQuantity": {
        "value": 1,
        "unit": "{score}"
      }
    }
    // Additional components...
  ]
}
```

## Success Metrics
- Valid Waterlow scores pass validation
- Risk categories correctly identified
- All required components present
- Clear error messages for invalid input
