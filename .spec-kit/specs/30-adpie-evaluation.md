# Spec 30: ADPIE Evaluation Profile

## Status
- [x] Specify
- [ ] Plan
- [ ] Tasks
- [ ] Implement

## Clinical Context
The **Evaluation** stage of ADPIE is the most neglected in digital systems. Most EHRs capture Assessment, create a CarePlan, but fail to formally **close the loop** by evaluating whether goals were achieved.

This specification creates a dedicated **Goal Evaluation** profile that forces explicit outcome measurement.

## The Problem
- Goals created but never formally evaluated
- No structured link between follow-up observations and original goals
- ClinicalImpression rarely used for nursing synthesis
- AI systems cannot learn from outcomes because evaluation data is missing

## The Solution
Create three linked profiles:
1. **ONCGoalEvaluation**: Explicit goal outcome assessment
2. **ONCNursingClinicalImpression**: Nursing synthesis of patient progress
3. **Enhanced Goal**: With mandatory evaluation timing

---

## Clinical Requirements

### Goal Evaluation Workflow
```
[Goal] ──creates──> [Target Metric]
   │
   └──evaluates──> [Follow-up Observation]
                          │
                          └──results in──> [Goal Evaluation]
                                                  │
                                                  └──updates──> [Goal.lifecycleStatus]
```

### SNOMED Coding
- **Goal Evaluation**: `390906007` - Follow-up assessment
- **Goal Achieved**: `385652002` - Objective achieved
- **Goal Not Achieved**: `385651009` - Objective not achieved
- **Goal Partially Achieved**: To be mapped

---

## FHIR Structure

### Profile: ONCGoalEvaluation

```fsh
Profile: ONCGoalEvaluation
Parent: Observation
Id: onc-goal-evaluation
Title: "ONC Goal Evaluation"
Description: "Explicit evaluation of whether a nursing goal was achieved."

* status MS
* code = http://snomed.info/sct#390906007 "Follow-up assessment"
* subject only Reference(Patient)
* focus 1..1 MS
* focus only Reference(Goal)
* valueCodeableConcept from ONCGoalOutcomeVS (required)
* derivedFrom 0..* MS
* derivedFrom only Reference(Observation)
* note 0..1 MS
```

### ValueSet: GoalOutcomeVS

```fsh
ValueSet: ONCGoalOutcomeVS
Id: onc-goal-outcome-vs
Title: "Goal Outcome ValueSet"
Description: "Possible outcomes of goal evaluation"

* http://snomed.info/sct#385652002 "Objective achieved"
* http://snomed.info/sct#385651009 "Objective not achieved"
* http://snomed.info/sct#255609007 "Partial"
* http://snomed.info/sct#723510000 "Sustained improvement"
* http://snomed.info/sct#260388008 "Worsening"
```

### Profile: ONCNursingClinicalImpression

```fsh
Profile: ONCNursingClinicalImpression
Parent: ClinicalImpression
Id: onc-nursing-clinical-impression
Title: "ONC Nursing Clinical Impression"
Description: "Nurse's synthesis of patient progress against care plan."

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
```

### Enhanced Goal Profile

```fsh
Profile: ONCNursingGoal
Parent: Goal
Id: onc-nursing-goal
Title: "ONC Nursing Goal"
Description: "Goal with mandatory evaluation requirements."

* lifecycleStatus MS
* achievementStatus MS
* category = http://terminology.hl7.org/CodeSystem/goal-category#nursing
* subject only Reference(Patient)
* target 1..* MS
* target.measure from ONCGoalTargetMeasureVS (extensible)
* target.dueDate 1..1 MS
* addresses 1..* MS
* addresses only Reference(Condition)

// Invariant: Must be evaluated by due date
* obeys onc-goal-evaluation-timing
```

### Invariant: Evaluation Timing

```fsh
Invariant: onc-goal-evaluation-timing
Description: "Goal must have evaluation observation by target.dueDate"
Expression: "target.dueDate.exists() implies (Goal.where(lifecycleStatus = 'completed' or lifecycleStatus = 'cancelled').exists())"
Severity: #warning
```

---

## CQL Logic for Auto-Update

```cql
library ONC_Goal_Evaluation version '1.0.0'

define "Goals Due for Evaluation":
  [Goal] G
    where G.target.dueDate <= Today()
      and G.lifecycleStatus in {'active', 'on-hold'}

define "Goals with Positive Outcome":
  [Observation: "ONCGoalEvaluation"] O
    where O.valueCodeableConcept.coding.code = '385652002'
    return O.focus

// Auto-update goal status
define "Should Update Goal to Achieved":
  exists("Goals with Positive Outcome")
```

---

## Success Metrics
- [ ] Goal Evaluation profile compiles without errors
- [ ] ClinicalImpression links correctly to multiple goal evaluations
- [ ] Goal lifecycleStatus updates based on evaluation outcome
- [ ] CQL correctly identifies overdue goals
- [ ] Example chain: Goal → Evaluation → Updated Goal → ClinicalImpression

---

## Example Instance Chain

```json
// 1. Original Goal
{
  "resourceType": "Goal",
  "id": "sp02-goal",
  "lifecycleStatus": "active",
  "description": { "text": "Maintain SpO2 > 95%" },
  "target": [{
    "measure": { "coding": [{ "code": "59408-5", "display": "SpO2" }] },
    "detailQuantity": { "value": 95, "comparator": ">" },
    "dueDate": "2026-01-15"
  }],
  "addresses": [{ "reference": "Condition/ineffective-airway" }]
}

// 2. Follow-up Observation
{
  "resourceType": "Observation",
  "id": "sp02-followup",
  "code": { "coding": [{ "code": "59408-5" }] },
  "valueQuantity": { "value": 97 }
}

// 3. Goal Evaluation
{
  "resourceType": "Observation",
  "id": "goal-eval-1",
  "code": { "coding": [{ "code": "390906007", "display": "Follow-up assessment" }] },
  "focus": [{ "reference": "Goal/sp02-goal" }],
  "derivedFrom": [{ "reference": "Observation/sp02-followup" }],
  "valueCodeableConcept": { "coding": [{ "code": "385652002", "display": "Objective achieved" }] }
}

// 4. Updated Goal
{
  "resourceType": "Goal",
  "id": "sp02-goal",
  "lifecycleStatus": "completed",
  "achievementStatus": { "coding": [{ "code": "achieved" }] }
}
```

---

## References
- HL7 FHIR Goal Resource
- NHS England: Patient Goals in Digital Records
- Foundation of Nursing Studies: Outcome Measurement
