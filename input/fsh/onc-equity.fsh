Extension: UKCoreEthnicCategory
Id: UKCore-Extension-EthnicCategory
Title: "UK Core Ethnic Category"
* ^url = "https://fhir.hl7.org.uk/StructureDefinition/UKCore-Extension-EthnicCategory"
* value[x] only CodeableConcept

Profile: ONCNHSPatient
Parent: Patient
Id: onc-nhs-patient
Title: "ONC NHS Patient"
* extension contains UKCoreEthnicCategory named ethnicCategory 1..1 MS

Profile: ONCSkinToneObservation
Parent: ONCNursingAssessment
Id: onc-skintone-observation
Title: "Skin Tone Observation"
* code = http://loinc.org#66472-2 "Fitzpatrick skin type"
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
* ^url = "http://open-nursing-core.org/CodeSystem/onc-observation-codes"
* #mst-score "Monk Skin Tone Score" "Assessment of skin tone using the Monk Skin Tone Scale"

ValueSet: ONCMonkScaleVS
Id: onc-monk-scale-vs
Title: "Monk Skin Tone Scale ValueSet"
* include codes from system ONCMonkScale

Profile: ONCMonkSkinToneObservation
Parent: ONCNursingAssessment
Id: onc-monk-skintone-observation
Title: "Monk Skin Tone Observation"
* code = http://open-nursing-core.org/CodeSystem/onc-observation-codes#mst-score "Monk Skin Tone Score"
* value[x] only CodeableConcept
* valueCodeableConcept from ONCMonkScaleVS (required)
