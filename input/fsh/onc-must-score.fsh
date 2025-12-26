// =============================================================================
// MUST Score (Malnutrition Universal Screening Tool)
// =============================================================================
Profile: ONCMUSTScore
Parent: ONCNursingAssessment
Id: onc-must-score
Title: "MUST Score (Malnutrition Universal Screening Tool)"
Description: "Malnutrition Universal Screening Tool for identifying adults at risk of malnutrition. Score 0=low risk, 1=medium risk, 2+=high risk. NHS-standard nutritional screening."
* status MS
* code = http://snomed.info/sct#870431003 "Malnutrition Universal Screening Tool score"
* code MS
* value[x] only Quantity
* valueQuantity 1..1 MS
* valueQuantity.value obeys must-total-range
* valueQuantity.unit = "{score}"
* valueQuantity.system = "http://unitsofmeasure.org"
* valueQuantity ^short = "MUST total score (0-6, higher = higher risk)"
* component 3..3 MS
* component ^slicing.discriminator.type = #pattern
* component ^slicing.discriminator.path = "code"
* component ^slicing.ordered = false
* component ^slicing.rules = #open
* component contains bmi 1..1 MS and weightLoss 1..1 MS and acuteDisease 1..1 MS
* component[bmi].code = http://snomed.info/sct#846931000000101 "Malnutrition Universal Screening Tool BMI score"
* component[bmi].value[x] only Quantity
* component[bmi].valueQuantity.value obeys must-component-range
* component[bmi].valueQuantity.unit = "{score}"
* component[bmi].valueQuantity.system = "http://unitsofmeasure.org"
* component[weightLoss].code = http://snomed.info/sct#846941000000105 "Malnutrition Universal Screening Tool weight loss score"
* component[weightLoss].value[x] only Quantity
* component[weightLoss].valueQuantity.value obeys must-component-range
* component[weightLoss].valueQuantity.unit = "{score}"
* component[weightLoss].valueQuantity.system = "http://unitsofmeasure.org"
* component[acuteDisease].code = http://snomed.info/sct#846951000000107 "Malnutrition Universal Screening Tool acute disease effect score"
* component[acuteDisease].value[x] only Quantity
* component[acuteDisease].valueQuantity.value obeys must-component-range
* component[acuteDisease].valueQuantity.unit = "{score}"
* component[acuteDisease].valueQuantity.system = "http://unitsofmeasure.org"

Invariant: must-total-range
Description: "MUST total score must be between 0 and 6"
Expression: "$this >= 0 and $this <= 6"
Severity: #error

Invariant: must-component-range
Description: "MUST component scores must be between 0 and 2"
Expression: "$this >= 0 and $this <= 2"
Severity: #error
