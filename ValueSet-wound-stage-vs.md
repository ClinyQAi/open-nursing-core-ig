# Wound Stage Value Set - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Wound Stage Value Set**

## ValueSet: Wound Stage Value Set 

| | |
| :--- | :--- |
| *Official URL*:https://clinyqai.github.io/open-nursing-core-ig/ValueSet/wound-stage-vs | *Version*:1.0.0 |
| Active as of 2025-12-26 | *Computable Name*:WoundStageValueSet |

 
SNOMED CT codes for pressure ulcer staging 

 **References** 

* [Wound Assessment](StructureDefinition-onc-wound-assessment.md)

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
  "id" : "wound-stage-vs",
  "url" : "https://clinyqai.github.io/open-nursing-core-ig/ValueSet/wound-stage-vs",
  "version" : "1.0.0",
  "name" : "WoundStageValueSet",
  "title" : "Wound Stage Value Set",
  "status" : "active",
  "date" : "2025-12-26T00:14:27+00:00",
  "description" : "SNOMED CT codes for pressure ulcer staging",
  "compose" : {
    "include" : [
      {
        "system" : "http://snomed.info/sct",
        "concept" : [
          {
            "code" : "421257003",
            "display" : "Stage 1 pressure ulcer"
          },
          {
            "code" : "420226007",
            "display" : "Stage 2 pressure ulcer"
          },
          {
            "code" : "420555000",
            "display" : "Stage 3 pressure ulcer"
          },
          {
            "code" : "420324007",
            "display" : "Stage 4 pressure ulcer"
          },
          {
            "code" : "421076008",
            "display" : "Unstageable pressure ulcer"
          },
          {
            "code" : "723071003",
            "display" : "Deep tissue injury"
          }
        ]
      }
    ]
  }
}

```
