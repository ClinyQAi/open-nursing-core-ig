# example-bristol-stool - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **example-bristol-stool**

## Example Observation: example-bristol-stool

Profile: [Bristol Stool Chart](StructureDefinition-onc-bristol-stool-chart.md)

**status**: Final

**category**: Survey

**code**: Bristol Stool Score

**subject**: [Jane Doe Female, DoB Unknown](Patient-patient-example-jane.md)

**performer**: [Practitioner Nightingale](Practitioner-practitioner-example.md)

**value**: 4 {score}



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "example-bristol-stool",
  "meta" : {
    "profile" : [
      "https://fhir.clinyq.ai/StructureDefinition/onc-bristol-stool-chart"
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
        "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
        "code" : "bristol-score"
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
    "value" : 4,
    "unit" : "{score}"
  }
}

```
