# observation-skin-tone - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **observation-skin-tone**

## Example Observation: observation-skin-tone

Profile: [Skin Tone Observation](StructureDefinition-onc-skintone-observation.md)

**status**: Final

**category**: Survey

**code**: Skin type [Fitzpatrick Classification Scale]

**subject**: [Jane Doe Female, DoB Unknown](Patient-patient-example-jane.md)

**performer**: [Practitioner Nightingale](Practitioner-practitioner-example.md)

**value**: Fitzpatrick skin type II



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "observation-skin-tone",
  "meta" : {
    "profile" : [
      "https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/onc-skintone-observation"
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
        "system" : "http://loinc.org",
        "code" : "66555-4",
        "display" : "Skin type [Fitzpatrick Classification Scale]"
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
        "system" : "http://snomed.info/sct",
        "code" : "403154004",
        "display" : "Fitzpatrick skin type II"
      }
    ]
  }
}

```
