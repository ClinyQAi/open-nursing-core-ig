# Open Nursing Core Goal Evaluation - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Open Nursing Core Goal Evaluation**

## Resource Profile: Open Nursing Core Goal Evaluation 

| | |
| :--- | :--- |
| *Official URL*:http://open-nursing-core.org/StructureDefinition/onc-goal-evaluation | *Version*:0.1.0 |
| Draft as of 2025-11-23 | *Computable Name*:ONCGoalEvaluation |

 
Evaluation of a patient's progress towards a goal. 

**Usages:**

* Examples for this Profile: [Observation/example-goal-evaluation](Observation-example-goal-evaluation.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/onc.ig|current/StructureDefinition/onc-goal-evaluation)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-onc-goal-evaluation.csv), [Excel](StructureDefinition-onc-goal-evaluation.xlsx), [Schematron](StructureDefinition-onc-goal-evaluation.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "onc-goal-evaluation",
  "url" : "http://open-nursing-core.org/StructureDefinition/onc-goal-evaluation",
  "version" : "0.1.0",
  "name" : "ONCGoalEvaluation",
  "title" : "Open Nursing Core Goal Evaluation",
  "status" : "draft",
  "date" : "2025-11-23T02:33:16+00:00",
  "description" : "Evaluation of a patient's progress towards a goal.",
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
        "id" : "Observation.extension",
        "path" : "Observation.extension",
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
        "id" : "Observation.extension:goalReference",
        "path" : "Observation.extension",
        "sliceName" : "goalReference",
        "min" : 0,
        "max" : "1",
        "type" : [
          {
            "code" : "Extension",
            "profile" : [
              "http://open-nursing-core.org/StructureDefinition/observation-goal-reference"
            ]
          }
        ],
        "mustSupport" : true
      },
      {
        "id" : "Observation.code",
        "path" : "Observation.code",
        "binding" : {
          "strength" : "required",
          "valueSet" : "http://open-nursing-core.org/ValueSet/goal-evaluation-valueset"
        }
      }
    ]
  }
}

```
