# ONC Observation Codes - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **ONC Observation Codes**

## CodeSystem: ONC Observation Codes 

| | |
| :--- | :--- |
| *Official URL*:https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes | *Version*:0.1.0 |
| Draft as of 2026-01-02 | *Computable Name*:ONCObservationCodes |

 
Custom observation codes for Open Nursing Core 

 This Code system is referenced in the content logical definition of the following value sets: 

* [NEWS2CodeValueSet](ValueSet-news2-code-vs.md)
* [NEWS2SubscoreCodeValueSet](ValueSet-news2-subscore-code-vs.md)
* [NursingProblemValueSet](ValueSet-nursing-problem-valueset.md)
* [AlertnessVS](ValueSet-onc-4at-alertness-vs.md)
* [ClinicalFrailtyScaleVS](ValueSet-onc-cfs-vs.md)
* [MentalCapacityVS](ValueSet-onc-mca-vs.md)
* [PBSFunctionVS](ValueSet-onc-pbs-function-vs.md)
* [SkinToneVS](ValueSet-skintone-vs.md)
* [WoundStageValueSet](ValueSet-wound-stage-vs.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "onc-observation-codes",
  "url" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
  "version" : "0.1.0",
  "name" : "ONCObservationCodes",
  "title" : "ONC Observation Codes",
  "status" : "draft",
  "date" : "2026-01-02T16:27:10+00:00",
  "description" : "Custom observation codes for Open Nursing Core",
  "content" : "complete",
  "count" : 121,
  "concept" : [
    {
      "code" : "mst-score",
      "display" : "Monk Skin Tone Score",
      "definition" : "Assessment of skin tone using the Monk Skin Tone Scale"
    },
    {
      "code" : "waterlow-score",
      "display" : "Waterlow Score",
      "definition" : "Total score for Waterlow pressure ulcer risk assessment"
    },
    {
      "code" : "must-score",
      "display" : "MUST Score",
      "definition" : "Malnutrition Universal Screening Tool total score"
    },
    {
      "code" : "must-bmi-score",
      "display" : "MUST BMI Score",
      "definition" : "Malnutrition Universal Screening Tool BMI score"
    },
    {
      "code" : "must-weight-loss-score",
      "display" : "MUST Weight Loss Score",
      "definition" : "Malnutrition Universal Screening Tool weight loss score"
    },
    {
      "code" : "must-acute-disease-score",
      "display" : "MUST Acute Disease Score",
      "definition" : "Malnutrition Universal Screening Tool acute disease effect score"
    },
    {
      "code" : "braden-total-score",
      "display" : "Braden Total Score",
      "definition" : "Braden scale total score"
    },
    {
      "code" : "braden-sensory",
      "display" : "Braden Sensory Perception",
      "definition" : "Sensory perception Braden scale"
    },
    {
      "code" : "braden-moisture",
      "display" : "Braden Moisture",
      "definition" : "Moisture Braden scale"
    },
    {
      "code" : "braden-activity",
      "display" : "Braden Activity",
      "definition" : "Activity Braden scale"
    },
    {
      "code" : "braden-mobility",
      "display" : "Braden Mobility",
      "definition" : "Mobility Braden scale"
    },
    {
      "code" : "braden-nutrition",
      "display" : "Braden Nutrition",
      "definition" : "Nutrition Braden scale"
    },
    {
      "code" : "braden-friction",
      "display" : "Braden Friction/Shear",
      "definition" : "Friction and shear Braden scale"
    },
    {
      "code" : "barthel-score",
      "display" : "Barthel Index Score",
      "definition" : "Total score for Barthel Index assessment"
    },
    {
      "code" : "news2-score",
      "display" : "NEWS2 Score",
      "definition" : "National Early Warning Score 2 Total Score"
    },
    {
      "code" : "news2-subscore",
      "display" : "NEWS2 Sub-score",
      "definition" : "Sub-score for NEWS2 parameter"
    },
    {
      "code" : "wound-stage",
      "display" : "Wound Stage",
      "definition" : "Stage of the wound"
    },
    {
      "code" : "stage-1",
      "display" : "Stage 1",
      "definition" : "Stage 1 pressure ulcer"
    },
    {
      "code" : "stage-2",
      "display" : "Stage 2",
      "definition" : "Stage 2 pressure ulcer"
    },
    {
      "code" : "stage-3",
      "display" : "Stage 3",
      "definition" : "Stage 3 pressure ulcer"
    },
    {
      "code" : "stage-4",
      "display" : "Stage 4",
      "definition" : "Stage 4 pressure ulcer"
    },
    {
      "code" : "unstageable",
      "display" : "Unstageable",
      "definition" : "Unstageable pressure ulcer"
    },
    {
      "code" : "deep-tissue",
      "display" : "Deep Tissue Injury",
      "definition" : "Deep tissue injury"
    },
    {
      "code" : "risk-falls",
      "display" : "Risk of Falls",
      "definition" : "Risk of falls diagnosis"
    },
    {
      "code" : "fitzpatrick-1",
      "display" : "Type I",
      "definition" : "Pale white; always burns, never tans"
    },
    {
      "code" : "fitzpatrick-2",
      "display" : "Type II",
      "definition" : "White; usually burns, tans with difficulty"
    },
    {
      "code" : "fitzpatrick-3",
      "display" : "Type III",
      "definition" : "Cream white; sometimes mild burn, gradually tans"
    },
    {
      "code" : "fitzpatrick-4",
      "display" : "Type IV",
      "definition" : "Moderate brown; rarely burns, tans with ease"
    },
    {
      "code" : "fitzpatrick-5",
      "display" : "Type V",
      "definition" : "Dark brown; very rarely burns, tans very easily"
    },
    {
      "code" : "fitzpatrick-6",
      "display" : "Type VI",
      "definition" : "Deeply pigmented dark brown to black; never burns, tans very easily"
    },
    {
      "code" : "what-matters",
      "display" : "What Matters to Me",
      "definition" : "Patient-identified priorities and non-clinical goals"
    },
    {
      "code" : "patient-story",
      "display" : "Patient Story",
      "definition" : "Narrative summary of patient background, preferences, and autobiography"
    },
    {
      "code" : "relational-engagement",
      "display" : "Relational Engagement Score",
      "definition" : "Assessment of the quality of nurse-patient engagement (1-5)"
    },
    {
      "code" : "cfs-score",
      "display" : "Clinical Frailty Scale Score",
      "definition" : "Total score for Rockwood Clinical Frailty Scale"
    },
    {
      "code" : "cfs-1",
      "display" : "Very Fit",
      "definition" : "Robus, active, energetic and motivated"
    },
    {
      "code" : "cfs-2",
      "display" : "Well",
      "definition" : "No active disease symptoms but less fit than category 1"
    },
    {
      "code" : "cfs-3",
      "display" : "Managing Well",
      "definition" : "Medical problems are well controlled, but not regularly active"
    },
    {
      "code" : "cfs-4",
      "display" : "Vulnerable",
      "definition" : "Not dependent for daily help, but symptoms limit activities"
    },
    {
      "code" : "cfs-5",
      "display" : "Mildly Frail",
      "definition" : "Need help with high order IADLs (finances, transportation, heavy housework)"
    },
    {
      "code" : "cfs-6",
      "display" : "Moderately Frail",
      "definition" : "Need help with all outside activities and some housekeeping"
    },
    {
      "code" : "cfs-7",
      "display" : "Severely Frail",
      "definition" : "Completely dependent for personal care"
    },
    {
      "code" : "cfs-8",
      "display" : "Very Severely Frail",
      "definition" : "Completely dependent, approaching end of life"
    },
    {
      "code" : "cfs-9",
      "display" : "Terminally Ill",
      "definition" : "Approaching the end of life (life expectancy <6 months)"
    },
    {
      "code" : "4at-score",
      "display" : "4AT Delirium Score",
      "definition" : "Total score for 4AT assessment"
    },
    {
      "code" : "4at-alertness",
      "display" : "Alertness",
      "definition" : "4AT Item 1: Alertness"
    },
    {
      "code" : "4at-amt4",
      "display" : "AMT4 Score",
      "definition" : "4AT Item 2: Abbreviated Mental Test 4"
    },
    {
      "code" : "4at-attention",
      "display" : "Attention",
      "definition" : "4AT Item 3: Attention (Months Backwards)"
    },
    {
      "code" : "4at-acute-change",
      "display" : "Acute Change",
      "definition" : "4AT Item 4: Acute Change or Fluctuating Course"
    },
    {
      "code" : "reasonable-adjustment",
      "display" : "Reasonable Adjustment",
      "definition" : "Requirement for adjustment to care delivery (Equality Act)"
    },
    {
      "code" : "mca-assessment",
      "display" : "Mental Capacity Assessment",
      "definition" : "Assessment of capacity to make a specific decision"
    },
    {
      "code" : "capacity-present",
      "display" : "Capacity Present",
      "definition" : "Patient has capacity for this decision"
    },
    {
      "code" : "capacity-absent",
      "display" : "Capacity Absent",
      "definition" : "Patient lacks capacity for this decision"
    },
    {
      "code" : "best-interest",
      "display" : "Best Interest Decision",
      "definition" : "Decision made in patient's best interest"
    },
    {
      "code" : "bristol-score",
      "display" : "Bristol Stool Score",
      "definition" : "Bristol Stool Form Scale Score (1-7)"
    },
    {
      "code" : "bristol-1",
      "display" : "Type 1",
      "definition" : "Separate hard lumps, like nuts (hard to pass)"
    },
    {
      "code" : "bristol-2",
      "display" : "Type 2",
      "definition" : "Sausage-shaped but lumpy"
    },
    {
      "code" : "bristol-3",
      "display" : "Type 3",
      "definition" : "Like a sausage but with cracks on its surface"
    },
    {
      "code" : "bristol-4",
      "display" : "Type 4",
      "definition" : "Like a sausage or snake, smooth and soft"
    },
    {
      "code" : "bristol-5",
      "display" : "Type 5",
      "definition" : "Soft blobs with clear-cut edges (passed easily)"
    },
    {
      "code" : "bristol-6",
      "display" : "Type 6",
      "definition" : "Fluffy pieces with ragged edges, a mushy stool"
    },
    {
      "code" : "bristol-7",
      "display" : "Type 7",
      "definition" : "Watery, no solid pieces. Entirely liquid"
    },
    {
      "code" : "abbey-score",
      "display" : "Abbey Pain Scale Score",
      "definition" : "Total Abbey Pain Scale Score (0-100+ but usually 0-18+)"
    },
    {
      "code" : "abbey-vocalization",
      "display" : "Vocalization",
      "definition" : "Whimpering, groaning, crying"
    },
    {
      "code" : "abbey-facial-expression",
      "display" : "Facial Expression",
      "definition" : "Looking tense, frowning, grimacing, looking frightened"
    },
    {
      "code" : "abbey-body-language",
      "display" : "Body Language",
      "definition" : "Fidgeting, rocking, guarding part of body, withdrawn"
    },
    {
      "code" : "abbey-behavioral-change",
      "display" : "Behavioral Change",
      "definition" : "Increased confusion, refusing to eat, alteration in usual pattern"
    },
    {
      "code" : "abbey-psychological-change",
      "display" : "Psychological Change",
      "definition" : "Temperature, pulse, blood pressure changes, perspiration, pallor"
    },
    {
      "code" : "abbey-physical-changes",
      "display" : "Physical Changes",
      "definition" : "Skin tears, pressure areas, arthritis, contractures, previous injuries"
    },
    {
      "code" : "fluid-input-total",
      "display" : "Total Fluid Input",
      "definition" : "Total fluid input over specified period (e.g. 24h)"
    },
    {
      "code" : "fluid-output-total",
      "display" : "Total Fluid Output",
      "definition" : "Total fluid output over specified period (e.g. 24h)"
    },
    {
      "code" : "fluid-balance",
      "display" : "Fluid Balance",
      "definition" : "Total Input minus Total Output"
    },
    {
      "code" : "urine-output",
      "display" : "Urine Output",
      "definition" : "Volume of urine passed"
    },
    {
      "code" : "abc-chart",
      "display" : "ABC Chart",
      "definition" : "Antecedent-Behaviour-Consequence Chart for PBS"
    },
    {
      "code" : "abc-antecedent",
      "display" : "Antecedent",
      "definition" : "What happened immediately before the behaviour (triggers)"
    },
    {
      "code" : "abc-behaviour",
      "display" : "Behaviour",
      "definition" : "Description of the behaviour itself (observable actions)"
    },
    {
      "code" : "abc-consequence",
      "display" : "Consequence",
      "definition" : "What happened immediately after (response/outcome)"
    },
    {
      "code" : "abc-function",
      "display" : "Function of Behaviour",
      "definition" : "Hypothesized function (e.g. Sensory, Escape, Attention, Tangible)"
    },
    {
      "code" : "abc-duration",
      "display" : "Duration",
      "definition" : "Duration of the episode"
    },
    {
      "code" : "abc-intensity",
      "display" : "Intensity",
      "definition" : "Intensity of the behaviour (1-10)"
    },
    {
      "code" : "oral-health-score",
      "display" : "Oral Health Score",
      "definition" : "Total Oral Health Assessment Score"
    },
    {
      "code" : "oral-lips",
      "display" : "Lips",
      "definition" : "Condition of lips (Pink/Moist vs Dry/Cracked)"
    },
    {
      "code" : "oral-tongue",
      "display" : "Tongue",
      "definition" : "Condition of tongue (Pink/Moist vs Coated/Red)"
    },
    {
      "code" : "oral-gums",
      "display" : "Gums",
      "definition" : "Condition of gums (Pink/Firm vs Bleeding/Receding)"
    },
    {
      "code" : "oral-teeth",
      "display" : "Teeth/Dentures",
      "definition" : "Condition of teeth or dentures (Clean/Intact vs Decayed/Broken/Loose)"
    },
    {
      "code" : "oral-saliva",
      "display" : "Saliva",
      "definition" : "Saliva quality (Moist/Watery vs Thick/Sticky/Absent)"
    },
    {
      "code" : "seizure-record",
      "display" : "Seizure Record",
      "definition" : "Record of a seizure event"
    },
    {
      "code" : "seizure-type",
      "display" : "Seizure Type",
      "definition" : "Type of seizure (Tonic-Clonic, Absence, Focal, etc)"
    },
    {
      "code" : "seizure-duration",
      "display" : "Seizure Duration",
      "definition" : "Duration of the active seizure phase"
    },
    {
      "code" : "seizure-recovery",
      "display" : "Recovery Phase",
      "definition" : "Duration/Description of post-ictal recovery"
    },
    {
      "code" : "seizure-trigger",
      "display" : "Trigger",
      "definition" : "Suspected trigger for the seizure"
    },
    {
      "code" : "sleep-record",
      "display" : "Sleep Record",
      "definition" : "Record of a sleep period"
    },
    {
      "code" : "sleep-quality",
      "display" : "Sleep Quality",
      "definition" : "Subjective or observed quality of sleep"
    },
    {
      "code" : "sleep-hours",
      "display" : "Hours Slept",
      "definition" : "Total hours of sleep achieved"
    },
    {
      "code" : "sleep-disturbances",
      "display" : "Disturbances",
      "definition" : "Number or description of distinct awakenings"
    },
    {
      "code" : "urinalysis-panel",
      "display" : "Urinalysis Panel",
      "definition" : "Urine Dipstick Test Panel"
    },
    {
      "code" : "ua-leukocytes",
      "display" : "Leukocytes",
      "definition" : "Leukocytes (WBCs) in urine"
    },
    {
      "code" : "ua-nitrites",
      "display" : "Nitrites",
      "definition" : "Nitrites in urine"
    },
    {
      "code" : "ua-protein",
      "display" : "Protein",
      "definition" : "Protein in urine"
    },
    {
      "code" : "ua-blood",
      "display" : "Blood",
      "definition" : "Blood (Hemoglobin) in urine"
    },
    {
      "code" : "ua-glucose",
      "display" : "Glucose",
      "definition" : "Glucose in urine"
    },
    {
      "code" : "ua-ketones",
      "display" : "Ketones",
      "definition" : "Ketones in urine"
    },
    {
      "code" : "ua-ph",
      "display" : "pH",
      "definition" : "Urine pH Level"
    },
    {
      "code" : "ua-sg",
      "display" : "Specific Gravity",
      "definition" : "Urine Specific Gravity"
    },
    {
      "code" : "mca-present",
      "display" : "Capacity Present",
      "definition" : "Patient has capacity for this decision"
    },
    {
      "code" : "4at-change-no",
      "display" : "No Acute Change",
      "definition" : "No indication of acute change or fluctuating course"
    },
    {
      "code" : "4at-amt4-1error",
      "display" : "1 Error",
      "definition" : "1 error in AMT4 test"
    },
    {
      "code" : "4at-attention-gt7",
      "display" : "Months Backwards < 7 months",
      "definition" : "Less than 7 months correctly recited backwards"
    },
    {
      "code" : "4at-alert-normal",
      "display" : "Normal Alertness",
      "definition" : "Patient is fully alert"
    },
    {
      "code" : "continence-assessment",
      "display" : "Continence Assessment",
      "definition" : "Assessment of bladder and bowel control"
    },
    {
      "code" : "bladder-assessment",
      "display" : "Bladder Assessment",
      "definition" : "Detailed assessment of bladder function"
    },
    {
      "code" : "bowel-assessment",
      "display" : "Bowel Assessment",
      "definition" : "Detailed assessment of bowel function"
    },
    {
      "code" : "catheter-care",
      "display" : "Catheter Care Interaction",
      "definition" : "Nursing interaction related to catheter care"
    },
    {
      "code" : "oral-intake",
      "display" : "Oral Intake Assessment",
      "definition" : "Assessment of food and fluid intake capability"
    },
    {
      "code" : "swallowing",
      "display" : "Swallowing Assessment",
      "definition" : "Assessment of swallowing ability (dysphagia risk)"
    },
    {
      "code" : "dietary-requirements",
      "display" : "Dietary Requirements",
      "definition" : "Specific dietary needs or restrictions"
    },
    {
      "code" : "mobility",
      "display" : "Mobility Assessment",
      "definition" : "Assessment of physical mobility and transfer ability"
    },
    {
      "code" : "device-use",
      "display" : "Device/Aid Usage",
      "definition" : "Observation of device or mobility aid usage"
    },
    {
      "code" : "hygiene-needs",
      "display" : "Personal Hygiene Needs",
      "definition" : "Assessment of assistance required for hygiene"
    },
    {
      "code" : "oral-care",
      "display" : "Oral Care Needs",
      "definition" : "Assessment of oral health and care requirements"
    },
    {
      "code" : "medication-ability",
      "display" : "Medication Management Ability",
      "definition" : "Ability to manage own medications"
    },
    {
      "code" : "medication-self-admin",
      "display" : "Medication Self-Administration",
      "definition" : "Observation of self-administration technique"
    }
  ]
}

```
