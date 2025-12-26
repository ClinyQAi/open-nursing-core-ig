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
