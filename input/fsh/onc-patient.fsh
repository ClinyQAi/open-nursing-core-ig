// =============================================================================
// Extension: UK Core Ethnic Category (defined locally to ensure build stability)
// =============================================================================
Extension: UKCoreEthnicCategory
Id: UKCore-Extension-EthnicCategory
Title: "UK Core Ethnic Category"
Description: "A code classifying the person's ethnicity."
* ^url = "https://fhir.hl7.org.uk/StructureDefinition/UKCore-Extension-EthnicCategory"
* value[x] only CodeableConcept
// In a real deployment, you would bind this to the specific NHS ValueSet.
// For this standard, we ensure the structural slot exists.

// =============================================================================
// Profile: ONCNHSPatient
// =============================================================================
Profile: ONCNHSPatient
Parent: Patient
Id: onc-nhs-patient
Title: "ONC NHS Patient"
Description: "An NHS-specific patient profile that mandates the inclusion of ethnicity data for health equity analysis."
* extension contains UKCoreEthnicCategory named ethnicCategory 1..1 MS