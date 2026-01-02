# Nursing Problem Value Set - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Nursing Problem Value Set**

## ValueSet: Nursing Problem Value Set 

| | |
| :--- | :--- |
| *Official URL*:https://opennursingcoreig.com/ValueSet/nursing-problem-valueset | *Version*:0.1.0 |
| Draft as of 2026-01-02 | *Computable Name*:NursingProblemValueSet |

 
Value set for nursing problems and diagnoses 

 **References** 

* [Nursing Problem](StructureDefinition-onc-nursing-problem.md)

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
  "id" : "nursing-problem-valueset",
  "url" : "https://opennursingcoreig.com/ValueSet/nursing-problem-valueset",
  "version" : "0.1.0",
  "name" : "NursingProblemValueSet",
  "title" : "Nursing Problem Value Set",
  "status" : "draft",
  "experimental" : false,
  "date" : "2026-01-02T23:54:54+00:00",
  "publisher" : "The Open Nursing Community",
  "description" : "Value set for nursing problems and diagnoses",
  "compose" : {
    "include" : [
      {
        "system" : "http://snomed.info/sct",
        "concept" : [
          {
            "code" : "129839007",
            "display" : "At risk for falls"
          },
          {
            "code" : "300893006",
            "display" : "Nutritional finding"
          },
          {
            "code" : "22253000",
            "display" : "Pain"
          }
        ]
      },
      {
        "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
        "concept" : [
          {
            "code" : "risk-falls",
            "display" : "Risk of falls"
          }
        ]
      }
    ]
  }
}

```
