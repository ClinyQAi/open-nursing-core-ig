# ACVPU Value Set - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **ACVPU Value Set**

## ValueSet: ACVPU Value Set 

| | |
| :--- | :--- |
| *Official URL*:http://open-nursing-core.org/ValueSet/acvpu-vs | *Version*:0.1.0 |
| Draft as of 2025-11-23 | *Computable Name*:ACVPUVS |

 
Codes representing the ACVPU (Alert, Confusion, Voice, Pain, Unresponsive) scale. 

 **References** 

* [ONC NEWS2 Assessment](StructureDefinition-onc-news2-assessment.md)

### Logical Definition (CLD)

 

### Expansion

Expansion from tx.fhir.org based on SNOMED CT International edition 01-Feb 2025

This value set contains 5 concepts

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
  "id" : "acvpu-vs",
  "url" : "http://open-nursing-core.org/ValueSet/acvpu-vs",
  "version" : "0.1.0",
  "name" : "ACVPUVS",
  "title" : "ACVPU Value Set",
  "status" : "draft",
  "experimental" : false,
  "date" : "2025-11-23T22:00:06+00:00",
  "description" : "Codes representing the ACVPU (Alert, Confusion, Voice, Pain, Unresponsive) scale.",
  "compose" : {
    "include" : [
      {
        "system" : "http://snomed.info/sct",
        "concept" : [
          {
            "code" : "248234008",
            "display" : "Mentally alert"
          },
          {
            "code" : "130987000",
            "display" : "Acute confusion"
          },
          {
            "code" : "300202002",
            "display" : "Responds to voice"
          },
          {
            "code" : "450847001",
            "display" : "Responds to pain"
          },
          {
            "code" : "422768004",
            "display" : "Unresponsive"
          }
        ]
      }
    ]
  }
}

```
