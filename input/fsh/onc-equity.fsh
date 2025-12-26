Extension: UKCoreEthnicCategory
Id: UKCore-Extension-EthnicCategory
Title: "UK Core Ethnic Category"
Description: "An extension to record the ethnic category of a patient, as per UK Core standards."
Context: Patient
* ^url = "https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/UKCore-Extension-EthnicCategory"
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
* ^url = "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes"
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

ValueSet: ONCMonkScaleVS
Id: onc-monk-scale-vs
Title: "Monk Skin Tone Scale ValueSet"
* include codes from system ONCMonkScale

Profile: ONCMonkSkinToneObservation
Parent: ONCNursingAssessment
Id: onc-monk-skintone-observation
Title: "Monk Skin Tone Observation"
Description: "Observation of patient skin tone using the Monk Skin Tone Scale (10-point scale A-J). Provides more granular skin tone assessment than Fitzpatrick scale, particularly for darker skin tones. Supports equitable care and accurate clinical assessment across diverse populations."
* code = https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes#mst-score "Monk Skin Tone Score"
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
* ^url = "https://fhir.clinyq.ai/StructureDefinition/onc-reasonable-adjustment"
* ^version = "0.1.0"
* ^status = #draft
* category = http://terminology.hl7.org/CodeSystem/observation-category#exam
* code = ONCObservationCodes#reasonable-adjustment
* value[x] only string
* valueString 1..1 MS
* valueString ^short = "Description of required adjustment"
* note 0..1 MS
