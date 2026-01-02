Extension: UKCoreEthnicCategory
Id: UKCore-Extension-EthnicCategory
Title: "UK Core Ethnic Category"
Description: "An extension to record the ethnic category of a patient, as per UK Core standards."
Context: Patient
* ^url = "https://opennursingcoreig.com/StructureDefinition/UKCore-Extension-EthnicCategory"
* value[x] only CodeableConcept
* value[x] 1..1

Profile: ONCNHSPatient
Parent: Patient
Id: onc-nhs-patient
Title: "ONC NHS Patient"
Description: "A patient profile for use in NHS nursing contexts with ethnic category extension."
* extension contains UKCoreEthnicCategory named ethnicCategory 0..1 MS

Profile: ONCSkinToneObservation
Parent: ONCNursingAssessment
Id: onc-skintone-observation
Title: "Skin Tone Observation"
Description: "Observation of patient skin tone using the Fitzpatrick skin type classification. Supports equitable care by enabling skin tone-aware clinical decision making, particularly for conditions that present differently across skin tones (e.g., pressure ulcers, cyanosis)."
* code = http://loinc.org#66555-4 "Skin type [Fitzpatrick Classification Scale]"
* value[x] only CodeableConcept
* valueCodeableConcept from SkinToneVS (required)

CodeSystem: ONCMonkScale
Id: onc-monk-scale
Title: "Monk Skin Tone Scale CodeSystem"
* #A "Light Skin"
* #B "Light-Medium Skin"
* #C "Medium Skin"
* #D "Medium-Dark Skin"
* #E "Dark Skin"
* #F "Deep Dark Skin"
* #G "Very Dark Skin"
* #H "Deepest Dark Skin"
* #I "Ultra Dark Skin"
* #J "Black Skin"

