// ==============================================================================
// VALUE SETS
// ==============================================================================

ValueSet: NursingProblemValueSet
Id: nursing-problem-valueset
Title: "Nursing Problem Value Set"
Description: "Value set for nursing problems and diagnoses"
* ^experimental = false
* include http://snomed.info/sct#129839007 "At risk for falls"
* include http://snomed.info/sct#162828007 "Risk of falls"
* include http://snomed.info/sct#300893006 "Nutritional finding"
* include http://snomed.info/sct#22253000 "Pain"

ValueSet: NursingInterventionValueSet
Id: nursing-intervention-valueset
Title: "Nursing Intervention Value Set"
Description: "Value set for nursing interventions"
* ^experimental = false
* include http://snomed.info/sct#71388002 "Procedure"
* include http://snomed.info/sct#225358003 "Wound care"
* include http://snomed.info/sct#386373004 "Nutrition therapy"

ValueSet: GoalEvaluationValueSet
Id: goal-evaluation-valueset
Title: "Goal Evaluation Value Set"
Description: "Value set for evaluating patient goal outcomes"
* ^experimental = false
* include http://snomed.info/sct#385633008 "Resolved"
* include http://snomed.info/sct#385634002 "Worsened"
* include http://snomed.info/sct#118222006 "General finding of observation of patient"

ValueSet: ProblemCategoryValueSet
Id: problem-category-valueset
Title: "Problem Category Value Set"
Description: "Value set for categorizing nursing problems"
* ^experimental = false
* include codes from system ONCProblemType

ValueSet: SkinToneVS
Id: skintone-vs
Title: "Fitzpatrick Skin Tone Value Set"
Description: "Value set for Fitzpatrick skin type classifications"
* ^experimental = false
* include http://snomed.info/sct#403153005 "Fitzpatrick skin type I"
* include http://snomed.info/sct#403154004 "Fitzpatrick skin type II"
* include http://snomed.info/sct#403155003 "Fitzpatrick skin type III"
* include http://snomed.info/sct#403156002 "Fitzpatrick skin type IV"
* include http://snomed.info/sct#403157006 "Fitzpatrick skin type V"
* include http://snomed.info/sct#403158001 "Fitzpatrick skin type VI"

ValueSet: HousingStatusVS
Id: housing-status-vs
Title: "Housing Status Value Set"
Description: "Value set for patient housing status"
* ^experimental = false
* include http://snomed.info/sct#266935003 "Housing problem"
* include http://snomed.info/sct#160724001 "Homeless"
* include http://snomed.info/sct#224224003 "Lives in own home"

// ==============================================================================
// CODE SYSTEMS
// ==============================================================================

CodeSystem: ONCProblemType
Id: onc-problem-type
Title: "Problem Type CodeSystem"
Description: "Code system for categorizing types of nursing problems"
* ^url = "http://open-nursing-core.org/CodeSystem/onc-problem-type"
* ^experimental = false
* ^caseSensitive = true
* #nursing-diagnosis "Nursing Diagnosis" "A clinical judgment about individual, family, or community responses to actual or potential health problems"
* #risk-diagnosis "Risk Diagnosis" "A clinical judgment about an individual's vulnerability to developing an undesirable health condition"
* #health-promotion "Health Promotion Diagnosis" "A clinical judgment about motivation to increase wellbeing"
