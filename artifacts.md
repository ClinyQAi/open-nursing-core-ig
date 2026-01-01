# Artifacts Summary - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* **Artifacts Summary**

## Artifacts Summary

This page provides a list of the FHIR artifacts defined as part of this implementation guide.

### Knowledge Artifacts: Plan Definitions 

These define workflows, rules, strategies, or protocols as part of content in this implementation guide.

| |
| :--- |
| [NEWS2 Escalation Protocol](PlanDefinition-news2-escalation-plan.md) |

### Knowledge Artifacts: Libraries 

These define logic, asset collections and other libraries as part of content in this implementation guide.

| | |
| :--- | :--- |
| [ONC NEWS2 Auto-Calculation Logic](Library-onc-news2-cql.md) | Logic library for calculating National Early Warning Score 2 (NEWS2) from FHIR Observations. |

### Structures: Resource Profiles 

These define constraints on FHIR resources for systems conforming to this implementation guide.

| | |
| :--- | :--- |
| [4AT Delirium Assessment](StructureDefinition-onc-4at-delirium.md) | Rapid clinical test for delirium (4AT) comprising Alertness, AMT4, Attention, and Acute Change/Fluctuating Course. A total score of 4 or more suggests possible delirium. |
| [ACVPU Consciousness Level](StructureDefinition-onc-acvpu.md) | ACVPU consciousness level assessment for NEWS2 (Alert, Confusion, Voice, Pain, Unresponsive) |
| [Abbey Pain Scale](StructureDefinition-onc-abbey-pain-scale.md) | Pain assessment for people with dementia or who cannot verbalise. Assesses 6 parameters: Vocalization, Facial Expression, Body Language, Behavioral Change, Physiological Change, Physical Changes. Total score determines pain severity (0-2 No pain, 3-7 Mild, 8-13 Moderate, 14+ Severe). |
| [Barthel Index](StructureDefinition-onc-barthel-index.md) | Barthel Index for measuring independence in activities of daily living (ADL). Score 0-20=total dependency, 91-99=slight dependency, 100=independent. Total range 0-100. |
| [Bladder Assessment](StructureDefinition-onc-bladder-assessment.md) | Detailed assessment of bladder function, including voiding patterns. |
| [Blood Pressure](StructureDefinition-onc-blood-pressure.md) | Blood pressure observation for NEWS2 (systolic BP used for scoring) |
| [Body Temperature](StructureDefinition-onc-body-temperature.md) | Body temperature observation for NEWS2 |
| [Bowel Assessment](StructureDefinition-onc-bowel-assessment.md) | Detailed assessment of bowel function and regularity. |
| [Braden Scale Assessment](StructureDefinition-onc-braden-scale-assessment.md) | A profile for the Braden Scale pressure ulcer risk assessment |
| [Bristol Stool Chart](StructureDefinition-onc-bristol-stool-chart.md) | Assessment of stool form using the Bristol Stool Chart (Types 1-7). Gold standard for bowel function assessment. |
| [Catheter Care](StructureDefinition-onc-catheter-care.md) | Documentation of catheter site care and status. |
| [Clinical Frailty Scale (CFS)](StructureDefinition-onc-clinical-frailty-scale.md) | Assessment of frailty using the Rockwood Clinical Frailty Scale (1-9). Essential for older adults to determine baseline functional status. |
| [Continence Assessment](StructureDefinition-onc-continence-assessment.md) | Assessment of bladder and bowel control status. |
| [Device Use Statement](StructureDefinition-onc-device-use-statement.md) | Documentation of mobility aids or other devices used by the patient. |
| [Dietary Requirements](StructureDefinition-onc-dietary-requirements.md) | Documentation of specific dietary needs (e.g. textural modification, cultural). |
| [Fluid Balance](StructureDefinition-onc-fluid-balance.md) | Assessment of fluid intake, output, and balance. Critical for renal function, hydration status, and heart failure monitoring. |
| [Glasgow Coma Scale](StructureDefinition-onc-glasgow-coma-scale.md) | Glasgow Coma Scale (GCS) for assessing level of consciousness. Total score 3-15 with three required components: Eye (1-4), Verbal (1-5), Motor (1-6). |
| [Heart Rate](StructureDefinition-onc-heart-rate.md) | Heart rate (pulse) observation for NEWS2 |
| [Inspired Oxygen](StructureDefinition-onc-inspired-oxygen.md) | Inspired oxygen observation for NEWS2 (air vs supplemental oxygen) |
| [MUST Score (Malnutrition Universal Screening Tool)](StructureDefinition-onc-must-score.md) | Malnutrition Universal Screening Tool for identifying adults at risk of malnutrition. Score 0=low risk, 1=medium risk, 2+=high risk. NHS-standard nutritional screening. |
| [Medication Management Ability](StructureDefinition-onc-medication-ability.md) | Assessment of the patient's ability to manage their own medication. |
| [Medication Self-Administration Observation](StructureDefinition-onc-medication-self-admin.md) | Observation of the patient performing self-administration. |
| [Mental Capacity Assessment](StructureDefinition-onc-mental-capacity.md) | Records the outcome of a Mental Capacity Assessment for a specific decision. Fundamental legal safeguard in UK nursing practice. |
| [Mini Mental State Examination (MMSE)](StructureDefinition-onc-mmse.md) | Mini Mental State Examination for cognitive function screening. Score 24-30=no impairment, 18-23=mild, 0-17=severe. Total range 0-30. |
| [Mobility Assessment](StructureDefinition-onc-mobility-assessment.md) | Assessment of capability to move and limitations. |
| [Monk Skin Tone Observation](StructureDefinition-onc-monk-skintone-observation.md) | Observation of patient skin tone using the Monk Skin Tone Scale (10-point scale A-J). Provides more granular skin tone assessment than Fitzpatrick scale, particularly for darker skin tones. Supports equitable care and accurate clinical assessment across diverse populations. |
| [Morse Fall Scale](StructureDefinition-onc-morse-fall-scale.md) | Morse Fall Scale for assessing fall risk. Score 0-24=no risk, 25-50=low risk, ≥51=high risk. Total range 0-125. |
| [NEWS2 Score](StructureDefinition-onc-news2-score.md) | National Early Warning Score 2 (NEWS2) for detecting clinical deterioration. Fully aligned with NHS CareConnect-NEWS2-Observation-1. |
| [NEWS2 Sub-Score](StructureDefinition-onc-news2-subscore.md) | Individual parameter sub-score for NEWS2 (0-3 for most parameters). References the related vital sign observation. |
| [Nursing Problem](StructureDefinition-onc-nursing-problem.md) | Nursing diagnosis or problem identified during assessment. Represents clinical judgments about individual, family, or community responses to actual or potential health problems. Part of the ADPIE framework's Diagnosis phase. |
| [ONC Goal Evaluation](StructureDefinition-onc-goal-evaluation.md) | Explicit evaluation of whether a nursing goal was achieved, closing the ADPIE loop. |
| [ONC NHS Patient](StructureDefinition-onc-nhs-patient.md) | A patient profile for use in NHS nursing contexts with ethnic category extension. |
| [ONC Nursing Clinical Impression](StructureDefinition-onc-nursing-clinical-impression.md) | Nurse's synthesis of patient progress against care plan, aggregating multiple goal evaluations. |
| [ONC Nursing Goal](StructureDefinition-onc-nursing-goal.md) | Patient-centered goal with mandatory evaluation requirements. Serves as the 'spine' of the CarePlan, linking problems to outcomes. |
| [ONC Nursing Intervention](StructureDefinition-onc-nursing-intervention.md) | Nursing intervention performed to achieve patient goals. Part of ADPIE Implementation phase. |
| [Open Nursing Core Assessment](StructureDefinition-onc-nursing-assessment.md) | Base profile for nursing assessment observations conforming to UK Core standards. Captures structured nursing assessment data as part of the ADPIE (Assessment, Diagnosis, Planning, Implementation, Evaluation) nursing process framework. Used as parent for specialized assessments like NEWS2, Braden Scale, and clinical observations. |
| [Oral Care Needs Assessment](StructureDefinition-onc-oral-care-assessment.md) | Assessment of mouth care needs and oral health. |
| [Oral Health Assessment](StructureDefinition-onc-oral-health.md) | Assessment of oral cavity health. Critical for prevention of pneumonia in frail elderly and maintaining nutrition/hydration. |
| [Oral Intake Assessment](StructureDefinition-onc-oral-intake-assessment.md) | Assessment of ability to take food and fluids orally. |
| [Oxygen Saturation](StructureDefinition-onc-oxygen-saturation.md) | Oxygen saturation (SpO2) observation for NEWS2 |
| [PBS ABC Chart](StructureDefinition-onc-abc-chart.md) | Antecedent-Behaviour-Consequence (ABC) Chart for recording behaviours of concern. Fundamental tool in Positive Behaviour Support (PBS) for Learning Disabilities. |
| [Pain Assessment (NRS 0-10)](StructureDefinition-onc-pain-assessment.md) | Pain severity assessment using the Numeric Rating Scale (0-10) |
| [Patient Story](StructureDefinition-onc-patient-story.md) | A narrative summary of the patient's background, biography, preferences, and personhood. Goes beyond clinical history to capture 'who the person is'. |
| [Personal Hygiene Needs Assessment](StructureDefinition-onc-hygiene-assessment.md) | Assessment of assistance required for personal hygiene. |
| [Reasonable Adjustment](StructureDefinition-onc-reasonable-adjustment.md) | Captures specific strict requirements for care adjustments under the Equality Act (e.g., 'Needs BSL Interpreter', 'Cannot use stairs', 'Requires large print'). |
| [Relational Engagement Score](StructureDefinition-onc-relational-observation.md) | Assessment of the quality and depth of the nurse-patient relationship or engagement level. Supports the relational aspect of care. |
| [Respiration Rate](StructureDefinition-onc-respiration-rate.md) | Respiration rate observation for NEWS2 |
| [Seizure Record](StructureDefinition-onc-seizure-record.md) | Record of a specific seizure event, including type, duration, triggers, and recovery phases. Essential for epilepsy management and identifying patterns. |
| [Skin Tone Observation](StructureDefinition-onc-skintone-observation.md) | Observation of patient skin tone using the Fitzpatrick skin type classification. Supports equitable care by enabling skin tone-aware clinical decision making, particularly for conditions that present differently across skin tones (e.g., pressure ulcers, cyanosis). |
| [Sleep Pattern](StructureDefinition-onc-sleep-pattern.md) | Observation of sleep quality, duration, and disturbances. Sleep pattern disturbance is a key indicator for delirium and general wellbeing. |
| [Swallowing Assessment](StructureDefinition-onc-swallowing-assessment.md) | Screening for dysphagia and swallowing difficulties. |
| [Urinalysis](StructureDefinition-onc-urinalysis.md) | Point-of-care urine dipstick test results. Used to screen for urinary tract infection (UTI), diabetes (glucose/ketones), and kidney health. |
| [Waterlow Score](StructureDefinition-onc-waterlow-score.md) | Waterlow Pressure Ulcer Risk Assessment - NHS standard tool. Score ≥10 indicates at risk, ≥15 high risk, ≥20 very high risk. |
| [What Matters to Me](StructureDefinition-onc-what-matters.md) | Captures the patient's specific, personal priorities and non-clinical goals (e.g., 'I want to walk my daughter down the aisle'). Fundamental to person-centred care. |
| [Wound Assessment](StructureDefinition-onc-wound-assessment.md) | Comprehensive wound assessment including staging and dimensions |
| [qSOFA (Quick SOFA)](StructureDefinition-onc-qsofa.md) | Quick Sequential Organ Failure Assessment for sepsis screening. Score ≥2 indicates high risk. Total range 0-3. |

