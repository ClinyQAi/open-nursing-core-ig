// =============================================================================
// Hydration & Fluid Balance Profile
// =============================================================================
Profile: ONCFluidBalance
Parent: ONCNursingAssessment
Id: onc-fluid-balance
Title: "Fluid Balance"
Description: "Assessment of fluid intake, output, and balance. Critical for renal function, hydration status, and heart failure monitoring."
* ^url = "https://fhir.clinyq.ai/StructureDefinition/onc-fluid-balance"
* ^version = "0.1.0"
* ^status = #draft
* category = http://terminology.hl7.org/CodeSystem/observation-category#exam
* code = ONCObservationCodes#fluid-balance
* value[x] only Quantity
* valueQuantity 1..1 MS
* valueQuantity.unit = "mL"
* valueQuantity.system = "http://unitsofmeasure.org"
* valueQuantity.code = #mL
* valueQuantity ^short = "Net Fluid Balance (Input - Output)"
* component 0..* MS
* component ^slicing.discriminator.type = #pattern
* component ^slicing.discriminator.path = "code"
* component ^slicing.ordered = false
* component ^slicing.rules = #open
* component contains 
    input 0..1 MS and 
    output 0..1 MS and
    urineOutput 0..1 MS

* component[input].code = ONCObservationCodes#fluid-input-total
* component[input].value[x] only Quantity
* component[input].valueQuantity 1..1 MS
* component[input].valueQuantity.unit = "mL"
* component[input].valueQuantity.system = "http://unitsofmeasure.org"
* component[input].valueQuantity.code = #mL

* component[output].code = ONCObservationCodes#fluid-output-total
* component[output].value[x] only Quantity
* component[output].valueQuantity 1..1 MS
* component[output].valueQuantity.unit = "mL"
* component[output].valueQuantity.system = "http://unitsofmeasure.org"
* component[output].valueQuantity.code = #mL

* component[urineOutput].code = ONCObservationCodes#urine-output
* component[urineOutput].value[x] only Quantity
* component[urineOutput].valueQuantity 1..1 MS
* component[urineOutput].valueQuantity.unit = "mL"
* component[urineOutput].valueQuantity.system = "http://unitsofmeasure.org"
* component[urineOutput].valueQuantity.code = #mL
