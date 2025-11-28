# Monk Skin Tone Value Set - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Monk Skin Tone Value Set**

## ValueSet: Monk Skin Tone Value Set 

| | |
| :--- | :--- |
| *Official URL*:https://clinyqai.github.io/open-nursing-core-ig/ValueSet/onc-monk-scale-vs | *Version*:1.0.0 |
| Active as of 2025-11-28 | *Computable Name*:ONCMonkScaleVS |

 **References** 

* [Monk Skin Tone Observation](StructureDefinition-onc-monk-skintone-observation.md)

### Logical Definition (CLD)

* Include all codes defined in [`https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-monk-scale`](CodeSystem-onc-monk-scale.md)version 📦1.0.0

 

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
  "id" : "onc-monk-scale-vs",
  "url" : "https://clinyqai.github.io/open-nursing-core-ig/ValueSet/onc-monk-scale-vs",
  "version" : "1.0.0",
  "name" : "ONCMonkScaleVS",
  "title" : "Monk Skin Tone Value Set",
  "status" : "active",
  "date" : "2025-11-28T02:23:26+00:00",
  "compose" : {
    "include" : [
      {
        "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-monk-scale"
      }
    ]
  }
}

```
