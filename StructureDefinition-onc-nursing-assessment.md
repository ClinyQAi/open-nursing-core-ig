# Open Nursing Core Assessment - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Open Nursing Core Assessment**

## Resource Profile: Open Nursing Core Assessment 

| | |
| :--- | :--- |
| *Official URL*:https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/onc-nursing-assessment | *Version*:1.0.0 |
| Active as of 2025-12-26 | *Computable Name*:ONCNursingAssessment |

**Usages:**

* Derived from this Profile: [ACVPU Consciousness Level](StructureDefinition-onc-acvpu.md), [Barthel Index](StructureDefinition-onc-barthel-index.md), [Blood Pressure](StructureDefinition-onc-blood-pressure.md), [Body Temperature](StructureDefinition-onc-body-temperature.md)...Show 18 more,[Braden Scale Assessment](StructureDefinition-onc-braden-scale-assessment.md),[Glasgow Coma Scale](StructureDefinition-onc-glasgow-coma-scale.md),[Goal Evaluation](StructureDefinition-onc-goal-evaluation.md),[Heart Rate](StructureDefinition-onc-heart-rate.md),[Inspired Oxygen](StructureDefinition-onc-inspired-oxygen.md),[Mini Mental State Examination (MMSE)](StructureDefinition-onc-mmse.md),[Monk Skin Tone Observation](StructureDefinition-onc-monk-skintone-observation.md),[Morse Fall Scale](StructureDefinition-onc-morse-fall-scale.md),[MUST Score (Malnutrition Universal Screening Tool)](StructureDefinition-onc-must-score.md),[NEWS2 Score](StructureDefinition-onc-news2-score.md),[NEWS2 Sub-Score](StructureDefinition-onc-news2-subscore.md),[Oxygen Saturation](StructureDefinition-onc-oxygen-saturation.md),[Pain Assessment (NRS 0-10)](StructureDefinition-onc-pain-assessment.md),[qSOFA (Quick SOFA)](StructureDefinition-onc-qsofa.md),[Respiration Rate](StructureDefinition-onc-respiration-rate.md),[Skin Tone Observation](StructureDefinition-onc-skintone-observation.md),[Waterlow Score](StructureDefinition-onc-waterlow-score.md)and[Wound Assessment](StructureDefinition-onc-wound-assessment.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/onc.ig|current/StructureDefinition/onc-nursing-assessment)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-onc-nursing-assessment.csv), [Excel](StructureDefinition-onc-nursing-assessment.xlsx), [Schematron](StructureDefinition-onc-nursing-assessment.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "onc-nursing-assessment",
  "url" : "https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/onc-nursing-assessment",
  "version" : "1.0.0",
  "name" : "ONCNursingAssessment",
  "title" : "Open Nursing Core Assessment",
  "status" : "active",
  "date" : "2025-12-26T01:02:00+00:00",
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
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Observation",
  "derivation" : "constraint",
  "differential" : {
    "element" : [
      {
        "id" : "Observation",
        "path" : "Observation"
      },
      {
        "id" : "Observation.category",
        "path" : "Observation.category",
        "slicing" : {
          "discriminator" : [
            {
              "type" : "pattern",
              "path" : "$this"
            }
          ],
          "ordered" : false,
          "rules" : "open"
        },
        "min" : 1
      },
      {
        "id" : "Observation.category:nursing",
        "path" : "Observation.category",
        "sliceName" : "nursing",
        "min" : 1,
        "max" : "1",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "http://terminology.hl7.org/CodeSystem/observation-category",
              "code" : "nursing"
            }
          ]
        },
        "mustSupport" : true
      },
      {
        "id" : "Observation.performer",
        "path" : "Observation.performer",
        "min" : 1,
        "max" : "1",
        "type" : [
          {
            "code" : "Reference",
            "targetProfile" : [
              "http://hl7.org/fhir/StructureDefinition/Practitioner",
              "http://hl7.org/fhir/StructureDefinition/PractitionerRole"
            ]
          }
        ],
        "mustSupport" : true
      },
      {
        "id" : "Observation.value[x]",
        "path" : "Observation.value[x]",
        "min" : 1,
        "type" : [
          {
            "code" : "Quantity"
          },
          {
            "code" : "CodeableConcept"
          }
        ],
        "mustSupport" : true
      }
    ]
  }
}

```
