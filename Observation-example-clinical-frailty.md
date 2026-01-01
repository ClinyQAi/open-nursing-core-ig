# example-clinical-frailty - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **example-clinical-frailty**

## Example Observation: example-clinical-frailty

Profile: [Clinical Frailty Scale (CFS)](StructureDefinition-onc-clinical-frailty-scale.md)

**status**: Final

**category**: Exam

**code**: Clinical Frailty Scale Score

**subject**: [Jane Doe Female, DoB Unknown](Patient-patient-example-jane.md)

**performer**: [Practitioner Nightingale](Practitioner-practitioner-example.md)

**value**: Mildly Frail

**note**: 

> 

Mildly Frail - slowing up, needs help with high order IADLs




## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "example-clinical-frailty",
  "meta" : {
    "profile" : [
      "https://fhir.clinyq.ai/StructureDefinition/onc-clinical-frailty-scale"
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
        "code" : "cfs-score"
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
    "coding" : [
      {
        "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
        "code" : "cfs-5",
        "display" : "Mildly Frail"
      }
    ]
  },
  "note" : [
    {
      "text" : "Mildly Frail - slowing up, needs help with high order IADLs"
    }
  ]
}

```
