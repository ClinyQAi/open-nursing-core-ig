# Mini Mental State Examination (MMSE) - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Mini Mental State Examination (MMSE)**

## Resource Profile: Mini Mental State Examination (MMSE) 

| | |
| :--- | :--- |
| *Official URL*:https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/onc-mmse | *Version*:1.0.0 |
| Active as of 2025-12-26 | *Computable Name*:ONCMMSE |

 
Mini Mental State Examination for cognitive function screening. Score 24-30=no impairment, 18-23=mild, 0-17=severe. Total range 0-30. 

**Usages:**

* This Profile is not used by any profiles in this Implementation Guide

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/onc.ig|current/StructureDefinition/onc-mmse)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-onc-mmse.csv), [Excel](StructureDefinition-onc-mmse.xlsx), [Schematron](StructureDefinition-onc-mmse.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "onc-mmse",
  "url" : "https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/onc-mmse",
  "version" : "1.0.0",
  "name" : "ONCMMSE",
  "title" : "Mini Mental State Examination (MMSE)",
  "status" : "active",
  "date" : "2025-12-26T10:16:19+00:00",
  "description" : "Mini Mental State Examination for cognitive function screening. Score 24-30=no impairment, 18-23=mild, 0-17=severe. Total range 0-30.",
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
              "system" : "http://loinc.org",
              "code" : "72106-8",
              "display" : "Mini-Mental State Examination (MMSE)"
            }
          ]
        },
        "mustSupport" : true
      },
      {
        "id" : "Observation.value[x]",
        "path" : "Observation.value[x]",
        "short" : "MMSE total score (0-30)",
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
            "key" : "mmse-range",
            "severity" : "error",
            "human" : "MMSE score must be between 0 and 30",
            "expression" : "$this >= 0 and $this <= 30",
            "source" : "https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/onc-mmse"
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
      }
    ]
  }
}

```
