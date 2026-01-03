# Goal Evaluation Value Set - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Goal Evaluation Value Set**

## ValueSet: Goal Evaluation Value Set 

| | |
| :--- | :--- |
| *Official URL*:https://opennursingcoreig.com/ValueSet/goal-evaluation-valueset | *Version*:0.1.0 |
| Draft as of 2026-01-03 | *Computable Name*:GoalEvaluationValueSet |

 
Value set for evaluating patient goal outcomes 

 **References** 

* [ONC Goal Evaluation](StructureDefinition-onc-goal-evaluation.md)

### Logical Definition (CLD)

 

### Expansion

-------

 Explanation of the columns that may appear on this page: 

| | |
| :--- | :--- |
| Level | A few code lists that FHIR defines are hierarchical - each code is assigned a level. In this scheme, some codes are under other codes, and imply that the code they are under also applies |
| System | The source of the definition of the code (when the value set draws in codes defined elsewhere) |
| Code | The code (used as the code in the resource instance) |
| Display | The display (used in the*display*element of a[Coding](http://hl7.org/fhir/R4/datatypes.html#Coding)). If there is no display, implementers should not simply display the code, but map the concept into their application |
| Definition | An explanation of the meaning of the concept |
| Comments | Additional notes about how to use the code |



## Resource Content

```json
{
  "resourceType" : "ValueSet",
  "id" : "goal-evaluation-valueset",
  "url" : "https://opennursingcoreig.com/ValueSet/goal-evaluation-valueset",
  "version" : "0.1.0",
  "name" : "GoalEvaluationValueSet",
  "title" : "Goal Evaluation Value Set",
  "status" : "draft",
  "experimental" : false,
  "date" : "2026-01-03T01:26:42+00:00",
  "publisher" : "The Open Nursing Community",
  "description" : "Value set for evaluating patient goal outcomes",
  "compose" : {
    "include" : [
      {
        "system" : "http://snomed.info/sct",
        "concept" : [
          {
            "code" : "385652002",
            "display" : "Objective achieved"
          },
          {
            "code" : "385651009",
            "display" : "Objective not achieved"
          },
          {
            "code" : "255609007",
            "display" : "Partial achievement"
          },
          {
            "code" : "723510000",
            "display" : "Sustained improvement"
          },
          {
            "code" : "260388008",
            "display" : "Worsening"
          }
        ]
      }
    ]
  }
}

```
