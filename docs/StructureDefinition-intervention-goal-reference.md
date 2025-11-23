# Intervention Goal Reference - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Intervention Goal Reference**

## Extension: Intervention Goal Reference 

| | |
| :--- | :--- |
| *Official URL*:http://open-nursing-core.org/StructureDefinition/intervention-goal-reference | *Version*:0.1.0 |
| Draft as of 2025-11-23 | *Computable Name*:InterventionGoalReference |

Reference to the goal this intervention addresses.

**Context of Use**

**Usage info**

**Usages:**

* Use this Extension: [Open Nursing Core Nursing Intervention](StructureDefinition-onc-nursing-intervention.md)

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
  "url" : "http://open-nursing-core.org/StructureDefinition/intervention-goal-reference",
  "version" : "0.1.0",
  "name" : "InterventionGoalReference",
  "title" : "Intervention Goal Reference",
  "status" : "draft",
  "date" : "2025-11-23T02:33:16+00:00",
  "description" : "Reference to the goal this intervention addresses.",
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
        "short" : "Intervention Goal Reference",
        "definition" : "Reference to the goal this intervention addresses."
      },
      {
        "id" : "Extension.extension",
        "path" : "Extension.extension",
        "max" : "0"
      },
      {
        "id" : "Extension.url",
        "path" : "Extension.url",
        "fixedUri" : "http://open-nursing-core.org/StructureDefinition/intervention-goal-reference"
      },
      {
        "id" : "Extension.value[x]",
        "path" : "Extension.value[x]",
        "type" : [
          {
            "code" : "Reference",
            "targetProfile" : [
              "http://open-nursing-core.org/StructureDefinition/onc-patient-goal"
            ]
          }
        ]
      }
    ]
  }
}

```
