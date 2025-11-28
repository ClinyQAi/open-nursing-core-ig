ValueSet: ACVPUVS
Id: acvpu-vs
Title: "ACVPU Value Set"
Description: "Codes representing the ACVPU (Alert, Confusion, Voice, Pain, Unresponsive) scale."
* ^experimental = false
* http://snomed.info/sct#248234008 "Mentally alert"
* http://snomed.info/sct#130987000 "Acute confusion"
* http://snomed.info/sct#300202002 "Responds to voice"
* http://snomed.info/sct#450847001 "Responds to pain"
* http://snomed.info/sct#422768004 "Unresponsive"

Profile: ONCMorseFallScale
Parent: ONCNursingAssessment
Id: onc-morse-fall-scale
Title: "ONC Morse Fall Scale Assessment"
Description: "Assessment of fall risk using the Morse Fall Scale."
* code = http://loinc.org#59460-6 "Morse Fall Scale total score"
* code MS
* value[x] only Quantity
* valueQuantity.unit = "{score}"
* valueQuantity.system = "http://unitsofmeasure.org"
* valueQuantity.code = #{score}
* component 6..* MS
* component ^slicing.discriminator.type = #pattern
* component ^slicing.discriminator.path = "code"
* component ^slicing.rules = #open
* component contains
    historyOfFalling 1..1 MS and
    secondaryDiagnosis 1..1 MS and
    ambulatoryAid 1..1 MS and
    intravenousTherapy 1..1 MS and
    gait 1..1 MS and
    mentalStatus 1..1 MS
* component[historyOfFalling].code = http://loinc.org#59461-4
* component[historyOfFalling].value[x] only Quantity
* component[historyOfFalling].valueQuantity.unit = "{score}"
* component[historyOfFalling].valueQuantity.code = #{score}
* component[secondaryDiagnosis].code = http://loinc.org#59462-2
* component[secondaryDiagnosis].value[x] only Quantity
* component[secondaryDiagnosis].valueQuantity.unit = "{score}"
* component[secondaryDiagnosis].valueQuantity.code = #{score}
* component[ambulatoryAid].code = http://loinc.org#59463-0
* component[ambulatoryAid].value[x] only Quantity
* component[ambulatoryAid].valueQuantity.unit = "{score}"
* component[ambulatoryAid].valueQuantity.code = #{score}
* component[intravenousTherapy].code = http://loinc.org#59464-8
* component[intravenousTherapy].value[x] only Quantity
* component[intravenousTherapy].valueQuantity.unit = "{score}"
* component[intravenousTherapy].valueQuantity.code = #{score}
* component[gait].code = http://loinc.org#59465-5
* component[gait].value[x] only Quantity
* component[gait].valueQuantity.unit = "{score}"
* component[gait].valueQuantity.code = #{score}
* component[mentalStatus].code = http://loinc.org#59466-3
* component[mentalStatus].value[x] only Quantity
* component[mentalStatus].valueQuantity.unit = "{score}"
* component[mentalStatus].valueQuantity.code = #{score}

Profile: ONCHousingStatus
Parent: ONCNursingAssessment
Id: onc-housing-status
Title: "ONC Housing Status Assessment"
Description: "Assessment of the patient's housing status."
* code = http://loinc.org#71802-3 "Housing status"
* code MS
* value[x] only CodeableConcept
* valueCodeableConcept from HousingStatusVS (required)

Profile: ONCNEWS2Assessment
Parent: ONCNursingAssessment
Id: onc-news2-assessment
Title: "ONC NEWS2 Assessment"
Description: "National Early Warning Score 2 (NEWS2) assessment."
* code = http://loinc.org#86585-7 "NEWS2 total score"
* code MS
* value[x] only Quantity
* valueQuantity 1..1
* valueQuantity.unit = "{score}"
* valueQuantity.system = "http://unitsofmeasure.org"
* valueQuantity.code = #{score}
* component 7..* MS
* component ^slicing.discriminator.type = #pattern
* component ^slicing.discriminator.path = "code"
* component ^slicing.rules = #open
* component contains
    respRate 1..1 MS and
    spo2 1..1 MS and
    temp 1..1 MS and
    systolicBP 1..1 MS and
    heartRate 1..1 MS and
    acvpu 1..1 MS and
    suppOxygen 1..1 MS
* component[respRate].code = http://loinc.org#9279-1
* component[respRate].value[x] only Quantity
* component[spo2].code = http://loinc.org#2708-6
* component[spo2].value[x] only Quantity
* component[temp].code = http://loinc.org#8310-5
* component[temp].value[x] only Quantity
* component[systolicBP].code = http://loinc.org#8480-6
* component[systolicBP].value[x] only Quantity
* component[heartRate].code = http://loinc.org#8867-4
* component[heartRate].value[x] only Quantity
* component[acvpu].code = http://loinc.org#11454-5
* component[acvpu].value[x] only CodeableConcept
* component[acvpu].valueCodeableConcept from ACVPUVS (required)
* component[suppOxygen].code = http://loinc.org#72274-4
* component[suppOxygen].value[x] only CodeableConcept
