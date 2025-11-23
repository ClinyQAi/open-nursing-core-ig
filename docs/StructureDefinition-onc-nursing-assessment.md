# Open Nursing Core Assessment - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Open Nursing Core Assessment**

## Resource Profile: Open Nursing Core Assessment 

| | |
| :--- | :--- |
| *Official URL*:http://open-nursing-core.org/StructureDefinition/onc-nursing-assessment | *Version*:0.1.0 |
| Draft as of 2025-11-23 | *Computable Name*:ONCNursingAssessment |

 
Base profile for nursing assessments. 

**Usages:**

* Derived from this Profile: [Open Nursing Core Braden Scale Assessment](StructureDefinition-onc-braden-scale-assessment.md), [Open Nursing Core Goal Evaluation](StructureDefinition-onc-goal-evaluation.md), [ONC Housing Status Assessment](StructureDefinition-onc-housing-status.md), [ONC Morse Fall Scale Assessment](StructureDefinition-onc-morse-fall-scale.md) and [ONC NEWS2 Assessment](StructureDefinition-onc-news2-assessment.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/onc.ig|current/StructureDefinition/onc-nursing-assessment)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-onc-nursing-assessment.csv), [Excel](StructureDefinition-onc-nursing-assessment.xlsx), [Schematron](StructureDefinition-onc-nursing-assessment.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "onc-nursing-assessment",
  "url" : "http://open-nursing-core.org/StructureDefinition/onc-nursing-assessment",
  "version" : "0.1.0",
  "name" : "ONCNursingAssessment",
  "title" : "Open Nursing Core Assessment",
  "status" : "draft",
  "date" : "2025-11-23T22:00:06+00:00",
  "description" : "Base profile for nursing assessments.",
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
        "slicing" : {
          "discriminator" : [
            {
              "type" : "pattern",
              "path" : "coding"
            }
          ],
          "rules" : "open"
        },
        "min" : 1
      },
      {
        "id" : "Observation.category:nursing",
        "path" : "Observation.category",
        "sliceName" : "nursing",
        "min" : 1,
        "max" : "1",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "http://terminology.hl7.org/CodeSystem/observation-category",
              "code" : "nursing"
            }
          ]
        },
        "mustSupport" : true
      },
      {
        "id" : "Observation.performer",
        "path" : "Observation.performer",
        "min" : 1,
        "max" : "1",
        "type" : [
          {
            "code" : "Reference",
            "targetProfile" : [
              "http://hl7.org/fhir/StructureDefinition/Practitioner",
              "http://hl7.org/fhir/StructureDefinition/PractitionerRole"
            ]
          }
        ],
        "mustSupport" : true
      },
      {
        "id" : "Observation.value[x]",
        "path" : "Observation.value[x]",
        "min" : 1,
        "type" : [
          {
            "code" : "Quantity"
          },
          {
            "code" : "CodeableConcept"
          }
        ],
        "mustSupport" : true
      }
    ]
  }
}

```
