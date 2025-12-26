# Housing Status Value Set - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Housing Status Value Set**

## ValueSet: Housing Status Value Set 

| | |
| :--- | :--- |
| *Official URL*:https://clinyqai.github.io/open-nursing-core-ig/ValueSet/housing-status-vs | *Version*:1.0.0 |
| Active as of 2025-12-26 | *Computable Name*:HousingStatusVS |

 
Value set for patient housing status 

 **References** 

This value set is not used here; it may be used elsewhere (e.g. specifications and/or implementations that use this content)

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
  "id" : "housing-status-vs",
  "url" : "https://clinyqai.github.io/open-nursing-core-ig/ValueSet/housing-status-vs",
  "version" : "1.0.0",
  "name" : "HousingStatusVS",
  "title" : "Housing Status Value Set",
  "status" : "active",
  "experimental" : false,
  "date" : "2025-12-26T00:40:38+00:00",
  "description" : "Value set for patient housing status",
  "compose" : {
    "include" : [
      {
        "system" : "http://snomed.info/sct",
        "concept" : [
          {
            "code" : "266935003",
            "display" : "Housing problem"
          },
          {
            "code" : "160724001",
            "display" : "Homeless"
          },
          {
            "code" : "224224003",
            "display" : "Lives in own home"
          }
        ]
      }
    ]
  }
}

```
