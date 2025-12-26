// =============================================================================
// Waterlow Score Profile (NHS Pressure Ulcer Risk Assessment)
// =============================================================================
Profile: ONCWaterlowScore
Parent: ONCNursingAssessment
Id: onc-waterlow-score
Title: "Waterlow Score"
Description: "Waterlow Pressure Ulcer Risk Assessment - NHS standard tool. Score ≥10 indicates at risk, ≥15 high risk, ≥20 very high risk."
* status MS
* code = https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes#waterlow-score "Waterlow Score"
* code MS
* value[x] only Quantity
* valueQuantity 1..1 MS
* valueQuantity.value obeys waterlow-range
* valueQuantity.unit = "{score}"
* valueQuantity.system = "http://unitsofmeasure.org"
* valueQuantity ^short = "Waterlow total score (0-64+, higher = higher risk)"
* component 0..* MS
* component ^short = "Risk factor components (build, skin type, age, continence, mobility, appetite, special risks)"

Invariant: waterlow-range
Description: "Waterlow score must be 0 or greater"
Expression: "$this >= 0"
Severity: #error
