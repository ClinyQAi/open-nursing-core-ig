Profile: ONCNursingAssessment
Parent: Observation
Id: onc-nursing-assessment
Title: "Open Nursing Core Assessment"
* category ^slicing.discriminator.type = #pattern
* category ^slicing.discriminator.path = "$this"
* category ^slicing.ordered = false
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
Title: "Braden Scale Assessment"
Description: "A profile for the Braden Scale pressure ulcer risk assessment"
* status = #final
* status MS
* code = http://loinc.org#38227-0 "Braden scale total score"
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
* component[sensoryPerception].code = http://loinc.org#38222-1 "Sensory perception Braden scale"
* component[sensoryPerception].value[x] only Quantity
* component[moisture].code = http://loinc.org#38229-6 "Moisture Braden scale"
* component[moisture].value[x] only Quantity
* component[activity].code = http://loinc.org#38223-9 "Activity Braden scale"
* component[activity].value[x] only Quantity
* component[mobility].code = http://loinc.org#38224-7 "Mobility Braden scale"
* component[mobility].value[x] only Quantity
* component[nutrition].code = http://loinc.org#38225-4 "Nutrition Braden scale"
* component[nutrition].value[x] only Quantity
* component[frictionAndShear].code = http://loinc.org#38226-2 "Friction and shear Braden scale"
* component[frictionAndShear].value[x] only Quantity


Profile: ONCNursingProblem
Parent: Condition
Id: onc-nursing-problem
Title: "Nursing Problem"
* category 1..1 MS
* category from ProblemCategoryValueSet (required)
* clinicalStatus 1..1 MS
* code 1..1 MS
* code from NursingProblemValueSet (required)

Profile: ONCPatientGoal
Parent: Goal
Id: onc-patient-goal
Title: "Patient Goal"
* lifecycleStatus 1..1 MS
* description 1..1 MS
* addresses 1..* MS
* addresses only Reference(ONCNursingProblem)

Profile: ONCNursingIntervention
Parent: Procedure
Id: onc-nursing-intervention
Title: "Nursing Intervention"
// FIX: Separated Value and MS Flag
* status = #completed
* status MS
* code 1..1 MS
* code from NursingInterventionValueSet (required)
* extension contains InterventionGoalReference named interventionGoal 0..* MS

Profile: ONCGoalEvaluation
Parent: ONCNursingAssessment
Id: onc-goal-evaluation
Title: "Goal Evaluation"
* code from GoalEvaluationValueSet (required)
* extension contains ObservationGoalReference named goalReference 1..1 MS

Extension: ObservationGoalReference
Id: observation-goal-reference
Title: "Observation Goal Reference"
* value[x] only Reference(ONCPatientGoal)

Extension: InterventionGoalReference
Id: intervention-goal-reference
Title: "Intervention Goal Reference"
* value[x] only Reference(ONCPatientGoal)
