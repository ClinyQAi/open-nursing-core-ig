// =============================================================================
// Glasgow Coma Scale (GCS) Profile
// =============================================================================
Profile: ONCGlasgowComaScale
Parent: ONCNursingAssessment
Id: onc-glasgow-coma-scale
Title: "Glasgow Coma Scale"
Description: "Glasgow Coma Scale (GCS) for assessing level of consciousness. Total score 3-15 with three required components: Eye (1-4), Verbal (1-5), Motor (1-6)."
* status MS
* code = http://loinc.org#9269-2 "Glasgow coma score total"
* code MS
* value[x] only Quantity
* valueQuantity 1..1 MS
* valueQuantity.value obeys gcs-total-range
* valueQuantity.unit = "{score}"
* valueQuantity.system = "http://unitsofmeasure.org"
* valueQuantity ^short = "GCS total score (3-15)"
* component 3..3 MS
* component ^slicing.discriminator.type = #pattern
* component ^slicing.discriminator.path = "code"
* component ^slicing.ordered = false
* component ^slicing.rules = #open
* component contains eye 1..1 MS and verbal 1..1 MS and motor 1..1 MS
* component[eye].code = http://loinc.org#9267-6 "Glasgow coma score eye opening"
* component[eye].value[x] only Quantity
* component[eye].valueQuantity.value obeys gcs-eye-range
* component[eye].valueQuantity.unit = "{score}"
* component[eye].valueQuantity.system = "http://unitsofmeasure.org"
* component[verbal].code = http://loinc.org#9270-0 "Glasgow coma score verbal"
* component[verbal].value[x] only Quantity
* component[verbal].valueQuantity.value obeys gcs-verbal-range
* component[verbal].valueQuantity.unit = "{score}"
* component[verbal].valueQuantity.system = "http://unitsofmeasure.org"
* component[motor].code = http://loinc.org#9268-4 "Glasgow coma score motor"
* component[motor].value[x] only Quantity
* component[motor].valueQuantity.value obeys gcs-motor-range
* component[motor].valueQuantity.unit = "{score}"
* component[motor].valueQuantity.system = "http://unitsofmeasure.org"

Invariant: gcs-total-range
Description: "GCS total score must be between 3 and 15"
Expression: "$this >= 3 and $this <= 15"
Severity: #error

Invariant: gcs-eye-range
Description: "GCS eye response must be between 1 and 4"
Expression: "$this >= 1 and $this <= 4"
Severity: #error

Invariant: gcs-verbal-range
Description: "GCS verbal response must be between 1 and 5"
Expression: "$this >= 1 and $this <= 5"
Severity: #error

Invariant: gcs-motor-range
Description: "GCS motor response must be between 1 and 6"
Expression: "$this >= 1 and $this <= 6"
Severity: #error
