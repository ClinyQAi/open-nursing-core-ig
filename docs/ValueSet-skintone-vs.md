# Fitzpatrick Skin Tone Value Set - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Fitzpatrick Skin Tone Value Set**

## ValueSet: Fitzpatrick Skin Tone Value Set 

| | |
| :--- | :--- |
| *Official URL*:http://open-nursing-core.org/ValueSet/skintone-vs | *Version*:0.1.0 |
| Draft as of 2025-11-23 | *Computable Name*:SkinToneVS |

 
Values for Fitzpatrick Skin Type I-VI using standard SNOMED CT codes. 

 **References** 

* [ONC Skin Tone Observation](StructureDefinition-onc-skintone-observation.md)

### Logical Definition (CLD)

 

### Expansion

Expansion from tx.fhir.org based on SNOMED CT International edition 01-Feb 2025

This value set contains 6 concepts

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
  "id" : "skintone-vs",
  "url" : "http://open-nursing-core.org/ValueSet/skintone-vs",
  "version" : "0.1.0",
  "name" : "SkinToneVS",
  "title" : "Fitzpatrick Skin Tone Value Set",
  "status" : "draft",
  "date" : "2025-11-23T21:00:20+00:00",
  "description" : "Values for Fitzpatrick Skin Type I-VI using standard SNOMED CT codes.",
  "compose" : {
    "include" : [
      {
        "system" : "http://snomed.info/sct",
        "concept" : [
          {
            "code" : "403153005",
            "display" : "Fitzpatrick skin type I"
          },
          {
            "code" : "403154004",
            "display" : "Fitzpatrick skin type II"
          },
          {
            "code" : "403155003",
            "display" : "Fitzpatrick skin type III"
          },
          {
            "code" : "403156002",
            "display" : "Fitzpatrick skin type IV"
          },
          {
            "code" : "403157006",
            "display" : "Fitzpatrick skin type V"
          },
          {
            "code" : "403158001",
            "display" : "Fitzpatrick skin type VI"
          }
        ]
      }
    ]
  }
}

```
