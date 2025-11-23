# ONC Housing Status Assessment - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **ONC Housing Status Assessment**

## Resource Profile: ONC Housing Status Assessment 

| | |
| :--- | :--- |
| *Official URL*:http://open-nursing-core.org/StructureDefinition/onc-housing-status | *Version*:0.1.0 |
| Draft as of 2025-11-23 | *Computable Name*:ONCHousingStatus |

 
Assessment of the patient's housing status. 

**Usages:**

* Examples for this Profile: [Observation/example-housing-status](Observation-example-housing-status.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/onc.ig|current/StructureDefinition/onc-housing-status)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-onc-housing-status.csv), [Excel](StructureDefinition-onc-housing-status.xlsx), [Schematron](StructureDefinition-onc-housing-status.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "onc-housing-status",
  "url" : "http://open-nursing-core.org/StructureDefinition/onc-housing-status",
  "version" : "0.1.0",
  "name" : "ONCHousingStatus",
  "title" : "ONC Housing Status Assessment",
  "status" : "draft",
  "date" : "2025-11-23T22:00:06+00:00",
  "description" : "Assessment of the patient's housing status.",
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
  "baseDefinition" : "http://open-nursing-core.org/StructureDefinition/onc-nursing-assessment",
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
              "system" : "http://loinc.org",
              "code" : "71802-3",
              "display" : "Housing status"
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
            "code" : "CodeableConcept"
          }
        ],
        "binding" : {
          "strength" : "required",
          "valueSet" : "http://open-nursing-core.org/ValueSet/housing-status-vs"
        }
      }
    ]
  }
}

```
