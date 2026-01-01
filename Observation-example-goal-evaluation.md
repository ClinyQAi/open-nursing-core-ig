# example-goal-evaluation - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **example-goal-evaluation**

## Example Observation: example-goal-evaluation

Profile: [ONC Goal Evaluation](StructureDefinition-onc-goal-evaluation.md)

**status**: Final

**category**: Survey

**code**: Follow-up assessment

**subject**: [Jane Doe Female, DoB Unknown](Patient-patient-example-jane.md)

**focus**: [Goal: lifecycleStatus = active; description =](Goal-example-patient-goal.md)

**performer**: [Practitioner Nightingale](Practitioner-practitioner-example.md)

**value**: Objective achieved



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
        "system" : "http://snomed.info/sct",
        "code" : "390906007",
        "display" : "Follow-up assessment"
      }
    ]
  },
  "subject" : {
    "reference" : "Patient/patient-example-jane"
  },
  "focus" : [
    {
      "reference" : "Goal/example-patient-goal"
    }
  ],
  "performer" : [
    {
      "reference" : "Practitioner/practitioner-example"
    }
  ],
  "valueCodeableConcept" : {
    "coding" : [
      {
        "system" : "http://snomed.info/sct",
        "code" : "385652002",
        "display" : "Objective achieved"
      }
    ]
  }
}

```
