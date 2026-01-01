# 4AT Delirium Assessment - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **4AT Delirium Assessment**

## Resource Profile: 4AT Delirium Assessment 

| | |
| :--- | :--- |
| *Official URL*:https://fhir.clinyq.ai/StructureDefinition/onc-4at-delirium | *Version*:0.1.0 |
| Draft as of 2026-01-01 | *Computable Name*:ONC4ATDelirium |

 
Rapid clinical test for delirium (4AT) comprising Alertness, AMT4, Attention, and Acute Change/Fluctuating Course. A total score of 4 or more suggests possible delirium. 

**Usages:**

* Examples for this Profile: [Observation/example-4at-delirium](Observation-example-4at-delirium.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/onc.ig|current/StructureDefinition/onc-4at-delirium)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-onc-4at-delirium.csv), [Excel](StructureDefinition-onc-4at-delirium.xlsx), [Schematron](StructureDefinition-onc-4at-delirium.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "onc-4at-delirium",
  "url" : "https://fhir.clinyq.ai/StructureDefinition/onc-4at-delirium",
  "version" : "0.1.0",
  "name" : "ONC4ATDelirium",
  "title" : "4AT Delirium Assessment",
  "status" : "draft",
  "date" : "2026-01-01T13:37:23+00:00",
  "description" : "Rapid clinical test for delirium (4AT) comprising Alertness, AMT4, Attention, and Acute Change/Fluctuating Course. A total score of 4 or more suggests possible delirium.",
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
        "id" : "Observation.category",
        "path" : "Observation.category",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "http://terminology.hl7.org/CodeSystem/observation-category",
              "code" : "survey"
            }
          ]
        }
      },
      {
        "id" : "Observation.code",
        "path" : "Observation.code",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
              "code" : "4at-score"
            }
          ]
        }
      },
      {
        "id" : "Observation.value[x]",
        "path" : "Observation.value[x]",
        "short" : "Total 4AT Score (0-12)",
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
            "key" : "score-range-4at",
            "severity" : "error",
            "human" : "4AT score must be between 0 and 12",
            "expression" : "$this >= 0 and $this <= 12",
            "source" : "https://fhir.clinyq.ai/StructureDefinition/onc-4at-delirium"
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
        "id" : "Observation.value[x].code",
        "path" : "Observation.value[x].code",
        "patternCode" : "1"
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
        "min" : 4,
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:alertness",
        "path" : "Observation.component",
        "sliceName" : "alertness",
        "min" : 1,
        "max" : "1",
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:alertness.code",
        "path" : "Observation.component.code",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
              "code" : "4at-alertness"
            }
          ]
        }
      },
      {
        "id" : "Observation.component:alertness.value[x]",
        "path" : "Observation.component.value[x]",
        "type" : [
          {
            "code" : "CodeableConcept"
          }
        ],
        "binding" : {
          "strength" : "required",
          "valueSet" : "https://clinyqai.github.io/open-nursing-core-ig/ValueSet/onc-4at-alertness-vs"
        }
      },
      {
        "id" : "Observation.component:amt4",
        "path" : "Observation.component",
        "sliceName" : "amt4",
        "min" : 1,
        "max" : "1",
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:amt4.code",
        "path" : "Observation.component.code",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
              "code" : "4at-amt4"
            }
          ]
        }
      },
      {
        "id" : "Observation.component:amt4.value[x]",
        "path" : "Observation.component.value[x]",
        "type" : [
          {
            "code" : "CodeableConcept"
          }
        ],
        "binding" : {
          "strength" : "required",
          "valueSet" : "https://clinyqai.github.io/open-nursing-core-ig/ValueSet/onc-4at-amt4-vs"
        }
      },
      {
        "id" : "Observation.component:attention",
        "path" : "Observation.component",
        "sliceName" : "attention",
        "min" : 1,
        "max" : "1",
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:attention.code",
        "path" : "Observation.component.code",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
              "code" : "4at-attention"
            }
          ]
        }
      },
      {
        "id" : "Observation.component:attention.value[x]",
        "path" : "Observation.component.value[x]",
        "type" : [
          {
            "code" : "CodeableConcept"
          }
        ],
        "binding" : {
          "strength" : "required",
          "valueSet" : "https://clinyqai.github.io/open-nursing-core-ig/ValueSet/onc-4at-attention-vs"
        }
      },
      {
        "id" : "Observation.component:acuteChange",
        "path" : "Observation.component",
        "sliceName" : "acuteChange",
        "min" : 1,
        "max" : "1",
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:acuteChange.code",
        "path" : "Observation.component.code",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
              "code" : "4at-acute-change"
            }
          ]
        }
      },
      {
        "id" : "Observation.component:acuteChange.value[x]",
        "path" : "Observation.component.value[x]",
        "type" : [
          {
            "code" : "CodeableConcept"
          }
        ],
        "binding" : {
          "strength" : "required",
          "valueSet" : "https://clinyqai.github.io/open-nursing-core-ig/ValueSet/onc-4at-acute-change-vs"
        }
      }
    ]
  }
}

```
