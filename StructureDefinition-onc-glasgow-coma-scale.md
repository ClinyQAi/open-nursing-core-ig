# Glasgow Coma Scale - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Glasgow Coma Scale**

## Resource Profile: Glasgow Coma Scale 

| | |
| :--- | :--- |
| *Official URL*:https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/onc-glasgow-coma-scale | *Version*:1.0.0 |
| Active as of 2025-12-26 | *Computable Name*:ONCGlasgowComaScale |

 
Glasgow Coma Scale (GCS) for assessing level of consciousness. Total score 3-15 with three required components: Eye (1-4), Verbal (1-5), Motor (1-6). 

**Usages:**

* This Profile is not used by any profiles in this Implementation Guide

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/onc.ig|current/StructureDefinition/onc-glasgow-coma-scale)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-onc-glasgow-coma-scale.csv), [Excel](StructureDefinition-onc-glasgow-coma-scale.xlsx), [Schematron](StructureDefinition-onc-glasgow-coma-scale.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "onc-glasgow-coma-scale",
  "url" : "https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/onc-glasgow-coma-scale",
  "version" : "1.0.0",
  "name" : "ONCGlasgowComaScale",
  "title" : "Glasgow Coma Scale",
  "status" : "active",
  "date" : "2025-12-26T12:02:28+00:00",
  "description" : "Glasgow Coma Scale (GCS) for assessing level of consciousness. Total score 3-15 with three required components: Eye (1-4), Verbal (1-5), Motor (1-6).",
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
  "baseDefinition" : "https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/onc-nursing-assessment",
  "derivation" : "constraint",
  "differential" : {
    "element" : [
      {
        "id" : "Observation",
        "path" : "Observation"
      },
      {
        "id" : "Observation.status",
        "path" : "Observation.status",
        "mustSupport" : true
      },
      {
        "id" : "Observation.code",
        "path" : "Observation.code",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "http://loinc.org",
              "code" : "9269-2",
              "display" : "Glasgow coma score total"
            }
          ]
        },
        "mustSupport" : true
      },
      {
        "id" : "Observation.value[x]",
        "path" : "Observation.value[x]",
        "short" : "GCS total score (3-15)",
        "type" : [
          {
            "code" : "Quantity"
          }
        ]
      },
      {
        "id" : "Observation.value[x].value",
        "path" : "Observation.value[x].value",
        "constraint" : [
          {
            "key" : "gcs-total-range",
            "severity" : "error",
            "human" : "GCS total score must be between 3 and 15",
            "expression" : "$this >= 3 and $this <= 15",
            "source" : "https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/onc-glasgow-coma-scale"
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
          "ordered" : false,
          "rules" : "open"
        },
        "min" : 3,
        "max" : "3",
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:eye",
        "path" : "Observation.component",
        "sliceName" : "eye",
        "min" : 1,
        "max" : "1",
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:eye.code",
        "path" : "Observation.component.code",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "http://loinc.org",
              "code" : "9267-6",
              "display" : "Glasgow coma score eye opening"
            }
          ]
        }
      },
      {
        "id" : "Observation.component:eye.value[x]",
        "path" : "Observation.component.value[x]",
        "type" : [
          {
            "code" : "Quantity"
          }
        ]
      },
      {
        "id" : "Observation.component:eye.value[x].value",
        "path" : "Observation.component.value[x].value",
        "constraint" : [
          {
            "key" : "gcs-eye-range",
            "severity" : "error",
            "human" : "GCS eye response must be between 1 and 4",
            "expression" : "$this >= 1 and $this <= 4",
            "source" : "https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/onc-glasgow-coma-scale"
          }
        ]
      },
      {
        "id" : "Observation.component:eye.value[x].unit",
        "path" : "Observation.component.value[x].unit",
        "patternString" : "{score}"
      },
      {
        "id" : "Observation.component:eye.value[x].system",
        "path" : "Observation.component.value[x].system",
        "patternUri" : "http://unitsofmeasure.org"
      },
      {
        "id" : "Observation.component:verbal",
        "path" : "Observation.component",
        "sliceName" : "verbal",
        "min" : 1,
        "max" : "1",
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:verbal.code",
        "path" : "Observation.component.code",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "http://loinc.org",
              "code" : "9270-0",
              "display" : "Glasgow coma score verbal"
            }
          ]
        }
      },
      {
        "id" : "Observation.component:verbal.value[x]",
        "path" : "Observation.component.value[x]",
        "type" : [
          {
            "code" : "Quantity"
          }
        ]
      },
      {
        "id" : "Observation.component:verbal.value[x].value",
        "path" : "Observation.component.value[x].value",
        "constraint" : [
          {
            "key" : "gcs-verbal-range",
            "severity" : "error",
            "human" : "GCS verbal response must be between 1 and 5",
            "expression" : "$this >= 1 and $this <= 5",
            "source" : "https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/onc-glasgow-coma-scale"
          }
        ]
      },
      {
        "id" : "Observation.component:verbal.value[x].unit",
        "path" : "Observation.component.value[x].unit",
        "patternString" : "{score}"
      },
      {
        "id" : "Observation.component:verbal.value[x].system",
        "path" : "Observation.component.value[x].system",
        "patternUri" : "http://unitsofmeasure.org"
      },
      {
        "id" : "Observation.component:motor",
        "path" : "Observation.component",
        "sliceName" : "motor",
        "min" : 1,
        "max" : "1",
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:motor.code",
        "path" : "Observation.component.code",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "http://loinc.org",
              "code" : "9268-4",
              "display" : "Glasgow coma score motor"
            }
          ]
        }
      },
      {
        "id" : "Observation.component:motor.value[x]",
        "path" : "Observation.component.value[x]",
        "type" : [
          {
            "code" : "Quantity"
          }
        ]
      },
      {
        "id" : "Observation.component:motor.value[x].value",
        "path" : "Observation.component.value[x].value",
        "constraint" : [
          {
            "key" : "gcs-motor-range",
            "severity" : "error",
            "human" : "GCS motor response must be between 1 and 6",
            "expression" : "$this >= 1 and $this <= 6",
            "source" : "https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/onc-glasgow-coma-scale"
          }
        ]
      },
      {
        "id" : "Observation.component:motor.value[x].unit",
        "path" : "Observation.component.value[x].unit",
        "patternString" : "{score}"
      },
      {
        "id" : "Observation.component:motor.value[x].system",
        "path" : "Observation.component.value[x].system",
        "patternUri" : "http://unitsofmeasure.org"
      }
    ]
  }
}

```
