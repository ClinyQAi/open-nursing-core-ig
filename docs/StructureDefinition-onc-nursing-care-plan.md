# Open Nursing Core Nursing Care Plan - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Open Nursing Core Nursing Care Plan**

## Resource Profile: Open Nursing Core Nursing Care Plan 

| | |
| :--- | :--- |
| *Official URL*:http://open-nursing-core.org/StructureDefinition/onc-nursing-care-plan | *Version*:0.1.0 |
| Draft as of 2025-11-23 | *Computable Name*:ONCNursingCarePlan |

 
Nursing care plan. 

**Usages:**

* Examples for this Profile: [CarePlan/example-nursing-care-plan](CarePlan-example-nursing-care-plan.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/onc.ig|current/StructureDefinition/onc-nursing-care-plan)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-onc-nursing-care-plan.csv), [Excel](StructureDefinition-onc-nursing-care-plan.xlsx), [Schematron](StructureDefinition-onc-nursing-care-plan.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "onc-nursing-care-plan",
  "url" : "http://open-nursing-core.org/StructureDefinition/onc-nursing-care-plan",
  "version" : "0.1.0",
  "name" : "ONCNursingCarePlan",
  "title" : "Open Nursing Core Nursing Care Plan",
  "status" : "draft",
  "date" : "2025-11-23T22:00:06+00:00",
  "description" : "Nursing care plan.",
  "fhirVersion" : "4.0.1",
  "mapping" : [
    {
      "identity" : "workflow",
      "uri" : "http://hl7.org/fhir/workflow",
      "name" : "Workflow Pattern"
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
      "identity" : "v2",
      "uri" : "http://hl7.org/v2",
      "name" : "HL7 v2 Mapping"
    }
  ],
  "kind" : "resource",
  "abstract" : false,
  "type" : "CarePlan",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/CarePlan",
  "derivation" : "constraint",
  "differential" : {
    "element" : [
      {
        "id" : "CarePlan",
        "path" : "CarePlan"
      },
      {
        "id" : "CarePlan.addresses",
        "path" : "CarePlan.addresses",
        "min" : 1,
        "type" : [
          {
            "code" : "Reference",
            "targetProfile" : [
              "http://open-nursing-core.org/StructureDefinition/onc-nursing-problem"
            ]
          }
        ],
        "mustSupport" : true
      },
      {
        "id" : "CarePlan.goal",
        "path" : "CarePlan.goal",
        "min" : 1,
        "type" : [
          {
            "code" : "Reference",
            "targetProfile" : [
              "http://open-nursing-core.org/StructureDefinition/onc-patient-goal"
            ]
          }
        ],
        "mustSupport" : true
      },
      {
        "id" : "CarePlan.activity.detail.code",
        "path" : "CarePlan.activity.detail.code",
        "binding" : {
          "strength" : "required",
          "valueSet" : "http://open-nursing-core.org/ValueSet/nursing-intervention-valueset"
        }
      }
    ]
  }
}

```
