# Barthel Index - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Barthel Index**

## Resource Profile: Barthel Index 

| | |
| :--- | :--- |
| *Official URL*:https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/onc-barthel-index | *Version*:0.1.0 |
| Draft as of 2025-12-26 | *Computable Name*:ONCBarthelIndex |

 
Barthel Index for measuring independence in activities of daily living (ADL). Score 0-20=total dependency, 91-99=slight dependency, 100=independent. Total range 0-100. 

**Usages:**

* This Profile is not used by any profiles in this Implementation Guide

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/onc.ig|current/StructureDefinition/onc-barthel-index)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-onc-barthel-index.csv), [Excel](StructureDefinition-onc-barthel-index.xlsx), [Schematron](StructureDefinition-onc-barthel-index.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "onc-barthel-index",
  "url" : "https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/onc-barthel-index",
  "version" : "0.1.0",
  "name" : "ONCBarthelIndex",
  "title" : "Barthel Index",
  "status" : "draft",
  "date" : "2025-12-26T15:08:13+00:00",
  "description" : "Barthel Index for measuring independence in activities of daily living (ADL). Score 0-20=total dependency, 91-99=slight dependency, 100=independent. Total range 0-100.",
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
              "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
              "code" : "barthel-score",
              "display" : "Barthel Index Score"
            }
          ]
        },
        "mustSupport" : true
      },
      {
        "id" : "Observation.value[x]",
        "path" : "Observation.value[x]",
        "short" : "Barthel Index total (0-100)",
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
            "key" : "barthel-range",
            "severity" : "error",
            "human" : "Barthel Index must be between 0 and 100",
            "expression" : "$this >= 0 and $this <= 100",
            "source" : "https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/onc-barthel-index"
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
