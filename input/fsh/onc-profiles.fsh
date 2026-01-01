Profile: ONCNursingAssessment
Parent: Observation
Id: onc-nursing-assessment
Title: "Open Nursing Core Assessment"
Description: "Base profile for nursing assessment observations conforming to UK Core standards. Captures structured nursing assessment data as part of the ADPIE (Assessment, Diagnosis, Planning, Implementation, Evaluation) nursing process framework. Used as parent for specialized assessments like NEWS2, Braden Scale, and clinical observations."
* category ^slicing.discriminator.type = #pattern
* category ^slicing.discriminator.path = "$this"
* category ^slicing.ordered = false
* category ^slicing.rules = #open
* category contains nursing 1..1 MS
* category[nursing] = http://terminology.hl7.org/CodeSystem/observation-category#survey
* performer 1..1 MS
* performer only Reference(Practitioner or PractitionerRole)
* value[x] 1..1 MS
* value[x] only CodeableConcept or Quantity or string

Profile: ONCBradenScaleAssessment
Parent: ONCNursingAssessment
Id: onc-braden-scale-assessment
Title: "Braden Scale Assessment"
Description: "A profile for the Braden Scale pressure ulcer risk assessment"
* status = #final
* status MS
* code = https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes#braden-total-score "Braden Total Score"
* code MS
* value[x] only Quantity
* valueQuantity 1..1 MS
* valueQuantity.unit = "{score}"
* valueQuantity.system = "http://unitsofmeasure.org"
* valueQuantity.code = #1
* component 6..6 MS
* component ^slicing.discriminator.type = #pattern
* component ^slicing.discriminator.path = "code"
* component ^slicing.ordered = false
* component ^slicing.rules = #open
* component contains sensoryPerception 1..1 MS and moisture 1..1 MS and activity 1..1 MS and mobility 1..1 MS and nutrition 1..1 MS and frictionAndShear 1..1 MS
* component[sensoryPerception].code = https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes#braden-sensory "Braden Sensory Perception"
* component[sensoryPerception].value[x] only Quantity
* component[moisture].code = https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes#braden-moisture "Braden Moisture"
* component[moisture].value[x] only Quantity
* component[activity].code = https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes#braden-activity "Braden Activity"
* component[activity].value[x] only Quantity
* component[mobility].code = https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes#braden-mobility "Braden Mobility"
* component[mobility].value[x] only Quantity
* component[nutrition].code = https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes#braden-nutrition "Braden Nutrition"
* component[nutrition].value[x] only Quantity
* component[frictionAndShear].code = https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes#braden-friction "Braden Friction/Shear"
* component[frictionAndShear].value[x] only Quantity

* obeys onc-equity-skin-tone-required
* hasMember MS
* hasMember ^slicing.discriminator.type = #pattern
* hasMember ^slicing.discriminator.path = "resolve().code"
* hasMember ^slicing.rules = #open
* hasMember contains skinTone 1..1 MS
* hasMember[skinTone] only Reference(ONCSkinToneObservation or ONCMonkSkinToneObservation)
* hasMember[skinTone] ^short = "Mandatory Skin Tone Context (Equity Gate)"



Profile: ONCNursingProblem
Parent: Condition
Id: onc-nursing-problem
Title: "Nursing Problem"
Description: "Nursing diagnosis or problem identified during assessment. Represents clinical judgments about individual, family, or community responses to actual or potential health problems. Part of the ADPIE framework's Diagnosis phase."
* category 1..1 MS
* category from ProblemCategoryValueSet (required)
* clinicalStatus 1..1 MS
* code 1..1 MS
* code from NursingProblemValueSet (required)

