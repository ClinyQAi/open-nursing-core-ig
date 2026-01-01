# 4AT Attention Value Set - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **4AT Attention Value Set**

## ValueSet: 4AT Attention Value Set 

| | |
| :--- | :--- |
| *Official URL*:https://clinyqai.github.io/open-nursing-core-ig/ValueSet/onc-4at-attention-vs | *Version*:0.1.0 |
| Draft as of 2026-01-01 | *Computable Name*:AttentionVS |

 
Scoring for Months Backwards test 

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
  "id" : "onc-4at-attention-vs",
  "url" : "https://clinyqai.github.io/open-nursing-core-ig/ValueSet/onc-4at-attention-vs",
  "version" : "0.1.0",
  "name" : "AttentionVS",
  "title" : "4AT Attention Value Set",
  "status" : "draft",
  "date" : "2026-01-01T16:16:25+00:00",
  "description" : "Scoring for Months Backwards test",
  "compose" : {
    "include" : [
      {
        "system" : "http://snomed.info/sct",
        "concept" : [
          {
            "code" : "4851000147101",
            "display" : "Achieves 7 months or more correctly"
          },
          {
            "code" : "4861000147105",
            "display" : "Starts but scores <7 months / refuses"
          },
          {
            "code" : "4871000147108",
            "display" : "Untestable"
          }
        ]
      }
    ]
  }
}

```
