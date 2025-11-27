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
