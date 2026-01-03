# Monk Skin Tone Observation - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Monk Skin Tone Observation**

## Resource Profile: Monk Skin Tone Observation 

| | |
| :--- | :--- |
| *Official URL*:https://opennursingcoreig.com/StructureDefinition/onc-monk-skintone-observation | *Version*:0.1.0 |
| Draft as of 2026-01-03 | *Computable Name*:ONCMonkSkinToneObservation |

 
Observation of patient skin tone using the Monk Skin Tone Scale (10-point scale A-J). Provides more granular skin tone assessment than Fitzpatrick scale, particularly for darker skin tones. Supports equitable care and accurate clinical assessment across diverse populations. 

**Usages:**

* Refer to this Profile: [Braden Scale Assessment](StructureDefinition-onc-braden-scale-assessment.md) and [Waterlow Score](StructureDefinition-onc-waterlow-score.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/onc.ig|current/StructureDefinition/onc-monk-skintone-observation)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-onc-monk-skintone-observation.csv), [Excel](StructureDefinition-onc-monk-skintone-observation.xlsx), [Schematron](StructureDefinition-onc-monk-skintone-observation.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "onc-monk-skintone-observation",
  "url" : "https://opennursingcoreig.com/StructureDefinition/onc-monk-skintone-observation",
  "version" : "0.1.0",
  "name" : "ONCMonkSkinToneObservation",
  "title" : "Monk Skin Tone Observation",
  "status" : "draft",
  "date" : "2026-01-03T00:34:03+00:00",
  "publisher" : "The Open Nursing Community",
  "description" : "Observation of patient skin tone using the Monk Skin Tone Scale (10-point scale A-J). Provides more granular skin tone assessment than Fitzpatrick scale, particularly for darker skin tones. Supports equitable care and accurate clinical assessment across diverse populations.",
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
  "baseDefinition" : "https://opennursingcoreig.com/StructureDefinition/onc-nursing-assessment",
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
              "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
              "code" : "mst-score",
              "display" : "Monk Skin Tone Score"
            }
          ]
        }
      },
      {
        "id" : "Observation.value[x]",
        "path" : "Observation.value[x]",
        "type" : [
          {
            "code" : "CodeableConcept"
          }
        ],
        "binding" : {
          "strength" : "required",
          "valueSet" : "https://opennursingcoreig.com/ValueSet/onc-monk-scale-vs"
        }
      }
    ]
  }
}

```
