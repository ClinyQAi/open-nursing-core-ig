# example-nursing-problem - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **example-nursing-problem**

## Example Condition: example-nursing-problem

Profile: [Nursing Problem](StructureDefinition-onc-nursing-problem.md)

**clinicalStatus**: Active

**category**: Nursing Diagnosis

**code**: Risk of falls

**subject**: [Jane Doe Female, DoB Unknown](Patient-patient-example-jane.md)



## Resource Content

```json
{
  "resourceType" : "Condition",
  "id" : "example-nursing-problem",
  "meta" : {
    "profile" : [
      "https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/onc-nursing-problem"
    ]
  },
  "clinicalStatus" : {
    "coding" : [
      {
        "system" : "http://terminology.hl7.org/CodeSystem/condition-clinical",
        "code" : "active",
        "display" : "Active"
      }
    ]
  },
  "category" : [
    {
      "coding" : [
        {
          "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-problem-type",
          "code" : "nursing-diagnosis",
          "display" : "Nursing Diagnosis"
        }
      ]
    }
  ],
  "code" : {
    "coding" : [
      {
        "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
        "code" : "risk-falls",
        "display" : "Risk of falls"
      }
    ]
  },
  "subject" : {
    "reference" : "Patient/patient-example-jane"
  }
}

```
