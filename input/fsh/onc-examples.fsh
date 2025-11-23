// =============================================================================
// Example Patient and Practitioner
// =============================================================================
Instance: patient-example
InstanceOf: Patient
Usage: #example
* name.family = "Smith"
* name.given = "John"
* gender = #male

Instance: practitioner-example
InstanceOf: Practitioner
Usage: #example
* name.family = "Nightingale"
* name.given = "Florence"

// =============================================================================
// Example 1: A Nursing Problem
// =============================================================================
Instance: example-nursing-problem
InstanceOf: ONCNursingProblem
Usage: #example
* subject = Reference(patient-example)
* clinicalStatus = http://terminology.hl7.org/CodeSystem/condition-clinical#active "Active"
* category = http://open-nursing-core.org/CodeSystem/onc-problem-type#nursing-diagnosis "Nursing Diagnosis"
* code = http://snomed.info/sct#162828007 "Risk of falls (finding)"

// =============================================================================
// Example 2: A Patient Goal
// =============================================================================
Instance: example-patient-goal
InstanceOf: ONCPatientGoal
Usage: #example
* lifecycleStatus = #active
* subject = Reference(patient-example)
* description.text = "Patient will remain free from falls throughout the hospital stay."
* addresses = Reference(example-nursing-problem)

// =============================================================================
// Example 3: A Nursing Intervention
// =============================================================================
Instance: example-nursing-intervention
InstanceOf: ONCNursingIntervention
Usage: #example
* status = #completed
* subject = Reference(patient-example)
* performer.actor = Reference(practitioner-example)
* code = http://hl7.org/fhir/sid/icnp#10012345 "Patient Education"

// =============================================================================
// Example 4: A Braden Scale Assessment
// =============================================================================
Instance: example-braden-scale
InstanceOf: ONCBradenScaleAssessment
Usage: #example
* status = #final
* subject = Reference(patient-example)
* performer = Reference(practitioner-example)
* category[nursing].coding = http://terminology.hl7.org/CodeSystem/observation-category#nursing
* code = http://loinc.org#9017-7 "Braden Scale total score"
// FIX: Removed the extra "score" string
* valueQuantity = 18 '{score}'

// FIX: Removed the extra "score" string from all components below
* component[sensoryPerception]
  * code = http://loinc.org#74012-8 "Sensory Perception"
  * valueQuantity = 3 '{score}'

* component[moisture]
  * code = http://loinc.org#74013-6 "Moisture"
  * valueQuantity = 4 '{score}'

* component[activity]
  * code = http://loinc.org#74014-4 "Activity"
  * valueQuantity = 2 '{score}'

* component[mobility]
  * code = http://loinc.org#74015-1 "Mobility"
  * valueQuantity = 3 '{score}'

* component[nutrition]
  * code = http://loinc.org#74016-9 "Nutrition"
  * valueQuantity = 3 '{score}'

* component[frictionAndShear]
  * code = http://loinc.org#74017-7 "Friction and Shear"
  * valueQuantity = 3 '{score}'

// =============================================================================
// Example 5: A Goal Evaluation
// =============================================================================
Instance: example-goal-evaluation
InstanceOf: ONCGoalEvaluation
Usage: #example
* status = #final
* subject = Reference(patient-example)
* performer = Reference(practitioner-example)
* category[nursing].coding = http://terminology.hl7.org/CodeSystem/observation-category#nursing
* code = http://snomed.info/sct#385633008 "Goal achieved (finding)"
// FIX: Added the required value
* valueCodeableConcept = http://snomed.info/sct#385633008 "Goal achieved (finding)"
* extension[observation-goal-reference].valueReference = Reference(example-patient-goal)

// =============================================================================
// Example 6: A Full Nursing Care Plan
// =============================================================================
Instance: example-nursing-care-plan
InstanceOf: ONCNursingCarePlan
Usage: #example
* status = #active
* intent = #plan
* subject = Reference(patient-example)
* addresses = Reference(example-nursing-problem)
* goal = Reference(example-patient-goal)
* activity.detail.code = http://hl7.org/fhir/sid/icnp#10012345 "Patient Education"
* activity.detail.status = #completed