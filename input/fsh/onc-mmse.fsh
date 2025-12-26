// =============================================================================
// Mini Mental State Examination (MMSE) Profile
// =============================================================================
Profile: ONCMMSE
Parent: ONCNursingAssessment
Id: onc-mmse
Title: "Mini Mental State Examination (MMSE)"
Description: "Mini Mental State Examination for cognitive function screening. Score 24-30=no impairment, 18-23=mild, 0-17=severe. Total range 0-30."
* status MS
* code = http://loinc.org#72106-8 "Mini-Mental State Examination (MMSE)"
* code MS
* value[x] only Quantity
* valueQuantity 1..1 MS
* valueQuantity.value obeys mmse-range
* valueQuantity.unit = "{score}"
* valueQuantity.system = "http://unitsofmeasure.org"
* valueQuantity ^short = "MMSE total score (0-30)"

Invariant: mmse-range
Description: "MMSE score must be between 0 and 30"
Expression: "$this >= 0 and $this <= 30"
Severity: #error
