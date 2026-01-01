# Open Nursing Core Assessment - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Open Nursing Core Assessment**

## Resource Profile: Open Nursing Core Assessment 

| | |
| :--- | :--- |
| *Official URL*:https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/onc-nursing-assessment | *Version*:0.1.0 |
| Draft as of 2026-01-01 | *Computable Name*:ONCNursingAssessment |

 
Base profile for nursing assessment observations conforming to UK Core standards. Captures structured nursing assessment data as part of the ADPIE (Assessment, Diagnosis, Planning, Implementation, Evaluation) nursing process framework. Used as parent for specialized assessments like NEWS2, Braden Scale, and clinical observations. 

**Usages:**

* Derived from this Profile: [4AT Delirium Assessment](StructureDefinition-onc-4at-delirium.md), [Abbey Pain Scale](StructureDefinition-onc-abbey-pain-scale.md), [PBS ABC Chart](StructureDefinition-onc-abc-chart.md), [ACVPU Consciousness Level](StructureDefinition-onc-acvpu.md)...Show 29 more,[Barthel Index](StructureDefinition-onc-barthel-index.md),[Blood Pressure](StructureDefinition-onc-blood-pressure.md),[Body Temperature](StructureDefinition-onc-body-temperature.md),[Braden Scale Assessment](StructureDefinition-onc-braden-scale-assessment.md),[Bristol Stool Chart](StructureDefinition-onc-bristol-stool-chart.md),[Clinical Frailty Scale (CFS)](StructureDefinition-onc-clinical-frailty-scale.md),[Fluid Balance](StructureDefinition-onc-fluid-balance.md),[Glasgow Coma Scale](StructureDefinition-onc-glasgow-coma-scale.md),[Heart Rate](StructureDefinition-onc-heart-rate.md),[Inspired Oxygen](StructureDefinition-onc-inspired-oxygen.md),[Mental Capacity Assessment](StructureDefinition-onc-mental-capacity.md),[Mini Mental State Examination (MMSE)](StructureDefinition-onc-mmse.md),[Monk Skin Tone Observation](StructureDefinition-onc-monk-skintone-observation.md),[Morse Fall Scale](StructureDefinition-onc-morse-fall-scale.md),[MUST Score (Malnutrition Universal Screening Tool)](StructureDefinition-onc-must-score.md),[NEWS2 Score](StructureDefinition-onc-news2-score.md),[NEWS2 Sub-Score](StructureDefinition-onc-news2-subscore.md),[Oral Health Assessment](StructureDefinition-onc-oral-health.md),[Oxygen Saturation](StructureDefinition-onc-oxygen-saturation.md),[Pain Assessment (NRS 0-10)](StructureDefinition-onc-pain-assessment.md),[qSOFA (Quick SOFA)](StructureDefinition-onc-qsofa.md),[Reasonable Adjustment](StructureDefinition-onc-reasonable-adjustment.md),[Respiration Rate](StructureDefinition-onc-respiration-rate.md),[Seizure Record](StructureDefinition-onc-seizure-record.md),[Skin Tone Observation](StructureDefinition-onc-skintone-observation.md),[Sleep Pattern](StructureDefinition-onc-sleep-pattern.md),[Urinalysis](StructureDefinition-onc-urinalysis.md),[Waterlow Score](StructureDefinition-onc-waterlow-score.md)and[Wound Assessment](StructureDefinition-onc-wound-assessment.md)

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
  "version" : "0.1.0",
  "name" : "ONCNursingAssessment",
  "title" : "Open Nursing Core Assessment",
  "status" : "draft",
  "date" : "2026-01-01T13:37:23+00:00",
  "description" : "Base profile for nursing assessment observations conforming to UK Core standards. Captures structured nursing assessment data as part of the ADPIE (Assessment, Diagnosis, Planning, Implementation, Evaluation) nursing process framework. Used as parent for specialized assessments like NEWS2, Braden Scale, and clinical observations.",
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
              "code" : "survey"
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
          },
          {
            "code" : "string"
          }
        ],
        "mustSupport" : true
      }
    ]
  }
}

```
