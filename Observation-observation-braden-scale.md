# observation-braden-scale - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **observation-braden-scale**

## Example Observation: observation-braden-scale

Profile: [Braden Scale Assessment](StructureDefinition-onc-braden-scale-assessment.md)

**status**: Final

**category**: nursing

**code**: Braden scale total score

**subject**: [Jane Doe Female, DoB Unknown](Patient-patient-example-jane.md)

**performer**: [Practitioner Nightingale](Practitioner-practitioner-example.md)

**value**: 18 {score}(Details: UCUM code1 = '1')

> **component****code**:Sensory perception Braden scale**value**: 3 {score}(Details: UCUM code1 = '1')

> **component****code**:Moisture Braden scale**value**: 4 {score}(Details: UCUM code1 = '1')

> **component****code**:Activity Braden scale**value**: 2 {score}(Details: UCUM code1 = '1')

> **component****code**:Mobility Braden scale**value**: 3 {score}(Details: UCUM code1 = '1')

> **component****code**:Nutrition Braden scale**value**: 3 {score}(Details: UCUM code1 = '1')

> **component****code**:Friction and shear Braden scale**value**: 3 {score}(Details: UCUM code1 = '1')



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
        "code" : "38227-0",
        "display" : "Braden scale total score"
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
  "component" : [
    {
      "code" : {
        "coding" : [
          {
            "system" : "http://loinc.org",
            "code" : "38222-1",
            "display" : "Sensory perception Braden scale"
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
            "system" : "http://loinc.org",
            "code" : "38229-6",
            "display" : "Moisture Braden scale"
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
            "system" : "http://loinc.org",
            "code" : "38223-9",
            "display" : "Activity Braden scale"
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
            "system" : "http://loinc.org",
            "code" : "38224-7",
            "display" : "Mobility Braden scale"
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
            "system" : "http://loinc.org",
            "code" : "38225-4",
            "display" : "Nutrition Braden scale"
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
            "system" : "http://loinc.org",
            "code" : "38226-2",
            "display" : "Friction and shear Braden scale"
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
