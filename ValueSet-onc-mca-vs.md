# Mental Capacity Finding Value Set - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Mental Capacity Finding Value Set**

## ValueSet: Mental Capacity Finding Value Set 

| | |
| :--- | :--- |
| *Official URL*:https://clinyqai.github.io/open-nursing-core-ig/ValueSet/onc-mca-vs | *Version*:0.1.0 |
| Draft as of 2026-01-02 | *Computable Name*:MentalCapacityVS |

 
Codes indicating presence or absence of capacity 

 **References** 

* [Mental Capacity Assessment](StructureDefinition-onc-mental-capacity.md)

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
  "id" : "onc-mca-vs",
  "url" : "https://clinyqai.github.io/open-nursing-core-ig/ValueSet/onc-mca-vs",
  "version" : "0.1.0",
  "name" : "MentalCapacityVS",
  "title" : "Mental Capacity Finding Value Set",
  "status" : "draft",
  "date" : "2026-01-02T16:06:53+00:00",
  "description" : "Codes indicating presence or absence of capacity",
  "compose" : {
    "include" : [
      {
        "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
        "concept" : [
          {
            "code" : "capacity-present",
            "display" : "Capacity Present"
          },
          {
            "code" : "capacity-absent",
            "display" : "Capacity Absent"
          },
          {
            "code" : "best-interest",
            "display" : "Best Interest Decision Required"
          }
        ]
      }
    ]
  }
}

```
