// =============================================================================
// CLINICAL FRAILTY MODULE
// This file defines profiles for the Clinical Frailty Scale (Rockwood).
// Mandated for all patients >65 in acute care contexts.
// =============================================================================

// =============================================================================
// Clinical Frailty Scale (CFS)
// =============================================================================
Profile: ONCClinicalFrailtyScale
Parent: ONCNursingAssessment
Id: onc-clinical-frailty-scale
Title: "Clinical Frailty Scale (CFS)"
Description: "Assessment of frailty using the Rockwood Clinical Frailty Scale (1-9). Essential for older adults to determine baseline functional status."
* ^url = "https://fhir.clinyq.ai/StructureDefinition/onc-clinical-frailty-scale"
* ^version = "0.1.0"
* ^status = #draft
* category = http://terminology.hl7.org/CodeSystem/observation-category#survey
* code = ONCObservationCodes#cfs-score
* value[x] only CodeableConcept
* valueCodeableConcept 1..1 MS
* valueCodeableConcept from ClinicalFrailtyScaleVS (required)
* valueCodeableConcept ^short = "Frailty Level (1-9)"

ValueSet: ClinicalFrailtyScaleVS
Id: onc-cfs-vs
Title: "Clinical Frailty Scale Value Set"
Description: "Codes for Rockwood Clinical Frailty Scale (1-9)"
* include ONCObservationCodes#cfs-1
* include ONCObservationCodes#cfs-2
* include ONCObservationCodes#cfs-3
* include ONCObservationCodes#cfs-4
* include ONCObservationCodes#cfs-5
* include ONCObservationCodes#cfs-6
* include ONCObservationCodes#cfs-7
* include ONCObservationCodes#cfs-8
* include ONCObservationCodes#cfs-9
