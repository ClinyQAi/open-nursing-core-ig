# Bristol Stool Chart - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Bristol Stool Chart**

## Resource Profile: Bristol Stool Chart 

| | |
| :--- | :--- |
| *Official URL*:https://fhir.clinyq.ai/StructureDefinition/onc-bristol-stool-chart | *Version*:0.1.0 |
| Draft as of 2026-01-03 | *Computable Name*:ONCBristolStoolChart |

 
Assessment of stool form using the Bristol Stool Chart (Types 1-7). Gold standard for bowel function assessment. 

**Usages:**

* Examples for this Profile: [Observation/example-bristol-stool](Observation-example-bristol-stool.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/onc.ig|current/StructureDefinition/onc-bristol-stool-chart)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-onc-bristol-stool-chart.csv), [Excel](StructureDefinition-onc-bristol-stool-chart.xlsx), [Schematron](StructureDefinition-onc-bristol-stool-chart.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "onc-bristol-stool-chart",
  "url" : "https://fhir.clinyq.ai/StructureDefinition/onc-bristol-stool-chart",
  "version" : "0.1.0",
  "name" : "ONCBristolStoolChart",
  "title" : "Bristol Stool Chart",
  "status" : "draft",
  "date" : "2026-01-03T00:34:03+00:00",
  "publisher" : "The Open Nursing Community",
  "description" : "Assessment of stool form using the Bristol Stool Chart (Types 1-7). Gold standard for bowel function assessment.",
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
              "code" : "bristol-score"
            }
          ]
        }
      },
      {
        "id" : "Observation.value[x]",
        "path" : "Observation.value[x]",
        "short" : "Bristol Stool Type (1-7)",
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
            "key" : "bristol-range",
            "severity" : "error",
            "human" : "Bristol score must be between 1 and 7",
            "expression" : "$this >= 1 and $this <= 7",
            "source" : "https://fhir.clinyq.ai/StructureDefinition/onc-bristol-stool-chart"
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
        "id" : "Observation.note",
        "path" : "Observation.note",
        "short" : "Additional notes (e.g., colour, amount)",
        "mustSupport" : true
      }
    ]
  }
}

```
