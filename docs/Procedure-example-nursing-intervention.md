# example-nursing-intervention - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **example-nursing-intervention**

## Example Procedure: example-nursing-intervention

Profile: [Open Nursing Core Nursing Intervention](StructureDefinition-onc-nursing-intervention.md)

**status**: Completed

**code**: Patient Education

**subject**: [John Smith Male, DoB Unknown](Patient-patient-example.md)

### Performers

| | |
| :--- | :--- |
| - | **Actor** |
| * | [Practitioner Florence Nightingale](Practitioner-practitioner-example.md) |



## Resource Content

```json
{
  "resourceType" : "Procedure",
  "id" : "example-nursing-intervention",
  "meta" : {
    "profile" : [
      "http://open-nursing-core.org/StructureDefinition/onc-nursing-intervention"
    ]
  },
  "status" : "completed",
  "code" : {
    "coding" : [
      {
        "system" : "http://hl7.org/fhir/sid/icnp",
        "code" : "10012345",
        "display" : "Patient Education"
      }
    ]
  },
  "subject" : {
    "reference" : "Patient/patient-example"
  },
  "performer" : [
    {
      "actor" : {
        "reference" : "Practitioner/practitioner-example"
      }
    }
  ]
}

```
