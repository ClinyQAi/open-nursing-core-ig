# example-news2-assessment - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **example-news2-assessment**

## Example Observation: example-news2-assessment

Profile: [ONC NEWS2 Assessment](StructureDefinition-onc-news2-assessment.md)

**status**: Final

**category**: nursing

**code**: NEWS2 total score

**subject**: [John Smith Male, DoB Unknown](Patient-patient-example.md)

**performer**: [Practitioner Florence Nightingale](Practitioner-practitioner-example.md)

**value**: 5 {score}(Details: UCUM code{score} = '{score}')

> **component****code**:Respiratory rate**value**: 22 /min(Details: UCUM code/min = '/min')

> **component****code**:Oxygen saturation in Arterial blood**value**: 95 %(Details: UCUM code% = '%')

> **component****code**:Body temperature**value**: 38.5 Cel(Details: UCUM codeCel = 'Cel')

> **component****code**:Systolic blood pressure**value**: 100 mm[Hg](Details: UCUM codemm[Hg] = 'mm[Hg]')

> **component****code**:Heart rate**value**: 100 /min(Details: UCUM code/min = '/min')

> **component****code**:11454-5**value**:Mentally alert

> **component****code**:t(15;17)(q24.1;q21.1)(PML,RARA) fusion transcript/control transcript [# Ratio] in Blood or Tissue by Molecular genetics method**value**:Yes



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "example-news2-assessment",
  "meta" : {
    "profile" : [
      "http://open-nursing-core.org/StructureDefinition/onc-news2-assessment"
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
        "code" : "86585-7",
        "display" : "NEWS2 total score"
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
    "value" : 5,
    "system" : "http://unitsofmeasure.org",
    "code" : "{score}"
  },
  "component" : [
    {
      "code" : {
        "coding" : [
          {
            "system" : "http://loinc.org",
            "code" : "9279-1"
          }
        ]
      },
      "valueQuantity" : {
        "value" : 22,
        "system" : "http://unitsofmeasure.org",
        "code" : "/min"
      }
    },
    {
      "code" : {
        "coding" : [
          {
            "system" : "http://loinc.org",
            "code" : "2708-6"
          }
        ]
      },
      "valueQuantity" : {
        "value" : 95,
        "system" : "http://unitsofmeasure.org",
        "code" : "%"
      }
    },
    {
      "code" : {
        "coding" : [
          {
            "system" : "http://loinc.org",
            "code" : "8310-5"
          }
        ]
      },
      "valueQuantity" : {
        "value" : 38.5,
        "system" : "http://unitsofmeasure.org",
        "code" : "Cel"
      }
    },
    {
      "code" : {
        "coding" : [
          {
            "system" : "http://loinc.org",
            "code" : "8480-6"
          }
        ]
      },
      "valueQuantity" : {
        "value" : 100,
        "system" : "http://unitsofmeasure.org",
        "code" : "mm[Hg]"
      }
    },
    {
      "code" : {
        "coding" : [
          {
            "system" : "http://loinc.org",
            "code" : "8867-4"
          }
        ]
      },
      "valueQuantity" : {
        "value" : 100,
        "system" : "http://unitsofmeasure.org",
        "code" : "/min"
      }
    },
    {
      "code" : {
        "coding" : [
          {
            "system" : "http://loinc.org",
            "code" : "11454-5"
          }
        ]
      },
      "valueCodeableConcept" : {
        "coding" : [
          {
            "system" : "http://snomed.info/sct",
            "code" : "248234008",
            "display" : "Mentally alert"
          }
        ]
      }
    },
    {
      "code" : {
        "coding" : [
          {
            "system" : "http://loinc.org",
            "code" : "72274-4"
          }
        ]
      },
      "valueCodeableConcept" : {
        "coding" : [
          {
            "system" : "http://snomed.info/sct",
            "code" : "373066001",
            "display" : "Yes"
          }
        ]
      }
    }
  ]
}

```
