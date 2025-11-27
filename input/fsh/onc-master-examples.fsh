// ==============================================================================
// 1. FOUNDATION
// ==============================================================================
Instance: patient-example-jane
InstanceOf: ONCNHSPatient
Usage: #example
* name.family = "Doe"
* name.given = "Jane"
* gender = #female
* extension[ethnicCategory].valueCodeableConcept = https://fhir.hl7.org.uk/CodeSystem/UKCore-EthnicCategory#A "British, Mixed British"

Instance: practitioner-example
InstanceOf: Practitioner
Usage: #example
* name.family = "Nightingale"

// ==============================================================================
// 2. EQUITY
// ==============================================================================
Instance: observation-skin-tone
InstanceOf: ONCSkinToneObservation
Usage: #example
* status = #final
* subject = Reference(patient-example-jane)
* performer = Reference(practitioner-example)
// FIX: Added the mandatory Nursing Category
* category[nursing].coding = http://terminology.hl7.org/CodeSystem/observation-category#nursing
* valueCodeableConcept = http://snomed.info/sct#403154004 "Fitzpatrick skin type II"

// ==============================================================================
// 3. SAFETY
// ==============================================================================
Instance: observation-braden-scale
InstanceOf: ONCBradenScaleAssessment
Usage: #example
* status = #final
* subject = Reference(patient-example-jane)
* performer = Reference(practitioner-example)
* category[nursing].coding = http://terminology.hl7.org/CodeSystem/observation-category#nursing
* valueQuantity = 18 'score' "score"
* component[sensoryPerception].code = http://loinc.org#74012-8 "Sensory Perception"
* component[sensoryPerception].valueQuantity = 3 'score' "score"
* component[moisture].code = http://loinc.org#74013-6 "Moisture"
* component[moisture].valueQuantity = 4 'score' "score"
* component[activity].code = http://loinc.org#74014-4 "Activity"
* component[activity].valueQuantity = 2 'score' "score"
* component[mobility].code = http://loinc.org#74015-1 "Mobility"
* component[mobility].valueQuantity = 3 'score' "score"
* component[nutrition].code = http://loinc.org#74016-9 "Nutrition"
* component[nutrition].valueQuantity = 3 'score' "score"
* component[frictionAndShear].code = http://loinc.org#74017-7 "Friction and Shear"
* component[frictionAndShear].valueQuantity = 3 'score' "score"

// ==============================================================================
// 4. CARE PLANNING
// ==============================================================================
Instance: example-nursing-problem
InstanceOf: ONCNursingProblem
Usage: #example
* subject = Reference(patient-example-jane)
* clinicalStatus = http://terminology.hl7.org/CodeSystem/condition-clinical#active "Active"
* category = http://open-nursing-core.org/CodeSystem/onc-problem-type#nursing-diagnosis "Nursing Diagnosis"
* code = http://snomed.info/sct#162828007 "Risk of falls (finding)"

Instance: example-patient-goal
InstanceOf: ONCPatientGoal
Usage: #example
* lifecycleStatus = #active
* subject = Reference(patient-example-jane)
* description.text = "Patient will remain free from falls."
* addresses = Reference(example-nursing-problem)

Instance: example-nursing-intervention
InstanceOf: ONCNursingIntervention
Usage: #example
* status = #completed
* subject = Reference(patient-example-jane)
* performer.actor = Reference(practitioner-example)
* code = http://snomed.info/sct#71388002 "Procedure"
* extension[interventionGoal].valueReference = Reference(example-patient-goal)

Instance: example-goal-evaluation
InstanceOf: ONCGoalEvaluation
Usage: #example
* status = #final
* subject = Reference(patient-example-jane)
* performer = Reference(practitioner-example)
* category[nursing].coding = http://terminology.hl7.org/CodeSystem/observation-category#nursing
* code = http://snomed.info/sct#385633008 "Goal achieved"
* valueCodeableConcept = http://snomed.info/sct#385633008 "Goal achieved"
* extension[goalReference].valueReference = Reference(example-patient-goal)
