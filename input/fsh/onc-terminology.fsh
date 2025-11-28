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

CodeSystem: ONCMonkScale
Id: onc-monk-scale
Title: "Monk Skin Tone Scale"
Description: "The Monk Skin Tone (MST) Scale is a 10-shade scale designed to represent a broader range of skin tones for AI and equity applications."
* ^url = "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-monk-scale"
* #MST-01 "Monk Scale 01" "Lightest skin tone"
* #MST-02 "Monk Scale 02"
* #MST-03 "Monk Scale 03"
* #MST-04 "Monk Scale 04"
* #MST-05 "Monk Scale 05"
* #MST-06 "Monk Scale 06"
* #MST-07 "Monk Scale 07"
* #MST-08 "Monk Scale 08"
* #MST-09 "Monk Scale 09"
* #MST-10 "Monk Scale 10" "Darkest skin tone"

ValueSet: ONCMonkScaleVS
Id: onc-monk-scale-vs
Title: "Monk Skin Tone Value Set"
* include codes from system ONCMonkScale

CodeSystem: ONCObservationCodes
Id: onc-observation-codes
Title: "ONC Observation Codes"
Description: "Local observation codes for Open Nursing Core IG."
* ^url = "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes"
* #onc-mst-assessment "Monk Skin Tone Assessment"
