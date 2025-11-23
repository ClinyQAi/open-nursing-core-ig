# Open Nursing Core Braden Scale Assessment - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Open Nursing Core Braden Scale Assessment**

## Resource Profile: Open Nursing Core Braden Scale Assessment 

| | |
| :--- | :--- |
| *Official URL*:http://open-nursing-core.org/StructureDefinition/onc-braden-scale-assessment | *Version*:0.1.0 |
| Draft as of 2025-11-23 | *Computable Name*:ONCBradenScaleAssessment |

 
Braden Scale assessment for pressure injury risk. 

**Usages:**

* Examples for this Profile: [Observation/example-braden-scale](Observation-example-braden-scale.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/onc.ig|current/StructureDefinition/onc-braden-scale-assessment)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-onc-braden-scale-assessment.csv), [Excel](StructureDefinition-onc-braden-scale-assessment.xlsx), [Schematron](StructureDefinition-onc-braden-scale-assessment.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "onc-braden-scale-assessment",
  "url" : "http://open-nursing-core.org/StructureDefinition/onc-braden-scale-assessment",
  "version" : "0.1.0",
  "name" : "ONCBradenScaleAssessment",
  "title" : "Open Nursing Core Braden Scale Assessment",
  "status" : "draft",
  "date" : "2025-11-23T21:00:20+00:00",
  "description" : "Braden Scale assessment for pressure injury risk.",
  "fhirVersion" : "4.0.1",
  "mapping" : [
    {
      "identity" : "workflow",
      "uri" : "http://hl7.org/fhir/workflow",
      "name" : "Workflow Pattern"
    },
    {
      "identity" : "sct-concept",
      "uri" : "http://snomed.info/conceptdomain",
      "name" : "SNOMED CT Concept Domain Binding"
    },
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
    },
    {
      "identity" : "sct-attr",
      "uri" : "http://snomed.org/attributebinding",
      "name" : "SNOMED CT Attribute Binding"
    }
  ],
  "kind" : "resource",
  "abstract" : false,
  "type" : "Observation",
  "baseDefinition" : "http://open-nursing-core.org/StructureDefinition/onc-nursing-assessment",
  "derivation" : "constraint",
  "differential" : {
    "element" : [
      {
        "id" : "Observation",
        "path" : "Observation"
      },
      {
        "id" : "Observation.code",
        "path" : "Observation.code",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "http://loinc.org",
              "code" : "9017-7",
              "display" : "Braden Scale total score"
            }
          ]
        },
        "mustSupport" : true
      },
      {
        "id" : "Observation.value[x]",
        "path" : "Observation.value[x]",
        "type" : [
          {
            "code" : "Quantity"
          }
        ]
      },
      {
        "id" : "Observation.value[x].unit",
        "path" : "Observation.value[x].unit",
        "patternString" : "{score}"
      },
      {
        "id" : "Observation.value[x].system",
        "path" : "Observation.value[x].system",
        "patternUri" : "http://unitsofmeasure.org"
      },
      {
        "id" : "Observation.component",
        "path" : "Observation.component",
        "slicing" : {
          "discriminator" : [
            {
              "type" : "pattern",
              "path" : "code"
            }
          ],
          "rules" : "open"
        },
        "min" : 6,
        "max" : "6",
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:sensoryPerception",
        "path" : "Observation.component",
        "sliceName" : "sensoryPerception",
        "min" : 1,
        "max" : "1",
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:moisture",
        "path" : "Observation.component",
        "sliceName" : "moisture",
        "min" : 1,
        "max" : "1",
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:activity",
        "path" : "Observation.component",
        "sliceName" : "activity",
        "min" : 1,
        "max" : "1",
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:mobility",
        "path" : "Observation.component",
        "sliceName" : "mobility",
        "min" : 1,
        "max" : "1",
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:nutrition",
        "path" : "Observation.component",
        "sliceName" : "nutrition",
        "min" : 1,
        "max" : "1",
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:frictionAndShear",
        "path" : "Observation.component",
        "sliceName" : "frictionAndShear",
        "min" : 1,
        "max" : "1",
        "mustSupport" : true
      }
    ]
  }
}

```
