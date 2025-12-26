# Morse Fall Scale - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Morse Fall Scale**

## Resource Profile: Morse Fall Scale 

| | |
| :--- | :--- |
| *Official URL*:https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/onc-morse-fall-scale | *Version*:1.0.0 |
| Active as of 2025-12-26 | *Computable Name*:ONCMorseFallScale |

 
Morse Fall Scale for assessing fall risk. Score 0-24=no risk, 25-50=low risk, ≥51=high risk. Total range 0-125. 

**Usages:**

* This Profile is not used by any profiles in this Implementation Guide

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/onc.ig|current/StructureDefinition/onc-morse-fall-scale)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-onc-morse-fall-scale.csv), [Excel](StructureDefinition-onc-morse-fall-scale.xlsx), [Schematron](StructureDefinition-onc-morse-fall-scale.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "onc-morse-fall-scale",
  "url" : "https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/onc-morse-fall-scale",
  "version" : "1.0.0",
  "name" : "ONCMorseFallScale",
  "title" : "Morse Fall Scale",
  "status" : "active",
  "date" : "2025-12-26T11:27:38+00:00",
  "description" : "Morse Fall Scale for assessing fall risk. Score 0-24=no risk, 25-50=low risk, ≥51=high risk. Total range 0-125.",
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
              "code" : "73830-2",
              "display" : "Morse Fall Scale panel"
            }
          ]
        },
        "mustSupport" : true
      },
      {
        "id" : "Observation.value[x]",
        "path" : "Observation.value[x]",
        "short" : "Morse Fall Scale total (0-125)",
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
            "key" : "morse-range",
            "severity" : "error",
            "human" : "Morse Fall Scale must be between 0 and 125",
            "expression" : "$this >= 0 and $this <= 125",
            "source" : "https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/onc-morse-fall-scale"
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
