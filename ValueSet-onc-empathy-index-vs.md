# ONC Empathy & Relational Engagement Index - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **ONC Empathy & Relational Engagement Index**

## ValueSet: ONC Empathy & Relational Engagement Index 

| | |
| :--- | :--- |
| *Official URL*:https://opennursingcoreig.com/ValueSet/onc-empathy-index-vs | *Version*:0.1.0 |
| Draft as of 2026-01-03 | *Computable Name*:ONCEmpathyIndexVS |

 
A clinical scale measuring the depth of therapeutic empathy in nurse-patient interactions. Traditional EHRs ignore this; the Super-Gold Standard makes it a primary outcome. 

 **References** 

* [Relational Care Logical Model](StructureDefinition-onc-relational-care-logical.md)

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
  "id" : "onc-empathy-index-vs",
  "url" : "https://opennursingcoreig.com/ValueSet/onc-empathy-index-vs",
  "version" : "0.1.0",
  "name" : "ONCEmpathyIndexVS",
  "title" : "ONC Empathy & Relational Engagement Index",
  "status" : "draft",
  "date" : "2026-01-03T00:14:22+00:00",
  "publisher" : "The Open Nursing Community",
  "description" : "A clinical scale measuring the depth of therapeutic empathy in nurse-patient interactions. Traditional EHRs ignore this; the Super-Gold Standard makes it a primary outcome.",
  "compose" : {
    "include" : [
      {
        "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
        "concept" : [
          {
            "code" : "empathy-1",
            "display" : "Low Empathy: Task-focused interaction with minimal person-centred engagement."
          },
          {
            "code" : "empathy-2",
            "display" : "Basic Empathy: Professional interaction with patient identity acknowledged."
          },
          {
            "code" : "empathy-3",
            "display" : "Moderate Empathy: Active relational engagement with shared decision making."
          },
          {
            "code" : "empathy-4",
            "display" : "High Empathy: Authentic partnership with deep understanding of patient experience."
          },
          {
            "code" : "empathy-5",
            "display" : "Relational Excellence: Flourishing partnership with total alignment on 'What Matters to Me'."
          }
        ]
      }
    ]
  }
}

```
