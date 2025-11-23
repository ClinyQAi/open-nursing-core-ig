# Artifacts Summary - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* **Artifacts Summary**

## Artifacts Summary

This page provides a list of the FHIR artifacts defined as part of this implementation guide.

### Structures: Resource Profiles 

These define constraints on FHIR resources for systems conforming to this implementation guide.

| | |
| :--- | :--- |
| [Open Nursing Core Assessment](StructureDefinition-onc-nursing-assessment.md) | Base profile for nursing assessments. |
| [Open Nursing Core Braden Scale Assessment](StructureDefinition-onc-braden-scale-assessment.md) | Braden Scale assessment for pressure injury risk. |
| [Open Nursing Core Goal Evaluation](StructureDefinition-onc-goal-evaluation.md) | Evaluation of a patient's progress towards a goal. |
| [Open Nursing Core Nursing Care Plan](StructureDefinition-onc-nursing-care-plan.md) | Nursing care plan. |
| [Open Nursing Core Nursing Intervention](StructureDefinition-onc-nursing-intervention.md) | Nursing intervention performed. |
| [Open Nursing Core Nursing Problem](StructureDefinition-onc-nursing-problem.md) | Nursing problem or diagnosis. |
| [Open Nursing Core Patient Goal](StructureDefinition-onc-patient-goal.md) | Patient goal addressing a nursing problem. |

### Structures: Extension Definitions 

These define constraints on FHIR data types for systems conforming to this implementation guide.

| | |
| :--- | :--- |
| [Intervention Goal Reference](StructureDefinition-intervention-goal-reference.md) | Reference to the goal this intervention addresses. |
| [Observation Goal Reference](StructureDefinition-observation-goal-reference.md) | Reference to the goal that is being evaluated. |

### Terminology: Value Sets 

These define sets of codes used by systems conforming to this implementation guide.

| |
| :--- |
| [Goal Evaluation Value Set](ValueSet-goal-evaluation-valueset.md) |
| [Nursing Intervention Value Set](ValueSet-nursing-intervention-valueset.md) |
| [Nursing Problem Value Set](ValueSet-nursing-problem-valueset.md) |

### Terminology: Code Systems 

These define new code systems used by systems conforming to this implementation guide.

| |
| :--- |
| [Open Nursing Core Problem Type CodeSystem](CodeSystem-onc-problem-type.md) |

### Example: Example Instances 

These are example instances that show what data produced and consumed by systems conforming with this implementation guide might look like.

| | |
| :--- | :--- |
| [example-braden-scale](Observation-example-braden-scale.md) |  |
| [example-goal-evaluation](Observation-example-goal-evaluation.md) |  |
| [example-nursing-care-plan](CarePlan-example-nursing-care-plan.md) |  |
| [example-nursing-intervention](Procedure-example-nursing-intervention.md) |  |
| [example-nursing-problem](Condition-example-nursing-problem.md) |  |
| [example-patient-goal](Goal-example-patient-goal.md) | Patient will remain free from falls throughout the hospital stay. |
| [patient-example](Patient-patient-example.md) |  |
| [practitioner-example](Practitioner-practitioner-example.md) |  |

