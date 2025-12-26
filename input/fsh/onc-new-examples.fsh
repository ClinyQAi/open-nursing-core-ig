// ==============================================================================
// 5. RELATIONAL CARE (Phase 8)
// ==============================================================================
Instance: example-what-matters
InstanceOf: ONCWhatMattersToMe
Usage: #example
* status = #final
* subject = Reference(patient-example-jane)
* performer = Reference(practitioner-example)
* category[nursing].coding = http://terminology.hl7.org/CodeSystem/observation-category#social-history
* valueString = "Being able to walk her dog (Buster) daily."
* note.text = "This is her primary motivation for physiotherapy."

Instance: example-patient-story
InstanceOf: ONCPatientStory
Usage: #example
* status = #final
* subject = Reference(patient-example-jane)
* performer = Reference(practitioner-example)
* category[nursing].coding = http://terminology.hl7.org/CodeSystem/observation-category#social-history
* valueString = "Jane was a librarian for 40 years. She loves classical music and gardening. She lost her husband 2 years ago."

// ==============================================================================
// 6. FRAILTY & DELIRIUM (Phase 9)
// ==============================================================================
Instance: example-clinical-frailty
InstanceOf: ONCClinicalFrailtyScale
Usage: #example
* status = #final
* subject = Reference(patient-example-jane)
* performer = Reference(practitioner-example)
* category[nursing].coding = http://terminology.hl7.org/CodeSystem/observation-category#exam
* valueInteger = 5
* note.text = "Mildly Frail - slowing up, needs help with high order IADLs"

Instance: example-4at-delirium
InstanceOf: ONC4ATDelirium
Usage: #example
* status = #final
* subject = Reference(patient-example-jane)
* performer = Reference(practitioner-example)
* category[nursing].coding = http://terminology.hl7.org/CodeSystem/observation-category#exam
* valueQuantity.value = 5
* valueQuantity.unit = "{score}"
* component[alertness].valueCodeableConcept = https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes#4at-alert-normal "Normal"
* component[amt4].valueCodeableConcept = https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes#4at-amt4-1error "1 Error"
* component[attention].valueCodeableConcept = https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes#4at-attention-gt7 "Months backwards < 7 months correct"
* component[acuteChange].valueCodeableConcept = https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes#4at-change-no "No"

// ==============================================================================
// 7. EQUALITY & MENTAL CAPACITY (Phase 11)
// ==============================================================================
Instance: example-reasonable-adjustment
InstanceOf: ONCReasonableAdjustment
Usage: #example
* status = #final
* subject = Reference(patient-example-jane)
* category[nursing].coding = http://terminology.hl7.org/CodeSystem/observation-category#exam
* valueString = "Requires large print documents (Font size 16+)."

Instance: example-mental-capacity
InstanceOf: ONCMentalCapacity
Usage: #example
* status = #final
* subject = Reference(patient-example-jane)
* category[nursing].coding = http://terminology.hl7.org/CodeSystem/observation-category#exam
* valueCodeableConcept = https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes#mca-present "Capacity Present"
* note.text = "Assessment for decision to return home."

// ==============================================================================
// 8. FUNDAMENTAL CARE (Phases 12-14)
// ==============================================================================
Instance: example-bristol-stool
InstanceOf: ONCBristolStoolChart
Usage: #example
* status = #final
* subject = Reference(patient-example-jane)
* category[nursing].coding = http://terminology.hl7.org/CodeSystem/observation-category#exam
* valueQuantity.value = 4
* valueQuantity.unit = "{score}"

Instance: example-abbey-pain
InstanceOf: ONCAbbeyPainScale
Usage: #example
* status = #final
* subject = Reference(patient-example-jane)
* category[nursing].coding = http://terminology.hl7.org/CodeSystem/observation-category#exam
* valueQuantity.value = 2
* valueQuantity.unit = "{score}"
* component[vocalization].valueInteger = 0
* component[facialExpression].valueInteger = 1
* component[bodyLanguage].valueInteger = 0
* component[behavioralChange].valueInteger = 1
* component[physiologicalChange].valueInteger = 0
* component[physicalChanges].valueInteger = 0

Instance: example-fluid-balance
InstanceOf: ONCFluidBalance
Usage: #example
* status = #final
* subject = Reference(patient-example-jane)
* category[nursing].coding = http://terminology.hl7.org/CodeSystem/observation-category#exam
* valueString = "Positive Balance +500ml"
* component[input].valueQuantity.value = 2000
* component[input].valueQuantity.unit = "ml"
* component[output].valueQuantity.value = 1500
* component[output].valueQuantity.unit = "ml"

// ==============================================================================
// 9. SPECIALIZED CARE (Phases 15-19)
// ==============================================================================
Instance: example-abc-chart
InstanceOf: ONCABCChart
Usage: #example
* status = #final
* subject = Reference(patient-example-jane)
* category[nursing].coding = http://terminology.hl7.org/CodeSystem/observation-category#exam
* valueString = "Aggressive episode managed with de-escalation."
* component[antecedent].valueString = "Denied access to garden due to rain."
* component[behaviour].valueString = "Shouting and hitting door."
* component[consequence].valueString = "Verbal de-escalation, distraction with music."
* component[function].valueString = "Frustration/Tangible"

Instance: example-oral-health
InstanceOf: ONCOralHealth
Usage: #example
* status = #final
* subject = Reference(patient-example-jane)
* category[nursing].coding = http://terminology.hl7.org/CodeSystem/observation-category#exam
* valueInteger = 0
* component[lips].valueString = "Pink, moist"
* component[tongue].valueString = "Pink, moist"
* component[gums].valueString = "Healthy"
* component[teeth].valueString = "Own teeth, good repair"

Instance: example-seizure-record
InstanceOf: ONCSeizureRecord
Usage: #example
* status = #final
* subject = Reference(patient-example-jane)
* category[nursing].coding = http://terminology.hl7.org/CodeSystem/observation-category#exam
* valueString = "Tonic-clonic seizure lasting 2 mins"
* component[type].valueString = "Tonic-Clonic"
* component[duration].valueQuantity.value = 2
* component[duration].valueQuantity.unit = "min"
* component[recovery].valueString = "Sleepy for 30 mins post-ictal"

Instance: example-urinalysis
InstanceOf: ONCUrinalysis
Usage: #example
* status = #final
* subject = Reference(patient-example-jane)
* category[nursing].coding = http://terminology.hl7.org/CodeSystem/observation-category#exam
* valueString = "Suggestive of UTI"
* component[leukocytes].valueString = "++"
* component[nitrites].valueString = "Positive"
* component[blood].valueString = "Negative"
* component[ph].valueQuantity.value = 6
* component[ph].valueQuantity.unit = "{pH}"
