# example-4at-delirium - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **example-4at-delirium**

## Example Observation: example-4at-delirium

Profile: [4AT Delirium Assessment](StructureDefinition-onc-4at-delirium.md)

**status**: Final

**category**: Exam

**code**: 4AT Delirium Score

**subject**: [Jane Doe Female, DoB Unknown](Patient-patient-example-jane.md)

**performer**: [Practitioner Nightingale](Practitioner-practitioner-example.md)

**value**: 5 {score}

> **component****code**:Alertness**value**:Normal

> **component****code**:AMT4 Score**value**:1 Error

> **component****code**:Attention**value**:Months backwards < 7 months correct

> **component****code**:Acute Change**value**:No



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "example-4at-delirium",
  "meta" : {
    "profile" : [
      "https://fhir.clinyq.ai/StructureDefinition/onc-4at-delirium"
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
        "code" : "4at-score"
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
  "valueQuantity" : {
    "value" : 5,
    "unit" : "{score}"
  },
  "component" : [
    {
      "code" : {
        "coding" : [
          {
            "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
            "code" : "4at-alertness"
          }
        ]
      },
      "valueCodeableConcept" : {
        "coding" : [
          {
            "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
            "code" : "4at-alert-normal",
            "display" : "Normal"
          }
        ]
      }
    },
    {
      "code" : {
        "coding" : [
          {
            "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
            "code" : "4at-amt4"
          }
        ]
      },
      "valueCodeableConcept" : {
        "coding" : [
          {
            "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
            "code" : "4at-amt4-1error",
            "display" : "1 Error"
          }
        ]
      }
    },
    {
      "code" : {
        "coding" : [
          {
            "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
            "code" : "4at-attention"
          }
        ]
      },
      "valueCodeableConcept" : {
        "coding" : [
          {
            "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
            "code" : "4at-attention-gt7",
            "display" : "Months backwards < 7 months correct"
          }
        ]
      }
    },
    {
      "code" : {
        "coding" : [
          {
            "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
            "code" : "4at-acute-change"
          }
        ]
      },
      "valueCodeableConcept" : {
        "coding" : [
          {
            "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
            "code" : "4at-change-no",
            "display" : "No"
          }
        ]
      }
    }
  ]
}

```
