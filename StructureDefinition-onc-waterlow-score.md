# Waterlow Score - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Waterlow Score**

## Resource Profile: Waterlow Score 

| | |
| :--- | :--- |
| *Official URL*:https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/onc-waterlow-score | *Version*:1.0.0 |
| Active as of 2025-12-26 | *Computable Name*:ONCWaterlowScore |

 
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
  "url" : "https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/onc-waterlow-score",
  "version" : "1.0.0",
  "name" : "ONCWaterlowScore",
  "title" : "Waterlow Score",
  "status" : "active",
  "date" : "2025-12-26T01:59:09+00:00",
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
  "baseDefinition" : "https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/onc-nursing-assessment",
  "derivation" : "constraint",
  "differential" : {
    "element" : [
      {
        "id" : "Observation",
        "path" : "Observation"
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
              "system" : "http://snomed.info/sct",
              "code" : "443846001",
              "display" : "Waterlow score (observable entity)"
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
            "source" : "https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/onc-waterlow-score"
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
        "id" : "Observation.component",
        "path" : "Observation.component",
        "short" : "Risk factor components (build, skin type, age, continence, mobility, appetite, special risks)",
        "mustSupport" : true
      }
    ]
  }
}

```
