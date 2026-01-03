# Braden Scale Assessment - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Braden Scale Assessment**

## Resource Profile: Braden Scale Assessment 

| | |
| :--- | :--- |
| *Official URL*:https://opennursingcoreig.com/StructureDefinition/onc-braden-scale-assessment | *Version*:0.1.0 |
| Draft as of 2026-01-03 | *Computable Name*:ONCBradenScaleAssessment |

 
A profile for the Braden Scale pressure ulcer risk assessment 

**Usages:**

* Examples for this Profile: [Observation/observation-braden-scale](Observation-observation-braden-scale.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/onc.ig|current/StructureDefinition/onc-braden-scale-assessment)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-onc-braden-scale-assessment.csv), [Excel](StructureDefinition-onc-braden-scale-assessment.xlsx), [Schematron](StructureDefinition-onc-braden-scale-assessment.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "onc-braden-scale-assessment",
  "url" : "https://opennursingcoreig.com/StructureDefinition/onc-braden-scale-assessment",
  "version" : "0.1.0",
  "name" : "ONCBradenScaleAssessment",
  "title" : "Braden Scale Assessment",
  "status" : "draft",
  "date" : "2026-01-03T01:44:04+00:00",
  "publisher" : "The Open Nursing Community",
  "description" : "A profile for the Braden Scale pressure ulcer risk assessment",
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
            "source" : "https://opennursingcoreig.com/StructureDefinition/onc-braden-scale-assessment"
          }
        ]
      },
      {
        "id" : "Observation.status",
        "path" : "Observation.status",
        "patternCode" : "final",
        "mustSupport" : true
      },
      {
        "id" : "Observation.code",
        "path" : "Observation.code",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
              "code" : "braden-total-score",
              "display" : "Braden Total Score"
            }
          ]
        },
        "mustSupport" : true
      },
      {
        "id" : "Observation.value[x]",
        "path" : "Observation.value[x]",
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
        "id" : "Observation.value[x].code",
        "path" : "Observation.value[x].code",
        "patternCode" : "1"
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
        "min" : 6,
        "max" : "6",
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:sensoryPerception",
        "path" : "Observation.component",
        "sliceName" : "sensoryPerception",
        "min" : 1,
        "max" : "1",
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:sensoryPerception.code",
        "path" : "Observation.component.code",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
              "code" : "braden-sensory",
              "display" : "Braden Sensory Perception"
            }
          ]
        }
      },
      {
        "id" : "Observation.component:sensoryPerception.value[x]",
        "path" : "Observation.component.value[x]",
        "type" : [
          {
            "code" : "Quantity"
          }
        ]
      },
      {
        "id" : "Observation.component:moisture",
        "path" : "Observation.component",
        "sliceName" : "moisture",
        "min" : 1,
        "max" : "1",
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:moisture.code",
        "path" : "Observation.component.code",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
              "code" : "braden-moisture",
              "display" : "Braden Moisture"
            }
          ]
        }
      },
      {
        "id" : "Observation.component:moisture.value[x]",
        "path" : "Observation.component.value[x]",
        "type" : [
          {
            "code" : "Quantity"
          }
        ]
      },
      {
        "id" : "Observation.component:activity",
        "path" : "Observation.component",
        "sliceName" : "activity",
        "min" : 1,
        "max" : "1",
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:activity.code",
        "path" : "Observation.component.code",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
              "code" : "braden-activity",
              "display" : "Braden Activity"
            }
          ]
        }
      },
      {
        "id" : "Observation.component:activity.value[x]",
        "path" : "Observation.component.value[x]",
        "type" : [
          {
            "code" : "Quantity"
          }
        ]
      },
      {
        "id" : "Observation.component:mobility",
        "path" : "Observation.component",
        "sliceName" : "mobility",
        "min" : 1,
        "max" : "1",
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:mobility.code",
        "path" : "Observation.component.code",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
              "code" : "braden-mobility",
              "display" : "Braden Mobility"
            }
          ]
        }
      },
      {
        "id" : "Observation.component:mobility.value[x]",
        "path" : "Observation.component.value[x]",
        "type" : [
          {
            "code" : "Quantity"
          }
        ]
      },
      {
        "id" : "Observation.component:nutrition",
        "path" : "Observation.component",
        "sliceName" : "nutrition",
        "min" : 1,
        "max" : "1",
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:nutrition.code",
        "path" : "Observation.component.code",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
              "code" : "braden-nutrition",
              "display" : "Braden Nutrition"
            }
          ]
        }
      },
      {
        "id" : "Observation.component:nutrition.value[x]",
        "path" : "Observation.component.value[x]",
        "type" : [
          {
            "code" : "Quantity"
          }
        ]
      },
      {
        "id" : "Observation.component:frictionAndShear",
        "path" : "Observation.component",
        "sliceName" : "frictionAndShear",
        "min" : 1,
        "max" : "1",
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:frictionAndShear.code",
        "path" : "Observation.component.code",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
              "code" : "braden-friction",
              "display" : "Braden Friction/Shear"
            }
          ]
        }
      },
      {
        "id" : "Observation.component:frictionAndShear.value[x]",
        "path" : "Observation.component.value[x]",
        "type" : [
          {
            "code" : "Quantity"
          }
        ]
      }
    ]
  }
}

```
