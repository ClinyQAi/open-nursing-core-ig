// =============================================================================
// 1. FOUNDATION: Patient & Practitioner
// =============================================================================
Instance: patient-example-jane
InstanceOf: ONCNHSPatient
Usage: #example
Title: "Example Patient: Jane Doe"
Description: "A fictional patient example demonstrating NHS Ethnicity constraints."
* name.family = "Doe"
* name.given = "Jane"
* gender = #female
// Valid NHS Ethnicity Code (White - British)
* extension[ethnicCategory].valueCodeableConcept = https://fhir.hl7.org.uk/CodeSystem/UKCore-EthnicCategory#A "British, Mixed British, British Scottish, or British Welsh"

Instance: practitioner-example
InstanceOf: Practitioner
Usage: #example
Title: "Example Practitioner: Nurse Nightingale"
* name.family = "Nightingale"
* name.given = "Florence"

// =============================================================================
// 2. EQUITY: Skin Tone Observation
// =============================================================================
Instance: observation-skin-tone
InstanceOf: ONCSkinToneObservation
Usage: #example
Title: "Assessment: Skin Tone"
* status = #final
* subject = Reference(patient-example-jane)
* performer = Reference(practitioner-example)
* code = http://loinc.org#66472-2 "Fitzpatrick skin type"
// Valid SNOMED Code for Type II
* valueCodeableConcept = http://snomed.info/sct#403154004 "Fitzpatrick skin type II"

// =============================================================================
// 3. SAFETY: Braden Scale (Pressure Injury)
// =============================================================================
Instance: observation-braden-scale
InstanceOf: ONCBradenScaleAssessment
Usage: #example
Title: "Assessment: Braden Scale"
* status = #final
* subject = Reference(patient-example-jane)
* performer = Reference(practitioner-example)
* category[nursing].coding = http://terminology.hl7.org/CodeSystem/observation-category#nursing
* code = http://loinc.org#9017-7 "Braden scale total score"
* valueQuantity = 18 '{score}'

// 1. Sensory Perception (LOINC 74012-8)
* component[sensoryPerception].code = http://loinc.org#74012-8 "Braden scale.sensory perception"
* component[sensoryPerception].valueQuantity = 3 '{score}'

// 2. Moisture (LOINC 74013-6)
* component[moisture].code = http://loinc.org#74013-6 "Braden scale.moisture"
* component[moisture].valueQuantity = 4 '{score}'

// 3. Activity (LOINC 74014-4)
* component[activity].code = http://loinc.org#74014-4 "Braden scale.activity"
* component[activity].valueQuantity = 2 '{score}'

// 4. Mobility (LOINC 74015-1)
* component[mobility].code = http://loinc.org#74015-1 "Braden scale.mobility"
* component[mobility].valueQuantity = 3 '{score}'

// 5. Nutrition (LOINC 74016-9)
* component[nutrition].code = http://loinc.org#74016-9 "Braden scale.nutrition"
* component[nutrition].valueQuantity = 3 '{score}'

// 6. Friction/Shear (LOINC 74017-7)
* component[frictionAndShear].code = http://loinc.org#74017-7 "Braden scale.friction and shear"
* component[frictionAndShear].valueQuantity = 3 '{score}'// =============================================================================
// 4. SAFETY: Morse Fall Scale
// =============================================================================
Instance: observation-morse-scale
InstanceOf: ONCMorseFallScale
Usage: #example
Title: "Assessment: Morse Fall Scale"
* status = #final
* subject = Reference(patient-example-jane)
* performer = Reference(practitioner-example)
* category[nursing].coding = http://terminology.hl7.org/CodeSystem/observation-category#nursing
* code = http://loinc.org#59460-6 "Fall risk assessment.Morse Scale"
* valueQuantity = 50 '{score}'

// 6 Mandatory Components
* component[historyFalling].code = http://loinc.org#59461-4 "History of falling"
* component[historyFalling].valueQuantity = 25 '{score}'

* component[secondaryDiagnosis].code = http://loinc.org#59462-2 "Secondary diagnosis"
* component[secondaryDiagnosis].valueQuantity = 15 '{score}'

* component[ambulatoryAid].code = http://loinc.org#59463-0 "Ambulatory aid"
* component[ambulatoryAid].valueQuantity = 0 '{score}'

* component[ivLock].code = http://loinc.org#59464-8 "Intravenous therapy or heparin lock"
* component[ivLock].valueQuantity = 0 '{score}'

* component[gait].code = http://loinc.org#59465-5 "Gait/transferring"
* component[gait].valueQuantity = 10 '{score}'

* component[mentalStatus].code = http://loinc.org#59466-3 "Mental status"
* component[mentalStatus].valueQuantity = 0 '{score}'

