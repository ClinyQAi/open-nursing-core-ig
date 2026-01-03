# Relational Engagement Score - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Relational Engagement Score**

## Resource Profile: Relational Engagement Score 

| | |
| :--- | :--- |
| *Official URL*:https://fhir.clinyq.ai/StructureDefinition/onc-relational-observation | *Version*:0.1.0 |
| Draft as of 2026-01-03 | *Computable Name*:ONCRelationalObservation |

 
Assessment of the quality and depth of the nurse-patient relationship or engagement level. Supports the relational aspect of care. 

**Usages:**

* This Profile is not used by any profiles in this Implementation Guide

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/onc.ig|current/StructureDefinition/onc-relational-observation)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-onc-relational-observation.csv), [Excel](StructureDefinition-onc-relational-observation.xlsx), [Schematron](StructureDefinition-onc-relational-observation.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "onc-relational-observation",
  "url" : "https://fhir.clinyq.ai/StructureDefinition/onc-relational-observation",
  "version" : "0.1.0",
  "name" : "ONCRelationalObservation",
  "title" : "Relational Engagement Score",
  "status" : "draft",
  "date" : "2026-01-03T01:44:04+00:00",
  "publisher" : "The Open Nursing Community",
  "description" : "Assessment of the quality and depth of the nurse-patient relationship or engagement level. Supports the relational aspect of care.",
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
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Observation",
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
              "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
              "code" : "relational-engagement"
            }
          ]
        }
      },
      {
        "id" : "Observation.value[x]",
        "path" : "Observation.value[x]",
        "short" : "Engagement Level (1-5)",
        "min" : 1,
        "type" : [
          {
            "code" : "integer"
          }
        ],
        "constraint" : [
          {
            "key" : "engagement-range",
            "severity" : "error",
            "human" : "Engagement score must be between 1 (Low) and 5 (High)",
            "expression" : "$this >= 1 and $this <= 5",
            "source" : "https://fhir.clinyq.ai/StructureDefinition/onc-relational-observation"
          }
        ],
        "mustSupport" : true
      }
    ]
  }
}

```
