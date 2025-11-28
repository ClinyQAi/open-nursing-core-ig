// =============================================================================
// Example: Nursing Assessment
// =============================================================================
Instance: ExampleNursingAssessment
InstanceOf: ONCNursingAssessment
Usage: #example
Title: "Example Nursing Assessment"
Description: "An example of a basic nursing assessment observation"
* status = #final
* category[nursing] = http://terminology.hl7.org/CodeSystem/observation-category#nursing
* code = http://snomed.info/sct#225597009 "Pain assessment"
* subject = Reference(Patient/example-patient)
* performer = Reference(Practitioner/example-nurse)
* effectiveDateTime = "2025-11-21T08:00:00Z"
* valueCodeableConcept = http://snomed.info/sct#76948002 "Severe pain"

// =============================================================================
// Example: Braden Scale Assessment
// =============================================================================
Instance: ExampleBradenScale
InstanceOf: ONCBradenScaleAssessment
Usage: #example
Title: "Example Braden Scale Assessment"
Description: "An example of a Braden Scale pressure injury risk assessment"
* status = #final
* category[nursing] = http://terminology.hl7.org/CodeSystem/observation-category#nursing
* code = http://loinc.org#9017-7 "Braden Scale total score"
* subject = Reference(Patient/example-patient)
* performer = Reference(Practitioner/example-nurse)
* effectiveDateTime = "2025-11-21T08:00:00Z"
* valueQuantity = 14 '{score}'
* valueQuantity.system = "http://unitsofmeasure.org"
* component[sensoryPerception].code = http://loinc.org#9018-5 "Sensory perception"
* component[sensoryPerception].valueCodeableConcept = http://loinc.org#LA9604-5 "No impairment"
* component[moisture].code = http://loinc.org#9019-3 "Moisture"
* component[moisture].valueCodeableConcept = http://loinc.org#LA9608-6 "Rarely moist"
* component[activity].code = http://loinc.org#9020-1 "Activity"
* component[activity].valueCodeableConcept = http://loinc.org#LA9611-0 "Walks frequently"
* component[mobility].code = http://loinc.org#9021-9 "Mobility"
* component[mobility].valueCodeableConcept = http://loinc.org#LA9615-1 "No limitation"
* component[nutrition].code = http://loinc.org#9022-7 "Nutrition"
* component[nutrition].valueCodeableConcept = http://loinc.org#LA9618-5 "Excellent"
* component[frictionAndShear].code = http://loinc.org#9023-5 "Friction and shear"
* component[frictionAndShear].valueCodeableConcept = http://loinc.org#LA9620-1 "No apparent problem"

// =============================================================================
// Example: Nursing Problem
// =============================================================================
Instance: ExampleNursingProblem
InstanceOf: ONCNursingProblem
Usage: #example
Title: "Example Nursing Problem"
Description: "An example of a nursing diagnosis"
* clinicalStatus = http://terminology.hl7.org/CodeSystem/condition-clinical#active
* code = http://snomed.info/sct#161891005 "Impaired skin integrity"
* subject = Reference(Patient/example-patient)
* onsetDateTime = "2025-11-20"
// Category is fixed in profile, no need to restate unless different (which would be an error)

// =============================================================================
// Example: Patient Goal
// =============================================================================
Instance: ExamplePatientGoal
InstanceOf: ONCPatientGoal
Usage: #example
Title: "Example Patient Goal"
Description: "An example of a patient-centered goal"
* lifecycleStatus = #active
* description.text = "Patient will maintain intact skin throughout hospitalization"
* subject = Reference(Patient/example-patient)
* addresses = Reference(ExampleNursingProblem)
* target.measure = http://loinc.org#39107-8 "Braden Scale panel"
* target.detailString = "Maintain Braden score above 18"

// =============================================================================
// Example: Nursing Intervention
// =============================================================================
Instance: ExampleNursingIntervention
InstanceOf: ONCNursingIntervention
Usage: #example
Title: "Example Nursing Intervention"
Description: "An example of a nursing intervention"
* status = #completed
* code = http://snomed.info/sct#225358003 "Wound care"
* subject = Reference(Patient/example-patient)
* performedDateTime = "2025-11-21T10:00:00Z"
* performer.actor = Reference(Practitioner/example-nurse)
* extension[relatedGoal].valueReference = Reference(ExamplePatientGoal)

// =============================================================================
// Example: Goal Evaluation
// =============================================================================
Instance: ExampleGoalEvaluation
InstanceOf: ONCGoalEvaluation
Usage: #example
Title: "Example Goal Evaluation"
Description: "An example of evaluating progress towards a goal"
* status = #final
* category[nursing] = http://terminology.hl7.org/CodeSystem/observation-category#nursing
* code = http://snomed.info/sct#385633008 "Goal achieved (finding)"
* subject = Reference(Patient/example-patient)
* performer = Reference(Practitioner/example-nurse)
* effectiveDateTime = "2025-11-21T16:00:00Z"
* valueCodeableConcept = http://snomed.info/sct#385633008 "Goal achieved"
* extension[relatedGoal].valueReference = Reference(ExamplePatientGoal)

// =============================================================================
// Example: Nursing Care Plan
// =============================================================================
Instance: ExampleNursingCarePlan
InstanceOf: ONCNursingCarePlan
Usage: #example
Title: "Example Nursing Care Plan"
Description: "An example of a comprehensive nursing care plan"
* status = #active
* intent = #plan
* subject = Reference(Patient/example-patient)
* addresses = Reference(ExampleNursingProblem)
* goal = Reference(ExamplePatientGoal)
* activity.detail.kind = #ServiceRequest
* activity.detail.status = #completed
* activity.detail.description = "Provide wound care and monitor skin integrity"
