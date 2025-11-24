Profile: ONCNursingAssessment
Parent: Observation
Id: onc-nursing-assessment
Title: "Open Nursing Core Assessment"
Description: "Base profile for nursing assessments."
* category ^slicing.discriminator.type = #pattern
* category ^slicing.discriminator.path = "coding"
* category ^slicing.rules = #open
* category contains nursing 1..1 MS
* category[nursing] = http://terminology.hl7.org/CodeSystem/observation-category#nursing
* performer 1..1 MS
* performer only Reference(Practitioner or PractitionerRole)
* value[x] 1..1 MS
* value[x] only CodeableConcept or Quantity

Profile: ONCBradenScaleAssessment
Parent: ONCNursingAssessment
Id: onc-braden-scale-assessment
Title: "Open Nursing Core Braden Scale Assessment"
Description: "Braden Scale assessment for pressure injury risk."
* code = http://loinc.org#9017-7 "Braden Scale total score"
* code MS
* value[x] only Quantity
* valueQuantity.unit = "{score}"
* valueQuantity.system = "http://unitsofmeasure.org"
* component 6..6 MS
* component ^slicing.discriminator.type = #pattern
* component ^slicing.discriminator.path = "code"
* component ^slicing.rules = #open
* component ^slicing.ordered = false
* component contains
    sensoryPerception 1..1 MS and
    moisture 1..1 MS and
    activity 1..1 MS and
    mobility 1..1 MS and
    nutrition 1..1 MS and
    frictionAndShear 1..1 MS

Profile: ONCNursingProblem
Parent: Condition
Id: onc-nursing-problem
Title: "Open Nursing Core Nursing Problem"
Description: "Nursing problem or diagnosis."
* category 1..1 MS
* category = http://open-nursing-core.org/CodeSystem/onc-problem-type#nursing-diagnosis "Nursing Diagnosis"
* clinicalStatus 1..1 MS
* code 1..1 MS
* code from NursingProblemValueSet (required)

Profile: ONCPatientGoal
Parent: Goal
Id: onc-patient-goal
Title: "Open Nursing Core Patient Goal"
Description: "Patient goal addressing a nursing problem."
* lifecycleStatus 1..1 MS
* description 1..1 MS
* addresses 1..* MS
* addresses only Reference(ONCNursingProblem)

Extension: InterventionGoalReference
Id: intervention-goal-reference
Title: "Intervention Goal Reference"
Description: "Reference to the goal this intervention addresses."
* value[x] only Reference(ONCPatientGoal)

Profile: ONCNursingIntervention
Parent: Procedure
Id: onc-nursing-intervention
Title: "Open Nursing Core Nursing Intervention"
Description: "Nursing intervention performed."
* status = #completed
* status MS
* code 1..1 MS
* code from NursingInterventionValueSet (required)
* extension contains InterventionGoalReference named interventionGoal 0..* MS

Extension: ObservationGoalReference
Id: observation-goal-reference
Title: "Observation Goal Reference"
Description: "Reference to the goal that is being evaluated."
* value[x] only Reference(Goal)

Profile: ONCGoalEvaluation
Parent: ONCNursingAssessment
Id: onc-goal-evaluation
Title: "Open Nursing Core Goal Evaluation"
Description: "Evaluation of a patient's progress towards a goal."
* extension contains ObservationGoalReference named goalReference 0..1 MS
* code from GoalEvaluationValueSet (required)

Profile: ONCNursingCarePlan
Parent: CarePlan
Id: onc-nursing-care-plan
Title: "Open Nursing Core Nursing Care Plan"
Description: "Nursing care plan."
* addresses 1..* MS
* addresses only Reference(ONCNursingProblem)
* goal 1..* MS
* goal only Reference(ONCPatientGoal)
* activity.detail.code from NursingInterventionValueSet (required)
