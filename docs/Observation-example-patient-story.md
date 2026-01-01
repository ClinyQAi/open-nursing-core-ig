# example-patient-story - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **example-patient-story**

## Example Observation: example-patient-story

Profile: [Patient Story](StructureDefinition-onc-patient-story.md)

**status**: Final

**category**: Social History

**code**: Patient Story

**subject**: [Jane Doe Female, DoB Unknown](Patient-patient-example-jane.md)

**performer**: [Practitioner Nightingale](Practitioner-practitioner-example.md)

**value**: Jane was a librarian for 40 years. She loves classical music and gardening. She lost her husband 2 years ago.



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "example-patient-story",
  "meta" : {
    "profile" : [
      "https://fhir.clinyq.ai/StructureDefinition/onc-patient-story"
    ]
  },
  "status" : "final",
  "category" : [
    {
      "coding" : [
        {
          "system" : "http://terminology.hl7.org/CodeSystem/observation-category",
          "code" : "social-history"
        }
      ]
    }
  ],
  "code" : {
    "coding" : [
      {
        "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
        "code" : "patient-story"
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
  "valueString" : "Jane was a librarian for 40 years. She loves classical music and gardening. She lost her husband 2 years ago."
}

```
