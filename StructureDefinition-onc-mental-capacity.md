# Mental Capacity Assessment - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Mental Capacity Assessment**

## Resource Profile: Mental Capacity Assessment 

| | |
| :--- | :--- |
| *Official URL*:https://fhir.clinyq.ai/StructureDefinition/onc-mental-capacity | *Version*:0.1.0 |
| Draft as of 2026-01-03 | *Computable Name*:ONCMentalCapacity |

 
Records the outcome of a Mental Capacity Assessment for a specific decision. Fundamental legal safeguard in UK nursing practice. 

**Usages:**

* Examples for this Profile: [Observation/example-mental-capacity](Observation-example-mental-capacity.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/onc.ig|current/StructureDefinition/onc-mental-capacity)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-onc-mental-capacity.csv), [Excel](StructureDefinition-onc-mental-capacity.xlsx), [Schematron](StructureDefinition-onc-mental-capacity.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "onc-mental-capacity",
  "url" : "https://fhir.clinyq.ai/StructureDefinition/onc-mental-capacity",
  "version" : "0.1.0",
  "name" : "ONCMentalCapacity",
  "title" : "Mental Capacity Assessment",
  "status" : "draft",
  "date" : "2026-01-03T01:26:42+00:00",
  "publisher" : "The Open Nursing Community",
  "description" : "Records the outcome of a Mental Capacity Assessment for a specific decision. Fundamental legal safeguard in UK nursing practice.",
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
              "code" : "exam"
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
              "code" : "mca-assessment"
            }
          ]
        }
      },
      {
        "id" : "Observation.value[x]",
        "path" : "Observation.value[x]",
        "short" : "Outcome (Capacity Present/Absent)",
        "type" : [
          {
            "code" : "CodeableConcept"
          }
        ],
        "binding" : {
          "strength" : "required",
          "valueSet" : "https://opennursingcoreig.com/ValueSet/onc-mca-vs"
        }
      },
      {
        "id" : "Observation.note",
        "path" : "Observation.note",
        "short" : "The specific decision being assessed (CRITICAL)",
        "min" : 1,
        "mustSupport" : true
      }
    ]
  }
}

```
