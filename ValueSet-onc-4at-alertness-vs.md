# 4AT Alertness Value Set - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **4AT Alertness Value Set**

## ValueSet: 4AT Alertness Value Set 

| | |
| :--- | :--- |
| *Official URL*:https://opennursingcoreig.com/ValueSet/onc-4at-alertness-vs | *Version*:0.1.0 |
| Draft as of 2026-01-03 | *Computable Name*:AlertnessVS |

 
Scoring options for 4AT Alertness 

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
  "id" : "onc-4at-alertness-vs",
  "url" : "https://opennursingcoreig.com/ValueSet/onc-4at-alertness-vs",
  "version" : "0.1.0",
  "name" : "AlertnessVS",
  "title" : "4AT Alertness Value Set",
  "status" : "draft",
  "date" : "2026-01-03T01:26:42+00:00",
  "publisher" : "The Open Nursing Community",
  "description" : "Scoring options for 4AT Alertness",
  "compose" : {
    "include" : [
      {
        "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
        "concept" : [
          {
            "code" : "4at-alertness",
            "display" : "Normal (fully alert, not agitated)"
          }
        ]
      },
      {
        "system" : "http://snomed.info/sct",
        "concept" : [
          {
            "code" : "17621005",
            "display" : "Normal"
          },
          {
            "code" : "263654008",
            "display" : "Abnormal"
          }
        ]
      }
    ]
  }
}

```