CodeSystem: ONCObservationCodes
Id: onc-observation-codes
Title: "ONC Observation Codes"
Description: "Custom observation codes for Open Nursing Core"
* ^url = "https://opennursingcoreig.com/CodeSystem/onc-observation-codes"
* #mst-score "Monk Skin Tone Score" "Assessment of skin tone using the Monk Skin Tone Scale"
* #waterlow-score "Waterlow Score" "Total score for Waterlow pressure ulcer risk assessment"
* #must-score "MUST Score" "Malnutrition Universal Screening Tool total score"
* #must-bmi-score "MUST BMI Score" "Malnutrition Universal Screening Tool BMI score"
* #must-weight-loss-score "MUST Weight Loss Score" "Malnutrition Universal Screening Tool weight loss score"
* #must-acute-disease-score "MUST Acute Disease Score" "Malnutrition Universal Screening Tool acute disease effect score"
* #braden-total-score "Braden Total Score" "Braden scale total score"
* #braden-sensory "Braden Sensory Perception" "Sensory perception Braden scale"
* #braden-moisture "Braden Moisture" "Moisture Braden scale"
* #braden-activity "Braden Activity" "Activity Braden scale"
* #braden-mobility "Braden Mobility" "Mobility Braden scale"
* #braden-nutrition "Braden Nutrition" "Nutrition Braden scale"
* #braden-friction "Braden Friction/Shear" "Friction and shear Braden scale"
* #barthel-score "Barthel Index Score" "Total score for Barthel Index assessment"
* #news2-score "NEWS2 Score" "National Early Warning Score 2 Total Score"
* #news2-subscore "NEWS2 Sub-score" "Sub-score for NEWS2 parameter"
* #wound-stage "Wound Stage" "Stage of the wound"
* #stage-1 "Stage 1" "Stage 1 pressure ulcer"
* #stage-2 "Stage 2" "Stage 2 pressure ulcer"
* #stage-3 "Stage 3" "Stage 3 pressure ulcer"
* #stage-4 "Stage 4" "Stage 4 pressure ulcer"
* #unstageable "Unstageable" "Unstageable pressure ulcer"
* #deep-tissue "Deep Tissue Injury" "Deep tissue injury"
* #risk-falls "Risk of Falls" "Risk of falls diagnosis"
* #fitzpatrick-1 "Type I" "Pale white; always burns, never tans"
* #fitzpatrick-2 "Type II" "White; usually burns, tans with difficulty"
* #fitzpatrick-3 "Type III" "Cream white; sometimes mild burn, gradually tans"
* #fitzpatrick-4 "Type IV" "Moderate brown; rarely burns, tans with ease"
* #fitzpatrick-5 "Type V" "Dark brown; very rarely burns, tans very easily"
* #fitzpatrick-6 "Type VI" "Deeply pigmented dark brown to black; never burns, tans very easily"
* #what-matters "What Matters to Me" "Patient-identified priorities and non-clinical goals"
* #patient-story "Patient Story" "Narrative summary of patient background, preferences, and autobiography"
* #relational-engagement "Relational Engagement Score" "Assessment of the quality of nurse-patient engagement (1-5)"
* #cfs-score "Clinical Frailty Scale Score" "Total score for Rockwood Clinical Frailty Scale"
* #cfs-1 "Very Fit" "Robus, active, energetic and motivated"
* #cfs-2 "Well" "No active disease symptoms but less fit than category 1"
* #cfs-3 "Managing Well" "Medical problems are well controlled, but not regularly active"
* #cfs-4 "Vulnerable" "Not dependent for daily help, but symptoms limit activities"
* #cfs-5 "Mildly Frail" "Need help with high order IADLs (finances, transportation, heavy housework)"
* #cfs-6 "Moderately Frail" "Need help with all outside activities and some housekeeping"
* #cfs-7 "Severely Frail" "Completely dependent for personal care"
* #cfs-8 "Very Severely Frail" "Completely dependent, approaching end of life"
* #cfs-9 "Terminally Ill" "Approaching the end of life (life expectancy <6 months)"
* #4at-score "4AT Delirium Score" "Total score for 4AT assessment"
* #4at-alertness "Alertness" "4AT Item 1: Alertness"
* #4at-amt4 "AMT4 Score" "4AT Item 2: Abbreviated Mental Test 4"
* #4at-attention "Attention" "4AT Item 3: Attention (Months Backwards)"
* #4at-acute-change "Acute Change" "4AT Item 4: Acute Change or Fluctuating Course"
* #reasonable-adjustment "Reasonable Adjustment" "Requirement for adjustment to care delivery (Equality Act)"
* #mca-assessment "Mental Capacity Assessment" "Assessment of capacity to make a specific decision"
* #capacity-present "Capacity Present" "Patient has capacity for this decision"
* #capacity-absent "Capacity Absent" "Patient lacks capacity for this decision"
* #best-interest "Best Interest Decision" "Decision made in patient's best interest"
* #bristol-score "Bristol Stool Score" "Bristol Stool Form Scale Score (1-7)"
* #bristol-1 "Type 1" "Separate hard lumps, like nuts (hard to pass)"
* #bristol-2 "Type 2" "Sausage-shaped but lumpy"
* #bristol-3 "Type 3" "Like a sausage but with cracks on its surface"
* #bristol-4 "Type 4" "Like a sausage or snake, smooth and soft"
* #bristol-5 "Type 5" "Soft blobs with clear-cut edges (passed easily)"
* #bristol-6 "Type 6" "Fluffy pieces with ragged edges, a mushy stool"
* #bristol-7 "Type 7" "Watery, no solid pieces. Entirely liquid"
* #adpie-a "Assessment" "Assessment phase of the nursing process"
* #adpie-d "Diagnosis" "Diagnosis phase of the nursing process"
* #adpie-p "Planning" "Planning phase of the nursing process"
* #adpie-i "Implementation" "Implementation phase of the nursing process"
* #adpie-e "Evaluation" "Evaluation phase of the nursing process"
* #empathy-1 "Low Empathy" "Task-focused interaction with minimal person-centred engagement."
* #empathy-2 "Basic Empathy" "Professional interaction with patient identity acknowledged."
* #empathy-3 "Moderate Empathy" "Active relational engagement with shared decision making."
* #empathy-4 "High Empathy" "Authentic partnership with deep understanding of patient experience."
* #empathy-5 "Relational Excellence" "Flourishing partnership with total alignment on 'What Matters to Me'."

