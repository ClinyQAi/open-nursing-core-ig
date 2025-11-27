Profile: ONCNursingAssessment
Parent: Observation
Id: onc-nursing-assessment
Title: "Open Nursing Core Assessment"
* category ^slicing.discriminator.type = #pattern
* category ^slicing.discriminator.path = "coding.code"
* category ^slicing.ordered = false
* category ^slicing.rules = #open
* category contains nursing 1..1 MS
* category[nursing].coding.system = "http://terminology.hl7.org/CodeSystem/observation-category"
* category[nursing].coding.code = #nursing
* performer 1..1 MS
* performer only Reference(Practitioner or PractitionerRole)
* value[x] 1..1 MS
* value[x] only CodeableConcept or Quantity

Profile: ONCBradenScaleAssessment
Parent: ONCNursingAssessment
Id: onc-braden-scale-assessment
Title: "Braden Scale Assessment"
// FIX: Separated Value and MS Flag
* status = #final
* status MS
* code = http://loinc.org#9017-7 "Braden Scale total score"
* code MS
* value[x] only Quantity
* valueQuantity 1..1 MS
* valueQuantity.unit = "score"
* valueQuantity.system = "http://unitsofmeasure.org"
* component 6..6 MS
* component ^slicing.discriminator.type = #pattern
* component ^slicing.discriminator.path = "code"
* component ^slicing.ordered = false
* component ^slicing.rules = #open
* component contains sensoryPerception 1..1 MS and moisture 1..1 MS and activity 1..1 MS and mobility 1..1 MS and nutrition 1..1 MS and frictionAndShear 1..1 MS
* component[sensoryPerception].code = http://loinc.org#74012-8 "Sensory Perception"
* component[sensoryPerception].value[x] only Quantity
* component[moisture].code = http://loinc.org#74013-6 "Moisture"
* component[moisture].value[x] only Quantity
* component[activity].code = http://loinc.org#74014-4 "Activity"
* component[activity].value[x] only Quantity
* component[mobility].code = http://loinc.org#74015-1 "Mobility"
* component[mobility].value[x] only Quantity
* component[nutrition].code = http://loinc.org#74016-9 "Nutrition"
* component[nutrition].value[x] only Quantity
* component[frictionAndShear].code = http://loinc.org#74017-7 "Friction and Shear"
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
