# Clinical Frailty Scale Value Set - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Clinical Frailty Scale Value Set**

## ValueSet: Clinical Frailty Scale Value Set 

| | |
| :--- | :--- |
| *Official URL*:https://clinyqai.github.io/open-nursing-core-ig/ValueSet/onc-cfs-vs | *Version*:0.1.0 |
| Draft as of 2026-01-01 | *Computable Name*:ClinicalFrailtyScaleVS |

 
Codes for Rockwood Clinical Frailty Scale (1-9) 

 **References** 

* [Clinical Frailty Scale (CFS)](StructureDefinition-onc-clinical-frailty-scale.md)

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
  "id" : "onc-cfs-vs",
  "url" : "https://clinyqai.github.io/open-nursing-core-ig/ValueSet/onc-cfs-vs",
  "version" : "0.1.0",
  "name" : "ClinicalFrailtyScaleVS",
  "title" : "Clinical Frailty Scale Value Set",
  "status" : "draft",
  "date" : "2026-01-01T16:16:25+00:00",
  "description" : "Codes for Rockwood Clinical Frailty Scale (1-9)",
  "compose" : {
    "include" : [
      {
        "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
        "concept" : [
          {
            "code" : "cfs-1"
          },
          {
            "code" : "cfs-2"
          },
          {
            "code" : "cfs-3"
          },
          {
            "code" : "cfs-4"
          },
          {
            "code" : "cfs-5"
          },
          {
            "code" : "cfs-6"
          },
          {
            "code" : "cfs-7"
          },
          {
            "code" : "cfs-8"
          },
          {
            "code" : "cfs-9"
          }
        ]
      }
    ]
  }
}

```
