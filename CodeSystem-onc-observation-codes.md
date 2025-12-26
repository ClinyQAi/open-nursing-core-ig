# ONC Observation Codes - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **ONC Observation Codes**

## CodeSystem: ONC Observation Codes 

| | |
| :--- | :--- |
| *Official URL*:https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes | *Version*:0.1.0 |
| Draft as of 2025-12-26 | *Computable Name*:ONCObservationCodes |

 
Custom observation codes for Open Nursing Core 

 This Code system is referenced in the content logical definition of the following value sets: 

* [NEWS2CodeValueSet](ValueSet-news2-code-vs.md)
* [NEWS2SubscoreCodeValueSet](ValueSet-news2-subscore-code-vs.md)
* [NursingProblemValueSet](ValueSet-nursing-problem-valueset.md)
* [SkinToneVS](ValueSet-skintone-vs.md)
* [WoundStageValueSet](ValueSet-wound-stage-vs.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "onc-observation-codes",
  "url" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
  "version" : "0.1.0",
  "name" : "ONCObservationCodes",
  "title" : "ONC Observation Codes",
  "status" : "draft",
  "date" : "2025-12-26T14:28:37+00:00",
  "description" : "Custom observation codes for Open Nursing Core",
  "content" : "complete",
  "count" : 30,
  "concept" : [
    {
      "code" : "mst-score",
      "display" : "Monk Skin Tone Score",
      "definition" : "Assessment of skin tone using the Monk Skin Tone Scale"
    },
    {
      "code" : "waterlow-score",
      "display" : "Waterlow Score",
      "definition" : "Total score for Waterlow pressure ulcer risk assessment"
    },
    {
      "code" : "must-score",
      "display" : "MUST Score",
      "definition" : "Malnutrition Universal Screening Tool total score"
    },
    {
      "code" : "must-bmi-score",
      "display" : "MUST BMI Score",
      "definition" : "Malnutrition Universal Screening Tool BMI score"
    },
    {
      "code" : "must-weight-loss-score",
      "display" : "MUST Weight Loss Score",
      "definition" : "Malnutrition Universal Screening Tool weight loss score"
    },
    {
      "code" : "must-acute-disease-score",
      "display" : "MUST Acute Disease Score",
      "definition" : "Malnutrition Universal Screening Tool acute disease effect score"
    },
    {
      "code" : "braden-total-score",
      "display" : "Braden Total Score",
      "definition" : "Braden scale total score"
    },
    {
      "code" : "braden-sensory",
      "display" : "Braden Sensory Perception",
      "definition" : "Sensory perception Braden scale"
    },
    {
      "code" : "braden-moisture",
      "display" : "Braden Moisture",
      "definition" : "Moisture Braden scale"
    },
    {
      "code" : "braden-activity",
      "display" : "Braden Activity",
      "definition" : "Activity Braden scale"
    },
    {
      "code" : "braden-mobility",
      "display" : "Braden Mobility",
      "definition" : "Mobility Braden scale"
    },
    {
      "code" : "braden-nutrition",
      "display" : "Braden Nutrition",
      "definition" : "Nutrition Braden scale"
    },
    {
      "code" : "braden-friction",
      "display" : "Braden Friction/Shear",
      "definition" : "Friction and shear Braden scale"
    },
    {
      "code" : "barthel-score",
      "display" : "Barthel Index Score",
      "definition" : "Total score for Barthel Index assessment"
    },
    {
      "code" : "news2-score",
      "display" : "NEWS2 Score",
      "definition" : "National Early Warning Score 2 Total Score"
    },
    {
      "code" : "news2-subscore",
      "display" : "NEWS2 Sub-score",
      "definition" : "Sub-score for NEWS2 parameter"
    },
    {
      "code" : "wound-stage",
      "display" : "Wound Stage",
      "definition" : "Stage of the wound"
    },
    {
      "code" : "stage-1",
      "display" : "Stage 1",
      "definition" : "Stage 1 pressure ulcer"
    },
    {
      "code" : "stage-2",
      "display" : "Stage 2",
      "definition" : "Stage 2 pressure ulcer"
    },
    {
      "code" : "stage-3",
      "display" : "Stage 3",
      "definition" : "Stage 3 pressure ulcer"
    },
    {
      "code" : "stage-4",
      "display" : "Stage 4",
      "definition" : "Stage 4 pressure ulcer"
    },
    {
      "code" : "unstageable",
      "display" : "Unstageable",
      "definition" : "Unstageable pressure ulcer"
    },
    {
      "code" : "deep-tissue",
      "display" : "Deep Tissue Injury",
      "definition" : "Deep tissue injury"
    },
    {
      "code" : "risk-falls",
      "display" : "Risk of Falls",
      "definition" : "Risk of falls diagnosis"
    },
    {
      "code" : "fitzpatrick-1",
      "display" : "Type I",
      "definition" : "Pale white; always burns, never tans"
    },
    {
      "code" : "fitzpatrick-2",
      "display" : "Type II",
      "definition" : "White; usually burns, tans with difficulty"
    },
    {
      "code" : "fitzpatrick-3",
      "display" : "Type III",
      "definition" : "Cream white; sometimes mild burn, gradually tans"
    },
    {
      "code" : "fitzpatrick-4",
      "display" : "Type IV",
      "definition" : "Moderate brown; rarely burns, tans with ease"
    },
    {
      "code" : "fitzpatrick-5",
      "display" : "Type V",
      "definition" : "Dark brown; very rarely burns, tans very easily"
    },
    {
      "code" : "fitzpatrick-6",
      "display" : "Type VI",
      "definition" : "Deeply pigmented dark brown to black; never burns, tans very easily"
    }
  ]
}

```
