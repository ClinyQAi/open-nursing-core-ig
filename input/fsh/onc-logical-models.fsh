// =============================================================================
// LOGICAL MODELS (openEHR Inspired)
// These files define the "Clinical Truth" independent of FHIR Resource constraints.
// They serve as the foundational clinical definitions for the Relational AI.
// =============================================================================

Logical: ONCRelationalCareModel
Id: onc-relational-care-logical
Title: "Relational Care Logical Model"
Description: "A vendor-neutral clinical model of the relational nursing assessment. Defines WHAT data must be captured, regardless of HOW it is stored in FHIR."
* patientPreferences 1..1 string "The patient's personal goals and what matters most to them today."
* relationalEngagement 1..1 integer "A score from 1-5 representing the depth of the therapeutic relationship."
* empathyIndex 1..1 code "The ONC Empathy Index (1-5) measuring relational quality."
* skinToneEquity 1..1 code "The patient's skin tone classification (Fitzpatrick or Monk) used to guide clinical assessment."
* mandatoryEquityValidation 1..1 boolean "Technical flag ensuring the 'Fairness Gate' was passed."
* adpieStatus 1..1 code "The current stage of the professional nursing process (Assessment, Diagnosis, Planning, Implementation, Evaluation)."
* clinicalNarrative 1..1 string "The person-centred narrative describing the patient's experience."

// =============================================================================
// TERMINOLOGY BINDINGS
// =============================================================================
* adpieStatus from ONCADPIEVS (required)
* skinToneEquity from ONCSkinToneVS (extensible)
* empathyIndex from ONCEmpathyIndexVS (required)

// =============================================================================
// VALUE SETS for Logical Model
// =============================================================================
ValueSet: ONCADPIEVS
Id: onc-adpie-vs
Title: "ADPIE Nursing Process Phases"
Description: "The five phases of the professional nursing process."
* #A "Assessment"
* #D "Diagnosis"
* #P "Planning"
* #I "Implementation"
* #E "Evaluation"
