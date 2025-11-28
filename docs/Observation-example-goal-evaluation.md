# example-goal-evaluation - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **example-goal-evaluation**

## Example Observation: example-goal-evaluation

Profile: [Goal Evaluation](StructureDefinition-onc-goal-evaluation.md)

**Observation Goal Reference**: [Goal: lifecycleStatus = active; description =](Goal-example-patient-goal.md)

**status**: Final

**category**: nursing

**code**: Goal achieved

**subject**: [Jane Doe Female, DoB Unknown](Patient-patient-example-jane.md)

**performer**: [Practitioner Nightingale](Practitioner-practitioner-example.md)

**value**: Goal achieved



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "example-goal-evaluation",
  "meta" : {
    "profile" : [
      "https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/onc-goal-evaluation"
    ]
  },
  "extension" : [
    {
      "url" : "https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/observation-goal-reference",
      "valueReference" : {
        "reference" : "Goal/example-patient-goal"
      }
    }
  ],
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
        "system" : "http://snomed.info/sct",
        "code" : "385633008",
        "display" : "Goal achieved"
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
        "code" : "385633008",
        "display" : "Goal achieved"
      }
    ]
  }
}

```
