# Relational Care Logical Model - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Relational Care Logical Model**

## Logical Model: Relational Care Logical Model 

| | |
| :--- | :--- |
| *Official URL*:https://opennursingcoreig.com/StructureDefinition/onc-relational-care-logical | *Version*:0.1.0 |
| Draft as of 2026-01-03 | *Computable Name*:ONCRelationalCareModel |

 
A vendor-neutral clinical model of the relational nursing assessment. Defines WHAT data must be captured, regardless of HOW it is stored in FHIR. 

**Usages:**

* This Logical Model is not used by any profiles in this Implementation Guide

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/onc.ig|current/StructureDefinition/onc-relational-care-logical)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-onc-relational-care-logical.csv), [Excel](StructureDefinition-onc-relational-care-logical.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "onc-relational-care-logical",
  "url" : "https://opennursingcoreig.com/StructureDefinition/onc-relational-care-logical",
  "version" : "0.1.0",
  "name" : "ONCRelationalCareModel",
  "title" : "Relational Care Logical Model",
  "status" : "draft",
  "date" : "2026-01-03T00:34:03+00:00",
  "publisher" : "The Open Nursing Community",
  "description" : "A vendor-neutral clinical model of the relational nursing assessment. Defines WHAT data must be captured, regardless of HOW it is stored in FHIR.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "https://opennursingcoreig.com/StructureDefinition/onc-relational-care-logical",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [
      {
        "id" : "onc-relational-care-logical",
        "path" : "onc-relational-care-logical",
        "short" : "Relational Care Logical Model",
        "definition" : "A vendor-neutral clinical model of the relational nursing assessment. Defines WHAT data must be captured, regardless of HOW it is stored in FHIR."
      },
      {
        "id" : "onc-relational-care-logical.patientPreferences",
        "path" : "onc-relational-care-logical.patientPreferences",
        "short" : "The patient's personal goals and what matters most to them today.",
        "definition" : "The patient's personal goals and what matters most to them today.",
        "min" : 1,
        "max" : "1",
        "type" : [
          {
            "code" : "string"
          }
        ]
      },
      {
        "id" : "onc-relational-care-logical.relationalEngagement",
        "path" : "onc-relational-care-logical.relationalEngagement",
        "short" : "A score from 1-5 representing the depth of the therapeutic relationship.",
        "definition" : "A score from 1-5 representing the depth of the therapeutic relationship.",
        "min" : 1,
        "max" : "1",
        "type" : [
          {
            "code" : "integer"
          }
        ]
      },
      {
        "id" : "onc-relational-care-logical.empathyIndex",
        "path" : "onc-relational-care-logical.empathyIndex",
        "short" : "The ONC Empathy Index (1-5) measuring relational quality.",
        "definition" : "The ONC Empathy Index (1-5) measuring relational quality.",
        "min" : 1,
        "max" : "1",
        "type" : [
          {
            "code" : "code"
          }
        ],
        "binding" : {
          "strength" : "required",
          "valueSet" : "https://opennursingcoreig.com/ValueSet/onc-empathy-index-vs"
        }
      },
      {
        "id" : "onc-relational-care-logical.skinToneEquity",
        "path" : "onc-relational-care-logical.skinToneEquity",
        "short" : "The patient's skin tone classification (Fitzpatrick or Monk) used to guide clinical assessment.",
        "definition" : "The patient's skin tone classification (Fitzpatrick or Monk) used to guide clinical assessment.",
        "min" : 1,
        "max" : "1",
        "type" : [
          {
            "code" : "code"
          }
        ],
        "binding" : {
          "strength" : "extensible",
          "valueSet" : "https://opennursingcoreig.com/ValueSet/onc-skintone-vs"
        }
      },
      {
        "id" : "onc-relational-care-logical.mandatoryEquityValidation",
        "path" : "onc-relational-care-logical.mandatoryEquityValidation",
        "short" : "Technical flag ensuring the 'Fairness Gate' was passed.",
        "definition" : "Technical flag ensuring the 'Fairness Gate' was passed.",
        "min" : 1,
        "max" : "1",
        "type" : [
          {
            "code" : "boolean"
          }
        ]
      },
      {
        "id" : "onc-relational-care-logical.adpieStatus",
        "path" : "onc-relational-care-logical.adpieStatus",
        "short" : "The current stage of the professional nursing process (Assessment, Diagnosis, Planning, Implementation, Evaluation).",
        "definition" : "The current stage of the professional nursing process (Assessment, Diagnosis, Planning, Implementation, Evaluation).",
        "min" : 1,
        "max" : "1",
        "type" : [
          {
            "code" : "code"
          }
        ],
        "binding" : {
          "strength" : "required",
          "valueSet" : "https://opennursingcoreig.com/ValueSet/onc-adpie-vs"
        }
      },
      {
        "id" : "onc-relational-care-logical.clinicalNarrative",
        "path" : "onc-relational-care-logical.clinicalNarrative",
        "short" : "The person-centred narrative describing the patient's experience.",
        "definition" : "The person-centred narrative describing the patient's experience.",
        "min" : 1,
        "max" : "1",
        "type" : [
          {
            "code" : "string"
          }
        ]
      }
    ]
  }
}

```
