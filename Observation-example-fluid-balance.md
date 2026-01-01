# example-fluid-balance - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **example-fluid-balance**

## Example Observation: example-fluid-balance

Profile: [Fluid Balance](StructureDefinition-onc-fluid-balance.md)

**status**: Final

**category**: Exam

**code**: Fluid Balance

**subject**: [Jane Doe Female, DoB Unknown](Patient-patient-example-jane.md)

**performer**: [Practitioner Nightingale](Practitioner-practitioner-example.md)

**value**: 500 mL

> **component****code**:Total Fluid Input**value**: 2000 mL

> **component****code**:Total Fluid Output**value**: 1500 mL



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "example-fluid-balance",
  "meta" : {
    "profile" : [
      "https://fhir.clinyq.ai/StructureDefinition/onc-fluid-balance"
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
        "code" : "fluid-balance"
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
    "value" : 500,
    "unit" : "mL"
  },
  "component" : [
    {
      "code" : {
        "coding" : [
          {
            "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
            "code" : "fluid-input-total"
          }
        ]
      },
      "valueQuantity" : {
        "value" : 2000,
        "unit" : "mL"
      }
    },
    {
      "code" : {
        "coding" : [
          {
            "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
            "code" : "fluid-output-total"
          }
        ]
      },
      "valueQuantity" : {
        "value" : 1500,
        "unit" : "mL"
      }
    }
  ]
}

```
