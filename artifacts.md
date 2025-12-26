# Artifacts Summary - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* **Artifacts Summary**

## Artifacts Summary

This page provides a list of the FHIR artifacts defined as part of this implementation guide.

### Structures: Resource Profiles 

These define constraints on FHIR resources for systems conforming to this implementation guide.

| | |
| :--- | :--- |
| [ACVPU Consciousness Level](StructureDefinition-onc-acvpu.md) | ACVPU consciousness level assessment for NEWS2 (Alert, Confusion, Voice, Pain, Unresponsive) |
| [Barthel Index](StructureDefinition-onc-barthel-index.md) | Barthel Index for measuring independence in activities of daily living (ADL). Score 0-20=total dependency, 91-99=slight dependency, 100=independent. Total range 0-100. |
| [Blood Pressure](StructureDefinition-onc-blood-pressure.md) | Blood pressure observation for NEWS2 (systolic BP used for scoring) |
| [Body Temperature](StructureDefinition-onc-body-temperature.md) | Body temperature observation for NEWS2 |
| [Braden Scale Assessment](StructureDefinition-onc-braden-scale-assessment.md) | A profile for the Braden Scale pressure ulcer risk assessment |
| [Glasgow Coma Scale](StructureDefinition-onc-glasgow-coma-scale.md) | Glasgow Coma Scale (GCS) for assessing level of consciousness. Total score 3-15 with three required components: Eye (1-4), Verbal (1-5), Motor (1-6). |
| [Goal Evaluation](StructureDefinition-onc-goal-evaluation.md) |  |
| [Heart Rate](StructureDefinition-onc-heart-rate.md) | Heart rate (pulse) observation for NEWS2 |
| [Inspired Oxygen](StructureDefinition-onc-inspired-oxygen.md) | Inspired oxygen observation for NEWS2 (air vs supplemental oxygen) |
| [MUST Score (Malnutrition Universal Screening Tool)](StructureDefinition-onc-must-score.md) | Malnutrition Universal Screening Tool for identifying adults at risk of malnutrition. Score 0=low risk, 1=medium risk, 2+=high risk. NHS-standard nutritional screening. |
| [Mini Mental State Examination (MMSE)](StructureDefinition-onc-mmse.md) | Mini Mental State Examination for cognitive function screening. Score 24-30=no impairment, 18-23=mild, 0-17=severe. Total range 0-30. |
| [Monk Skin Tone Observation](StructureDefinition-onc-monk-skintone-observation.md) |  |
| [Morse Fall Scale](StructureDefinition-onc-morse-fall-scale.md) | Morse Fall Scale for assessing fall risk. Score 0-24=no risk, 25-50=low risk, ≥51=high risk. Total range 0-125. |
| [NEWS2 Score](StructureDefinition-onc-news2-score.md) | National Early Warning Score 2 (NEWS2) for detecting clinical deterioration. Fully aligned with NHS CareConnect-NEWS2-Observation-1. |
| [NEWS2 Sub-Score](StructureDefinition-onc-news2-subscore.md) | Individual parameter sub-score for NEWS2 (0-3 for most parameters). References the related vital sign observation. |
| [Nursing Intervention](StructureDefinition-onc-nursing-intervention.md) |  |
| [Nursing Problem](StructureDefinition-onc-nursing-problem.md) |  |
| [ONC NHS Patient](StructureDefinition-onc-nhs-patient.md) | A patient profile for use in NHS nursing contexts with ethnic category extension. |
| [Open Nursing Core Assessment](StructureDefinition-onc-nursing-assessment.md) |  |
| [Oxygen Saturation](StructureDefinition-onc-oxygen-saturation.md) | Oxygen saturation (SpO2) observation for NEWS2 |
| [Pain Assessment (NRS 0-10)](StructureDefinition-onc-pain-assessment.md) | Pain severity assessment using the Numeric Rating Scale (0-10) |
| [Patient Goal](StructureDefinition-onc-patient-goal.md) |  |
| [Respiration Rate](StructureDefinition-onc-respiration-rate.md) | Respiration rate observation for NEWS2 |
| [Skin Tone Observation](StructureDefinition-onc-skintone-observation.md) |  |
| [Waterlow Score](StructureDefinition-onc-waterlow-score.md) | Waterlow Pressure Ulcer Risk Assessment - NHS standard tool. Score ≥10 indicates at risk, ≥15 high risk, ≥20 very high risk. |
| [Wound Assessment](StructureDefinition-onc-wound-assessment.md) | Comprehensive wound assessment including staging and dimensions |
| [qSOFA (Quick SOFA)](StructureDefinition-onc-qsofa.md) | Quick Sequential Organ Failure Assessment for sepsis screening. Score ≥2 indicates high risk. Total range 0-3. |

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
| [ACVPU Value Set](ValueSet-acvpu-vs.md) | ACVPU consciousness level codes |
| [Fitzpatrick Skin Tone Value Set](ValueSet-skintone-vs.md) | Value set for Fitzpatrick skin type classifications |
| [Goal Evaluation Value Set](ValueSet-goal-evaluation-valueset.md) | Value set for evaluating patient goal outcomes |
| [Housing Status Value Set](ValueSet-housing-status-vs.md) | Value set for patient housing status |
| [Inspired Oxygen Value Set](ValueSet-inspired-oxygen-vs.md) | Codes for inspired oxygen status |
| [Monk Skin Tone Scale ValueSet](ValueSet-onc-monk-scale-vs.md) |  |
| [NEWS2 Code Value Set](ValueSet-news2-code-vs.md) | LOINC and SNOMED codes for NEWS2 |
| [NEWS2 Sub-Score Codes](ValueSet-news2-subscore-code-vs.md) | SNOMED codes for NEWS2 sub-scores |
| [Nursing Intervention Value Set](ValueSet-nursing-intervention-valueset.md) | Value set for nursing interventions |
| [Nursing Problem Value Set](ValueSet-nursing-problem-valueset.md) | Value set for nursing problems and diagnoses |
| [Pain Assessment Code Value Set](ValueSet-pain-assessment-code-vs.md) | LOINC codes for pain severity assessment |
| [Problem Category Value Set](ValueSet-problem-category-valueset.md) | Value set for categorizing nursing problems |
| [Wound Stage Value Set](ValueSet-wound-stage-vs.md) | SNOMED CT codes for pressure ulcer staging |

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