// =============================================================================
// 5. SAFETY: NEWS2 (Deterioration)
// =============================================================================
Instance: observation-news2
InstanceOf: ONCNEWS2Assessment
Usage: #example
Title: "Assessment: NEWS2"
* status = #final
* subject = Reference(patient-example-jane)
* performer = Reference(practitioner-example)
* category[nursing].coding = http://terminology.hl7.org/CodeSystem/observation-category#nursing
* code = http://loinc.org#86585-7 "NEWS2 score"
* valueQuantity = 4 '{score}'

// 7 Mandatory Components
* component[respiration].code = http://loinc.org#9279-1 "Respiratory rate"
* component[respiration].valueQuantity = 18 '/min'

* component[spo2].code = http://loinc.org#2708-6 "Oxygen saturation in Arterial blood"
* component[spo2].valueQuantity = 96 '%'

* component[oxygen].code = http://loinc.org#72274-4 "Supplemental oxygen used"
* component[oxygen].valueCodeableConcept = http://snomed.info/sct#373066001 "Yes"

* component[temperature].code = http://loinc.org#8310-5 "Body temperature"
* component[temperature].valueQuantity = 38.1 'Cel'

* component[systolicBP].code = http://loinc.org#8480-6 "Systolic blood pressure"
* component[systolicBP].valueQuantity = 110 'mm[Hg]'

* component[heartRate].code = http://loinc.org#8867-4 "Heart rate"
* component[heartRate].valueQuantity = 95 '/min'

* component[consciousness].code = http://loinc.org#11454-5 "Level of consciousness"
* component[consciousness].valueCodeableConcept = http://snomed.info/sct#110265006 "Alert to voice"

// =============================================================================
// 6. SDOH: Housing Status
// =============================================================================
Instance: observation-housing
InstanceOf: ONCHousingStatus
Usage: #example
Title: "Assessment: Housing Status"
* status = #final
* subject = Reference(patient-example-jane)
* performer = Reference(practitioner-example)
* category[nursing].coding = http://terminology.hl7.org/CodeSystem/observation-category#nursing
* code = http://loinc.org#71802-3 "Housing status"
* valueCodeableConcept = http://snomed.info/sct#160753008 "Lives with family"

// =============================================================================
// 7. CARE PLANNING: Problem, Goal, Intervention, Evaluation
// =============================================================================
Instance: condition-risk-falls
InstanceOf: ONCNursingProblem
Usage: #example
Title: "Problem: Risk of Falls"
* subject = Reference(patient-example-jane)
* clinicalStatus = http://terminology.hl7.org/CodeSystem/condition-clinical#active "Active"
* category = http://open-nursing-core.org/CodeSystem/onc-problem-type#nursing-diagnosis "Nursing Diagnosis"
* code = http://snomed.info/sct#162828007 "Risk of falls (finding)"

Instance: goal-no-falls
InstanceOf: ONCPatientGoal
Usage: #example
Title: "Goal: No Falls"
* lifecycleStatus = #active
* subject = Reference(patient-example-jane)
* description.text = "Patient will remain free from falls throughout the hospital stay."
* addresses = Reference(condition-risk-falls)

Instance: procedure-education
InstanceOf: ONCNursingIntervention
Usage: #example
Title: "Intervention: Patient Education"
* status = #completed
* subject = Reference(patient-example-jane)
* performer.actor = Reference(practitioner-example)
* code = http://hl7.org/fhir/sid/icnp#10012345 "Patient Education"
// NOTE: Using extension to link to goal
* extension[interventionGoal].valueReference = Reference(goal-no-falls)

Instance: observation-evaluation
InstanceOf: ONCGoalEvaluation
Usage: #example
Title: "Evaluation: Goal Achieved"
* status = #final
* subject = Reference(patient-example-jane)
* performer = Reference(practitioner-example)
* category[nursing].coding = http://terminology.hl7.org/CodeSystem/observation-category#nursing
* code = http://snomed.info/sct#385633008 "Goal achieved (finding)"
* valueCodeableConcept = http://snomed.info/sct#385633008 "Goal achieved (finding)"
* extension[observation-goal-reference].valueReference = Reference(goal-no-falls)

Instance: careplan-falls
InstanceOf: ONCNursingCarePlan
Usage: #example
Title: "Care Plan: Falls Risk"
* status = #active
* intent = #plan
* subject = Reference(patient-example-jane)
* addresses = Reference(condition-risk-falls)
* goal = Reference(goal-no-falls)
* activity.detail.code = http://hl7.org/fhir/sid/icnp#10012345 "Patient Education"
* activity.detail.status = #completed