// =============================================================================
// Urinalysis (Dipstick)
// =============================================================================
Profile: ONCUrinalysis
Parent: ONCNursingAssessment
Id: onc-urinalysis
Title: "Urinalysis"
Description: "Point-of-care urine dipstick test results. Used to screen for urinary tract infection (UTI), diabetes (glucose/ketones), and kidney health."
* ^url = "https://fhir.clinyq.ai/StructureDefinition/onc-urinalysis"
* ^version = "0.1.0"
* ^status = #draft
* category = http://terminology.hl7.org/CodeSystem/observation-category#exam
* code = ONCObservationCodes#urinalysis-panel
* value[x] only string
* valueString 1..1 MS
* valueString ^short = "Overall Interpretation (e.g. 'suggestive of UTI')"
* component 0..* MS
* component ^slicing.discriminator.type = #pattern
* component ^slicing.discriminator.path = "code"
* component ^slicing.ordered = false
* component ^slicing.rules = #open
* component contains 
    leukocytes 0..1 MS and 
    nitrites 0..1 MS and 
    blood 0..1 MS and 
    protein 0..1 MS and 
    glucose 0..1 MS and 
    ketones 0..1 MS and 
    ph 0..1 MS and 
    sg 0..1 MS

* component[leukocytes].code = ONCObservationCodes#ua-leukocytes
* component[leukocytes].value[x] only string
* component[leukocytes].valueString ^short = "e.g., 'Trace', '+', '++'"

* component[nitrites].code = ONCObservationCodes#ua-nitrites
* component[nitrites].value[x] only string
* component[nitrites].valueString ^short = "Positive/Negative"

* component[blood].code = ONCObservationCodes#ua-blood
* component[blood].value[x] only string
* component[blood].valueString ^short = "e.g., 'Non-hemolyzed', 'Large'"

* component[protein].code = ONCObservationCodes#ua-protein
* component[protein].value[x] only string

* component[glucose].code = ONCObservationCodes#ua-glucose
* component[glucose].value[x] only string

* component[ketones].code = ONCObservationCodes#ua-ketones
* component[ketones].value[x] only string

* component[ph].code = ONCObservationCodes#ua-ph
* component[ph].value[x] only Quantity

* component[sg].code = ONCObservationCodes#ua-sg
* component[sg].value[x] only Quantity
