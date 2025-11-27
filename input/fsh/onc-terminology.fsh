ValueSet: NursingProblemValueSet
Id: nursing-problem-valueset
Title: "Nursing Problem Value Set"
* include codes from system http://snomed.info/sct where concept is-a #409586006

ValueSet: NursingInterventionValueSet
Id: nursing-intervention-valueset
Title: "Nursing Intervention Value Set"
* include codes from system http://snomed.info/sct where concept is-a #71388002

ValueSet: GoalEvaluationValueSet
Id: goal-evaluation-valueset
Title: "Goal Evaluation Value Set"
* include http://snomed.info/sct#385633008
* include http://snomed.info/sct#385634002

ValueSet: ProblemCategoryValueSet
Id: problem-category-valueset
Title: "Problem Category Value Set"
* include codes from system ONCProblemType

CodeSystem: ONCProblemType
Id: onc-problem-type
Title: "Problem Type CodeSystem"
* #nursing-diagnosis "Nursing Diagnosis"

ValueSet: SkinToneVS
Id: skintone-vs
Title: "Fitzpatrick Skin Tone Value Set"
* include codes from system http://snomed.info/sct where concept is-a #403153005

ValueSet: HousingStatusVS
Id: housing-status-vs
Title: "Housing Status Value Set"
* include http://snomed.info/sct#32911000
* include http://snomed.info/sct#160753008
