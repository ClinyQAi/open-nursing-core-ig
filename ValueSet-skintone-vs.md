# Fitzpatrick Skin Tone Value Set - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Fitzpatrick Skin Tone Value Set**

## ValueSet: Fitzpatrick Skin Tone Value Set 

| | |
| :--- | :--- |
| *Official URL*:https://clinyqai.github.io/open-nursing-core-ig/ValueSet/skintone-vs | *Version*:0.1.0 |
| Draft as of 2025-12-26 | *Computable Name*:SkinToneVS |

 
Value set for Fitzpatrick skin type classifications 

 **References** 

* [Skin Tone Observation](StructureDefinition-onc-skintone-observation.md)

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
  "id" : "skintone-vs",
  "url" : "https://clinyqai.github.io/open-nursing-core-ig/ValueSet/skintone-vs",
  "version" : "0.1.0",
  "name" : "SkinToneVS",
  "title" : "Fitzpatrick Skin Tone Value Set",
  "status" : "draft",
  "experimental" : false,
  "date" : "2025-12-26T14:29:21+00:00",
  "description" : "Value set for Fitzpatrick skin type classifications",
  "compose" : {
    "include" : [
      {
        "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
        "concept" : [
          {
            "code" : "fitzpatrick-1",
            "display" : "Type I"
          },
          {
            "code" : "fitzpatrick-2",
            "display" : "Type II"
          },
          {
            "code" : "fitzpatrick-3",
            "display" : "Type III"
          },
          {
            "code" : "fitzpatrick-4",
            "display" : "Type IV"
          },
          {
            "code" : "fitzpatrick-5",
            "display" : "Type V"
          },
          {
            "code" : "fitzpatrick-6",
            "display" : "Type VI"
          }
        ]
      }
    ]
  }
}

```
