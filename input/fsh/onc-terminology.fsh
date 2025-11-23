ValueSet: NursingProblemValueSet
Id: nursing-problem-valueset
Title: "Nursing Problem Value Set"
* include codes from system http://hl7.org/fhir/sid/icnp where concept is-a #10045151
* include codes from system http://snomed.info/sct where concept is-a #409586006

ValueSet: NursingInterventionValueSet
Id: nursing-intervention-valueset
Title: "Nursing Intervention Value Set"
* include codes from system http://hl7.org/fhir/sid/icnp where concept is-a #10045153
* include codes from system http://snomed.info/sct where concept is-a #71388002

ValueSet: GoalEvaluationValueSet
Id: goal-evaluation-valueset
Title: "Goal Evaluation Value Set"
* include http://snomed.info/sct#385633008
* include http://snomed.info/sct#385634002

CodeSystem: ONCProblemType
Id: onc-problem-type
Title: "Open Nursing Core Problem Type CodeSystem"
* #nursing-diagnosis "Nursing Diagnosis"
