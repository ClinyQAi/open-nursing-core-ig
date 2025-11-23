# ONC Morse Fall Scale Assessment - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **ONC Morse Fall Scale Assessment**

## Resource Profile: ONC Morse Fall Scale Assessment 

| | |
| :--- | :--- |
| *Official URL*:http://open-nursing-core.org/StructureDefinition/onc-morse-fall-scale | *Version*:0.1.0 |
| Draft as of 2025-11-23 | *Computable Name*:ONCMorseFallScale |

 
Assessment of fall risk using the Morse Fall Scale. 

**Usages:**

* Examples for this Profile: [Observation/example-morse-fall-scale](Observation-example-morse-fall-scale.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/onc.ig|current/StructureDefinition/onc-morse-fall-scale)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-onc-morse-fall-scale.csv), [Excel](StructureDefinition-onc-morse-fall-scale.xlsx), [Schematron](StructureDefinition-onc-morse-fall-scale.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "onc-morse-fall-scale",
  "url" : "http://open-nursing-core.org/StructureDefinition/onc-morse-fall-scale",
  "version" : "0.1.0",
  "name" : "ONCMorseFallScale",
  "title" : "ONC Morse Fall Scale Assessment",
  "status" : "draft",
  "date" : "2025-11-23T22:00:06+00:00",
  "description" : "Assessment of fall risk using the Morse Fall Scale.",
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
              "code" : "59460-6",
              "display" : "Morse Fall Scale total score"
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
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:historyOfFalling",
        "path" : "Observation.component",
        "sliceName" : "historyOfFalling",
        "min" : 1,
        "max" : "1",
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:historyOfFalling.code",
        "path" : "Observation.component.code",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "http://loinc.org",
              "code" : "59461-4"
            }
          ]
        }
      },
      {
        "id" : "Observation.component:historyOfFalling.value[x]",
        "path" : "Observation.component.value[x]",
        "type" : [
          {
            "code" : "Quantity"
          }
        ]
      },
      {
        "id" : "Observation.component:historyOfFalling.value[x].unit",
        "path" : "Observation.component.value[x].unit",
        "patternString" : "{score}"
      },
      {
        "id" : "Observation.component:secondaryDiagnosis",
        "path" : "Observation.component",
        "sliceName" : "secondaryDiagnosis",
        "min" : 1,
        "max" : "1",
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:secondaryDiagnosis.code",
        "path" : "Observation.component.code",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "http://loinc.org",
              "code" : "59462-2"
            }
          ]
        }
      },
      {
        "id" : "Observation.component:secondaryDiagnosis.value[x]",
        "path" : "Observation.component.value[x]",
        "type" : [
          {
            "code" : "Quantity"
          }
        ]
      },
      {
        "id" : "Observation.component:secondaryDiagnosis.value[x].unit",
        "path" : "Observation.component.value[x].unit",
        "patternString" : "{score}"
      },
      {
        "id" : "Observation.component:ambulatoryAid",
        "path" : "Observation.component",
        "sliceName" : "ambulatoryAid",
        "min" : 1,
        "max" : "1",
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:ambulatoryAid.code",
        "path" : "Observation.component.code",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "http://loinc.org",
              "code" : "59463-0"
            }
          ]
        }
      },
      {
        "id" : "Observation.component:ambulatoryAid.value[x]",
        "path" : "Observation.component.value[x]",
        "type" : [
          {
            "code" : "Quantity"
          }
        ]
      },
      {
        "id" : "Observation.component:ambulatoryAid.value[x].unit",
        "path" : "Observation.component.value[x].unit",
        "patternString" : "{score}"
      },
      {
        "id" : "Observation.component:intravenousTherapy",
        "path" : "Observation.component",
        "sliceName" : "intravenousTherapy",
        "min" : 1,
        "max" : "1",
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:intravenousTherapy.code",
        "path" : "Observation.component.code",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "http://loinc.org",
              "code" : "59464-8"
            }
          ]
        }
      },
      {
        "id" : "Observation.component:intravenousTherapy.value[x]",
        "path" : "Observation.component.value[x]",
        "type" : [
          {
            "code" : "Quantity"
          }
        ]
      },
      {
        "id" : "Observation.component:intravenousTherapy.value[x].unit",
        "path" : "Observation.component.value[x].unit",
        "patternString" : "{score}"
      },
      {
        "id" : "Observation.component:gait",
        "path" : "Observation.component",
        "sliceName" : "gait",
        "min" : 1,
        "max" : "1",
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:gait.code",
        "path" : "Observation.component.code",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "http://loinc.org",
              "code" : "59465-5"
            }
          ]
        }
      },
      {
        "id" : "Observation.component:gait.value[x]",
        "path" : "Observation.component.value[x]",
        "type" : [
          {
            "code" : "Quantity"
          }
        ]
      },
      {
        "id" : "Observation.component:gait.value[x].unit",
        "path" : "Observation.component.value[x].unit",
        "patternString" : "{score}"
      },
      {
        "id" : "Observation.component:mentalStatus",
        "path" : "Observation.component",
        "sliceName" : "mentalStatus",
        "min" : 1,
        "max" : "1",
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:mentalStatus.code",
        "path" : "Observation.component.code",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "http://loinc.org",
              "code" : "59466-3"
            }
          ]
        }
      },
      {
        "id" : "Observation.component:mentalStatus.value[x]",
        "path" : "Observation.component.value[x]",
        "type" : [
          {
            "code" : "Quantity"
          }
        ]
      },
      {
        "id" : "Observation.component:mentalStatus.value[x].unit",
        "path" : "Observation.component.value[x].unit",
        "patternString" : "{score}"
      }
    ]
  }
}

```
