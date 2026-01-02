# 4AT Acute Change Value Set - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **4AT Acute Change Value Set**

## ValueSet: 4AT Acute Change Value Set 

| | |
| :--- | :--- |
| *Official URL*:https://opennursingcoreig.com/ValueSet/onc-4at-acute-change-vs | *Version*:0.1.0 |
| Draft as of 2026-01-02 | *Computable Name*:AcuteChangeVS |

 
Scoring for Acute Change or Fluctuating Course 

 **References** 

* [4AT Delirium Assessment](StructureDefinition-onc-4at-delirium.md)

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
  "id" : "onc-4at-acute-change-vs",
  "url" : "https://opennursingcoreig.com/ValueSet/onc-4at-acute-change-vs",
  "version" : "0.1.0",
  "name" : "AcuteChangeVS",
  "title" : "4AT Acute Change Value Set",
  "status" : "draft",
  "date" : "2026-01-02T23:54:54+00:00",
  "publisher" : "The Open Nursing Community",
  "description" : "Scoring for Acute Change or Fluctuating Course",
  "compose" : {
    "include" : [
      {
        "system" : "http://snomed.info/sct",
        "concept" : [
          {
            "code" : "521000176101",
            "display" : "No"
          },
          {
            "code" : "531000176103",
            "display" : "Yes"
          }
        ]
      }
    ]
  }
}

```
