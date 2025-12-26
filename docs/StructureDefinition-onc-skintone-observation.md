# Skin Tone Observation - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Skin Tone Observation**

## Resource Profile: Skin Tone Observation 

| | |
| :--- | :--- |
| *Official URL*:https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/onc-skintone-observation | *Version*:0.1.0 |
| Draft as of 2025-12-26 | *Computable Name*:ONCSkinToneObservation |

 
Observation of patient skin tone using the Fitzpatrick skin type classification. Supports equitable care by enabling skin tone-aware clinical decision making, particularly for conditions that present differently across skin tones (e.g., pressure ulcers, cyanosis). 

**Usages:**

* Examples for this Profile: [Observation/observation-skin-tone](Observation-observation-skin-tone.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/onc.ig|current/StructureDefinition/onc-skintone-observation)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-onc-skintone-observation.csv), [Excel](StructureDefinition-onc-skintone-observation.xlsx), [Schematron](StructureDefinition-onc-skintone-observation.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "onc-skintone-observation",
  "url" : "https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/onc-skintone-observation",
  "version" : "0.1.0",
  "name" : "ONCSkinToneObservation",
  "title" : "Skin Tone Observation",
  "status" : "draft",
  "date" : "2025-12-26T15:22:58+00:00",
  "description" : "Observation of patient skin tone using the Fitzpatrick skin type classification. Supports equitable care by enabling skin tone-aware clinical decision making, particularly for conditions that present differently across skin tones (e.g., pressure ulcers, cyanosis).",
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
        "id" : "Observation.code",
        "path" : "Observation.code",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "http://loinc.org",
              "code" : "66555-4",
              "display" : "Skin type [Fitzpatrick Classification Scale]"
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
          "valueSet" : "https://clinyqai.github.io/open-nursing-core-ig/ValueSet/skintone-vs"
        }
      }
    ]
  }
}

```