// =============================================================================
// Abbey Pain Scale Codes
// =============================================================================
* #abbey-score "Abbey Pain Scale Score" "Total Abbey Pain Scale Score (0-100+ but usually 0-18+)"
* #abbey-vocalization "Vocalization" "Whimpering, groaning, crying"
* #abbey-facial-expression "Facial Expression" "Looking tense, frowning, grimacing, looking frightened"
* #abbey-body-language "Body Language" "Fidgeting, rocking, guarding part of body, withdrawn"
* #abbey-behavioral-change "Behavioral Change" "Increased confusion, refusing to eat, alteration in usual pattern"
* #abbey-psychological-change "Psychological Change" "Temperature, pulse, blood pressure changes, perspiration, pallor"
* #abbey-physical-changes "Physical Changes" "Skin tears, pressure areas, arthritis, contractures, previous injuries"

// =============================================================================
// Fluid Balance Codes
// =============================================================================
* #fluid-input-total "Total Fluid Input" "Total fluid input over specified period (e.g. 24h)"
* #fluid-output-total "Total Fluid Output" "Total fluid output over specified period (e.g. 24h)"
* #fluid-balance "Fluid Balance" "Total Input minus Total Output"
* #urine-output "Urine Output" "Volume of urine passed"

// =============================================================================
// Positive Behaviour Support (PBS) Codes
// =============================================================================
* #abc-chart "ABC Chart" "Antecedent-Behaviour-Consequence Chart for PBS"
* #abc-antecedent "Antecedent" "What happened immediately before the behaviour (triggers)"
* #abc-behaviour "Behaviour" "Description of the behaviour itself (observable actions)"
* #abc-consequence "Consequence" "What happened immediately after (response/outcome)"
* #abc-function "Function of Behaviour" "Hypothesized function (e.g. Sensory, Escape, Attention, Tangible)"
* #abc-duration "Duration" "Duration of the episode"

* #abc-intensity "Intensity" "Intensity of the behaviour (1-10)"

// =============================================================================
// Oral Health Codes
// =============================================================================
* #oral-health-score "Oral Health Score" "Total Oral Health Assessment Score"
* #oral-lips "Lips" "Condition of lips (Pink/Moist vs Dry/Cracked)"
* #oral-tongue "Tongue" "Condition of tongue (Pink/Moist vs Coated/Red)"
* #oral-gums "Gums" "Condition of gums (Pink/Firm vs Bleeding/Receding)"
* #oral-teeth "Teeth/Dentures" "Condition of teeth or dentures (Clean/Intact vs Decayed/Broken/Loose)"
* #oral-saliva "Saliva" "Saliva quality (Moist/Watery vs Thick/Sticky/Absent)"

// =============================================================================
// Seizure Record Codes
// =============================================================================
* #seizure-record "Seizure Record" "Record of a seizure event"
* #seizure-type "Seizure Type" "Type of seizure (Tonic-Clonic, Absence, Focal, etc)"
* #seizure-duration "Seizure Duration" "Duration of the active seizure phase"
* #seizure-recovery "Recovery Phase" "Duration/Description of post-ictal recovery"
* #seizure-trigger "Trigger" "Suspected trigger for the seizure"

// =============================================================================
// Sleep Pattern Codes
// =============================================================================
* #sleep-record "Sleep Record" "Record of a sleep period"
* #sleep-quality "Sleep Quality" "Subjective or observed quality of sleep"
* #sleep-hours "Hours Slept" "Total hours of sleep achieved"
* #sleep-disturbances "Disturbances" "Number or description of distinct awakenings"

