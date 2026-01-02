# example-abc-chart - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **example-abc-chart**

## Example Observation: example-abc-chart

Profile: [PBS ABC Chart](StructureDefinition-onc-abc-chart.md)

**status**: Final

**category**: Survey

**code**: ABC Chart

**subject**: [Jane Doe Female, DoB Unknown](Patient-patient-example-jane.md)

**performer**: [Practitioner Nightingale](Practitioner-practitioner-example.md)

**value**: Frustration/Tangible

**note**: 

> 

Aggressive episode managed with de-escalation.


> **component****code**:Antecedent**value**: Denied access to garden due to rain.

> **component****code**:Behaviour**value**: Shouting and hitting door.

> **component****code**:Consequence**value**: Verbal de-escalation, distraction with music.



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "example-abc-chart",
  "meta" : {
    "profile" : ["https://fhir.clinyq.ai/StructureDefinition/onc-abc-chart"]
  },
  "status" : "final",
  "category" : [
    {
      "coding" : [
        {
          "system" : "http://terminology.hl7.org/CodeSystem/observation-category",
          "code" : "survey"
        }
      ]
    }
  ],
  "code" : {
    "coding" : [
      {
        "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
        "code" : "abc-chart"
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
  "valueCodeableConcept" : {
    "text" : "Frustration/Tangible"
  },
  "note" : [
    {
      "text" : "Aggressive episode managed with de-escalation."
    }
  ],
  "component" : [
    {
      "code" : {
        "coding" : [
          {
            "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
            "code" : "abc-antecedent"
          }
        ]
      },
      "valueString" : "Denied access to garden due to rain."
    },
    {
      "code" : {
        "coding" : [
          {
            "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
            "code" : "abc-behaviour"
          }
        ]
      },
      "valueString" : "Shouting and hitting door."
    },
    {
      "code" : {
        "coding" : [
          {
            "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
            "code" : "abc-consequence"
          }
        ]
      },
      "valueString" : "Verbal de-escalation, distraction with music."
    }
  ]
}

```
