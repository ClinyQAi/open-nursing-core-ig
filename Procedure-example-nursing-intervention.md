# example-nursing-intervention - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **example-nursing-intervention**

## Example Procedure: example-nursing-intervention

Profile: [ONC Nursing Intervention](StructureDefinition-onc-nursing-intervention.md)

**Intervention Goal Reference**: [Goal: lifecycleStatus = active; description =](Goal-example-patient-goal.md)

**status**: Completed

**code**: Procedure

**subject**: [Jane Doe Female, DoB Unknown](Patient-patient-example-jane.md)

### Performers

| | |
| :--- | :--- |
| - | **Actor** |
| * | [Practitioner Nightingale](Practitioner-practitioner-example.md) |



## Resource Content

```json
{
  "resourceType" : "Procedure",
  "id" : "example-nursing-intervention",
  "meta" : {
    "profile" : [
      "https://opennursingcoreig.com/StructureDefinition/onc-nursing-intervention"
    ]
  },
  "extension" : [
    {
      "url" : "https://opennursingcoreig.com/StructureDefinition/intervention-goal-reference",
      "valueReference" : {
        "reference" : "Goal/example-patient-goal"
      }
    }
  ],
  "status" : "completed",
  "code" : {
    "coding" : [
      {
        "system" : "http://snomed.info/sct",
        "code" : "71388002",
        "display" : "Procedure"
      }
    ]
  },
  "subject" : {
    "reference" : "Patient/patient-example-jane"
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
