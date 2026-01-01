# example-mental-capacity - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **example-mental-capacity**

## Example Observation: example-mental-capacity

Profile: [Mental Capacity Assessment](StructureDefinition-onc-mental-capacity.md)

**status**: Final

**category**: Exam

**code**: Mental Capacity Assessment

**subject**: [Jane Doe Female, DoB Unknown](Patient-patient-example-jane.md)

**performer**: [Practitioner Nightingale](Practitioner-practitioner-example.md)

**value**: Capacity Present

**note**: 

> 

Assessment for decision to return home.




## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "example-mental-capacity",
  "meta" : {
    "profile" : [
      "https://fhir.clinyq.ai/StructureDefinition/onc-mental-capacity"
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
        "code" : "mca-assessment"
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
        "code" : "mca-present",
        "display" : "Capacity Present"
      }
    ]
  },
  "note" : [
    {
      "text" : "Assessment for decision to return home."
    }
  ]
}

```
