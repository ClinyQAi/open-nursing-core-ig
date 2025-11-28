# example-patient-goal - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **example-patient-goal**

## Example Goal: example-patient-goal

Profile: [Patient Goal](StructureDefinition-onc-patient-goal.md)

**lifecycleStatus**: Active

**description**: Patient will remain free from falls.

**subject**: [Jane Doe Female, DoB Unknown](Patient-patient-example-jane.md)

**addresses**: [Condition Risk of falls (finding)](Condition-example-nursing-problem.md)



## Resource Content

```json
{
  "resourceType" : "Goal",
  "id" : "example-patient-goal",
  "meta" : {
    "profile" : [
      "https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/onc-patient-goal"
    ]
  },
  "lifecycleStatus" : "active",
  "description" : {
    "text" : "Patient will remain free from falls."
  },
  "subject" : {
    "reference" : "Patient/patient-example-jane"
  },
  "addresses" : [
    {
      "reference" : "Condition/example-nursing-problem"
    }
  ]
}

```
