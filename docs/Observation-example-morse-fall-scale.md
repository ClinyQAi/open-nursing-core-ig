# example-morse-fall-scale - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **example-morse-fall-scale**

## Example Observation: example-morse-fall-scale

Profile: [ONC Morse Fall Scale Assessment](StructureDefinition-onc-morse-fall-scale.md)

**status**: Final

**category**: nursing

**code**: Morse Fall Scale total score

**subject**: [John Smith Male, DoB Unknown](Patient-patient-example.md)

**performer**: [Practitioner Florence Nightingale](Practitioner-practitioner-example.md)

**value**: 70 {score}(Details: UCUM code{score} = '{score}')

> **component****code**:Fall risk level [Morse Fall Scale]**value**: 25 {score}(Details: UCUM code{score} = '{score}')

> **component****code**:Clinical biochemist review of results**value**: 15 {score}(Details: UCUM code{score} = '{score}')

> **component****code**:Lymphocytes/Leukocytes in Dialysis fluid**value**: 0 {score}(Details: UCUM code{score} = '{score}')

> **component****code**:Microbiologist review of results**value**: 20 {score}(Details: UCUM code{score} = '{score}')

> **component****code**:Pathologist review of results**value**: 10 {score}(Details: UCUM code{score} = '{score}')

> **component****code**:Hematologist review of results**value**: 0 {score}(Details: UCUM code{score} = '{score}')



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "example-morse-fall-scale",
  "meta" : {
    "profile" : [
      "http://open-nursing-core.org/StructureDefinition/onc-morse-fall-scale"
    ]
  },
  "status" : "final",
  "category" : [
    {
      "coding" : [
        {
          "system" : "http://terminology.hl7.org/CodeSystem/observation-category",
          "code" : "nursing"
        }
      ]
    }
  ],
  "code" : {
    "coding" : [
      {
        "system" : "http://loinc.org",
        "code" : "59460-6",
        "display" : "Morse Fall Scale total score"
      }
    ]
  },
  "subject" : {
    "reference" : "Patient/patient-example"
  },
  "performer" : [
    {
      "reference" : "Practitioner/practitioner-example"
    }
  ],
  "valueQuantity" : {
    "value" : 70,
    "system" : "http://unitsofmeasure.org",
    "code" : "{score}"
  },
  "component" : [
    {
      "code" : {
        "coding" : [
          {
            "system" : "http://loinc.org",
            "code" : "59461-4"
          }
        ]
      },
      "valueQuantity" : {
        "value" : 25,
        "system" : "http://unitsofmeasure.org",
        "code" : "{score}"
      }
    },
    {
      "code" : {
        "coding" : [
          {
            "system" : "http://loinc.org",
            "code" : "59462-2"
          }
        ]
      },
      "valueQuantity" : {
        "value" : 15,
        "system" : "http://unitsofmeasure.org",
        "code" : "{score}"
      }
    },
    {
      "code" : {
        "coding" : [
          {
            "system" : "http://loinc.org",
            "code" : "59463-0"
          }
        ]
      },
      "valueQuantity" : {
        "value" : 0,
        "system" : "http://unitsofmeasure.org",
        "code" : "{score}"
      }
    },
    {
      "code" : {
        "coding" : [
          {
            "system" : "http://loinc.org",
            "code" : "59464-8"
          }
        ]
      },
      "valueQuantity" : {
        "value" : 20,
        "system" : "http://unitsofmeasure.org",
        "code" : "{score}"
      }
    },
    {
      "code" : {
        "coding" : [
          {
            "system" : "http://loinc.org",
            "code" : "59465-5"
          }
        ]
      },
      "valueQuantity" : {
        "value" : 10,
        "system" : "http://unitsofmeasure.org",
        "code" : "{score}"
      }
    },
    {
      "code" : {
        "coding" : [
          {
            "system" : "http://loinc.org",
            "code" : "59466-3"
          }
        ]
      },
      "valueQuantity" : {
        "value" : 0,
        "system" : "http://unitsofmeasure.org",
        "code" : "{score}"
      }
    }
  ]
}

```
