# Wound Assessment - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Wound Assessment**

## Resource Profile: Wound Assessment 

| | |
| :--- | :--- |
| *Official URL*:https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/onc-wound-assessment | *Version*:1.0.0 |
| Active as of 2025-12-26 | *Computable Name*:ONCWoundAssessment |

 
Comprehensive wound assessment including staging and dimensions 

**Usages:**

* This Profile is not used by any profiles in this Implementation Guide

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/onc.ig|current/StructureDefinition/onc-wound-assessment)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-onc-wound-assessment.csv), [Excel](StructureDefinition-onc-wound-assessment.xlsx), [Schematron](StructureDefinition-onc-wound-assessment.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "onc-wound-assessment",
  "url" : "https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/onc-wound-assessment",
  "version" : "1.0.0",
  "name" : "ONCWoundAssessment",
  "title" : "Wound Assessment",
  "status" : "active",
  "date" : "2025-12-26T12:02:28+00:00",
  "description" : "Comprehensive wound assessment including staging and dimensions",
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
              "code" : "399912005",
              "display" : "Pressure Ulcer"
            }
          ]
        },
        "mustSupport" : true
      },
      {
        "id" : "Observation.value[x]",
        "path" : "Observation.value[x]",
        "short" : "Wound stage",
        "type" : [
          {
            "code" : "CodeableConcept"
          }
        ],
        "binding" : {
          "strength" : "required",
          "valueSet" : "https://clinyqai.github.io/open-nursing-core-ig/ValueSet/wound-stage-vs"
        }
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
        "id" : "Observation.component:length",
        "path" : "Observation.component",
        "sliceName" : "length",
        "min" : 0,
        "max" : "1",
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:length.code",
        "path" : "Observation.component.code",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "http://snomed.info/sct",
              "code" : "410668003",
              "display" : "Length"
            }
          ]
        }
      },
      {
        "id" : "Observation.component:length.value[x]",
        "path" : "Observation.component.value[x]",
        "type" : [
          {
            "code" : "Quantity"
          }
        ]
      },
      {
        "id" : "Observation.component:length.value[x].value",
        "path" : "Observation.component.value[x].value",
        "constraint" : [
          {
            "key" : "positive-dimension",
            "severity" : "error",
            "human" : "Wound dimensions must be positive",
            "expression" : "$this > 0",
            "source" : "https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/onc-wound-assessment"
          }
        ]
      },
      {
        "id" : "Observation.component:length.value[x].unit",
        "path" : "Observation.component.value[x].unit",
        "patternString" : "cm"
      },
      {
        "id" : "Observation.component:length.value[x].system",
        "path" : "Observation.component.value[x].system",
        "patternUri" : "http://unitsofmeasure.org"
      },
      {
        "id" : "Observation.component:length.value[x].code",
        "path" : "Observation.component.value[x].code",
        "patternCode" : "cm"
      },
      {
        "id" : "Observation.component:width",
        "path" : "Observation.component",
        "sliceName" : "width",
        "min" : 0,
        "max" : "1",
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:width.code",
        "path" : "Observation.component.code",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "http://snomed.info/sct",
              "code" : "410669006",
              "display" : "Width"
            }
          ]
        }
      },
      {
        "id" : "Observation.component:width.value[x]",
        "path" : "Observation.component.value[x]",
        "type" : [
          {
            "code" : "Quantity"
          }
        ]
      },
      {
        "id" : "Observation.component:width.value[x].value",
        "path" : "Observation.component.value[x].value",
        "constraint" : [
          {
            "key" : "positive-dimension",
            "severity" : "error",
            "human" : "Wound dimensions must be positive",
            "expression" : "$this > 0",
            "source" : "https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/onc-wound-assessment"
          }
        ]
      },
      {
        "id" : "Observation.component:width.value[x].unit",
        "path" : "Observation.component.value[x].unit",
        "patternString" : "cm"
      },
      {
        "id" : "Observation.component:width.value[x].system",
        "path" : "Observation.component.value[x].system",
        "patternUri" : "http://unitsofmeasure.org"
      },
      {
        "id" : "Observation.component:width.value[x].code",
        "path" : "Observation.component.value[x].code",
        "patternCode" : "cm"
      },
      {
        "id" : "Observation.component:depth",
        "path" : "Observation.component",
        "sliceName" : "depth",
        "min" : 0,
        "max" : "1",
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:depth.code",
        "path" : "Observation.component.code",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "http://snomed.info/sct",
              "code" : "410670007",
              "display" : "Depth"
            }
          ]
        }
      },
      {
        "id" : "Observation.component:depth.value[x]",
        "path" : "Observation.component.value[x]",
        "type" : [
          {
            "code" : "Quantity"
          }
        ]
      },
      {
        "id" : "Observation.component:depth.value[x].value",
        "path" : "Observation.component.value[x].value",
        "constraint" : [
          {
            "key" : "positive-dimension",
            "severity" : "error",
            "human" : "Wound dimensions must be positive",
            "expression" : "$this > 0",
            "source" : "https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/onc-wound-assessment"
          }
        ]
      },
      {
        "id" : "Observation.component:depth.value[x].unit",
        "path" : "Observation.component.value[x].unit",
        "patternString" : "cm"
      },
      {
        "id" : "Observation.component:depth.value[x].system",
        "path" : "Observation.component.value[x].system",
        "patternUri" : "http://unitsofmeasure.org"
      },
      {
        "id" : "Observation.component:depth.value[x].code",
        "path" : "Observation.component.value[x].code",
        "patternCode" : "cm"
      }
    ]
  }
}

```
