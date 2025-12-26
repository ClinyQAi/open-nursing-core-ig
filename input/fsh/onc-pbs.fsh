// =============================================================================
// Positive Behaviour Support (PBS) - ABC Chart
// =============================================================================
Profile: ONCABCChart
Parent: ONCNursingAssessment
Id: onc-abc-chart
Title: "PBS ABC Chart"
Description: "Antecedent-Behaviour-Consequence (ABC) Chart for recording behaviours of concern. Fundamental tool in Positive Behaviour Support (PBS) for Learning Disabilities."
* ^url = "https://fhir.clinyq.ai/StructureDefinition/onc-abc-chart"
* ^version = "0.1.0"
* ^status = #draft
* category = http://terminology.hl7.org/CodeSystem/observation-category#exam
* code = ONCObservationCodes#abc-chart
* value[x] only CodeableConcept
* valueCodeableConcept 1..1 MS
* valueCodeableConcept from PBSFunctionVS (preferred)
* valueCodeableConcept ^short = "Hypothesized Function (SEAT)"
* component 0..* MS
* component ^slicing.discriminator.type = #pattern
* component ^slicing.discriminator.path = "code"
* component ^slicing.ordered = false
* component ^slicing.rules = #open
* component contains 
    antecedent 1..1 MS and 
    behaviour 1..1 MS and 
    consequence 1..1 MS and
    duration 0..1 MS and
    intensity 0..1 MS

* component[antecedent].code = ONCObservationCodes#abc-antecedent
* component[antecedent].value[x] only string
* component[antecedent].valueString 1..1 MS
* component[antecedent].valueString ^short = "Trigger/Context (Who, What, Where, When)"

* component[behaviour].code = ONCObservationCodes#abc-behaviour
* component[behaviour].value[x] only string
* component[behaviour].valueString 1..1 MS
* component[behaviour].valueString ^short = "Exact description of what was done"

* component[consequence].code = ONCObservationCodes#abc-consequence
* component[consequence].value[x] only string
* component[consequence].valueString 1..1 MS
* component[consequence].valueString ^short = "Staff response & Outcome"

* component[duration].code = ONCObservationCodes#abc-duration
* component[duration].value[x] only Quantity
* component[duration].valueQuantity 1..1 MS
* component[duration].valueQuantity.unit = "min"
* component[duration].valueQuantity.system = "http://unitsofmeasure.org"
* component[duration].valueQuantity.code = #min

* component[intensity].code = ONCObservationCodes#abc-intensity
* component[intensity].value[x] only integer
* component[intensity].valueInteger 1..1 MS
* component[intensity].valueInteger ^short = "1 (Mild) to 10 (Severe)"

ValueSet: PBSFunctionVS
Id: onc-pbs-function-vs
Title: "PBS Behaviour Function ValueSet"
Description: "Common functions of behaviour (SEAT)"
* ONCObservationCodes#abc-function "Function of Behaviour" 
// Note: In detailed implementation, this would contain codes for Sensory, Escape, Attention, Tangible.
// For now, we allow the parent code or free text if CodeableConcept allows text.
