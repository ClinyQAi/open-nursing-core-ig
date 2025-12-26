// =============================================================================
// Pain Assessment (Numeric Rating Scale 0-10) Profile
// =============================================================================
Profile: ONCPainAssessment
Parent: ONCNursingAssessment
Id: onc-pain-assessment
Title: "Pain Assessment (NRS 0-10)"
Description: "Pain severity assessment using the Numeric Rating Scale (0-10)"
* status MS
* code from PainAssessmentCodeValueSet (required)
* code MS
* value[x] only Quantity
* valueQuantity 1..1 MS
* valueQuantity.value obeys pain-range
* valueQuantity.unit = "{score}"
* valueQuantity.system = "http://unitsofmeasure.org"
* valueQuantity ^short = "Pain severity score (0-10)"
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
* component[length].valueQuantity.value obeys positive-dimension
* component[length].valueQuantity.unit = "cm"
* component[length].valueQuantity.system = "http://unitsofmeasure.org"
* component[length].valueQuantity.code = #cm
* component[width].code = http://snomed.info/sct#401239006 "Width of wound"
* component[width].value[x] only Quantity
* component[width].valueQuantity.value obeys positive-dimension
* component[width].valueQuantity.unit = "cm"
* component[width].valueQuantity.system = "http://unitsofmeasure.org"
* component[width].valueQuantity.code = #cm
* component[depth].code = http://snomed.info/sct#425094009 "Depth of wound"
* component[depth].value[x] only Quantity
* component[depth].valueQuantity.value obeys positive-dimension
* component[depth].valueQuantity.unit = "cm"
* component[depth].valueQuantity.system = "http://unitsofmeasure.org"
* component[depth].valueQuantity.code = #cm

Invariant: positive-dimension
Description: "Wound dimensions must be positive"
Expression: "$this > 0"
Severity: #error

ValueSet: WoundStageValueSet
Id: wound-stage-vs
Title: "Wound Stage Value Set"
* include ONCObservationCodes#stage-1
* include ONCObservationCodes#stage-2
* include ONCObservationCodes#stage-3
* include ONCObservationCodes#stage-4
* include ONCObservationCodes#unstageable
* include ONCObservationCodes#deep-tissue
