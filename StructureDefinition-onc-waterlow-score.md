# Waterlow Score - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Waterlow Score**

## Resource Profile: Waterlow Score 

| | |
| :--- | :--- |
| *Official URL*:https://opennursingcoreig.com/StructureDefinition/onc-waterlow-score | *Version*:0.1.0 |
| Draft as of 2026-01-03 | *Computable Name*:ONCWaterlowScore |

 
Waterlow Pressure Ulcer Risk Assessment - NHS standard tool. Score ≥10 indicates at risk, ≥15 high risk, ≥20 very high risk. 

**Usages:**

* This Profile is not used by any profiles in this Implementation Guide

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/onc.ig|current/StructureDefinition/onc-waterlow-score)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-onc-waterlow-score.csv), [Excel](StructureDefinition-onc-waterlow-score.xlsx), [Schematron](StructureDefinition-onc-waterlow-score.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "onc-waterlow-score",
  "url" : "https://opennursingcoreig.com/StructureDefinition/onc-waterlow-score",
  "version" : "0.1.0",
  "name" : "ONCWaterlowScore",
  "title" : "Waterlow Score",
  "status" : "draft",
  "date" : "2026-01-03T00:34:03+00:00",
  "publisher" : "The Open Nursing Community",
  "description" : "Waterlow Pressure Ulcer Risk Assessment - NHS standard tool. Score ≥10 indicates at risk, ≥15 high risk, ≥20 very high risk.",
  "fhirVersion" : "4.0.1",
  "mapping" : [
    {
      "identity" : "workflow",
      "uri" : "http://hl7.org/fhir/workflow",
      "name" : "Workflow Pattern"
    },
    {
      "identity" : "sct-concept",
      "uri" : "http://snomed.info/conceptdomain",
      "name" : "SNOMED CT Concept Domain Binding"
    },
    {
      "identity" : "v2",
      "uri" : "http://hl7.org/v2",
      "name" : "HL7 v2 Mapping"
    },
    {
      "identity" : "rim",
      "uri" : "http://hl7.org/v3",
      "name" : "RIM Mapping"
    },
    {
      "identity" : "w5",
      "uri" : "http://hl7.org/fhir/fivews",
      "name" : "FiveWs Pattern Mapping"
    },
    {
      "identity" : "sct-attr",
      "uri" : "http://snomed.org/attributebinding",
      "name" : "SNOMED CT Attribute Binding"
    }
  ],
  "kind" : "resource",
  "abstract" : false,
  "type" : "Observation",
  "baseDefinition" : "https://opennursingcoreig.com/StructureDefinition/onc-nursing-assessment",
  "derivation" : "constraint",
  "differential" : {
    "element" : [
      {
        "id" : "Observation",
        "path" : "Observation",
        "constraint" : [
          {
            "key" : "onc-equity-gate-1",
            "severity" : "error",
            "human" : "Clinical safety rule: Skin observations (pressure ulcers, wounds) MUST include a Skin Tone assessment to ensure equitable care thresholds.",
            "expression" : "hasMember.resolve().code.coding.where(code = '66555-4' or code = 'mst-score').exists()",
            "source" : "https://opennursingcoreig.com/StructureDefinition/onc-waterlow-score"
          }
        ]
      },
      {
        "id" : "Observation.status",
        "path" : "Observation.status",
        "mustSupport" : true
      },
      {
        "id" : "Observation.code",
        "path" : "Observation.code",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
              "code" : "waterlow-score",
              "display" : "Waterlow Score"
            }
          ]
        },
        "mustSupport" : true
      },
      {
        "id" : "Observation.value[x]",
        "path" : "Observation.value[x]",
        "short" : "Waterlow total score (0-64+, higher = higher risk)",
        "type" : [
          {
            "code" : "Quantity"
          }
        ]
      },
      {
        "id" : "Observation.value[x].value",
        "path" : "Observation.value[x].value",
        "constraint" : [
          {
            "key" : "waterlow-range",
            "severity" : "error",
            "human" : "Waterlow score must be 0 or greater",
            "expression" : "$this >= 0",
            "source" : "https://opennursingcoreig.com/StructureDefinition/onc-waterlow-score"
          }
        ]
      },
      {
        "id" : "Observation.value[x].unit",
        "path" : "Observation.value[x].unit",
        "patternString" : "{score}"
      },
      {
        "id" : "Observation.value[x].system",
        "path" : "Observation.value[x].system",
        "patternUri" : "http://unitsofmeasure.org"
      },
      {
        "id" : "Observation.hasMember",
        "path" : "Observation.hasMember",
        "slicing" : {
          "discriminator" : [
            {
              "type" : "pattern",
              "path" : "resolve().code"
            }
          ],
          "rules" : "open"
        },
        "min" : 1,
        "mustSupport" : true
      },
      {
        "id" : "Observation.hasMember:skinTone",
        "path" : "Observation.hasMember",
        "sliceName" : "skinTone",
        "short" : "Mandatory Skin Tone Context (Equity Gate)",
        "min" : 1,
        "max" : "1",
        "type" : [
          {
            "code" : "Reference",
            "targetProfile" : [
              "https://opennursingcoreig.com/StructureDefinition/onc-skintone-observation",
              "https://opennursingcoreig.com/StructureDefinition/onc-monk-skintone-observation"
            ]
          }
        ],
        "mustSupport" : true
      },
      {
        "id" : "Observation.component",
        "path" : "Observation.component",
        "short" : "Risk factor components (build, skin type, age, continence, mobility, appetite, special risks)",
        "mustSupport" : true
      }
    ]
  }
}

```
