// =============================================================================
// NEWS2 (National Early Warning Score 2) - Full NHS CareConnect Alignment
// =============================================================================

// -----------------------------------------------------------------------------
// Main NEWS2 Score Profile
// -----------------------------------------------------------------------------
Profile: ONCNEWS2Score
Parent: ONCNursingAssessment
Id: onc-news2-score
Title: "NEWS2 Score"
Description: "National Early Warning Score 2 (NEWS2) for detecting clinical deterioration. Fully aligned with NHS CareConnect-NEWS2-Observation-1."
* status = #final
* status MS
* code from NEWS2CodeValueSet (required)
* code MS
* value[x] only Quantity
* valueQuantity 1..1 MS
* valueQuantity.value obeys news2-range
* valueQuantity.unit = "{score}"
* valueQuantity.system = "http://unitsofmeasure.org"
* valueQuantity ^short = "NEWS2 total score (0-20)"

Invariant: news2-range
Description: "NEWS2 score must be between 0 and 20"
Expression: "$this >= 0 and $this <= 20"
Severity: #error

ValueSet: NEWS2CodeValueSet
Id: news2-code-vs
Title: "NEWS2 Code Value Set"
Description: "LOINC and SNOMED codes for NEWS2"
* http://loinc.org#88330-6 "National Early Warning Score [NEWS]"
* http://snomed.info/sct#1104051000000101 "National Early Warning Score 2 (observable entity)"

// -----------------------------------------------------------------------------
// NEWS2 Sub-Score Profile
// -----------------------------------------------------------------------------
Profile: ONCNEWS2Subscore
Parent: ONCNursingAssessment
Id: onc-news2-subscore
Title: "NEWS2 Sub-Score"
Description: "Individual parameter sub-score for NEWS2 (0-3 for most parameters). References the related vital sign observation."
* status = #final
* status MS
* code from NEWS2SubscoreCodeValueSet (required)
* code MS
* value[x] only Quantity
* valueQuantity 1..1 MS
* valueQuantity.value obeys subscore-range
* valueQuantity.unit = "{score}"
* valueQuantity.system = "http://unitsofmeasure.org"

Invariant: subscore-range
Description: "NEWS2 sub-score must be between 0 and 3"
Expression: "$this >= 0 and $this <= 3"
Severity: #error

ValueSet: NEWS2SubscoreCodeValueSet
Id: news2-subscore-code-vs
Title: "NEWS2 Sub-Score Codes"
Description: "SNOMED codes for NEWS2 sub-scores"
* http://snomed.info/sct#1104301000000104 "Royal College of Physicians National Early Warning Score 2 - pulse score"
* http://snomed.info/sct#1104311000000102 "Royal College of Physicians National Early Warning Score 2 - respiration rate score"
* http://snomed.info/sct#1104331000000106 "Royal College of Physicians National Early Warning Score 2 - temperature score"
* http://snomed.info/sct#1104351000000100 "Royal College of Physicians National Early Warning Score 2 - ACVPU score"
* http://snomed.info/sct#1104341000000103 "Royal College of Physicians National Early Warning Score 2 - oxygen saturation scale 1 score"
* http://snomed.info/sct#1104321000000108 "Royal College of Physicians National Early Warning Score 2 - systolic blood pressure score"

// -----------------------------------------------------------------------------
// Supporting Vital Sign Observation Profiles
// -----------------------------------------------------------------------------

Profile: ONCRespirationRate
Parent: ONCNursingAssessment
Id: onc-respiration-rate
Title: "Respiration Rate"
Description: "Respiration rate observation for NEWS2"
* code = http://loinc.org#9279-1 "Respiratory rate"
* value[x] only Quantity
* valueQuantity.unit = "/min"
* valueQuantity.system = "http://unitsofmeasure.org"
* valueQuantity.code = #/min

