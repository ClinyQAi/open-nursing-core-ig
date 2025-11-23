# Open Nursing Core Nursing Intervention - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Open Nursing Core Nursing Intervention**

## Resource Profile: Open Nursing Core Nursing Intervention 

| | |
| :--- | :--- |
| *Official URL*:http://open-nursing-core.org/StructureDefinition/onc-nursing-intervention | *Version*:0.1.0 |
| Draft as of 2025-11-23 | *Computable Name*:ONCNursingIntervention |

 
Nursing intervention performed. 

**Usages:**

* Examples for this Profile: [Procedure/example-nursing-intervention](Procedure-example-nursing-intervention.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/onc.ig|current/StructureDefinition/onc-nursing-intervention)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-onc-nursing-intervention.csv), [Excel](StructureDefinition-onc-nursing-intervention.xlsx), [Schematron](StructureDefinition-onc-nursing-intervention.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "onc-nursing-intervention",
  "url" : "http://open-nursing-core.org/StructureDefinition/onc-nursing-intervention",
  "version" : "0.1.0",
  "name" : "ONCNursingIntervention",
  "title" : "Open Nursing Core Nursing Intervention",
  "status" : "draft",
  "date" : "2025-11-23T21:00:20+00:00",
  "description" : "Nursing intervention performed.",
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
  "type" : "Procedure",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Procedure",
  "derivation" : "constraint",
  "differential" : {
    "element" : [
      {
        "id" : "Procedure",
        "path" : "Procedure"
      },
      {
        "id" : "Procedure.extension",
        "path" : "Procedure.extension",
        "slicing" : {
          "discriminator" : [
            {
              "type" : "value",
              "path" : "url"
            }
          ],
          "ordered" : false,
          "rules" : "open"
        }
      },
      {
        "id" : "Procedure.extension:interventionGoal",
        "path" : "Procedure.extension",
        "sliceName" : "interventionGoal",
        "min" : 0,
        "max" : "*",
        "type" : [
          {
            "code" : "Extension",
            "profile" : [
              "http://open-nursing-core.org/StructureDefinition/intervention-goal-reference"
            ]
          }
        ],
        "mustSupport" : true
      },
      {
        "id" : "Procedure.status",
        "path" : "Procedure.status",
        "patternCode" : "completed",
        "mustSupport" : true
      },
      {
        "id" : "Procedure.code",
        "path" : "Procedure.code",
        "min" : 1,
        "mustSupport" : true,
        "binding" : {
          "strength" : "required",
          "valueSet" : "http://open-nursing-core.org/ValueSet/nursing-intervention-valueset"
        }
      }
    ]
  }
}

```
