# NEWS2 Code Value Set - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **NEWS2 Code Value Set**

## ValueSet: NEWS2 Code Value Set 

| | |
| :--- | :--- |
| *Official URL*:https://clinyqai.github.io/open-nursing-core-ig/ValueSet/news2-code-vs | *Version*:0.1.0 |
| Draft as of 2025-12-26 | *Computable Name*:NEWS2CodeValueSet |

 
LOINC and SNOMED codes for NEWS2 

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
  "id" : "news2-code-vs",
  "url" : "https://clinyqai.github.io/open-nursing-core-ig/ValueSet/news2-code-vs",
  "version" : "0.1.0",
  "name" : "NEWS2CodeValueSet",
  "title" : "NEWS2 Code Value Set",
  "status" : "draft",
  "date" : "2025-12-26T14:36:57+00:00",
  "description" : "LOINC and SNOMED codes for NEWS2",
  "compose" : {
    "include" : [
      {
        "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
        "concept" : [
          {
            "code" : "news2-score"
          }
        ]
      }
    ]
  }
}

```
