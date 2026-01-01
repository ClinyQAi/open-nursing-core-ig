// =============================================================================
// PRSB Alignment Profiles
// Aligning with Professional Record Standards Body (PRSB) Nursing Care Needs Standard
// =============================================================================

// -----------------------------------------------------------------------------
// 1. Elimination
// -----------------------------------------------------------------------------
Profile: ONCContinenceAssessment
Parent: ONCNursingAssessment
Id: onc-continence-assessment
Title: "Continence Assessment"
Description: "Assessment of bladder and bowel control status."
* code = https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes#continence-assessment
* value[x] only CodeableConcept
* valueCodeableConcept from http://hl7.org/fhir/ValueSet/consistency-type (example)

Profile: ONCBladderAssessment
Parent: ONCNursingAssessment
Id: onc-bladder-assessment
Title: "Bladder Assessment"
Description: "Detailed assessment of bladder function, including voiding patterns."
* code = https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes#bladder-assessment
* value[x] only CodeableConcept

Profile: ONCBowelAssessment
Parent: ONCNursingAssessment
Id: onc-bowel-assessment
Title: "Bowel Assessment"
Description: "Detailed assessment of bowel function and regularity."
* code = https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes#bowel-assessment
* value[x] only CodeableConcept

Profile: ONCCatheterCare
Parent: ONCNursingAssessment
Id: onc-catheter-care
Title: "Catheter Care"
Description: "Documentation of catheter site care and status."
* code = https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes#catheter-care
* value[x] only string or CodeableConcept

// -----------------------------------------------------------------------------
// 2. Eating and Drinking
// -----------------------------------------------------------------------------
Profile: ONCOralIntakeAssessment
Parent: ONCNursingAssessment
Id: onc-oral-intake-assessment
Title: "Oral Intake Assessment"
Description: "Assessment of ability to take food and fluids orally."
* code = https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes#oral-intake
* value[x] only CodeableConcept

Profile: ONCSwallowingAssessment
Parent: ONCNursingAssessment
Id: onc-swallowing-assessment
Title: "Swallowing Assessment"
Description: "Screening for dysphagia and swallowing difficulties."
* code = https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes#swallowing
* value[x] only CodeableConcept

Profile: ONCDietaryRequirements
Parent: ONCNursingAssessment
Id: onc-dietary-requirements
Title: "Dietary Requirements"
Description: "Documentation of specific dietary needs (e.g. textural modification, cultural)."
* code = https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes#dietary-requirements
* value[x] only CodeableConcept or string

// -----------------------------------------------------------------------------
// 3. Mobility
// -----------------------------------------------------------------------------
Profile: ONCMobilityAssessment
Parent: ONCNursingAssessment
Id: onc-mobility-assessment
Title: "Mobility Assessment"
Description: "Assessment of capability to move and limitations."
* code = https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes#mobility
* value[x] only CodeableConcept

Profile: ONCDeviceUseStatement
Parent: DeviceUseStatement
Id: onc-device-use-statement
Title: "Device Use Statement"
Description: "Documentation of mobility aids or other devices used by the patient."
* subject only Reference(Patient)
* device only Reference(Device)
* timing[x] MS
* bodySite MS

// -----------------------------------------------------------------------------
// 4. Personal Hygiene
// -----------------------------------------------------------------------------
Profile: ONCHygieneAssessment
Parent: ONCNursingAssessment
Id: onc-hygiene-assessment
Title: "Personal Hygiene Needs Assessment"
Description: "Assessment of assistance required for personal hygiene."
* code = https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes#hygiene-needs
* value[x] only CodeableConcept

Profile: ONCOralCareAssessment
Parent: ONCNursingAssessment
Id: onc-oral-care-assessment
Title: "Oral Care Needs Assessment"
Description: "Assessment of mouth care needs and oral health."
* code = https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes#oral-care
* value[x] only CodeableConcept

// -----------------------------------------------------------------------------
// 5. Medication Self-Management
// -----------------------------------------------------------------------------
Profile: ONCMedicationAbility
Parent: ONCNursingAssessment
Id: onc-medication-ability
Title: "Medication Management Ability"
Description: "Assessment of the patient's ability to manage their own medication."
* code = https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes#medication-ability
* value[x] only CodeableConcept

Profile: ONCMedicationSelfAdmin
Parent: ONCNursingAssessment
Id: onc-medication-self-admin
Title: "Medication Self-Administration Observation"
Description: "Observation of the patient performing self-administration."
* code = https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes#medication-self-admin
* value[x] only CodeableConcept
