# example-goal-evaluation - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **example-goal-evaluation**

## Example Observation: example-goal-evaluation

Profile: [Open Nursing Core Goal Evaluation](StructureDefinition-onc-goal-evaluation.md)

**Observation Goal Reference**: [Goal: lifecycleStatus = active; description =](Goal-example-patient-goal.md)

**status**: Final

**category**: nursing

**code**: Goal achieved (finding)

**subject**: [John Smith Male, DoB Unknown](Patient-patient-example.md)

**performer**: [Practitioner Florence Nightingale](Practitioner-practitioner-example.md)

**value**: Goal achieved (finding)



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "example-goal-evaluation",
  "meta" : {
    "profile" : [
      "http://open-nursing-core.org/StructureDefinition/onc-goal-evaluation"
    ]
  },
  "extension" : [
    {
      "url" : "http://open-nursing-core.org/StructureDefinition/observation-goal-reference",
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
        "display" : "Goal achieved (finding)"
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
        "code" : "385633008",
        "display" : "Goal achieved (finding)"
      }
    ]
  }
}

```
