# Problem Type CodeSystem - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Problem Type CodeSystem**

## CodeSystem: Problem Type CodeSystem 

| | |
| :--- | :--- |
| *Official URL*:https://opennursingcoreig.com/CodeSystem/onc-problem-type | *Version*:0.1.0 |
| Draft as of 2026-01-02 | *Computable Name*:ONCProblemType |

 
Code system for categorizing types of nursing problems 

 This Code system is referenced in the content logical definition of the following value sets: 

* [ProblemCategoryValueSet](ValueSet-problem-category-valueset.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "onc-problem-type",
  "url" : "https://opennursingcoreig.com/CodeSystem/onc-problem-type",
  "version" : "0.1.0",
  "name" : "ONCProblemType",
  "title" : "Problem Type CodeSystem",
  "status" : "draft",
  "experimental" : false,
  "date" : "2026-01-02T23:54:54+00:00",
  "publisher" : "The Open Nursing Community",
  "description" : "Code system for categorizing types of nursing problems",
  "caseSensitive" : true,
  "content" : "complete",
  "count" : 3,
  "concept" : [
    {
      "code" : "nursing-diagnosis",
      "display" : "Nursing Diagnosis",
      "definition" : "A clinical judgment about individual, family, or community responses to actual or potential health problems"
    },
    {
      "code" : "risk-diagnosis",
      "display" : "Risk Diagnosis",
      "definition" : "A clinical judgment about an individual's vulnerability to developing an undesirable health condition"
    },
    {
      "code" : "health-promotion",
      "display" : "Health Promotion Diagnosis",
      "definition" : "A clinical judgment about motivation to increase wellbeing"
    }
  ]
}

```
