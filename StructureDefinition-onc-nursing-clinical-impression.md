# ONC Nursing Clinical Impression - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **ONC Nursing Clinical Impression**

## Resource Profile: ONC Nursing Clinical Impression 

| | |
| :--- | :--- |
| *Official URL*:https://opennursingcoreig.com/StructureDefinition/onc-nursing-clinical-impression | *Version*:0.1.0 |
| Draft as of 2026-01-02 | *Computable Name*:ONCNursingClinicalImpression |

 
Nurse's synthesis of patient progress against care plan, aggregating multiple goal evaluations. 

**Usages:**

* This Profile is not used by any profiles in this Implementation Guide

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/onc.ig|current/StructureDefinition/onc-nursing-clinical-impression)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-onc-nursing-clinical-impression.csv), [Excel](StructureDefinition-onc-nursing-clinical-impression.xlsx), [Schematron](StructureDefinition-onc-nursing-clinical-impression.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "onc-nursing-clinical-impression",
  "url" : "https://opennursingcoreig.com/StructureDefinition/onc-nursing-clinical-impression",
  "version" : "0.1.0",
  "name" : "ONCNursingClinicalImpression",
  "title" : "ONC Nursing Clinical Impression",
  "status" : "draft",
  "date" : "2026-01-02T23:54:54+00:00",
  "publisher" : "The Open Nursing Community",
  "description" : "Nurse's synthesis of patient progress against care plan, aggregating multiple goal evaluations.",
  "fhirVersion" : "4.0.1",
  "mapping" : [
    {
      "identity" : "workflow",
      "uri" : "http://hl7.org/fhir/workflow",
      "name" : "Workflow Pattern"
    },
    {
      "identity" : "v2",
      "uri" : "http://hl7.org/v2",
      "name" : "HL7 v2 Mapping"
    },
    {
      "identity" : "w5",
      "uri" : "http://hl7.org/fhir/fivews",
      "name" : "FiveWs Pattern Mapping"
    },
    {
      "identity" : "rim",
      "uri" : "http://hl7.org/v3",
      "name" : "RIM Mapping"
    }
  ],
  "kind" : "resource",
  "abstract" : false,
  "type" : "ClinicalImpression",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/ClinicalImpression",
  "derivation" : "constraint",
  "differential" : {
    "element" : [
      {
        "id" : "ClinicalImpression",
        "path" : "ClinicalImpression"
      },
      {
        "id" : "ClinicalImpression.status",
        "path" : "ClinicalImpression.status",
        "mustSupport" : true
      },
      {
        "id" : "ClinicalImpression.code",
        "path" : "ClinicalImpression.code",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "http://snomed.info/sct",
              "code" : "225358003",
              "display" : "Nursing assessment"
            }
          ]
        }
      },
      {
        "id" : "ClinicalImpression.subject",
        "path" : "ClinicalImpression.subject",
        "type" : [
          {
            "code" : "Reference",
            "targetProfile" : ["http://hl7.org/fhir/StructureDefinition/Patient"]
          }
        ]
      },
      {
        "id" : "ClinicalImpression.encounter",
        "path" : "ClinicalImpression.encounter",
        "mustSupport" : true
      },
      {
        "id" : "ClinicalImpression.effective[x]",
        "path" : "ClinicalImpression.effective[x]",
        "slicing" : {
          "discriminator" : [
            {
              "type" : "type",
              "path" : "$this"
            }
          ],
          "ordered" : false,
          "rules" : "open"
        }
      },
      {
        "id" : "ClinicalImpression.effective[x]:effectiveDateTime",
        "path" : "ClinicalImpression.effective[x]",
        "sliceName" : "effectiveDateTime",
        "min" : 0,
        "max" : "1",
        "type" : [
          {
            "code" : "dateTime"
          }
        ],
        "mustSupport" : true
      },
      {
        "id" : "ClinicalImpression.assessor",
        "path" : "ClinicalImpression.assessor",
        "type" : [
          {
            "code" : "Reference",
            "targetProfile" : ["http://hl7.org/fhir/StructureDefinition/Practitioner"]
          }
        ]
      },
      {
        "id" : "ClinicalImpression.problem",
        "path" : "ClinicalImpression.problem",
        "min" : 1,
        "type" : [
          {
            "code" : "Reference",
            "targetProfile" : ["http://hl7.org/fhir/StructureDefinition/Condition"]
          }
        ],
        "mustSupport" : true
      },
      {
        "id" : "ClinicalImpression.summary",
        "path" : "ClinicalImpression.summary",
        "mustSupport" : true
      },
      {
        "id" : "ClinicalImpression.prognosisCodeableConcept",
        "path" : "ClinicalImpression.prognosisCodeableConcept",
        "binding" : {
          "strength" : "extensible",
          "valueSet" : "https://opennursingcoreig.com/ValueSet/onc-prognosis-vs"
        }
      },
      {
        "id" : "ClinicalImpression.supportingInfo",
        "path" : "ClinicalImpression.supportingInfo",
        "type" : [
          {
            "code" : "Reference",
            "targetProfile" : [
              "https://opennursingcoreig.com/StructureDefinition/onc-goal-evaluation"
            ]
          }
        ],
        "mustSupport" : true
      }
    ]
  }
}

```