Profile: ONCOxygenSaturation
Parent: ONCNursingAssessment
Id: onc-oxygen-saturation
Title: "Oxygen Saturation"
Description: "Oxygen saturation (SpO2) observation for NEWS2"
* code = http://loinc.org#59408-5 "Oxygen saturation in Arterial blood by Pulse oximetry"
* value[x] only Quantity
* valueQuantity.unit = "%"
* valueQuantity.system = "http://unitsofmeasure.org"
* valueQuantity.code = #%

Profile: ONCBodyTemperature
Parent: ONCNursingAssessment
Id: onc-body-temperature
Title: "Body Temperature"
Description: "Body temperature observation for NEWS2"
* code = http://loinc.org#8310-5 "Body temperature"
* value[x] only Quantity
* valueQuantity.unit = "Cel"
* valueQuantity.system = "http://unitsofmeasure.org"
* valueQuantity.code = #Cel

Profile: ONCBloodPressure
Parent: ONCNursingAssessment
Id: onc-blood-pressure
Title: "Blood Pressure"
Description: "Blood pressure observation for NEWS2 (systolic BP used for scoring)"
* code = http://loinc.org#85354-9 "Blood pressure panel with all children optional"
* component 2..2 MS
* component ^slicing.discriminator.type = #pattern
* component ^slicing.discriminator.path = "code"
* component ^slicing.rules = #open
* component contains systolic 1..1 MS and diastolic 1..1 MS
* component[systolic].code = http://loinc.org#8480-6 "Systolic blood pressure"
* component[systolic].value[x] only Quantity
* component[systolic].valueQuantity.unit = "mm[Hg]"
* component[systolic].valueQuantity.system = "http://unitsofmeasure.org"
* component[diastolic].code = http://loinc.org#8462-4 "Diastolic blood pressure"
* component[diastolic].value[x] only Quantity
* component[diastolic].valueQuantity.unit = "mm[Hg]"
* component[diastolic].valueQuantity.system = "http://unitsofmeasure.org"

Profile: ONCHeartRate
Parent: ONCNursingAssessment
Id: onc-heart-rate
Title: "Heart Rate"
Description: "Heart rate (pulse) observation for NEWS2"
* code = http://loinc.org#8867-4 "Heart rate"
* value[x] only Quantity
* valueQuantity.unit = "/min"
* valueQuantity.system = "http://unitsofmeasure.org"
* valueQuantity.code = #/min

Profile: ONCACVPU
Parent: ONCNursingAssessment
Id: onc-acvpu
Title: "ACVPU Consciousness Level"
Description: "ACVPU consciousness level assessment for NEWS2 (Alert, Confusion, Voice, Pain, Unresponsive)"
* code = http://snomed.info/sct#1104441000000107 "ACVPU (Alert Confusion Voice Pain Unresponsive) scale score"
* value[x] only CodeableConcept
* valueCodeableConcept from ACVPUValueSet (required)

ValueSet: ACVPUValueSet
Id: acvpu-vs
Title: "ACVPU Value Set"
Description: "ACVPU consciousness level codes"
* http://snomed.info/sct#248234008 "Mentally alert"
* http://snomed.info/sct#300202002 "Responds to voice"
* http://snomed.info/sct#450847001 "Responds to pain"
* http://snomed.info/sct#422768004 "Unresponsive"
* http://snomed.info/sct#130987000 "Acute confusion"

Profile: ONCInspiredOxygen
Parent: ONCNursingAssessment
Id: onc-inspired-oxygen
Title: "Inspired Oxygen"
Description: "Inspired oxygen observation for NEWS2 (air vs supplemental oxygen)"
* code = http://loinc.org#3151-8 "Inhaled oxygen flow rate"
* value[x] only Quantity or CodeableConcept
* valueQuantity.unit = "L/min"
* valueQuantity.system = "http://unitsofmeasure.org"
* valueCodeableConcept from InspiredOxygenValueSet (required)

ValueSet: InspiredOxygenValueSet
Id: inspired-oxygen-vs
Title: "Inspired Oxygen Value Set"
Description: "Codes for inspired oxygen status"
* http://snomed.info/sct#722742002 "Breathing room air"
* http://snomed.info/sct#371825009 "Patient on oxygen"
