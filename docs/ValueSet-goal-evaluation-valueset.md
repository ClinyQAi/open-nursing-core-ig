# Goal Evaluation Value Set - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Goal Evaluation Value Set**

## ValueSet: Goal Evaluation Value Set 

| | |
| :--- | :--- |
| *Official URL*:http://open-nursing-core.org/ValueSet/goal-evaluation-valueset | *Version*:0.1.0 |
| Draft as of 2025-11-23 | *Computable Name*:GoalEvaluationValueSet |

 **References** 

* [Open Nursing Core Goal Evaluation](StructureDefinition-onc-goal-evaluation.md)

### Logical Definition (CLD)

 

### Expansion

Expansion from tx.fhir.org based on SNOMED CT International edition 01-Feb 2025

This value set contains 2 concepts

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
  "url" : "http://open-nursing-core.org/ValueSet/goal-evaluation-valueset",
  "version" : "0.1.0",
  "name" : "GoalEvaluationValueSet",
  "title" : "Goal Evaluation Value Set",
  "status" : "draft",
  "date" : "2025-11-23T22:00:06+00:00",
  "compose" : {
    "include" : [
      {
        "system" : "http://snomed.info/sct",
        "concept" : [
          {
            "code" : "385633008"
          },
          {
            "code" : "385634002"
          }
        ]
      }
    ]
  }
}

```
