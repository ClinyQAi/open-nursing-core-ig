// =============================================================================
// Oral Health Assessment
// =============================================================================
Profile: ONCOralHealth
Parent: ONCNursingAssessment
Id: onc-oral-health
Title: "Oral Health Assessment"
Description: "Assessment of oral cavity health. Critical for prevention of pneumonia in frail elderly and maintaining nutrition/hydration."
* ^url = "https://fhir.clinyq.ai/StructureDefinition/onc-oral-health"
* ^version = "0.1.0"
* ^status = #draft
* category = http://terminology.hl7.org/CodeSystem/observation-category#exam
* code = ONCObservationCodes#oral-health-score
* value[x] only integer or string
* valueInteger 1..1 MS
* valueInteger ^short = "Total Score (if using a scored tool like OHAT)"
* component 0..* MS
* component ^slicing.discriminator.type = #pattern
* component ^slicing.discriminator.path = "code"
* component ^slicing.ordered = false
* component ^slicing.rules = #open
* component contains 
    lips 0..1 MS and 
    tongue 0..1 MS and 
    gums 0..1 MS and 
    teeth 0..1 MS and 
    saliva 0..1 MS

* component[lips].code = ONCObservationCodes#oral-lips
* component[lips].value[x] only string

* component[tongue].code = ONCObservationCodes#oral-tongue
* component[tongue].value[x] only string

* component[gums].code = ONCObservationCodes#oral-gums
* component[gums].value[x] only string

* component[teeth].code = ONCObservationCodes#oral-teeth
* component[teeth].value[x] only string

* component[saliva].code = ONCObservationCodes#oral-saliva
* component[saliva].value[x] only string
