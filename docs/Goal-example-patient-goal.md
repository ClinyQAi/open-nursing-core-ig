# example-patient-goal - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **example-patient-goal**

## Example Goal: example-patient-goal

Profile: [Open Nursing Core Patient Goal](StructureDefinition-onc-patient-goal.md)

**lifecycleStatus**: Active

**description**: Patient will remain free from falls throughout the hospital stay.

**subject**: [John Smith Male, DoB Unknown](Patient-patient-example.md)

**addresses**: [Condition Risk of falls (finding)](Condition-example-nursing-problem.md)



## Resource Content

```json
{
  "resourceType" : "Goal",
  "id" : "example-patient-goal",
  "meta" : {
    "profile" : [
      "http://open-nursing-core.org/StructureDefinition/onc-patient-goal"
    ]
  },
  "lifecycleStatus" : "active",
  "description" : {
    "text" : "Patient will remain free from falls throughout the hospital stay."
  },
  "subject" : {
    "reference" : "Patient/patient-example"
  },
  "addresses" : [
    {
      "reference" : "Condition/example-nursing-problem"
    }
  ]
}

```