// =============================================================================
// Urinalysis (Dipstick) Codes
// =============================================================================
* #urinalysis-panel "Urinalysis Panel" "Urine Dipstick Test Panel"
* #ua-leukocytes "Leukocytes" "Leukocytes (WBCs) in urine"
* #ua-nitrites "Nitrites" "Nitrites in urine"
* #ua-protein "Protein" "Protein in urine"
* #ua-blood "Blood" "Blood (Hemoglobin) in urine"
* #ua-glucose "Glucose" "Glucose in urine"
* #ua-ketones "Ketones" "Ketones in urine"
* #ua-ph "pH" "Urine pH Level"
* #ua-sg "Specific Gravity" "Urine Specific Gravity"
* #mca-present "Capacity Present" "Patient has capacity for this decision"
* #4at-change-no "No Acute Change" "No indication of acute change or fluctuating course"
* #4at-amt4-1error "1 Error" "1 error in AMT4 test"
* #4at-attention-gt7 "Months Backwards < 7 months" "Less than 7 months correctly recited backwards"
* #4at-alert-normal "Normal Alertness" "Patient is fully alert"

// PRSB Alignment Codes
* #continence-assessment "Continence Assessment" "Assessment of bladder and bowel control"
* #bladder-assessment "Bladder Assessment" "Detailed assessment of bladder function"
* #bowel-assessment "Bowel Assessment" "Detailed assessment of bowel function"
* #catheter-care "Catheter Care Interaction" "Nursing interaction related to catheter care"
* #oral-intake "Oral Intake Assessment" "Assessment of food and fluid intake capability"
* #swallowing "Swallowing Assessment" "Assessment of swallowing ability (dysphagia risk)"
* #dietary-requirements "Dietary Requirements" "Specific dietary needs or restrictions"
* #mobility "Mobility Assessment" "Assessment of physical mobility and transfer ability"
* #device-use "Device/Aid Usage" "Observation of device or mobility aid usage"
* #hygiene-needs "Personal Hygiene Needs" "Assessment of assistance required for hygiene"
* #oral-care "Oral Care Needs" "Assessment of oral health and care requirements"
* #medication-ability "Medication Management Ability" "Ability to manage own medications"
* #medication-self-admin "Medication Self-Administration" "Observation of self-administration technique"


ValueSet: ONCMonkScaleVS
Id: onc-monk-scale-vs
Title: "Monk Skin Tone Scale ValueSet"
* include codes from system ONCMonkScale

Profile: ONCMonkSkinToneObservation
Parent: ONCNursingAssessment
Id: onc-monk-skintone-observation
Title: "Monk Skin Tone Observation"
Description: "Observation of patient skin tone using the Monk Skin Tone Scale (10-point scale A-J). Provides more granular skin tone assessment than Fitzpatrick scale, particularly for darker skin tones. Supports equitable care and accurate clinical assessment across diverse populations."
* code = https://opennursingcoreig.com/CodeSystem/onc-observation-codes#mst-score "Monk Skin Tone Score"
* value[x] only CodeableConcept
* valueCodeableConcept from ONCMonkScaleVS (required)

// =============================================================================
// Reasonable Adjustment Profile (Equality Act)
// =============================================================================
Profile: ONCReasonableAdjustment
Parent: ONCNursingAssessment
Id: onc-reasonable-adjustment
Title: "Reasonable Adjustment"
Description: "Captures specific strict requirements for care adjustments under the Equality Act (e.g., 'Needs BSL Interpreter', 'Cannot use stairs', 'Requires large print')."
* ^url = "https://opennursingcoreig.com/StructureDefinition/onc-reasonable-adjustment"
* code = ONCObservationCodes#reasonable-adjustment
* value[x] only string
* valueString 1..1 MS
* valueString ^short = "Description of required adjustment"
* note 0..1 MS

// =============================================================================
// Equity Extensions (The "Safety Marker")
// =============================================================================
Extension: ONCEquityMarker
Id: onc-equity-marker
Title: "ONC Equity Marker"
Description: "A technical extension applied to observations that have passed the Mandatory Equity Gate (i.e., they are skin-tone aware)."
* ^url = "https://opennursingcoreig.com/StructureDefinition/onc-equity-marker"
* value[x] only boolean
* valueBoolean 1..1

