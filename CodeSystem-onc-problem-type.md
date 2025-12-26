# Problem Type CodeSystem - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Problem Type CodeSystem**

## CodeSystem: Problem Type CodeSystem 

| | |
| :--- | :--- |
| *Official URL*:https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-problem-type | *Version*:0.1.0 |
| Draft as of 2025-12-26 | *Computable Name*:ONCProblemType |

 
Code system for categorizing types of nursing problems 

 This Code system is referenced in the content logical definition of the following value sets: 

* [ProblemCategoryValueSet](ValueSet-problem-category-valueset.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "onc-problem-type",
  "url" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-problem-type",
  "version" : "0.1.0",
  "name" : "ONCProblemType",
  "title" : "Problem Type CodeSystem",
  "status" : "draft",
  "experimental" : false,
  "date" : "2025-12-26T14:39:04+00:00",
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
