// =============================================================================
// NEWS2 (National Early Warning Score 2) Profile
// =============================================================================
Profile: ONCNEWS2Score
Parent: ONCNursingAssessment
Id: onc-news2-score
Title: "NEWS2 Score"
Description: "National Early Warning Score 2 (NEWS2) for detecting clinical deterioration"
* status = #final
* status MS
* code = http://loinc.org#88330-6 "National Early Warning Score [NEWS]"
* code MS
* value[x] only integer
* valueInteger 1..1 MS
* valueInteger obeys news2-range
* valueInteger ^short = "NEWS2 total score (0-20)"

Invariant: news2-range
Description: "NEWS2 score must be between 0 and 20"
Expression: "$this >= 0 and $this <= 20"
Severity: #error

// =============================================================================
// Pain Assessment (Numeric Rating Scale 0-10) Profile
// =============================================================================
Profile: ONCPainAssessment
Parent: ONCNursingAssessment
Id: onc-pain-assessment
Title: "Pain Assessment (NRS 0-10)"
Description: "Pain severity assessment using the Numeric Rating Scale (0-10)"
* status = #final or #amended or #corrected
* status MS
* code from PainAssessmentCodeValueSet (required)
* code MS
* value[x] only integer
* valueInteger 1..1 MS
* valueInteger obeys pain-range
* valueInteger ^short = "Pain severity score (0-10)"
* bodySite 0..1 MS
* bodySite ^short = "Location of pain"
* effectiveDateTime 1..1 MS

Invariant: pain-range
Description: "Pain score must be between 0 and 10"
Expression: "$this >= 0 and $this <= 10"
Severity: #error

ValueSet: PainAssessmentCodeValueSet
Id: pain-assessment-code-vs
Title: "Pain Assessment Code Value Set"
Description: "LOINC codes for pain severity assessment"
* http://loinc.org#72514-3 "Pain severity - 0-10 verbal numeric rating"
* http://loinc.org#38208-5 "Pain severity - Reported"

// =============================================================================
// Wound Assessment Profile
// =============================================================================
Profile: ONCWoundAssessment
Parent: ONCNursingAssessment
Id: onc-wound-assessment
Title: "Wound Assessment"
Description: "Comprehensive wound assessment including staging and dimensions"
* status = #final or #amended or #corrected
* status MS
* code = http://snomed.info/sct#399912005 "Pressure Ulcer"
* code MS
* value[x] only CodeableConcept
* valueCodeableConcept 1..1 MS
* valueCodeableConcept from WoundStageValueSet (required)
* valueCodeableConcept ^short = "Wound stage"
* component 0..* MS
* component ^slicing.discriminator.type = #pattern
* component ^slicing.discriminator.path = "code"
* component ^slicing.ordered = false
* component ^slicing.rules = #open
* component contains length 0..1 MS and width 0..1 MS and depth 0..1 MS
* component[length].code = http://snomed.info/sct#410668003 "Length"
* component[length].value[x] only Quantity
* component[length].valueQuantity.unit = "cm"
* component[length].valueQuantity.system = "http://unitsofmeasure.org"
* component[length].valueQuantity.code = #cm
* component[length].valueQuantity obeys positive-dimension
* component[width].code = http://snomed.info/sct#410669006 "Width"
* component[width].value[x] only Quantity
* component[width].valueQuantity.unit = "cm"
* component[width].valueQuantity.system = "http://unitsofmeasure.org"
* component[width].valueQuantity.code = #cm
* component[width].valueQuantity obeys positive-dimension
* component[depth].code = http://snomed.info/sct#410670007 "Depth"
* component[depth].value[x] only Quantity
* component[depth].valueQuantity.unit = "cm"
* component[depth].valueQuantity.system = "http://unitsofmeasure.org"
* component[depth].valueQuantity.code = #cm
* component[depth].valueQuantity obeys positive-dimension

Invariant: positive-dimension
Description: "Wound dimensions must be positive"
Expression: "$this > 0"
Severity: #error

ValueSet: WoundStageValueSet
Id: wound-stage-vs
Title: "Wound Stage Value Set"
Description: "SNOMED CT codes for pressure ulcer staging"
* http://snomed.info/sct#421257003 "Stage 1 pressure ulcer"
* http://snomed.info/sct#420226007 "Stage 2 pressure ulcer"
* http://snomed.info/sct#420555000 "Stage 3 pressure ulcer"
* http://snomed.info/sct#420324007 "Stage 4 pressure ulcer"
* http://snomed.info/sct#421076008 "Unstageable pressure ulcer"
* http://snomed.info/sct#723071003 "Deep tissue injury"
