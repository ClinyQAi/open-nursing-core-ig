# example-seizure-record - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **example-seizure-record**

## Example Observation: example-seizure-record

Profile: [Seizure Record](StructureDefinition-onc-seizure-record.md)

**status**: Final

**category**: Exam

**code**: Seizure Record

**subject**: [Jane Doe Female, DoB Unknown](Patient-patient-example-jane.md)

**performer**: [Practitioner Nightingale](Practitioner-practitioner-example.md)

**value**: Tonic-clonic seizure lasting 2 mins

> **component****code**:Seizure Type**value**: Tonic-Clonic

> **component****code**:Seizure Duration**value**: 2 min

> **component****code**:Recovery Phase**value**: Sleepy for 30 mins post-ictal



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "example-seizure-record",
  "meta" : {
    "profile" : [
      "https://fhir.clinyq.ai/StructureDefinition/onc-seizure-record"
    ]
  },
  "status" : "final",
  "category" : [
    {
      "coding" : [
        {
          "system" : "http://terminology.hl7.org/CodeSystem/observation-category",
          "code" : "exam"
        }
      ]
    }
  ],
  "code" : {
    "coding" : [
      {
        "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
        "code" : "seizure-record"
      }
    ]
  },
  "subject" : {
    "reference" : "Patient/patient-example-jane"
  },
  "performer" : [
    {
      "reference" : "Practitioner/practitioner-example"
    }
  ],
  "valueString" : "Tonic-clonic seizure lasting 2 mins",
  "component" : [
    {
      "code" : {
        "coding" : [
          {
            "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
            "code" : "seizure-type"
          }
        ]
      },
      "valueString" : "Tonic-Clonic"
    },
    {
      "code" : {
        "coding" : [
          {
            "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
            "code" : "seizure-duration"
          }
        ]
      },
      "valueQuantity" : {
        "value" : 2,
        "unit" : "min"
      }
    },
    {
      "code" : {
        "coding" : [
          {
            "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
            "code" : "seizure-recovery"
          }
        ]
      },
      "valueString" : "Sleepy for 30 mins post-ictal"
    }
  ]
}

```
