# example-housing-status - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **example-housing-status**

## Example Observation: example-housing-status

Profile: [ONC Housing Status Assessment](StructureDefinition-onc-housing-status.md)

**status**: Final

**category**: nursing

**code**: Housing status

**subject**: [John Smith Male, DoB Unknown](Patient-patient-example.md)

**performer**: [Practitioner Florence Nightingale](Practitioner-practitioner-example.md)

**value**: Homeless



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "example-housing-status",
  "meta" : {
    "profile" : [
      "http://open-nursing-core.org/StructureDefinition/onc-housing-status"
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
        "code" : "71802-3",
        "display" : "Housing status"
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
  "valueCodeableConcept" : {
    "coding" : [
      {
        "system" : "http://snomed.info/sct",
        "code" : "32911000",
        "display" : "Homeless"
      }
    ]
  }
}

```
