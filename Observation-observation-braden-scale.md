# observation-braden-scale - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **observation-braden-scale**

## Example Observation: observation-braden-scale

Profile: [Braden Scale Assessment](StructureDefinition-onc-braden-scale-assessment.md)

**status**: Final

**category**: nursing

**code**: Braden Scale total score

**subject**: [Jane Doe Female, DoB Unknown](Patient-patient-example-jane.md)

**performer**: [Practitioner Nightingale](Practitioner-practitioner-example.md)

**value**: 18 score(Details: UCUM codescore = 'score')

> **component****code**:Sensory Perception**value**: 3 score(Details: UCUM codescore = 'score')

> **component****code**:Moisture**value**: 4 score(Details: UCUM codescore = 'score')

> **component****code**:Activity**value**: 2 score(Details: UCUM codescore = 'score')

> **component****code**:Mobility**value**: 3 score(Details: UCUM codescore = 'score')

> **component****code**:Nutrition**value**: 3 score(Details: UCUM codescore = 'score')

> **component****code**:Friction and Shear**value**: 3 score(Details: UCUM codescore = 'score')



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
          "code" : "nursing"
        }
      ]
    }
  ],
  "code" : {
    "coding" : [
      {
        "system" : "http://loinc.org",
        "code" : "9017-7",
        "display" : "Braden Scale total score"
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
    "unit" : "score",
    "system" : "http://unitsofmeasure.org",
    "code" : "score"
  },
  "component" : [
    {
      "code" : {
        "coding" : [
          {
            "system" : "http://loinc.org",
            "code" : "74012-8",
            "display" : "Sensory Perception"
          }
        ]
      },
      "valueQuantity" : {
        "value" : 3,
        "unit" : "score",
        "system" : "http://unitsofmeasure.org",
        "code" : "score"
      }
    },
    {
      "code" : {
        "coding" : [
          {
            "system" : "http://loinc.org",
            "code" : "74013-6",
            "display" : "Moisture"
          }
        ]
      },
      "valueQuantity" : {
        "value" : 4,
        "unit" : "score",
        "system" : "http://unitsofmeasure.org",
        "code" : "score"
      }
    },
    {
      "code" : {
        "coding" : [
          {
            "system" : "http://loinc.org",
            "code" : "74014-4",
            "display" : "Activity"
          }
        ]
      },
      "valueQuantity" : {
        "value" : 2,
        "unit" : "score",
        "system" : "http://unitsofmeasure.org",
        "code" : "score"
      }
    },
    {
      "code" : {
        "coding" : [
          {
            "system" : "http://loinc.org",
            "code" : "74015-1",
            "display" : "Mobility"
          }
        ]
      },
      "valueQuantity" : {
        "value" : 3,
        "unit" : "score",
        "system" : "http://unitsofmeasure.org",
        "code" : "score"
      }
    },
    {
      "code" : {
        "coding" : [
          {
            "system" : "http://loinc.org",
            "code" : "74016-9",
            "display" : "Nutrition"
          }
        ]
      },
      "valueQuantity" : {
        "value" : 3,
        "unit" : "score",
        "system" : "http://unitsofmeasure.org",
        "code" : "score"
      }
    },
    {
      "code" : {
        "coding" : [
          {
            "system" : "http://loinc.org",
            "code" : "74017-7",
            "display" : "Friction and Shear"
          }
        ]
      },
      "valueQuantity" : {
        "value" : 3,
        "unit" : "score",
        "system" : "http://unitsofmeasure.org",
        "code" : "score"
      }
    }
  ]
}

```
