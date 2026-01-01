# example-abbey-pain - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **example-abbey-pain**

## Example Observation: example-abbey-pain

Profile: [Abbey Pain Scale](StructureDefinition-onc-abbey-pain-scale.md)

**status**: Final

**category**: Exam

**code**: Abbey Pain Scale Score

**subject**: [Jane Doe Female, DoB Unknown](Patient-patient-example-jane.md)

**performer**: [Practitioner Nightingale](Practitioner-practitioner-example.md)

**value**: 2 {score}

> **component****code**:Vocalization**value**: 0

> **component****code**:Facial Expression**value**: 1

> **component****code**:Body Language**value**: 0

> **component****code**:Behavioral Change**value**: 1

> **component****code**:Psychological Change**value**: 0

> **component****code**:Physical Changes**value**: 0



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "example-abbey-pain",
  "meta" : {
    "profile" : [
      "https://fhir.clinyq.ai/StructureDefinition/onc-abbey-pain-scale"
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
        "code" : "abbey-score"
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
    "value" : 2,
    "unit" : "{score}"
  },
  "component" : [
    {
      "code" : {
        "coding" : [
          {
            "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
            "code" : "abbey-vocalization"
          }
        ]
      },
      "valueInteger" : 0
    },
    {
      "code" : {
        "coding" : [
          {
            "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
            "code" : "abbey-facial-expression"
          }
        ]
      },
      "valueInteger" : 1
    },
    {
      "code" : {
        "coding" : [
          {
            "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
            "code" : "abbey-body-language"
          }
        ]
      },
      "valueInteger" : 0
    },
    {
      "code" : {
        "coding" : [
          {
            "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
            "code" : "abbey-behavioral-change"
          }
        ]
      },
      "valueInteger" : 1
    },
    {
      "code" : {
        "coding" : [
          {
            "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
            "code" : "abbey-psychological-change"
          }
        ]
      },
      "valueInteger" : 0
    },
    {
      "code" : {
        "coding" : [
          {
            "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
            "code" : "abbey-physical-changes"
          }
        ]
      },
      "valueInteger" : 0
    }
  ]
}

```
