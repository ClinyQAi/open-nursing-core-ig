# Intervention Goal Reference - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Intervention Goal Reference**

## Extension: Intervention Goal Reference 

| | |
| :--- | :--- |
| *Official URL*:https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/intervention-goal-reference | *Version*:1.0.0 |
| Active as of 2025-12-25 | *Computable Name*:InterventionGoalReference |

**Context of Use**

**Usage info**

**Usages:**

* Use this Extension: [Nursing Intervention](StructureDefinition-onc-nursing-intervention.md)
* Examples for this Extension: [Procedure/example-nursing-intervention](Procedure-example-nursing-intervention.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/onc.ig|current/StructureDefinition/intervention-goal-reference)

### Formal Views of Extension Content

 [Description of Profiles, Differentials, Snapshots, and how the XML and JSON presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-intervention-goal-reference.csv), [Excel](StructureDefinition-intervention-goal-reference.xlsx), [Schematron](StructureDefinition-intervention-goal-reference.sch) 

#### Constraints



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "intervention-goal-reference",
  "url" : "https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/intervention-goal-reference",
  "version" : "1.0.0",
  "name" : "InterventionGoalReference",
  "title" : "Intervention Goal Reference",
  "status" : "active",
  "date" : "2025-12-25T23:47:50+00:00",
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
        "short" : "Intervention Goal Reference"
      },
      {
        "id" : "Extension.extension",
        "path" : "Extension.extension",
        "max" : "0"
      },
      {
        "id" : "Extension.url",
        "path" : "Extension.url",
        "fixedUri" : "https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/intervention-goal-reference"
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
