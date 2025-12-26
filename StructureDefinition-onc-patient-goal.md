# Patient Goal - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Patient Goal**

## Resource Profile: Patient Goal 

| | |
| :--- | :--- |
| *Official URL*:https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/onc-patient-goal | *Version*:0.1.0 |
| Draft as of 2025-12-26 | *Computable Name*:ONCPatientGoal |

 
Patient-centered goal established in response to identified nursing problems. Defines measurable outcomes and addresses specific nursing diagnoses. Part of the ADPIE framework's Planning phase. 

**Usages:**

* Refer to this Profile: [Intervention Goal Reference](StructureDefinition-intervention-goal-reference.md) and [Observation Goal Reference](StructureDefinition-observation-goal-reference.md)
* Examples for this Profile: [Goal/example-patient-goal](Goal-example-patient-goal.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/onc.ig|current/StructureDefinition/onc-patient-goal)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-onc-patient-goal.csv), [Excel](StructureDefinition-onc-patient-goal.xlsx), [Schematron](StructureDefinition-onc-patient-goal.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "onc-patient-goal",
  "url" : "https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/onc-patient-goal",
  "version" : "0.1.0",
  "name" : "ONCPatientGoal",
  "title" : "Patient Goal",
  "status" : "draft",
  "date" : "2025-12-26T15:08:13+00:00",
  "description" : "Patient-centered goal established in response to identified nursing problems. Defines measurable outcomes and addresses specific nursing diagnoses. Part of the ADPIE framework's Planning phase.",
  "fhirVersion" : "4.0.1",
  "mapping" : [
    {
      "identity" : "v2",
      "uri" : "http://hl7.org/v2",
      "name" : "HL7 v2 Mapping"
    },
    {
      "identity" : "rim",
      "uri" : "http://hl7.org/v3",
      "name" : "RIM Mapping"
    },
    {
      "identity" : "w5",
      "uri" : "http://hl7.org/fhir/fivews",
      "name" : "FiveWs Pattern Mapping"
    }
  ],
  "kind" : "resource",
  "abstract" : false,
  "type" : "Goal",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Goal",
  "derivation" : "constraint",
  "differential" : {
    "element" : [
      {
        "id" : "Goal",
        "path" : "Goal"
      },
      {
        "id" : "Goal.lifecycleStatus",
        "path" : "Goal.lifecycleStatus",
        "mustSupport" : true
      },
      {
        "id" : "Goal.description",
        "path" : "Goal.description",
        "mustSupport" : true
      },
      {
        "id" : "Goal.addresses",
        "path" : "Goal.addresses",
        "min" : 1,
        "type" : [
          {
            "code" : "Reference",
            "targetProfile" : [
              "https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/onc-nursing-problem"
            ]
          }
        ],
        "mustSupport" : true
      }
    ]
  }
}

```
