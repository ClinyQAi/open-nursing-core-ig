# Nursing Intervention Value Set - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Nursing Intervention Value Set**

## ValueSet: Nursing Intervention Value Set 

| | |
| :--- | :--- |
| *Official URL*:https://clinyqai.github.io/open-nursing-core-ig/ValueSet/nursing-intervention-valueset | *Version*:1.0.0 |
| Active as of 2025-11-28 | *Computable Name*:NursingInterventionValueSet |

 **References** 

* [Nursing Intervention](StructureDefinition-onc-nursing-intervention.md)

### Logical Definition (CLD)

* Include codes from[`http://snomed.info/sct`](http://www.snomed.org/)version Not Stated (use latest from terminology server) where concept is-a 71388002 (Procedure)

 

### Expansion

Expansion from tx.fhir.org based on SNOMED CT International edition 01-Feb 2025

This value set has >1000 codes in it. In order to keep the publication size manageable, only a selection (1000 codes) of the whole set of codes is shown

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
  "id" : "nursing-intervention-valueset",
  "url" : "https://clinyqai.github.io/open-nursing-core-ig/ValueSet/nursing-intervention-valueset",
  "version" : "1.0.0",
  "name" : "NursingInterventionValueSet",
  "title" : "Nursing Intervention Value Set",
  "status" : "active",
  "date" : "2025-11-28T01:24:36+00:00",
  "compose" : {
    "include" : [
      {
        "system" : "http://snomed.info/sct",
        "filter" : [
          {
            "property" : "concept",
            "op" : "is-a",
            "value" : "71388002"
          }
        ]
      }
    ]
  }
}

```
