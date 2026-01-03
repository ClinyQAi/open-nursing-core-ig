# Observation Goal Reference - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Observation Goal Reference**

## Extension: Observation Goal Reference 

| | |
| :--- | :--- |
| *Official URL*:https://opennursingcoreig.com/StructureDefinition/observation-goal-reference | *Version*:0.1.0 |
| Draft as of 2026-01-03 | *Computable Name*:ObservationGoalReference |

Extension to link goal evaluation observations to the patient goals being evaluated.

**Context of Use**

**Usage info**

**Usages:**

* Use this Extension: [ONC Goal Evaluation](StructureDefinition-onc-goal-evaluation.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/onc.ig|current/StructureDefinition/observation-goal-reference)

### Formal Views of Extension Content

 [Description of Profiles, Differentials, Snapshots, and how the XML and JSON presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-observation-goal-reference.csv), [Excel](StructureDefinition-observation-goal-reference.xlsx), [Schematron](StructureDefinition-observation-goal-reference.sch) 

#### Constraints



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "observation-goal-reference",
  "url" : "https://opennursingcoreig.com/StructureDefinition/observation-goal-reference",
  "version" : "0.1.0",
  "name" : "ObservationGoalReference",
  "title" : "Observation Goal Reference",
  "status" : "draft",
  "date" : "2026-01-03T01:44:04+00:00",
  "publisher" : "The Open Nursing Community",
  "description" : "Extension to link goal evaluation observations to the patient goals being evaluated.",
  "fhirVersion" : "4.0.1",
  "mapping" : [
    {
      "identity" : "rim",
      "uri" : "http://hl7.org/v3",
      "name" : "RIM Mapping"
    }
  ],
  "kind" : "complex-type",
  "abstract" : false,
  "context" : [
    {
      "type" : "element",
      "expression" : "Element"
    }
  ],
  "type" : "Extension",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Extension",
  "derivation" : "constraint",
  "differential" : {
    "element" : [
      {
        "id" : "Extension",
        "path" : "Extension",
        "short" : "Observation Goal Reference",
        "definition" : "Extension to link goal evaluation observations to the patient goals being evaluated."
      },
      {
        "id" : "Extension.extension",
        "path" : "Extension.extension",
        "max" : "0"
      },
      {
        "id" : "Extension.url",
        "path" : "Extension.url",
        "fixedUri" : "https://opennursingcoreig.com/StructureDefinition/observation-goal-reference"
      },
      {
        "id" : "Extension.value[x]",
        "path" : "Extension.value[x]",
        "type" : [
          {
            "code" : "Reference",
            "targetProfile" : [
              "https://opennursingcoreig.com/StructureDefinition/onc-nursing-goal"
            ]
          }
        ]
      }
    ]
  }
}

```
