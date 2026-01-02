# example-patient-goal - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **example-patient-goal**

## Example Goal: example-patient-goal

Profile: [ONC Nursing Goal](StructureDefinition-onc-nursing-goal.md)

**lifecycleStatus**: Active

**description**: Patient will remain free from falls.

**subject**: [Jane Doe Female, DoB Unknown](Patient-patient-example-jane.md)

### Targets

| | | | |
| :--- | :--- | :--- | :--- |
| - | **Measure** | **Detail[x]** | **Due[x]** |
| * | Functional status | Objective achieved | 2025-12-31 |

**addresses**: [Condition Risk of falls](Condition-example-nursing-problem.md)



## Resource Content

```json
{
  "resourceType" : "Goal",
  "id" : "example-patient-goal",
  "meta" : {
    "profile" : [
      "https://opennursingcoreig.com/StructureDefinition/onc-nursing-goal"
    ]
  },
  "lifecycleStatus" : "active",
  "description" : {
    "text" : "Patient will remain free from falls."
  },
  "subject" : {
    "reference" : "Patient/patient-example-jane"
  },
  "target" : [
    {
      "measure" : {
        "coding" : [
          {
            "system" : "http://loinc.org",
            "code" : "88020-3",
            "display" : "Functional status"
          }
        ]
      },
      "detailCodeableConcept" : {
        "coding" : [
          {
            "system" : "http://snomed.info/sct",
            "code" : "385652002",
            "display" : "Objective achieved"
          }
        ]
      },
      "dueDate" : "2025-12-31"
    }
  ],
  "addresses" : [
    {
      "reference" : "Condition/example-nursing-problem"
    }
  ]
}

```
