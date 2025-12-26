// =============================================================================
// Bristol Stool Chart Profile
// =============================================================================
Profile: ONCBristolStoolChart
Parent: ONCNursingAssessment
Id: onc-bristol-stool-chart
Title: "Bristol Stool Chart"
Description: "Assessment of stool form using the Bristol Stool Chart (Types 1-7). Gold standard for bowel function assessment."
* ^url = "https://fhir.clinyq.ai/StructureDefinition/onc-bristol-stool-chart"
* ^version = "0.1.0"
* ^status = #draft
* category = http://terminology.hl7.org/CodeSystem/observation-category#exam
* code = ONCObservationCodes#bristol-score
* value[x] only Quantity
* valueQuantity 1..1 MS
* valueQuantity.value obeys bristol-range
* valueQuantity.unit = "{score}"
* valueQuantity.system = "http://unitsofmeasure.org"
* valueQuantity ^short = "Bristol Stool Type (1-7)"
* note 0..* MS
* note ^short = "Additional notes (e.g., colour, amount)"

Invariant: bristol-range
Description: "Bristol score must be between 1 and 7"
Expression: "$this >= 1 and $this <= 7"
Severity: #error
