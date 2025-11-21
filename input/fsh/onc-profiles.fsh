// =============================================================================
// Profile: ONCNursingAssessment (Base for Observations)
// =============================================================================
Profile: ONCNursingAssessment
Parent: Observation
Id: onc-nursing-assessment
Title: "Open Nursing Core Assessment"
Description: "A foundational profile for any nursing-specific observation, assessment, or finding. It mandates a performer and a link to the nursing process."
* category contains nursing 1..1 MS
* category[nursing] = http://terminology.hl7.org/CodeSystem/observation-category#nursing
* performer 1..1 MS
* performer only Reference(Practitioner or PractitionerRole)
* value[x] 1..1 MS
* value[x] only CodeableConcept or Quantity

// =============================================================================
// Profile: ONCBradenScaleAssessment (Specialized Observation)
// =============================================================================
Profile: ONCBradenScaleAssessment
Parent: ONCNursingAssessment
Id: onc-braden-scale-assessment
Title: "Open Nursing Core Braden Scale Assessment"
Description: "A specific profile for recording a Braden Scale assessment for pressure injury risk."
* code = http://loinc.org#9017-7 "Braden Scale total score"
* code MS
* value[x] only Quantity
* valueQuantity.unit = "{score}"
* valueQuantity.system = "http://unitsofmeasure.org"
* component 6..6 MS
* component ^slicing.discriminator.type = #pattern
* component ^slicing.discriminator.path = "code"
* component ^slicing.rules = #open
* component contains
    sensoryPerception 1..1 MS and
    moisture 1..1 MS and
    activity 1..1 MS and
    mobility 1..1 MS and
    nutrition 1..1 MS and
    frictionAndShear 1..1 MS

// =============================================================================
// Profile: ONCNursingProblem (Based on Condition)
// =============================================================================
Profile: ONCNursingProblem
Parent: Condition
Id: onc-nursing-problem
Title: "Open Nursing Core Nursing Problem"
Description: "Represents a clinical judgment about a human response to a health condition, identified by a nurse."
* category 1..1 MS
* category = http://open-nursing-core.org/CodeSystem/onc-problem-type#nursing-diagnosis "Nursing Diagnosis"
* clinicalStatus 1..1 MS
* code 1..1 MS
* code from NursingProblemValueSet (required)

// =============================================================================
// Profile: ONCPatientGoal (Based on Goal)
// =============================================================================
Profile: ONCPatientGoal
Parent: Goal
Id: onc-patient-goal
Title: "Open Nursing Core Patient Goal"
Description: "A desired outcome for a patient, tied to a specific nursing problem."
* lifecycleStatus 1..1 MS
* description 1..1 MS
* addresses 1..* MS
* addresses only Reference(ONCNursingProblem)

// =============================================================================
// Profile: ONCNursingIntervention (Based on Procedure)
// =============================================================================
Profile: ONCNursingIntervention
Parent: Procedure
Id: onc-nursing-intervention
Title: "Open Nursing Core Nursing Intervention"
Description: "An action performed by a nurse as part of a care plan."
* status = #completed
* status MS
* code 1..1 MS
* code from NursingInterventionValueSet (required)
* reasonReference only Reference(ONCPatientGoal)

// =============================================================================
// Profile: ONCGoalEvaluation (Specialized Observation)
// =============================================================================
Profile: ONCGoalEvaluation
Parent: ONCNursingAssessment
Id: onc-goal-evaluation
Title: "Open Nursing Core Goal Evaluation"
Description: "An observation that evaluates a patient's progress towards a specific goal, closing the loop of the nursing process."
* derivedFrom 1..* MS
* derivedFrom only Reference(ONCPatientGoal)
* code from GoalEvaluationValueSet (required)

// =============================================================================
// Profile: ONCNursingCarePlan (Based on CarePlan)
// =============================================================================
Profile: ONCNursingCarePlan
Parent: CarePlan
Id: onc-nursing-care-plan
Title: "Open Nursing Core Nursing Care Plan"
Description: "A comprehensive care plan that orchestrates the entire nursing process from problem identification to evaluation."
* addresses 1..* MS
* addresses only Reference(ONCNursingProblem)
* goal 1..* MS
* goal only Reference(ONCPatientGoal)
* activity.detail.code from NursingInterventionValueSet (required)