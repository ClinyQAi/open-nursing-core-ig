# ADPIE Nursing Process Phases - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **ADPIE Nursing Process Phases**

## ValueSet: ADPIE Nursing Process Phases 

| | |
| :--- | :--- |
| *Official URL*:https://opennursingcoreig.com/ValueSet/onc-adpie-vs | *Version*:0.1.0 |
| Draft as of 2026-01-03 | *Computable Name*:ONCADPIEVS |

 
The five phases of the professional nursing process. 

 **References** 

* [Relational Care Logical Model](StructureDefinition-onc-relational-care-logical.md)

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
  "id" : "onc-adpie-vs",
  "url" : "https://opennursingcoreig.com/ValueSet/onc-adpie-vs",
  "version" : "0.1.0",
  "name" : "ONCADPIEVS",
  "title" : "ADPIE Nursing Process Phases",
  "status" : "draft",
  "date" : "2026-01-03T00:14:22+00:00",
  "publisher" : "The Open Nursing Community",
  "description" : "The five phases of the professional nursing process.",
  "compose" : {
    "include" : [
      {
        "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
        "concept" : [
          {
            "code" : "adpie-a",
            "display" : "Assessment"
          },
          {
            "code" : "adpie-d",
            "display" : "Diagnosis"
          },
          {
            "code" : "adpie-p",
            "display" : "Planning"
          },
          {
            "code" : "adpie-i",
            "display" : "Implementation"
          },
          {
            "code" : "adpie-e",
            "display" : "Evaluation"
          }
        ]
      }
    ]
  }
}

```
