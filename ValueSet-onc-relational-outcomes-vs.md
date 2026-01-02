# ONC Relational Care Outcomes - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **ONC Relational Care Outcomes**

## ValueSet: ONC Relational Care Outcomes 

| | |
| :--- | :--- |
| *Official URL*:https://opennursingcoreig.com/ValueSet/onc-relational-outcomes-vs | *Version*:0.1.0 |
| Draft as of 2026-01-02 | *Computable Name*:ONCRelationalOutcomesVS |

 
Captures the measurable outcomes of relational and empathic nursing care. 

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
  "id" : "onc-relational-outcomes-vs",
  "url" : "https://opennursingcoreig.com/ValueSet/onc-relational-outcomes-vs",
  "version" : "0.1.0",
  "name" : "ONCRelationalOutcomesVS",
  "title" : "ONC Relational Care Outcomes",
  "status" : "draft",
  "date" : "2026-01-02T23:43:46+00:00",
  "publisher" : "The Open Nursing Community",
  "description" : "Captures the measurable outcomes of relational and empathic nursing care.",
  "compose" : {
    "include" : [
      {
        "system" : "http://snomed.info/sct",
        "concept" : [
          {
            "code" : "161096001",
            "display" : "Patient feels respected"
          },
          {
            "code" : "307823004",
            "display" : "Patient feels heard"
          },
          {
            "code" : "428131006",
            "display" : "Therapeutic relationship established"
          }
        ]
      }
    ]
  }
}

```
