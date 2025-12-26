# Observation Goal Reference - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Observation Goal Reference**

## Extension: Observation Goal Reference 

| | |
| :--- | :--- |
| *Official URL*:https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/observation-goal-reference | *Version*:1.0.0 |
| Active as of 2025-12-26 | *Computable Name*:ObservationGoalReference |

**Context of Use**

**Usage info**

**Usages:**

* Use this Extension: [Goal Evaluation](StructureDefinition-onc-goal-evaluation.md)
* Examples for this Extension: [Observation/example-goal-evaluation](Observation-example-goal-evaluation.md)

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
  "url" : "https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/observation-goal-reference",
  "version" : "1.0.0",
  "name" : "ObservationGoalReference",
  "title" : "Observation Goal Reference",
  "status" : "active",
  "date" : "2025-12-26T11:36:15+00:00",
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
        "short" : "Observation Goal Reference"
      },
      {
        "id" : "Extension.extension",
        "path" : "Extension.extension",
        "max" : "0"
      },
      {
        "id" : "Extension.url",
        "path" : "Extension.url",
        "fixedUri" : "https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/observation-goal-reference"
      },
      {
        "id" : "Extension.value[x]",
        "path" : "Extension.value[x]",
        "type" : [
          {
            "code" : "Reference",
            "targetProfile" : [
              "https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/onc-patient-goal"
            ]
          }
        ]
      }
    ]
  }
}

```
