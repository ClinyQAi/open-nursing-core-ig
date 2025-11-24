# example-nursing-care-plan - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **example-nursing-care-plan**

## Example CarePlan: example-nursing-care-plan

Profile: [Open Nursing Core Nursing Care Plan](StructureDefinition-onc-nursing-care-plan.md)

**status**: Active

**intent**: Plan

**subject**: [John Smith Male, DoB Unknown](Patient-patient-example.md)

**addresses**: [Condition Risk of falls (finding)](Condition-example-nursing-problem.md)

**goal**: [Goal: lifecycleStatus = active; description =](Goal-example-patient-goal.md)

> **activity**

### Details

| | | |
| :--- | :--- | :--- |
| - | **Code** | **Status** |
| * | Patient Education | Completed |




## Resource Content

```json
{
  "resourceType" : "CarePlan",
  "id" : "example-nursing-care-plan",
  "meta" : {
    "profile" : [
      "http://open-nursing-core.org/StructureDefinition/onc-nursing-care-plan"
    ]
  },
  "status" : "active",
  "intent" : "plan",
  "subject" : {
    "reference" : "Patient/patient-example"
  },
  "addresses" : [
    {
      "reference" : "Condition/example-nursing-problem"
    }
  ],
  "goal" : [
    {
      "reference" : "Goal/example-patient-goal"
    }
  ],
  "activity" : [
    {
      "detail" : {
        "code" : {
          "coding" : [
            {
              "system" : "http://hl7.org/fhir/sid/icnp",
              "code" : "10012345",
              "display" : "Patient Education"
            }
          ]
        },
        "status" : "completed"
      }
    }
  ]
}

```
