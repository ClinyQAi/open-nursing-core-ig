# Artifacts Summary - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* **Artifacts Summary**

## Artifacts Summary

This page provides a list of the FHIR artifacts defined as part of this implementation guide.

### Structures: Resource Profiles 

These define constraints on FHIR resources for systems conforming to this implementation guide.

| | |
| :--- | :--- |
| [Braden Scale Assessment](StructureDefinition-onc-braden-scale-assessment.md) | A profile for the Braden Scale pressure ulcer risk assessment |
| [Goal Evaluation](StructureDefinition-onc-goal-evaluation.md) |  |
| [Monk Skin Tone Observation](StructureDefinition-onc-monk-skintone-observation.md) |  |
| [Nursing Intervention](StructureDefinition-onc-nursing-intervention.md) |  |
| [Nursing Problem](StructureDefinition-onc-nursing-problem.md) |  |
| [ONC NHS Patient](StructureDefinition-onc-nhs-patient.md) | A patient profile for use in NHS nursing contexts with ethnic category extension. |
| [Open Nursing Core Assessment](StructureDefinition-onc-nursing-assessment.md) |  |
| [Patient Goal](StructureDefinition-onc-patient-goal.md) |  |
| [Skin Tone Observation](StructureDefinition-onc-skintone-observation.md) |  |

### Structures: Extension Definitions 

These define constraints on FHIR data types for systems conforming to this implementation guide.

| | |
| :--- | :--- |
| [Intervention Goal Reference](StructureDefinition-intervention-goal-reference.md) |  |
| [Observation Goal Reference](StructureDefinition-observation-goal-reference.md) |  |
| [UK Core Ethnic Category](StructureDefinition-UKCore-Extension-EthnicCategory.md) | An extension to record the ethnic category of a patient, as per UK Core standards. |

### Terminology: Value Sets 

These define sets of codes used by systems conforming to this implementation guide.

| | |
| :--- | :--- |
| [Fitzpatrick Skin Tone Value Set](ValueSet-skintone-vs.md) | Value set for Fitzpatrick skin type classifications |
| [Goal Evaluation Value Set](ValueSet-goal-evaluation-valueset.md) | Value set for evaluating patient goal outcomes |
| [Housing Status Value Set](ValueSet-housing-status-vs.md) | Value set for patient housing status |
| [Monk Skin Tone Scale ValueSet](ValueSet-onc-monk-scale-vs.md) |  |
| [Nursing Intervention Value Set](ValueSet-nursing-intervention-valueset.md) | Value set for nursing interventions |
| [Nursing Problem Value Set](ValueSet-nursing-problem-valueset.md) | Value set for nursing problems and diagnoses |
| [Problem Category Value Set](ValueSet-problem-category-valueset.md) | Value set for categorizing nursing problems |

### Terminology: Code Systems 

These define new code systems used by systems conforming to this implementation guide.

| | |
| :--- | :--- |
| [Monk Skin Tone Scale CodeSystem](CodeSystem-onc-monk-scale.md) |  |
| [ONC Observation Codes](CodeSystem-onc-observation-codes.md) | Custom observation codes for Open Nursing Core |
| [Problem Type CodeSystem](CodeSystem-onc-problem-type.md) | Code system for categorizing types of nursing problems |

### Example: Example Instances 

These are example instances that show what data produced and consumed by systems conforming with this implementation guide might look like.

| | |
| :--- | :--- |
| [example-goal-evaluation](Observation-example-goal-evaluation.md) |  |
| [example-nursing-intervention](Procedure-example-nursing-intervention.md) |  |
| [example-nursing-problem](Condition-example-nursing-problem.md) |  |
| [example-patient-goal](Goal-example-patient-goal.md) | Patient will remain free from falls. |
| [observation-braden-scale](Observation-observation-braden-scale.md) |  |
| [observation-skin-tone](Observation-observation-skin-tone.md) |  |
| [patient-example-jane](Patient-patient-example-jane.md) |  |
| [practitioner-example](Practitioner-practitioner-example.md) |  |

