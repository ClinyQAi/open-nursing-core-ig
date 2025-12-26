# Problem Category Value Set - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Problem Category Value Set**

## ValueSet: Problem Category Value Set 

| | |
| :--- | :--- |
| *Official URL*:https://clinyqai.github.io/open-nursing-core-ig/ValueSet/problem-category-valueset | *Version*:0.1.0 |
| Draft as of 2025-12-26 | *Computable Name*:ProblemCategoryValueSet |

 
Value set for categorizing nursing problems 

 **References** 

* [Nursing Problem](StructureDefinition-onc-nursing-problem.md)

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
  "id" : "problem-category-valueset",
  "url" : "https://clinyqai.github.io/open-nursing-core-ig/ValueSet/problem-category-valueset",
  "version" : "0.1.0",
  "name" : "ProblemCategoryValueSet",
  "title" : "Problem Category Value Set",
  "status" : "draft",
  "experimental" : false,
  "date" : "2025-12-26T14:28:37+00:00",
  "description" : "Value set for categorizing nursing problems",
  "compose" : {
    "include" : [
      {
        "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-problem-type"
      }
    ]
  }
}

```
