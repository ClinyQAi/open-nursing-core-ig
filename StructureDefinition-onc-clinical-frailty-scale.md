# Clinical Frailty Scale (CFS) - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Clinical Frailty Scale (CFS)**

## Resource Profile: Clinical Frailty Scale (CFS) 

| | |
| :--- | :--- |
| *Official URL*:https://fhir.clinyq.ai/StructureDefinition/onc-clinical-frailty-scale | *Version*:0.1.0 |
| Draft as of 2026-01-03 | *Computable Name*:ONCClinicalFrailtyScale |

 
Assessment of frailty using the Rockwood Clinical Frailty Scale (1-9). Essential for older adults to determine baseline functional status. 

**Usages:**

* Examples for this Profile: [Observation/example-clinical-frailty](Observation-example-clinical-frailty.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/onc.ig|current/StructureDefinition/onc-clinical-frailty-scale)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-onc-clinical-frailty-scale.csv), [Excel](StructureDefinition-onc-clinical-frailty-scale.xlsx), [Schematron](StructureDefinition-onc-clinical-frailty-scale.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "onc-clinical-frailty-scale",
  "url" : "https://fhir.clinyq.ai/StructureDefinition/onc-clinical-frailty-scale",
  "version" : "0.1.0",
  "name" : "ONCClinicalFrailtyScale",
  "title" : "Clinical Frailty Scale (CFS)",
  "status" : "draft",
  "date" : "2026-01-03T00:34:03+00:00",
  "publisher" : "The Open Nursing Community",
  "description" : "Assessment of frailty using the Rockwood Clinical Frailty Scale (1-9). Essential for older adults to determine baseline functional status.",
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
        "id" : "Observation.category",
        "path" : "Observation.category",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "http://terminology.hl7.org/CodeSystem/observation-category",
              "code" : "survey"
            }
          ]
        }
      },
      {
        "id" : "Observation.code",
        "path" : "Observation.code",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
              "code" : "cfs-score"
            }
          ]
        }
      },
      {
        "id" : "Observation.value[x]",
        "path" : "Observation.value[x]",
        "short" : "Frailty Level (1-9)",
        "type" : [
          {
            "code" : "CodeableConcept"
          }
        ],
        "binding" : {
          "strength" : "required",
          "valueSet" : "https://opennursingcoreig.com/ValueSet/onc-cfs-vs"
        }
      }
    ]
  }
}

```
