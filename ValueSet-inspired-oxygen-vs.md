# Inspired Oxygen Value Set - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Inspired Oxygen Value Set**

## ValueSet: Inspired Oxygen Value Set 

| | |
| :--- | :--- |
| *Official URL*:https://opennursingcoreig.com/ValueSet/inspired-oxygen-vs | *Version*:0.1.0 |
| Draft as of 2026-01-03 | *Computable Name*:InspiredOxygenValueSet |

 
Codes for inspired oxygen status 

 **References** 

* [Inspired Oxygen](StructureDefinition-onc-inspired-oxygen.md)

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
  "id" : "inspired-oxygen-vs",
  "url" : "https://opennursingcoreig.com/ValueSet/inspired-oxygen-vs",
  "version" : "0.1.0",
  "name" : "InspiredOxygenValueSet",
  "title" : "Inspired Oxygen Value Set",
  "status" : "draft",
  "date" : "2026-01-03T00:34:03+00:00",
  "publisher" : "The Open Nursing Community",
  "description" : "Codes for inspired oxygen status",
  "compose" : {
    "include" : [
      {
        "system" : "http://snomed.info/sct",
        "concept" : [
          {
            "code" : "722742002",
            "display" : "Breathing room air"
          },
          {
            "code" : "371825009",
            "display" : "Patient on oxygen"
          }
        ]
      }
    ]
  }
}

```
