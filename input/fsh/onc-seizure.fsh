// =============================================================================
// Seizure Record (Epilepsy)
// =============================================================================
Profile: ONCSeizureRecord
Parent: ONCNursingAssessment
Id: onc-seizure-record
Title: "Seizure Record"
Description: "Record of a specific seizure event, including type, duration, triggers, and recovery phases. Essential for epilepsy management and identifying patterns."
* ^url = "https://fhir.clinyq.ai/StructureDefinition/onc-seizure-record"
* ^version = "0.1.0"
* ^status = #draft
* category = http://terminology.hl7.org/CodeSystem/observation-category#exam
* code = ONCObservationCodes#seizure-record
* value[x] only string
* valueString 1..1 MS
* valueString ^short = "Description of the event"
* component 0..* MS
* component ^slicing.discriminator.type = #pattern
* component ^slicing.discriminator.path = "code"
* component ^slicing.ordered = false
* component ^slicing.rules = #open
* component contains 
    type 0..1 MS and 
    duration 0..1 MS and 
    recovery 0..1 MS and 
    trigger 0..1 MS

* component[type].code = ONCObservationCodes#seizure-type
* component[type].value[x] only string

* component[duration].code = ONCObservationCodes#seizure-duration
* component[duration].value[x] only Quantity
* component[duration].valueQuantity.unit = "min"
* component[duration].valueQuantity.system = "http://unitsofmeasure.org"
* component[duration].valueQuantity.code = #min

* component[recovery].code = ONCObservationCodes#seizure-recovery
* component[recovery].value[x] only string

* component[trigger].code = ONCObservationCodes#seizure-trigger
* component[trigger].value[x] only string
