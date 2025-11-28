# Nursing Problem Value Set - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Nursing Problem Value Set**

## ValueSet: Nursing Problem Value Set 

| | |
| :--- | :--- |
| *Official URL*:https://clinyqai.github.io/open-nursing-core-ig/ValueSet/nursing-problem-valueset | *Version*:1.0.0 |
| Active as of 2025-11-28 | *Computable Name*:NursingProblemValueSet |

 **References** 

* [Nursing Problem](StructureDefinition-onc-nursing-problem.md)

### Logical Definition (CLD)

* Include codes from[`http://snomed.info/sct`](http://www.snomed.org/)version Not Stated (use latest from terminology server) where concept is-a 409586006 (Complaint (finding))

 

### Expansion

Expansion from tx.fhir.org based on SNOMED CT International edition 01-Feb 2025

This value set expansion contains 1 concepts.

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
  "id" : "nursing-problem-valueset",
  "url" : "https://clinyqai.github.io/open-nursing-core-ig/ValueSet/nursing-problem-valueset",
  "version" : "1.0.0",
  "name" : "NursingProblemValueSet",
  "title" : "Nursing Problem Value Set",
  "status" : "active",
  "date" : "2025-11-28T00:15:25+00:00",
  "compose" : {
    "include" : [
      {
        "system" : "http://snomed.info/sct",
        "filter" : [
          {
            "property" : "concept",
            "op" : "is-a",
            "value" : "409586006"
          }
        ]
      }
    ]
  }
}

```
