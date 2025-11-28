// =============================================================================
// 1. Core Nursing Process Value Sets
// =============================================================================

ValueSet: NursingProblemValueSet
Id: nursing-problem-valueset
Title: "Nursing Problem Value Set"
Description: "Codes representing clinical problems or conditions identified by nurses."
* include codes from system http://snomed.info/sct where concept is-a #409586006 "Complaint (finding)"
// Commenting out ICNP for now to ensure clean validation without external server dependencies
// * include codes from system http://hl7.org/fhir/sid/icnp where concept is-a #10045151

ValueSet: NursingInterventionValueSet
Id: nursing-intervention-valueset
Title: "Nursing Intervention Value Set"
Description: "Codes representing interventions performed by nurses."
* include codes from system http://snomed.info/sct where concept is-a #71388002 "Procedure (procedure)"
// * include codes from system http://hl7.org/fhir/sid/icnp where concept is-a #10045153

ValueSet: GoalEvaluationValueSet
Id: goal-evaluation-valueset
Title: "Goal Evaluation Value Set"
Description: "Codes used to evaluate the outcome of a patient goal."
* include http://snomed.info/sct#385633008 "Goal achieved"
* include http://snomed.info/sct#385634002 "Goal not achieved"

ValueSet: ProblemCategoryValueSet
Id: problem-category-valueset
Title: "Problem Category Value Set"
Description: "Classifies the type of problem (e.g. Nursing Diagnosis)."
* include codes from system ONCProblemType

// =============================================================================
// 2. Social Determinants & Safety Value Sets
// =============================================================================

ValueSet: HousingStatusVS
Id: housing-status-vs
Title: "Housing Status Value Set"
Description: "Codes representing a patient's housing situation."
* include http://snomed.info/sct#32911000 "Homeless"
* include http://snomed.info/sct#105529008 "Lives alone"
* include http://snomed.info/sct#160753008 "Lives with family"
* include http://snomed.info/sct#394923006 "Lives in a nursing home"

ValueSet: SkinToneVS
Id: skintone-vs
Title: "Fitzpatrick Skin Tone Value Set"
Description: "Codes for the Fitzpatrick skin type scale."
* include http://snomed.info/sct#403153005 "Fitzpatrick skin type I"
* include http://snomed.info/sct#403154004 "Fitzpatrick skin type II"
* include http://snomed.info/sct#403155003 "Fitzpatrick skin type III"
* include http://snomed.info/sct#403156002 "Fitzpatrick skin type IV"
* include http://snomed.info/sct#403157006 "Fitzpatrick skin type V"
* include http://snomed.info/sct#403158001 "Fitzpatrick skin type VI"

// =============================================================================
// 3. Code Systems
// =============================================================================

CodeSystem: ONCProblemType
Id: onc-problem-type
Title: "Open Nursing Core Problem Type CodeSystem"
Description: "A code system to distinguish nursing problems from other condition types."
* #nursing-diagnosis "Nursing Diagnosis" "A clinical judgment about a human response to a health condition, identified by a nurse."

CodeSystem: ONCObservationCodes
Id: onc-observation-codes
Title: "Open Nursing Core Observation Codes"
Description: "Local codes for observations where no standard LOINC/SNOMED code exists."
* #mst-score "Monk Skin Tone Scale Score" "A 10-point scale (MST-01 to MST-10) for classifying skin tone, designed to be more inclusive of darker skin tones than the Fitzpatrick scale."
