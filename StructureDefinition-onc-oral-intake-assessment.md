# Oral Intake Assessment - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Oral Intake Assessment**

## Resource Profile: Oral Intake Assessment 

| | |
| :--- | :--- |
| *Official URL*:https://opennursingcoreig.com/StructureDefinition/onc-oral-intake-assessment | *Version*:0.1.0 |
| Draft as of 2026-01-03 | *Computable Name*:ONCOralIntakeAssessment |

 
Assessment of ability to take food and fluids orally. 

**Usages:**

* This Profile is not used by any profiles in this Implementation Guide

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/onc.ig|current/StructureDefinition/onc-oral-intake-assessment)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-onc-oral-intake-assessment.csv), [Excel](StructureDefinition-onc-oral-intake-assessment.xlsx), [Schematron](StructureDefinition-onc-oral-intake-assessment.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "onc-oral-intake-assessment",
  "url" : "https://opennursingcoreig.com/StructureDefinition/onc-oral-intake-assessment",
  "version" : "0.1.0",
  "name" : "ONCOralIntakeAssessment",
  "title" : "Oral Intake Assessment",
  "status" : "draft",
  "date" : "2026-01-03T01:26:42+00:00",
  "publisher" : "The Open Nursing Community",
  "description" : "Assessment of ability to take food and fluids orally.",
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
        "id" : "Observation.code",
        "path" : "Observation.code",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
              "code" : "oral-intake"
            }
          ]
        }
      },
      {
        "id" : "Observation.value[x]",
        "path" : "Observation.value[x]",
        "type" : [
          {
            "code" : "CodeableConcept"
          }
        ]
      }
    ]
  }
}

```
