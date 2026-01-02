// =============================================================================
// Morse Fall Scale Profile
// =============================================================================
Profile: ONCMorseFallScale
Parent: ONCNursingAssessment
Id: onc-morse-fall-scale
Title: "Morse Fall Scale"
Description: "Morse Fall Scale for assessing fall risk. Score 0-24=no risk, 25-50=low risk, ≥51=high risk. Total range 0-125."
* status MS
* code = http://loinc.org#73830-2 "Fall risk assessment"
* code MS
* value[x] only Quantity
* valueQuantity 1..1 MS
* valueQuantity.value obeys morse-range
* valueQuantity.unit = "{score}"
* valueQuantity.system = "http://unitsofmeasure.org"
* valueQuantity ^short = "Morse Fall Scale total (0-125)"

Invariant: morse-range
Description: "Morse Fall Scale must be between 0 and 125"
Expression: "$this >= 0 and $this <= 125"
Severity: #error

// =============================================================================
// qSOFA (Quick Sequential Organ Failure Assessment) Profile
// =============================================================================
Profile: ONCqSOFA
Parent: ONCNursingAssessment
Id: onc-qsofa
Title: "qSOFA (Quick SOFA)"
Description: "Quick Sequential Organ Failure Assessment for sepsis screening. Score ≥2 indicates high risk. Total range 0-3."
* status MS
* code = http://loinc.org#96790-1 "SOFA Total Score"
* code MS
* value[x] only Quantity
* valueQuantity 1..1 MS
* valueQuantity.value obeys qsofa-range
* valueQuantity.unit = "{score}"
* valueQuantity.system = "http://unitsofmeasure.org"
* valueQuantity ^short = "qSOFA total score (0-3, ≥2 = high risk)"

Invariant: qsofa-range
Description: "qSOFA score must be between 0 and 3"
Expression: "$this >= 0 and $this <= 3"
Severity: #error

// =============================================================================
// Barthel Index Profile
// =============================================================================
Profile: ONCBarthelIndex
Parent: ONCNursingAssessment
Id: onc-barthel-index
Title: "Barthel Index"
Description: "Barthel Index for measuring independence in activities of daily living (ADL). Score 0-20=total dependency, 91-99=slight dependency, 100=independent. Total range 0-100."
* status MS
* code = https://opennursingcoreig.com/CodeSystem/onc-observation-codes#barthel-score "Barthel Index Score"
* code MS
* value[x] only Quantity
* valueQuantity 1..1 MS
* valueQuantity.value obeys barthel-range
* valueQuantity.unit = "{score}"
* valueQuantity.system = "http://unitsofmeasure.org"
* valueQuantity ^short = "Barthel Index total (0-100)"

Invariant: barthel-range
Description: "Barthel Index must be between 0 and 100"
Expression: "$this >= 0 and $this <= 100"
Severity: #error
