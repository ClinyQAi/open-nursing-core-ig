// =============================================================================
// Sleep Pattern Assessment
// =============================================================================
Profile: ONCSleepPattern
Parent: ONCNursingAssessment
Id: onc-sleep-pattern
Title: "Sleep Pattern"
Description: "Observation of sleep quality, duration, and disturbances. Sleep pattern disturbance is a key indicator for delirium and general wellbeing."
* ^url = "https://fhir.clinyq.ai/StructureDefinition/onc-sleep-pattern"
* ^version = "0.1.0"
* ^status = #draft
* category = http://terminology.hl7.org/CodeSystem/observation-category#exam
* code = ONCObservationCodes#sleep-record
* value[x] only string
* valueString 1..1 MS
* valueString ^short = "Overall summary of sleep period"
* component 0..* MS
* component ^slicing.discriminator.type = #pattern
* component ^slicing.discriminator.path = "code"
* component ^slicing.ordered = false
* component ^slicing.rules = #open
* component contains 
    quality 0..1 MS and 
    hours 0..1 MS and 
    disturbances 0..1 MS

* component[quality].code = ONCObservationCodes#sleep-quality
* component[quality].value[x] only string
* component[quality].valueString ^short = "e.g., 'Restful', 'Fitful', 'Broken'"

* component[hours].code = ONCObservationCodes#sleep-hours
* component[hours].value[x] only Quantity
* component[hours].valueQuantity.unit = "h"
* component[hours].valueQuantity.system = "http://unitsofmeasure.org"
* component[hours].valueQuantity.code = #h

* component[disturbances].code = ONCObservationCodes#sleep-disturbances
* component[disturbances].value[x] only string