### Structures: Extension Definitions 

These define constraints on FHIR data types for systems conforming to this implementation guide.

| | |
| :--- | :--- |
| [Intervention Goal Reference](StructureDefinition-intervention-goal-reference.md) | Extension to link nursing interventions to the patient goals they are intended to achieve. |
| [Observation Goal Reference](StructureDefinition-observation-goal-reference.md) | Extension to link goal evaluation observations to the patient goals being evaluated. |
| [UK Core Ethnic Category](StructureDefinition-UKCore-Extension-EthnicCategory.md) | An extension to record the ethnic category of a patient, as per UK Core standards. |

### Terminology: Value Sets 

These define sets of codes used by systems conforming to this implementation guide.

| | |
| :--- | :--- |
| [4AT AMT4 Value Set](ValueSet-onc-4at-amt4-vs.md) | Scoring options for AMT4 (Age, DOB, Place, Year) |
| [4AT Acute Change Value Set](ValueSet-onc-4at-acute-change-vs.md) | Scoring for Acute Change or Fluctuating Course |
| [4AT Alertness Value Set](ValueSet-onc-4at-alertness-vs.md) | Scoring options for 4AT Alertness |
| [4AT Attention Value Set](ValueSet-onc-4at-attention-vs.md) | Scoring for Months Backwards test |
| [ACVPU Value Set](ValueSet-acvpu-vs.md) | ACVPU consciousness level codes |
| [Clinical Frailty Scale Value Set](ValueSet-onc-cfs-vs.md) | Codes for Rockwood Clinical Frailty Scale (1-9) |
| [Fitzpatrick Skin Tone Value Set](ValueSet-skintone-vs.md) | Value set for Fitzpatrick skin type classifications |
| [Goal Evaluation Value Set](ValueSet-goal-evaluation-valueset.md) | Value set for evaluating patient goal outcomes |
| [Goal Target Measure ValueSet](ValueSet-onc-goal-target-measure-vs.md) | Codes used for goal target measures |
| [Housing Status Value Set](ValueSet-housing-status-vs.md) | Value set for patient housing status |
| [Inspired Oxygen Value Set](ValueSet-inspired-oxygen-vs.md) | Codes for inspired oxygen status |
| [Mental Capacity Finding Value Set](ValueSet-onc-mca-vs.md) | Codes indicating presence or absence of capacity |
| [Monk Skin Tone Scale ValueSet](ValueSet-onc-monk-scale-vs.md) |  |
| [NEWS2 Code Value Set](ValueSet-news2-code-vs.md) | LOINC and SNOMED codes for NEWS2 |
| [NEWS2 Sub-Score Codes](ValueSet-news2-subscore-code-vs.md) | SNOMED codes for NEWS2 sub-scores |
| [Nursing Intervention Value Set](ValueSet-nursing-intervention-valueset.md) | Value set for nursing interventions |
| [Nursing Problem Value Set](ValueSet-nursing-problem-valueset.md) | Value set for nursing problems and diagnoses |
| [Nursing Prognosis ValueSet](ValueSet-onc-prognosis-vs.md) | Prognosis codes for clinical impression |
| [PBS Behaviour Function ValueSet](ValueSet-onc-pbs-function-vs.md) | Common functions of behaviour (SEAT) |
| [Pain Assessment Code Value Set](ValueSet-pain-assessment-code-vs.md) | LOINC codes for pain severity assessment |
| [Problem Category Value Set](ValueSet-problem-category-valueset.md) | Value set for categorizing nursing problems |
| [Wound Stage Value Set](ValueSet-wound-stage-vs.md) |  |

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
| [example-4at-delirium](Observation-example-4at-delirium.md) |  |
| [example-abbey-pain](Observation-example-abbey-pain.md) |  |
| [example-abc-chart](Observation-example-abc-chart.md) |  |
| [example-bristol-stool](Observation-example-bristol-stool.md) |  |
| [example-clinical-frailty](Observation-example-clinical-frailty.md) |  |
| [example-fluid-balance](Observation-example-fluid-balance.md) |  |
| [example-goal-evaluation](Observation-example-goal-evaluation.md) |  |
| [example-mental-capacity](Observation-example-mental-capacity.md) |  |
| [example-nursing-intervention](Procedure-example-nursing-intervention.md) |  |
| [example-nursing-problem](Condition-example-nursing-problem.md) |  |
| [example-oral-health](Observation-example-oral-health.md) |  |
| [example-patient-goal](Goal-example-patient-goal.md) | Patient will remain free from falls. |
| [example-patient-story](Observation-example-patient-story.md) |  |
| [example-reasonable-adjustment](Observation-example-reasonable-adjustment.md) |  |
| [example-seizure-record](Observation-example-seizure-record.md) |  |
| [example-urinalysis](Observation-example-urinalysis.md) |  |
| [example-what-matters](Observation-example-what-matters.md) |  |
| [observation-braden-scale](Observation-observation-braden-scale.md) |  |
| [observation-skin-tone](Observation-observation-skin-tone.md) |  |
| [patient-example-jane](Patient-patient-example-jane.md) |  |
| [practitioner-example](Practitioner-practitioner-example.md) |  |

