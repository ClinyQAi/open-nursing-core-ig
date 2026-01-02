# Abbey Pain Scale - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Abbey Pain Scale**

## Resource Profile: Abbey Pain Scale 

| | |
| :--- | :--- |
| *Official URL*:https://fhir.clinyq.ai/StructureDefinition/onc-abbey-pain-scale | *Version*:0.1.0 |
| Draft as of 2026-01-02 | *Computable Name*:ONCAbbeyPainScale |

 
Pain assessment for people with dementia or who cannot verbalise. Assesses 6 parameters: Vocalization, Facial Expression, Body Language, Behavioral Change, Physiological Change, Physical Changes. Total score determines pain severity (0-2 No pain, 3-7 Mild, 8-13 Moderate, 14+ Severe). 

**Usages:**

* Examples for this Profile: [Observation/example-abbey-pain](Observation-example-abbey-pain.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/onc.ig|current/StructureDefinition/onc-abbey-pain-scale)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-onc-abbey-pain-scale.csv), [Excel](StructureDefinition-onc-abbey-pain-scale.xlsx), [Schematron](StructureDefinition-onc-abbey-pain-scale.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "onc-abbey-pain-scale",
  "url" : "https://fhir.clinyq.ai/StructureDefinition/onc-abbey-pain-scale",
  "version" : "0.1.0",
  "name" : "ONCAbbeyPainScale",
  "title" : "Abbey Pain Scale",
  "status" : "draft",
  "date" : "2026-01-02T23:43:46+00:00",
  "publisher" : "The Open Nursing Community",
  "description" : "Pain assessment for people with dementia or who cannot verbalise. Assesses 6 parameters: Vocalization, Facial Expression, Body Language, Behavioral Change, Physiological Change, Physical Changes. Total score determines pain severity (0-2 No pain, 3-7 Mild, 8-13 Moderate, 14+ Severe).",
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
        "id" : "Observation.category",
        "path" : "Observation.category",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "http://terminology.hl7.org/CodeSystem/observation-category",
              "code" : "exam"
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
              "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
              "code" : "abbey-score"
            }
          ]
        }
      },
      {
        "id" : "Observation.value[x]",
        "path" : "Observation.value[x]",
        "short" : "Abbey Pain Total Score",
        "type" : [
          {
            "code" : "Quantity"
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
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:vocalization",
        "path" : "Observation.component",
        "sliceName" : "vocalization",
        "min" : 0,
        "max" : "1",
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:vocalization.code",
        "path" : "Observation.component.code",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
              "code" : "abbey-vocalization"
            }
          ]
        }
      },
      {
        "id" : "Observation.component:vocalization.value[x]",
        "path" : "Observation.component.value[x]",
        "short" : "Score (0=Absent, 1=Mild, 2=Moderate, 3=Severe)",
        "min" : 1,
        "type" : [
          {
            "code" : "integer"
          }
        ],
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:facialExpression",
        "path" : "Observation.component",
        "sliceName" : "facialExpression",
        "min" : 0,
        "max" : "1",
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:facialExpression.code",
        "path" : "Observation.component.code",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
              "code" : "abbey-facial-expression"
            }
          ]
        }
      },
      {
        "id" : "Observation.component:facialExpression.value[x]",
        "path" : "Observation.component.value[x]",
        "min" : 1,
        "type" : [
          {
            "code" : "integer"
          }
        ],
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:bodyLanguage",
        "path" : "Observation.component",
        "sliceName" : "bodyLanguage",
        "min" : 0,
        "max" : "1",
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:bodyLanguage.code",
        "path" : "Observation.component.code",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
              "code" : "abbey-body-language"
            }
          ]
        }
      },
      {
        "id" : "Observation.component:bodyLanguage.value[x]",
        "path" : "Observation.component.value[x]",
        "min" : 1,
        "type" : [
          {
            "code" : "integer"
          }
        ],
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:behavioralChange",
        "path" : "Observation.component",
        "sliceName" : "behavioralChange",
        "min" : 0,
        "max" : "1",
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:behavioralChange.code",
        "path" : "Observation.component.code",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
              "code" : "abbey-behavioral-change"
            }
          ]
        }
      },
      {
        "id" : "Observation.component:behavioralChange.value[x]",
        "path" : "Observation.component.value[x]",
        "min" : 1,
        "type" : [
          {
            "code" : "integer"
          }
        ],
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:physiologicalChange",
        "path" : "Observation.component",
        "sliceName" : "physiologicalChange",
        "min" : 0,
        "max" : "1",
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:physiologicalChange.code",
        "path" : "Observation.component.code",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
              "code" : "abbey-psychological-change"
            }
          ]
        }
      },
      {
        "id" : "Observation.component:physiologicalChange.value[x]",
        "path" : "Observation.component.value[x]",
        "min" : 1,
        "type" : [
          {
            "code" : "integer"
          }
        ],
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:physicalChanges",
        "path" : "Observation.component",
        "sliceName" : "physicalChanges",
        "min" : 0,
        "max" : "1",
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:physicalChanges.code",
        "path" : "Observation.component.code",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
              "code" : "abbey-physical-changes"
            }
          ]
        }
      },
      {
        "id" : "Observation.component:physicalChanges.value[x]",
        "path" : "Observation.component.value[x]",
        "min" : 1,
        "type" : [
          {
            "code" : "integer"
          }
        ],
        "mustSupport" : true
      }
    ]
  }
}

```
