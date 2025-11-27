// 1. BASE ASSESSMENT
Profile: ONCNursingAssessment
Parent: Observation
Id: onc-nursing-assessment
Title: "Open Nursing Core Assessment"
Description: "A foundational profile for nursing observation."
* category ^slicing.discriminator.type = #pattern
* category ^slicing.discriminator.path = "coding.code"
* category ^slicing.rules = #open
* category contains nursing 1..1 MS
* category[nursing].coding.system = "http://terminology.hl7.org/CodeSystem/observation-category"
* category[nursing].coding.code = #nursing
* performer 1..1 MS

// 2. SKIN INTEGRITY (Braden Scale)
Profile: ONCBradenScaleAssessment
Parent: ONCNursingAssessment
Id: onc-braden-scale-assessment
Title: "Braden Scale Assessment"
Description: "Pressure Injury Risk Assessment."
* code = http://loinc.org#9017-7 "Braden Scale total score"
* code MS
* valueQuantity 1..1 MS
* valueQuantity.value 1..1 MS
* valueQuantity.unit = "{score}"
* valueQuantity.system = "http://unitsofmeasure.org"
* valueQuantity.code = #{score}
* component 6..6 MS
* component ^slicing.discriminator.type = #pattern
* component ^slicing.discriminator.path = "code"
* component ^slicing.rules = #open
* component contains
    sensoryPerception 1..1 MS and
    moisture 1..1 MS and
    activity 1..1 MS and
    mobility 1..1 MS and
    nutrition 1..1 MS and
    frictionAndShear 1..1 MS
* component[sensoryPerception].code = http://loinc.org#74012-8
* component[moisture].code = http://loinc.org#74013-6
* component[activity].code = http://loinc.org#74014-4
* component[mobility].code = http://loinc.org#74015-1
* component[nutrition].code = http://loinc.org#74016-9
* component[frictionAndShear].code = http://loinc.org#74017-7

// 3. FALLS (Morse Scale)
Profile: ONCMorseFallScale
Parent: ONCNursingAssessment
Id: onc-morse-fall-scale
Title: "Morse Fall Scale"
Description: "Fall Risk Assessment."
* code = http://loinc.org#59460-6 "Fall risk assessment.Morse Scale"
* code MS
* valueQuantity 1..1 MS
* valueQuantity.value 1..1 MS
* valueQuantity.unit = "{score}"
* valueQuantity.system = "http://unitsofmeasure.org"
* valueQuantity.code = #{score}

// 4. SAFETY (NEWS2)
Profile: ONCNEWS2Assessment
Parent: ONCNursingAssessment
Id: onc-news2-assessment
Title: "NEWS2 Assessment"
Description: "National Early Warning Score 2 for deterioration."
* code = http://loinc.org#86585-7 "NEWS2 score"
* code MS
* valueQuantity 1..1 MS
* valueQuantity.value 1..1 MS
* valueQuantity.unit = "{score}"
* valueQuantity.system = "http://unitsofmeasure.org"
* valueQuantity.code = #{score}

// 5. EQUITY (Skin Tone - Monk)
Profile: ONCSkinToneObservation
Parent: ONCNursingAssessment
Id: onc-skintone-observation
Title: "Skin Tone Assessment (Monk/Fitzpatrick)"
Description: "Assessment of skin tone to ensure equitable wound care."
* code = http://loinc.org#66472-2 "Skin type"
* code MS
* valueCodeableConcept from SkinToneVS (required)

// 6. SDOH (Housing)
Profile: ONCHousingStatus
Parent: ONCNursingAssessment
Id: onc-housing-status
Title: "Housing Status"
Description: "Social Determinants of Health: Housing."
* code = http://loinc.org#71802-3 "Housing status"
* code MS
* valueCodeableConcept from HousingStatusVS (required)

// 7. NHS PATIENT (Ethnicity)
Extension: UKCoreEthnicCategory
Id: UKCore-Extension-EthnicCategory
Title: "UK Core Ethnic Category"
Description: "Local definition of UK Core Ethnicity extension."
* ^url = "https://fhir.hl7.org.uk/StructureDefinition/UKCore-Extension-EthnicCategory"
* value[x] only CodeableConcept

Profile: ONCNHSPatient
Parent: Patient
Id: onc-nhs-patient
Title: "ONC NHS Patient"
* extension contains UKCoreEthnicCategory named ethnicCategory 1..1 MS
