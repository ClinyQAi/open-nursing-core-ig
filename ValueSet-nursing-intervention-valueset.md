# Nursing Intervention Value Set - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Nursing Intervention Value Set**

## ValueSet: Nursing Intervention Value Set 

| | |
| :--- | :--- |
| *Official URL*:https://clinyqai.github.io/open-nursing-core-ig/ValueSet/nursing-intervention-valueset | *Version*:1.0.0 |
| Active as of 2025-12-26 | *Computable Name*:NursingInterventionValueSet |

 
Value set for nursing interventions 

 **References** 

* [Nursing Intervention](StructureDefinition-onc-nursing-intervention.md)

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
  "id" : "nursing-intervention-valueset",
  "url" : "https://clinyqai.github.io/open-nursing-core-ig/ValueSet/nursing-intervention-valueset",
  "version" : "1.0.0",
  "name" : "NursingInterventionValueSet",
  "title" : "Nursing Intervention Value Set",
  "status" : "active",
  "experimental" : false,
  "date" : "2025-12-26T11:32:15+00:00",
  "description" : "Value set for nursing interventions",
  "compose" : {
    "include" : [
      {
        "system" : "http://snomed.info/sct",
        "concept" : [
          {
            "code" : "71388002",
            "display" : "Procedure"
          },
          {
            "code" : "225358003",
            "display" : "Wound care"
          },
          {
            "code" : "386373004",
            "display" : "Nutrition therapy"
          }
        ]
      }
    ]
  }
}

```
