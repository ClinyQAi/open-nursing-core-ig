# Pain Assessment Code Value Set - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Pain Assessment Code Value Set**

## ValueSet: Pain Assessment Code Value Set 

| | |
| :--- | :--- |
| *Official URL*:https://opennursingcoreig.com/ValueSet/pain-assessment-code-vs | *Version*:0.1.0 |
| Draft as of 2026-01-02 | *Computable Name*:PainAssessmentCodeValueSet |

 
LOINC codes for pain severity assessment 

 **References** 

* [Pain Assessment (NRS 0-10)](StructureDefinition-onc-pain-assessment.md)

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
  "id" : "pain-assessment-code-vs",
  "url" : "https://opennursingcoreig.com/ValueSet/pain-assessment-code-vs",
  "version" : "0.1.0",
  "name" : "PainAssessmentCodeValueSet",
  "title" : "Pain Assessment Code Value Set",
  "status" : "draft",
  "date" : "2026-01-02T23:54:54+00:00",
  "publisher" : "The Open Nursing Community",
  "description" : "LOINC codes for pain severity assessment",
  "compose" : {
    "include" : [
      {
        "system" : "http://loinc.org",
        "concept" : [
          {
            "code" : "72514-3",
            "display" : "Pain severity - 0-10 verbal numeric rating"
          },
          {
            "code" : "38208-5",
            "display" : "Pain severity - Reported"
          }
        ]
      }
    ]
  }
}

```
