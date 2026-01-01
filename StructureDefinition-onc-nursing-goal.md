# ONC Nursing Goal - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **ONC Nursing Goal**

## Resource Profile: ONC Nursing Goal 

| | |
| :--- | :--- |
| *Official URL*:https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/onc-nursing-goal | *Version*:0.1.0 |
| Draft as of 2026-01-01 | *Computable Name*:ONCNursingGoal |

 
Patient-centered goal with mandatory evaluation requirements. Serves as the 'spine' of the CarePlan, linking problems to outcomes. 

**Usages:**

* Refer to this Profile: [Intervention Goal Reference](StructureDefinition-intervention-goal-reference.md), [Observation Goal Reference](StructureDefinition-observation-goal-reference.md) and [ONC Goal Evaluation](StructureDefinition-onc-goal-evaluation.md)
* Examples for this Profile: [Goal/example-patient-goal](Goal-example-patient-goal.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/onc.ig|current/StructureDefinition/onc-nursing-goal)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-onc-nursing-goal.csv), [Excel](StructureDefinition-onc-nursing-goal.xlsx), [Schematron](StructureDefinition-onc-nursing-goal.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "onc-nursing-goal",
  "url" : "https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/onc-nursing-goal",
  "version" : "0.1.0",
  "name" : "ONCNursingGoal",
  "title" : "ONC Nursing Goal",
  "status" : "draft",
  "date" : "2026-01-01T16:16:25+00:00",
  "description" : "Patient-centered goal with mandatory evaluation requirements. Serves as the 'spine' of the CarePlan, linking problems to outcomes.",
  "fhirVersion" : "4.0.1",
  "mapping" : [
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
    }
  ],
  "kind" : "resource",
  "abstract" : false,
  "type" : "Goal",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Goal",
  "derivation" : "constraint",
  "differential" : {
    "element" : [
      {
        "id" : "Goal",
        "path" : "Goal",
        "constraint" : [
          {
            "key" : "onc-goal-evaluation-timing",
            "severity" : "warning",
            "human" : "Goal must have evaluation observation by target.dueDate",
            "expression" : "target.dueDate.exists() implies (lifecycleStatus = 'active' or lifecycleStatus = 'completed' or lifecycleStatus = 'cancelled')",
            "source" : "https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/onc-nursing-goal"
          }
        ]
      },
      {
        "id" : "Goal.lifecycleStatus",
        "path" : "Goal.lifecycleStatus",
        "mustSupport" : true
      },
      {
        "id" : "Goal.achievementStatus",
        "path" : "Goal.achievementStatus",
        "mustSupport" : true
      },
      {
        "id" : "Goal.category",
        "path" : "Goal.category",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "http://terminology.hl7.org/CodeSystem/goal-category",
              "code" : "nursing"
            }
          ]
        }
      },
      {
        "id" : "Goal.subject",
        "path" : "Goal.subject",
        "type" : [
          {
            "code" : "Reference",
            "targetProfile" : ["http://hl7.org/fhir/StructureDefinition/Patient"]
          }
        ]
      },
      {
        "id" : "Goal.target",
        "path" : "Goal.target",
        "min" : 1,
        "mustSupport" : true
      },
      {
        "id" : "Goal.target.measure",
        "path" : "Goal.target.measure",
        "binding" : {
          "strength" : "extensible",
          "valueSet" : "https://clinyqai.github.io/open-nursing-core-ig/ValueSet/onc-goal-target-measure-vs"
        }
      },
      {
        "id" : "Goal.target.due[x]",
        "path" : "Goal.target.due[x]",
        "slicing" : {
          "discriminator" : [
            {
              "type" : "type",
              "path" : "$this"
            }
          ],
          "ordered" : false,
          "rules" : "open"
        },
        "min" : 1
      },
      {
        "id" : "Goal.target.due[x]:dueDate",
        "path" : "Goal.target.due[x]",
        "sliceName" : "dueDate",
        "min" : 1,
        "max" : "1",
        "type" : [
          {
            "code" : "date"
          }
        ],
        "mustSupport" : true
      },
      {
        "id" : "Goal.addresses",
        "path" : "Goal.addresses",
        "min" : 1,
        "type" : [
          {
            "code" : "Reference",
            "targetProfile" : [
              "https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/onc-nursing-problem"
            ]
          }
        ],
        "mustSupport" : true
      }
    ]
  }
}

```
