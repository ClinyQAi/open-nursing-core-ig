# observation-braden-scale - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **observation-braden-scale**

## Example Observation: observation-braden-scale

Profile: [Braden Scale Assessment](StructureDefinition-onc-braden-scale-assessment.md)

**status**: Final

**category**: Survey

**code**: Braden Total Score

**subject**: [Jane Doe Female, DoB Unknown](Patient-patient-example-jane.md)

**performer**: [Practitioner Nightingale](Practitioner-practitioner-example.md)

**value**: 18 {score}(Details: UCUM code1 = '1')

**hasMember**: [Observation Skin type [Fitzpatrick Classification Scale]](Observation-observation-skin-tone.md)

> **component****code**:Braden Sensory Perception**value**: 3 {score}(Details: UCUM code1 = '1')

> **component****code**:Braden Moisture**value**: 4 {score}(Details: UCUM code1 = '1')

> **component****code**:Braden Activity**value**: 2 {score}(Details: UCUM code1 = '1')

> **component****code**:Braden Mobility**value**: 3 {score}(Details: UCUM code1 = '1')

> **component****code**:Braden Nutrition**value**: 3 {score}(Details: UCUM code1 = '1')

> **component****code**:Braden Friction/Shear**value**: 3 {score}(Details: UCUM code1 = '1')



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "observation-braden-scale",
  "meta" : {
    "profile" : [
      "https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/onc-braden-scale-assessment"
    ]
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
        "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
        "code" : "braden-total-score",
        "display" : "Braden Total Score"
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
    "value" : 18,
    "unit" : "{score}",
    "system" : "http://unitsofmeasure.org",
    "code" : "1"
  },
  "hasMember" : [
    {
      "reference" : "Observation/observation-skin-tone"
    }
  ],
  "component" : [
    {
      "code" : {
        "coding" : [
          {
            "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
            "code" : "braden-sensory",
            "display" : "Braden Sensory Perception"
          }
        ]
      },
      "valueQuantity" : {
        "value" : 3,
        "unit" : "{score}",
        "system" : "http://unitsofmeasure.org",
        "code" : "1"
      }
    },
    {
      "code" : {
        "coding" : [
          {
            "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
            "code" : "braden-moisture",
            "display" : "Braden Moisture"
          }
        ]
      },
      "valueQuantity" : {
        "value" : 4,
        "unit" : "{score}",
        "system" : "http://unitsofmeasure.org",
        "code" : "1"
      }
    },
    {
      "code" : {
        "coding" : [
          {
            "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
            "code" : "braden-activity",
            "display" : "Braden Activity"
          }
        ]
      },
      "valueQuantity" : {
        "value" : 2,
        "unit" : "{score}",
        "system" : "http://unitsofmeasure.org",
        "code" : "1"
      }
    },
    {
      "code" : {
        "coding" : [
          {
            "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
            "code" : "braden-mobility",
            "display" : "Braden Mobility"
          }
        ]
      },
      "valueQuantity" : {
        "value" : 3,
        "unit" : "{score}",
        "system" : "http://unitsofmeasure.org",
        "code" : "1"
      }
    },
    {
      "code" : {
        "coding" : [
          {
            "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
            "code" : "braden-nutrition",
            "display" : "Braden Nutrition"
          }
        ]
      },
      "valueQuantity" : {
        "value" : 3,
        "unit" : "{score}",
        "system" : "http://unitsofmeasure.org",
        "code" : "1"
      }
    },
    {
      "code" : {
        "coding" : [
          {
            "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
            "code" : "braden-friction",
            "display" : "Braden Friction/Shear"
          }
        ]
      },
      "valueQuantity" : {
        "value" : 3,
        "unit" : "{score}",
        "system" : "http://unitsofmeasure.org",
        "code" : "1"
      }
    }
  ]
}

```
