// =============================================================================
// ValueSets
// =============================================================================
ValueSet: NursingProblemValueSet
Id: nursing-problem-valueset
Title: "Nursing Problem Value Set"
Description: "A set of ICNP and SNOMED CT codes representing common nursing problems."
* include codes from system http://hl7.org/fhir/sid/icnp where concept is-a #10045151 // "Nursing diagnosis"
* include codes from system http://snomed.info/sct where concept is-a #409586006 // "Complaint (finding)"

ValueSet: NursingInterventionValueSet
Id: nursing-intervention-valueset
Title: "Nursing Intervention Value Set"
Description: "A set of ICNP and SNOMED CT codes representing core nursing interventions."
* include codes from system http://hl7.org/fhir/sid/icnp where concept is-a #10045153 // "Nursing intervention"
* include codes from system http://snomed.info/sct where concept is-a #71388002 // "Procedure (procedure)"

ValueSet: GoalEvaluationValueSet
Id: goal-evaluation-valueset
Title: "Goal Evaluation Value Set"
Description: "A set of codes indicating progress towards a goal."
* include http://snomed.info/sct#385633008 "Goal achieved (finding)"
* include http://snomed.info/sct#385634002 "Goal not achieved (finding)"

// =============================================================================
// CodeSystems
// =============================================================================
CodeSystem: ONCProblemType
Id: onc-problem-type
Title: "Open Nursing Core Problem Type CodeSystem"
Description: "A code system to distinguish nursing problems from other condition types."
* #nursing-diagnosis "Nursing Diagnosis" "A clinical judgment about a human response to a health condition, identified by a nurse."