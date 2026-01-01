# example-oral-health - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **example-oral-health**

## Example Observation: example-oral-health

Profile: [Oral Health Assessment](StructureDefinition-onc-oral-health.md)

**status**: Final

**category**: Exam

**code**: Oral Health Score

**subject**: [Jane Doe Female, DoB Unknown](Patient-patient-example-jane.md)

**performer**: [Practitioner Nightingale](Practitioner-practitioner-example.md)

**value**: 0 {score}

> **component****code**:Lips**value**: Pink, moist

> **component****code**:Tongue**value**: Pink, moist

> **component****code**:Gums**value**: Healthy

> **component****code**:Teeth/Dentures**value**: Own teeth, good repair



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "example-oral-health",
  "meta" : {
    "profile" : ["https://fhir.clinyq.ai/StructureDefinition/onc-oral-health"]
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
        "code" : "oral-health-score"
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
    "value" : 0,
    "unit" : "{score}"
  },
  "component" : [
    {
      "code" : {
        "coding" : [
          {
            "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
            "code" : "oral-lips"
          }
        ]
      },
      "valueString" : "Pink, moist"
    },
    {
      "code" : {
        "coding" : [
          {
            "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
            "code" : "oral-tongue"
          }
        ]
      },
      "valueString" : "Pink, moist"
    },
    {
      "code" : {
        "coding" : [
          {
            "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
            "code" : "oral-gums"
          }
        ]
      },
      "valueString" : "Healthy"
    },
    {
      "code" : {
        "coding" : [
          {
            "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
            "code" : "oral-teeth"
          }
        ]
      },
      "valueString" : "Own teeth, good repair"
    }
  ]
}

```
