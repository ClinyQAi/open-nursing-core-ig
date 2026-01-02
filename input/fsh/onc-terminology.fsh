// ==============================================================================
// VALUE SETS
// ==============================================================================

ValueSet: NursingProblemValueSet
Id: nursing-problem-valueset
Title: "Nursing Problem Value Set"
Description: "Value set for nursing problems and diagnoses"
* ^experimental = false
* include http://snomed.info/sct#129839007 "At risk for falls"
* include ONCObservationCodes#risk-falls "Risk of falls"
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
* include http://snomed.info/sct#385652002 "Objective achieved"
* include http://snomed.info/sct#385651009 "Objective not achieved"
* include http://snomed.info/sct#255609007 "Partial achievement"
* include http://snomed.info/sct#723510000 "Sustained improvement"
* include http://snomed.info/sct#260388008 "Worsening"

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
* include ONCObservationCodes#fitzpatrick-1 "Type I"
* include ONCObservationCodes#fitzpatrick-2 "Type II"
* include ONCObservationCodes#fitzpatrick-3 "Type III"
* include ONCObservationCodes#fitzpatrick-4 "Type IV"
* include ONCObservationCodes#fitzpatrick-5 "Type V"
* include ONCObservationCodes#fitzpatrick-6 "Type VI"

ValueSet: HousingStatusVS
Id: housing-status-vs
Title: "Housing Status Value Set"
Description: "Value set for patient housing status"
* ^experimental = false
* include http://snomed.info/sct#266935003 "Housing lack"
* include http://snomed.info/sct#224224003 "Lives in staffed home"

// ==============================================================================
// CODE SYSTEMS
// ==============================================================================

CodeSystem: ONCProblemType
Id: onc-problem-type
Title: "Problem Type CodeSystem"
Description: "Code system for categorizing types of nursing problems"
* ^url = "https://opennursingcoreig.com/CodeSystem/onc-problem-type"
* ^experimental = false
* ^caseSensitive = true
* #nursing-diagnosis "Nursing Diagnosis" "A clinical judgment about individual, family, or community responses to actual or potential health problems"
* #risk-diagnosis "Risk Diagnosis" "A clinical judgment about an individual's vulnerability to developing an undesirable health condition"
* #health-promotion "Health Promotion Diagnosis" "A clinical judgment about motivation to increase wellbeing"
