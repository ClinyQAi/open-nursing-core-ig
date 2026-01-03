# Nursing Prognosis ValueSet - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Nursing Prognosis ValueSet**

## ValueSet: Nursing Prognosis ValueSet 

| | |
| :--- | :--- |
| *Official URL*:https://opennursingcoreig.com/ValueSet/onc-prognosis-vs | *Version*:0.1.0 |
| Draft as of 2026-01-03 | *Computable Name*:ONCPrognosisVS |

 
Prognosis codes for clinical impression 

 **References** 

* [ONC Nursing Clinical Impression](StructureDefinition-onc-nursing-clinical-impression.md)

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
  "id" : "onc-prognosis-vs",
  "url" : "https://opennursingcoreig.com/ValueSet/onc-prognosis-vs",
  "version" : "0.1.0",
  "name" : "ONCPrognosisVS",
  "title" : "Nursing Prognosis ValueSet",
  "status" : "draft",
  "date" : "2026-01-03T00:14:22+00:00",
  "publisher" : "The Open Nursing Community",
  "description" : "Prognosis codes for clinical impression",
  "compose" : {
    "include" : [
      {
        "system" : "http://snomed.info/sct",
        "concept" : [
          {
            "code" : "17621005",
            "display" : "Normal"
          },
          {
            "code" : "260388008",
            "display" : "Worsening"
          },
          {
            "code" : "385633008",
            "display" : "Improving"
          }
        ]
      }
    ]
  }
}

```
