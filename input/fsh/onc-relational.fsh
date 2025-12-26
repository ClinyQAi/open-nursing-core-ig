// =============================================================================
// RELATIONAL CARE MODULE
// This file defines profiles for Person-Centred Nursing and Relational Intelligence.
// It captures "soft" data that is critical for holistic care but often missing from
// standard clinical IGs.
// =============================================================================

// =============================================================================
// 1. What Matters to Me (Goal/Priority)
// =============================================================================
Profile: ONCWhatMattersToMe
Parent: Observation
Id: onc-what-matters
Title: "What Matters to Me"
Description: "Captures the patient's specific, personal priorities and non-clinical goals (e.g., 'I want to walk my daughter down the aisle'). Fundamental to person-centred care."
* ^url = "https://fhir.clinyq.ai/StructureDefinition/onc-what-matters"
* ^version = "0.1.0"
* ^status = #draft
* category = http://terminology.hl7.org/CodeSystem/observation-category#social-history
* code = ONCObservationCodes#what-matters
* value[x] only string
* valueString 1..1 MS
* note 0..* MS

// =============================================================================
// 2. Patient Story (Narrative)
// =============================================================================
Profile: ONCPatientStory
Parent: Observation
Id: onc-patient-story
Title: "Patient Story"
Description: "A narrative summary of the patient's background, biography, preferences, and personhood. Goes beyond clinical history to capture 'who the person is'."
* ^url = "https://fhir.clinyq.ai/StructureDefinition/onc-patient-story"
* ^version = "0.1.0"
* ^status = #draft
* category = http://terminology.hl7.org/CodeSystem/observation-category#social-history
* code = ONCObservationCodes#patient-story
* value[x] only string
* valueString 1..1 MS
* valueString ^short = "Narrative story of the patient"

// =============================================================================
// 3. Relational Engagement Observation
// =============================================================================
Profile: ONCRelationalObservation
Parent: Observation
Id: onc-relational-observation
Title: "Relational Engagement Score"
Description: "Assessment of the quality and depth of the nurse-patient relationship or engagement level. Supports the relational aspect of care."
* ^url = "https://fhir.clinyq.ai/StructureDefinition/onc-relational-observation"
* ^version = "0.1.0"
* ^status = #draft
* category = http://terminology.hl7.org/CodeSystem/observation-category#survey
* code = ONCObservationCodes#relational-engagement
* value[x] only integer
* valueInteger 1..1 MS
* valueInteger ^short = "Engagement Level (1-5)"
* valueInteger obeys engagement-range

Invariant: engagement-range
Description: "Engagement score must be between 1 (Low) and 5 (High)"
Expression: "$this >= 1 and $this <= 5"
Severity: #error
