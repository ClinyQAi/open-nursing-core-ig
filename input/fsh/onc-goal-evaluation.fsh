// =============================================================================
// ADPIE Evaluation Profiles
// =============================================================================

// -----------------------------------------------------------------------------
// Goal Profile (with mandatory evaluation timing)
// -----------------------------------------------------------------------------
Profile: ONCNursingGoal
Parent: Goal
Id: onc-nursing-goal
Title: "ONC Nursing Goal"
Description: "Patient-centered goal with mandatory evaluation requirements. Serves as the 'spine' of the CarePlan, linking problems to outcomes."

* lifecycleStatus MS
* achievementStatus MS
* category = http://terminology.hl7.org/CodeSystem/goal-category#nursing
* subject only Reference(Patient)
* target 1..* MS
* target.measure from ONCGoalTargetMeasureVS (extensible)
* target.dueDate 1..1 MS
* addresses 1..* MS
* addresses only Reference(ONCNursingProblem)

// Invariant: Must be evaluated (closed loop)
* obeys onc-goal-evaluation-timing

// -----------------------------------------------------------------------------
// Nursing Intervention (Implementation)
// -----------------------------------------------------------------------------
Profile: ONCNursingIntervention
Parent: Procedure
Id: onc-nursing-intervention
Title: "ONC Nursing Intervention"
Description: "Nursing intervention performed to achieve patient goals. Part of ADPIE Implementation phase."

* status = #completed
* status MS
* code 1..1 MS
* code from NursingInterventionValueSet (required)
* extension contains InterventionGoalReference named interventionGoal 0..* MS

// -----------------------------------------------------------------------------
// Goal Evaluation Profile (The Outcome)
// -----------------------------------------------------------------------------
Profile: ONCGoalEvaluation
Parent: Observation
Id: onc-goal-evaluation
Title: "ONC Goal Evaluation"
Description: "Explicit evaluation of whether a nursing goal was achieved, closing the ADPIE loop."

* status MS
* code = http://snomed.info/sct#390906007 "Follow-up assessment"
* subject only Reference(Patient)
* focus 1..1 MS
* focus only Reference(ONCNursingGoal)
* value[x] only CodeableConcept
* valueCodeableConcept from GoalEvaluationValueSet (required)
* derivedFrom 0..* MS
* derivedFrom only Reference(Observation)
* note 0..1 MS
* extension contains ObservationGoalReference named goalReference 0..1 MS // Legacy support or explicit link


// -----------------------------------------------------------------------------
// Nursing Clinical Impression (The Synthesis)
// -----------------------------------------------------------------------------
Profile: ONCNursingClinicalImpression
Parent: ClinicalImpression
Id: onc-nursing-clinical-impression
Title: "ONC Nursing Clinical Impression"
Description: "Nurse's synthesis of patient progress against care plan, aggregating multiple goal evaluations."

* status MS
* code = http://snomed.info/sct#225358003 "Nursing assessment"
* subject only Reference(Patient)
* encounter MS
* effectiveDateTime MS
* assessor only Reference(Practitioner)
* problem 1..* MS
* problem only Reference(Condition)
* supportingInfo MS
* supportingInfo only Reference(ONCGoalEvaluation)
* summary MS
* prognosisCodeableConcept from ONCPrognosisVS (extensible)


// -----------------------------------------------------------------------------
// Extensions & ValueSets
// -----------------------------------------------------------------------------
Extension: ObservationGoalReference
Id: observation-goal-reference
Title: "Observation Goal Reference"
Description: "Extension to link goal evaluation observations to the patient goals being evaluated."
* value[x] only Reference(ONCNursingGoal)

Extension: InterventionGoalReference
Id: intervention-goal-reference
Title: "Intervention Goal Reference"
Description: "Extension to link nursing interventions to the patient goals they are intended to achieve."
* value[x] only Reference(ONCNursingGoal)

ValueSet: ONCGoalTargetMeasureVS
Id: onc-goal-target-measure-vs
Title: "Goal Target Measure ValueSet"
Description: "Codes used for goal target measures"
* include http://loinc.org#59408-5 "Oxygen saturation"
* include http://snomed.info/sct#225358003 "Wound care"
// Add more relevant target measures

ValueSet: ONCPrognosisVS
Id: onc-prognosis-vs
Title: "Nursing Prognosis ValueSet"
Description: "Prognosis codes for clinical impression"
* include http://snomed.info/sct#17621005 "Normal"
* include http://snomed.info/sct#260388008 "Worsening"
* include http://snomed.info/sct#385633008 "Improving"

// -----------------------------------------------------------------------------
// Invariants
// -----------------------------------------------------------------------------
Invariant: onc-goal-evaluation-timing
Description: "Goal must have evaluation observation by target.dueDate"
Expression: "target.dueDate.exists() implies (lifecycleStatus = 'active' or lifecycleStatus = 'completed' or lifecycleStatus = 'cancelled')"
Severity: #warning
