# NEWS2 Sub-Score Codes - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **NEWS2 Sub-Score Codes**

## ValueSet: NEWS2 Sub-Score Codes 

| | |
| :--- | :--- |
| *Official URL*:https://clinyqai.github.io/open-nursing-core-ig/ValueSet/news2-subscore-code-vs | *Version*:1.0.0 |
| Active as of 2025-12-26 | *Computable Name*:NEWS2SubscoreCodeValueSet |

 
SNOMED codes for NEWS2 sub-scores 

 **References** 

* [NEWS2 Sub-Score](StructureDefinition-onc-news2-subscore.md)

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
  "version" : "1.0.0",
  "name" : "NEWS2SubscoreCodeValueSet",
  "title" : "NEWS2 Sub-Score Codes",
  "status" : "active",
  "date" : "2025-12-26T11:23:52+00:00",
  "description" : "SNOMED codes for NEWS2 sub-scores",
  "compose" : {
    "include" : [
      {
        "system" : "http://snomed.info/sct",
        "concept" : [
          {
            "code" : "1104301000000104",
            "display" : "Royal College of Physicians National Early Warning Score 2 - pulse score"
          },
          {
            "code" : "1104311000000102",
            "display" : "Royal College of Physicians National Early Warning Score 2 - respiration rate score"
          },
          {
            "code" : "1104331000000106",
            "display" : "Royal College of Physicians National Early Warning Score 2 - temperature score"
          },
          {
            "code" : "1104351000000100",
            "display" : "Royal College of Physicians National Early Warning Score 2 - ACVPU score"
          },
          {
            "code" : "1104341000000103",
            "display" : "Royal College of Physicians National Early Warning Score 2 - oxygen saturation scale 1 score"
          },
          {
            "code" : "1104321000000108",
            "display" : "Royal College of Physicians National Early Warning Score 2 - systolic blood pressure score"
          }
        ]
      }
    ]
  }
}

```
