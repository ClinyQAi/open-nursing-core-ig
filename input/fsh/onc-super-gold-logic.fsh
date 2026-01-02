// =============================================================================
// SUPER-GOLD STANDARD: RELATIONAL METROLOGY & EQUITY GATES
// This file defines the advanced clinical logic that outpaces traditional
// static modeling (openEHR) by making clinical quality "computable."
// =============================================================================

// -----------------------------------------------------------------------------
// 1. Empathy Index (The "Heart" of Nursing)
// -----------------------------------------------------------------------------
ValueSet: ONCEmpathyIndexVS
Id: onc-empathy-index-vs
Title: "ONC Empathy & Relational Engagement Index"
Description: "A clinical scale measuring the depth of therapeutic empathy in nurse-patient interactions. Traditional EHRs ignore this; the Super-Gold Standard makes it a primary outcome."
* ONCObservationCodes#empathy-1 "Low Empathy: Task-focused interaction with minimal person-centred engagement."
* ONCObservationCodes#empathy-2 "Basic Empathy: Professional interaction with patient identity acknowledged."
* ONCObservationCodes#empathy-3 "Moderate Empathy: Active relational engagement with shared decision making."
* ONCObservationCodes#empathy-4 "High Empathy: Authentic partnership with deep understanding of patient experience."
* ONCObservationCodes#empathy-5 "Relational Excellence: Flourishing partnership with total alignment on 'What Matters to Me'."

// -----------------------------------------------------------------------------
// 2. Mandatory Equity Invariants (The "Fairness Gate")
// -----------------------------------------------------------------------------
// This invariant ensures that a skin assessment CANNOT be recorded without 
// an accompanying skin-tone observation (Fitzpatrick or Monk).
Invariant: onc-equity-gate-1
Description: "Clinical safety rule: Skin observations (pressure ulcers, wounds) MUST include a Skin Tone assessment to ensure equitable care thresholds."
Severity: #error
Expression: "extension('https://fhir.clinyq.ai/StructureDefinition/onc-equity-marker').exists()"

// -----------------------------------------------------------------------------
// 3. Relational Outcomes (Triple Link: NANDA + NIC + NOC)
// -----------------------------------------------------------------------------
ValueSet: ONCRelationalOutcomesVS
Id: onc-relational-outcomes-vs
Title: "ONC Relational Care Outcomes"
Description: "Captures the measurable outcomes of relational and empathic nursing care."
* http://snomed.info/sct#161096001 "Patient feels respected"
* http://snomed.info/sct#307823004 "Patient feels heard"
* http://snomed.info/sct#428131006 "Therapeutic relationship established"
