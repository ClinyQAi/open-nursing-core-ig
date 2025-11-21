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
* valueQuantity = 14 '{score}' "score"
* valueQuantity.system = "http://unitsofmeasure.org"

// =============================================================================
// Example: Nursing Problem
// =============================================================================
Instance: ExampleNursingProblem
InstanceOf: ONCNursingProblem
Usage: #example
Title: "Example Nursing Problem"
Description: "An example of a nursing diagnosis"
* clinicalStatus = http://terminology.hl7.org/CodeSystem/condition-clinical#active
* category = http://open-nursing-core.org/CodeSystem/onc-problem-type#nursing-diagnosis
* code = http://snomed.info/sct#161891005 "Impaired skin integrity"
* subject = Reference(Patient/example-patient)
* onsetDateTime = "2025-11-20"

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
* reasonReference = Reference(ExamplePatientGoal)

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
* derivedFrom = Reference(ExamplePatientGoal)

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