# MUST Score (Malnutrition Universal Screening Tool) - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **MUST Score (Malnutrition Universal Screening Tool)**

## Resource Profile: MUST Score (Malnutrition Universal Screening Tool) 

| | |
| :--- | :--- |
| *Official URL*:https://opennursingcoreig.com/StructureDefinition/onc-must-score | *Version*:0.1.0 |
| Draft as of 2026-01-03 | *Computable Name*:ONCMUSTScore |

 
Malnutrition Universal Screening Tool for identifying adults at risk of malnutrition. Score 0=low risk, 1=medium risk, 2+=high risk. NHS-standard nutritional screening. 

**Usages:**

* This Profile is not used by any profiles in this Implementation Guide

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/onc.ig|current/StructureDefinition/onc-must-score)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-onc-must-score.csv), [Excel](StructureDefinition-onc-must-score.xlsx), [Schematron](StructureDefinition-onc-must-score.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "onc-must-score",
  "url" : "https://opennursingcoreig.com/StructureDefinition/onc-must-score",
  "version" : "0.1.0",
  "name" : "ONCMUSTScore",
  "title" : "MUST Score (Malnutrition Universal Screening Tool)",
  "status" : "draft",
  "date" : "2026-01-03T00:34:03+00:00",
  "publisher" : "The Open Nursing Community",
  "description" : "Malnutrition Universal Screening Tool for identifying adults at risk of malnutrition. Score 0=low risk, 1=medium risk, 2+=high risk. NHS-standard nutritional screening.",
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
              "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
              "code" : "must-score",
              "display" : "MUST Score"
            }
          ]
        },
        "mustSupport" : true
      },
      {
        "id" : "Observation.value[x]",
        "path" : "Observation.value[x]",
        "short" : "MUST total score (0-6, higher = higher risk)",
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
            "key" : "must-total-range",
            "severity" : "error",
            "human" : "MUST total score must be between 0 and 6",
            "expression" : "$this >= 0 and $this <= 6",
            "source" : "https://opennursingcoreig.com/StructureDefinition/onc-must-score"
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
        "slicing" : {
          "discriminator" : [
            {
              "type" : "pattern",
              "path" : "code"
            }
          ],
          "ordered" : false,
          "rules" : "open"
        },
        "min" : 3,
        "max" : "3",
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:bmi",
        "path" : "Observation.component",
        "sliceName" : "bmi",
        "min" : 1,
        "max" : "1",
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:bmi.code",
        "path" : "Observation.component.code",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
              "code" : "must-bmi-score",
              "display" : "MUST BMI Score"
            }
          ]
        }
      },
      {
        "id" : "Observation.component:bmi.value[x]",
        "path" : "Observation.component.value[x]",
        "type" : [
          {
            "code" : "Quantity"
          }
        ]
      },
      {
        "id" : "Observation.component:bmi.value[x].value",
        "path" : "Observation.component.value[x].value",
        "constraint" : [
          {
            "key" : "must-component-range",
            "severity" : "error",
            "human" : "MUST component scores must be between 0 and 2",
            "expression" : "$this >= 0 and $this <= 2",
            "source" : "https://opennursingcoreig.com/StructureDefinition/onc-must-score"
          }
        ]
      },
      {
        "id" : "Observation.component:bmi.value[x].unit",
        "path" : "Observation.component.value[x].unit",
        "patternString" : "{score}"
      },
      {
        "id" : "Observation.component:bmi.value[x].system",
        "path" : "Observation.component.value[x].system",
        "patternUri" : "http://unitsofmeasure.org"
      },
      {
        "id" : "Observation.component:weightLoss",
        "path" : "Observation.component",
        "sliceName" : "weightLoss",
        "min" : 1,
        "max" : "1",
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:weightLoss.code",
        "path" : "Observation.component.code",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
              "code" : "must-weight-loss-score",
              "display" : "MUST Weight Loss Score"
            }
          ]
        }
      },
      {
        "id" : "Observation.component:weightLoss.value[x]",
        "path" : "Observation.component.value[x]",
        "type" : [
          {
            "code" : "Quantity"
          }
        ]
      },
      {
        "id" : "Observation.component:weightLoss.value[x].value",
        "path" : "Observation.component.value[x].value",
        "constraint" : [
          {
            "key" : "must-component-range",
            "severity" : "error",
            "human" : "MUST component scores must be between 0 and 2",
            "expression" : "$this >= 0 and $this <= 2",
            "source" : "https://opennursingcoreig.com/StructureDefinition/onc-must-score"
          }
        ]
      },
      {
        "id" : "Observation.component:weightLoss.value[x].unit",
        "path" : "Observation.component.value[x].unit",
        "patternString" : "{score}"
      },
      {
        "id" : "Observation.component:weightLoss.value[x].system",
        "path" : "Observation.component.value[x].system",
        "patternUri" : "http://unitsofmeasure.org"
      },
      {
        "id" : "Observation.component:acuteDisease",
        "path" : "Observation.component",
        "sliceName" : "acuteDisease",
        "min" : 1,
        "max" : "1",
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:acuteDisease.code",
        "path" : "Observation.component.code",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
              "code" : "must-acute-disease-score",
              "display" : "MUST Acute Disease Score"
            }
          ]
        }
      },
      {
        "id" : "Observation.component:acuteDisease.value[x]",
        "path" : "Observation.component.value[x]",
        "type" : [
          {
            "code" : "Quantity"
          }
        ]
      },
      {
        "id" : "Observation.component:acuteDisease.value[x].value",
        "path" : "Observation.component.value[x].value",
        "constraint" : [
          {
            "key" : "must-component-range",
            "severity" : "error",
            "human" : "MUST component scores must be between 0 and 2",
            "expression" : "$this >= 0 and $this <= 2",
            "source" : "https://opennursingcoreig.com/StructureDefinition/onc-must-score"
          }
        ]
      },
      {
        "id" : "Observation.component:acuteDisease.value[x].unit",
        "path" : "Observation.component.value[x].unit",
        "patternString" : "{score}"
      },
      {
        "id" : "Observation.component:acuteDisease.value[x].system",
        "path" : "Observation.component.value[x].system",
        "patternUri" : "http://unitsofmeasure.org"
      }
    ]
  }
}

```
