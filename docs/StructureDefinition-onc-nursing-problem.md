# Open Nursing Core Nursing Problem - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Open Nursing Core Nursing Problem**

## Resource Profile: Open Nursing Core Nursing Problem 

| | |
| :--- | :--- |
| *Official URL*:http://open-nursing-core.org/StructureDefinition/onc-nursing-problem | *Version*:0.1.0 |
| Draft as of 2025-11-23 | *Computable Name*:ONCNursingProblem |

 
Nursing problem or diagnosis. 

**Usages:**

* Refer to this Profile: [Open Nursing Core Nursing Care Plan](StructureDefinition-onc-nursing-care-plan.md) and [Open Nursing Core Patient Goal](StructureDefinition-onc-patient-goal.md)
* Examples for this Profile: [Condition/example-nursing-problem](Condition-example-nursing-problem.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/onc.ig|current/StructureDefinition/onc-nursing-problem)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-onc-nursing-problem.csv), [Excel](StructureDefinition-onc-nursing-problem.xlsx), [Schematron](StructureDefinition-onc-nursing-problem.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "onc-nursing-problem",
  "url" : "http://open-nursing-core.org/StructureDefinition/onc-nursing-problem",
  "version" : "0.1.0",
  "name" : "ONCNursingProblem",
  "title" : "Open Nursing Core Nursing Problem",
  "status" : "draft",
  "date" : "2025-11-23T21:00:20+00:00",
  "description" : "Nursing problem or diagnosis.",
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
  "type" : "Condition",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Condition",
  "derivation" : "constraint",
  "differential" : {
    "element" : [
      {
        "id" : "Condition",
        "path" : "Condition"
      },
      {
        "id" : "Condition.clinicalStatus",
        "path" : "Condition.clinicalStatus",
        "min" : 1,
        "mustSupport" : true
      },
      {
        "id" : "Condition.category",
        "path" : "Condition.category",
        "min" : 1,
        "max" : "1",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "http://open-nursing-core.org/CodeSystem/onc-problem-type",
              "code" : "nursing-diagnosis",
              "display" : "Nursing Diagnosis"
            }
          ]
        },
        "mustSupport" : true
      },
      {
        "id" : "Condition.code",
        "path" : "Condition.code",
        "min" : 1,
        "mustSupport" : true,
        "binding" : {
          "strength" : "required",
          "valueSet" : "http://open-nursing-core.org/ValueSet/nursing-problem-valueset"
        }
      }
    ]
  }
}

```
