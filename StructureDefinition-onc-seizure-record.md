# Seizure Record - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Seizure Record**

## Resource Profile: Seizure Record 

| | |
| :--- | :--- |
| *Official URL*:https://fhir.clinyq.ai/StructureDefinition/onc-seizure-record | *Version*:0.1.0 |
| Draft as of 2026-01-03 | *Computable Name*:ONCSeizureRecord |

 
Record of a specific seizure event, including type, duration, triggers, and recovery phases. Essential for epilepsy management and identifying patterns. 

**Usages:**

* Examples for this Profile: [Observation/example-seizure-record](Observation-example-seizure-record.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/onc.ig|current/StructureDefinition/onc-seizure-record)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-onc-seizure-record.csv), [Excel](StructureDefinition-onc-seizure-record.xlsx), [Schematron](StructureDefinition-onc-seizure-record.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "onc-seizure-record",
  "url" : "https://fhir.clinyq.ai/StructureDefinition/onc-seizure-record",
  "version" : "0.1.0",
  "name" : "ONCSeizureRecord",
  "title" : "Seizure Record",
  "status" : "draft",
  "date" : "2026-01-03T01:26:42+00:00",
  "publisher" : "The Open Nursing Community",
  "description" : "Record of a specific seizure event, including type, duration, triggers, and recovery phases. Essential for epilepsy management and identifying patterns.",
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
              "code" : "seizure-record"
            }
          ]
        }
      },
      {
        "id" : "Observation.value[x]",
        "path" : "Observation.value[x]",
        "short" : "Description of the event",
        "type" : [
          {
            "code" : "string"
          }
        ]
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
        "id" : "Observation.component:type",
        "path" : "Observation.component",
        "sliceName" : "type",
        "min" : 0,
        "max" : "1",
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:type.code",
        "path" : "Observation.component.code",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
              "code" : "seizure-type"
            }
          ]
        }
      },
      {
        "id" : "Observation.component:type.value[x]",
        "path" : "Observation.component.value[x]",
        "type" : [
          {
            "code" : "string"
          }
        ]
      },
      {
        "id" : "Observation.component:duration",
        "path" : "Observation.component",
        "sliceName" : "duration",
        "min" : 0,
        "max" : "1",
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:duration.code",
        "path" : "Observation.component.code",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
              "code" : "seizure-duration"
            }
          ]
        }
      },
      {
        "id" : "Observation.component:duration.value[x]",
        "path" : "Observation.component.value[x]",
        "type" : [
          {
            "code" : "Quantity"
          }
        ]
      },
      {
        "id" : "Observation.component:duration.value[x].unit",
        "path" : "Observation.component.value[x].unit",
        "patternString" : "min"
      },
      {
        "id" : "Observation.component:duration.value[x].system",
        "path" : "Observation.component.value[x].system",
        "patternUri" : "http://unitsofmeasure.org"
      },
      {
        "id" : "Observation.component:duration.value[x].code",
        "path" : "Observation.component.value[x].code",
        "patternCode" : "min"
      },
      {
        "id" : "Observation.component:recovery",
        "path" : "Observation.component",
        "sliceName" : "recovery",
        "min" : 0,
        "max" : "1",
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:recovery.code",
        "path" : "Observation.component.code",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
              "code" : "seizure-recovery"
            }
          ]
        }
      },
      {
        "id" : "Observation.component:recovery.value[x]",
        "path" : "Observation.component.value[x]",
        "type" : [
          {
            "code" : "string"
          }
        ]
      },
      {
        "id" : "Observation.component:trigger",
        "path" : "Observation.component",
        "sliceName" : "trigger",
        "min" : 0,
        "max" : "1",
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:trigger.code",
        "path" : "Observation.component.code",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
              "code" : "seizure-trigger"
            }
          ]
        }
      },
      {
        "id" : "Observation.component:trigger.value[x]",
        "path" : "Observation.component.value[x]",
        "type" : [
          {
            "code" : "string"
          }
        ]
      }
    ]
  }
}

```
