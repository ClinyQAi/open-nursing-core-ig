// =============================================================================
// Abbey Pain Scale Profile (Dementia/Non-Verbal)
// =============================================================================
Profile: ONCAbbeyPainScale
Parent: ONCNursingAssessment
Id: onc-abbey-pain-scale
Title: "Abbey Pain Scale"
Description: "Pain assessment for people with dementia or who cannot verbalise. Assesses 6 parameters: Vocalization, Facial Expression, Body Language, Behavioral Change, Physiological Change, Physical Changes. Total score determines pain severity (0-2 No pain, 3-7 Mild, 8-13 Moderate, 14+ Severe)."
* ^url = "https://fhir.clinyq.ai/StructureDefinition/onc-abbey-pain-scale"
* ^version = "0.1.0"
* ^status = #draft
* category = http://terminology.hl7.org/CodeSystem/observation-category#exam
* code = ONCObservationCodes#abbey-score
* value[x] only Quantity
* valueQuantity 1..1 MS
* valueQuantity.unit = "{score}"
* valueQuantity.system = "http://unitsofmeasure.org"
* valueQuantity ^short = "Abbey Pain Total Score"
* component 0..* MS
* component ^slicing.discriminator.type = #pattern
* component ^slicing.discriminator.path = "code"
* component ^slicing.ordered = false
* component ^slicing.rules = #open
* component contains 
    vocalization 0..1 MS and 
    facialExpression 0..1 MS and 
    bodyLanguage 0..1 MS and 
    behavioralChange 0..1 MS and 
    physiologicalChange 0..1 MS and 
    physicalChanges 0..1 MS

* component[vocalization].code = ONCObservationCodes#abbey-vocalization
* component[vocalization].value[x] only integer
* component[vocalization].valueInteger 1..1 MS
* component[vocalization].valueInteger ^short = "Score (0=Absent, 1=Mild, 2=Moderate, 3=Severe)"

* component[facialExpression].code = ONCObservationCodes#abbey-facial-expression
* component[facialExpression].value[x] only integer
* component[facialExpression].valueInteger 1..1 MS

* component[bodyLanguage].code = ONCObservationCodes#abbey-body-language
* component[bodyLanguage].value[x] only integer
* component[bodyLanguage].valueInteger 1..1 MS

* component[behavioralChange].code = ONCObservationCodes#abbey-behavioral-change
* component[behavioralChange].value[x] only integer
* component[behavioralChange].valueInteger 1..1 MS

* component[physiologicalChange].code = ONCObservationCodes#abbey-psychological-change
* component[physiologicalChange].value[x] only integer
* component[physiologicalChange].valueInteger 1..1 MS

* component[physicalChanges].code = ONCObservationCodes#abbey-physical-changes
* component[physicalChanges].value[x] only integer
* component[physicalChanges].valueInteger 1..1 MS
