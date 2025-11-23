# example-nursing-problem - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **example-nursing-problem**

## Example Condition: example-nursing-problem

Profile: [Open Nursing Core Nursing Problem](StructureDefinition-onc-nursing-problem.md)

**clinicalStatus**: Active

**category**: Nursing Diagnosis

**code**: Risk of falls (finding)

**subject**: [John Smith Male, DoB Unknown](Patient-patient-example.md)



## Resource Content

```json
{
  "resourceType" : "Condition",
  "id" : "example-nursing-problem",
  "meta" : {
    "profile" : [
      "http://open-nursing-core.org/StructureDefinition/onc-nursing-problem"
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
          "system" : "http://open-nursing-core.org/CodeSystem/onc-problem-type",
          "code" : "nursing-diagnosis",
          "display" : "Nursing Diagnosis"
        }
      ]
    }
  ],
  "code" : {
    "coding" : [
      {
        "system" : "http://snomed.info/sct",
        "code" : "162828007",
        "display" : "Risk of falls (finding)"
      }
    ]
  },
  "subject" : {
    "reference" : "Patient/patient-example"
  }
}

```
