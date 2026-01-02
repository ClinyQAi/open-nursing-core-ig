// =============================================================================
// TERMINOLOGY MAPPING (Semantic Alignment)
// This file maps custom ONC concepts to international nursing terminologies.
// =============================================================================

Instance: ONCToNandaMapping
InstanceOf: ConceptMap
Usage: #definition
* url = "https://fhir.clinyq.ai/ConceptMap/onc-to-nanda"
* name = "ONCToNandaMapping"
* title = "Mapping ONC Relational Concepts to NANDA-I"
* status = #draft
* description = "Maps Open Nursing Core clinical findings to NANDA-I Nursing Diagnoses."
* sourceCanonical = "https://fhir.clinyq.ai/ValueSet/onc-relational-findings-vs"
* targetCanonical = "http://terminology.hl7.org/CodeSystem/nanda-i" // Placeholder URL

// Example Mapping
* group[0].source = "https://fhir.clinyq.ai/CodeSystem/onc-observation-codes"
* group[0].target = "http://terminology.hl7.org/CodeSystem/nanda-i"

// Map: Patient Story narrative mentioning isolation -> NANDA Social Isolation
* group[0].element[0].code = #patient-story
* group[0].element[0].target[0].code = #00053
* group[0].element[0].target[0].display = "Social Isolation"
* group[0].element[0].target[0].equivalence = #relatedto

// Map: Relational Engagement score low -> NANDA Risk for Loneliness
* group[0].element[1].code = #relational-engagement
* group[0].element[1].target[0].code = #00054
* group[0].element[1].target[0].display = "Risk for Loneliness"
* group[0].element[1].target[0].equivalence = #relatedto

// Map: Skin Assessment finding -> SNOMED concepts for Equity
* group[0].element[2].code = #skintone-observation
* group[0].element[2].target[0].code = #399912005
* group[0].element[2].target[0].display = "Wound Assessment" 
* group[0].element[2].target[0].equivalence = #specializes
