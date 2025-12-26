# NEWS2 Sub-Score Codes - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **NEWS2 Sub-Score Codes**

## ValueSet: NEWS2 Sub-Score Codes 

| | |
| :--- | :--- |
| *Official URL*:https://clinyqai.github.io/open-nursing-core-ig/ValueSet/news2-subscore-code-vs | *Version*:0.1.0 |
| Draft as of 2025-12-26 | *Computable Name*:NEWS2SubscoreCodeValueSet |

 
SNOMED codes for NEWS2 sub-scores 

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
  "id" : "news2-subscore-code-vs",
  "url" : "https://clinyqai.github.io/open-nursing-core-ig/ValueSet/news2-subscore-code-vs",
  "version" : "0.1.0",
  "name" : "NEWS2SubscoreCodeValueSet",
  "title" : "NEWS2 Sub-Score Codes",
  "status" : "draft",
  "date" : "2025-12-26T14:29:21+00:00",
  "description" : "SNOMED codes for NEWS2 sub-scores",
  "compose" : {
    "include" : [
      {
        "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
        "concept" : [
          {
            "code" : "news2-subscore"
          }
        ]
      }
    ]
  }
}

```
