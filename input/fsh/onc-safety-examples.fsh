// =============================================================================
// Example: ONC Morse Fall Scale Assessment
// =============================================================================
Instance: example-morse-fall-scale
InstanceOf: ONCMorseFallScale
Usage: #example
* status = #final
* subject = Reference(patient-example)
* performer = Reference(practitioner-example)
* category[nursing].coding = http://terminology.hl7.org/CodeSystem/observation-category#nursing
* code = http://loinc.org#59460-6 "Morse Fall Scale total score"
* valueQuantity = 70 '{score}'

* component[historyOfFalling]
  * code = http://loinc.org#59461-4
  * valueQuantity = 25 '{score}' // Yes

* component[secondaryDiagnosis]
  * code = http://loinc.org#59462-2
  * valueQuantity = 15 '{score}' // Yes

* component[ambulatoryAid]
  * code = http://loinc.org#59463-0
  * valueQuantity = 0 '{score}' // None

* component[intravenousTherapy]
  * code = http://loinc.org#59464-8
  * valueQuantity = 20 '{score}' // Yes

* component[gait]
  * code = http://loinc.org#59465-5
  * valueQuantity = 10 '{score}' // Weak

* component[mentalStatus]
  * code = http://loinc.org#59466-3
  * valueQuantity = 0 '{score}' // Oriented

// =============================================================================
// Example: ONC Housing Status Assessment
// =============================================================================
Instance: example-housing-status
InstanceOf: ONCHousingStatus
Usage: #example
* status = #final
* subject = Reference(patient-example)
* performer = Reference(practitioner-example)
* category[nursing].coding = http://terminology.hl7.org/CodeSystem/observation-category#nursing
* code = http://loinc.org#71802-3 "Housing status"
* valueCodeableConcept = http://snomed.info/sct#32911000 "Homeless"

// =============================================================================
// Example: ONC NEWS2 Assessment
// =============================================================================
Instance: example-news2-assessment
InstanceOf: ONCNEWS2Assessment
Usage: #example
* status = #final
* subject = Reference(patient-example)
* performer = Reference(practitioner-example)
* category[nursing].coding = http://terminology.hl7.org/CodeSystem/observation-category#nursing
* code = http://loinc.org#86585-7 "NEWS2 total score"
* valueQuantity = 5 '{score}'

* component[respRate]
  * code = http://loinc.org#9279-1
  * valueQuantity = 22 '/min'

* component[spo2]
  * code = http://loinc.org#2708-6
  * valueQuantity = 95 '%'

* component[temp]
  * code = http://loinc.org#8310-5
  * valueQuantity = 38.5 'Cel'

* component[systolicBP]
  * code = http://loinc.org#8480-6
  * valueQuantity = 100 'mm[Hg]'

* component[heartRate]
  * code = http://loinc.org#8867-4
  * valueQuantity = 100 '/min'

* component[acvpu]
  * code = http://loinc.org#11454-5
  * valueCodeableConcept = http://snomed.info/sct#248234008 "Mentally alert"

* component[suppOxygen]
  * code = http://loinc.org#72274-4
  * valueCodeableConcept = http://snomed.info/sct#373066001 "Yes"
