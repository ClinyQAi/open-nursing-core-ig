// =============================================================================
// MENTAL CAPACITY MODULE
// This file defines profiles for Mental Capacity Assessment (MCA).
// Critical for legal compliance and frailty/delirium workflows in the UK.
// =============================================================================

Profile: ONCMentalCapacity
Parent: ONCNursingAssessment
Id: onc-mental-capacity
Title: "Mental Capacity Assessment"
Description: "Records the outcome of a Mental Capacity Assessment for a specific decision. Fundamental legal safeguard in UK nursing practice."
* ^url = "https://fhir.clinyq.ai/StructureDefinition/onc-mental-capacity"
* ^version = "0.1.0"
* ^status = #draft
* category = http://terminology.hl7.org/CodeSystem/observation-category#exam
* code = ONCObservationCodes#mca-assessment
* value[x] only CodeableConcept
* valueCodeableConcept 1..1 MS
* valueCodeableConcept from MentalCapacityVS (required)
* valueCodeableConcept ^short = "Outcome (Capacity Present/Absent)"
* note 1..* MS
* note ^short = "The specific decision being assessed (CRITICAL)"

ValueSet: MentalCapacityVS
Id: onc-mca-vs
Title: "Mental Capacity Finding Value Set"
Description: "Codes indicating presence or absence of capacity"
* ONCObservationCodes#capacity-present "Capacity Present"
* ONCObservationCodes#capacity-absent "Capacity Absent"
* ONCObservationCodes#best-interest "Best Interest Decision Required"
