# PBS ABC Chart - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **PBS ABC Chart**

## Resource Profile: PBS ABC Chart 

| | |
| :--- | :--- |
| *Official URL*:https://fhir.clinyq.ai/StructureDefinition/onc-abc-chart | *Version*:0.1.0 |
| Draft as of 2026-01-01 | *Computable Name*:ONCABCChart |

 
Antecedent-Behaviour-Consequence (ABC) Chart for recording behaviours of concern. Fundamental tool in Positive Behaviour Support (PBS) for Learning Disabilities. 

**Usages:**

* Examples for this Profile: [Observation/example-abc-chart](Observation-example-abc-chart.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/onc.ig|current/StructureDefinition/onc-abc-chart)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-onc-abc-chart.csv), [Excel](StructureDefinition-onc-abc-chart.xlsx), [Schematron](StructureDefinition-onc-abc-chart.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "onc-abc-chart",
  "url" : "https://fhir.clinyq.ai/StructureDefinition/onc-abc-chart",
  "version" : "0.1.0",
  "name" : "ONCABCChart",
  "title" : "PBS ABC Chart",
  "status" : "draft",
  "date" : "2026-01-01T13:37:23+00:00",
  "description" : "Antecedent-Behaviour-Consequence (ABC) Chart for recording behaviours of concern. Fundamental tool in Positive Behaviour Support (PBS) for Learning Disabilities.",
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
              "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
              "code" : "abc-chart"
            }
          ]
        }
      },
      {
        "id" : "Observation.value[x]",
        "path" : "Observation.value[x]",
        "short" : "Hypothesized Function (SEAT)",
        "type" : [
          {
            "code" : "CodeableConcept"
          }
        ],
        "binding" : {
          "strength" : "preferred",
          "valueSet" : "https://clinyqai.github.io/open-nursing-core-ig/ValueSet/onc-pbs-function-vs"
        }
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
          "ordered" : false,
          "rules" : "open"
        },
        "min" : 3,
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:antecedent",
        "path" : "Observation.component",
        "sliceName" : "antecedent",
        "min" : 1,
        "max" : "1",
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:antecedent.code",
        "path" : "Observation.component.code",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
              "code" : "abc-antecedent"
            }
          ]
        }
      },
      {
        "id" : "Observation.component:antecedent.value[x]",
        "path" : "Observation.component.value[x]",
        "short" : "Trigger/Context (Who, What, Where, When)",
        "min" : 1,
        "type" : [
          {
            "code" : "string"
          }
        ],
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:behaviour",
        "path" : "Observation.component",
        "sliceName" : "behaviour",
        "min" : 1,
        "max" : "1",
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:behaviour.code",
        "path" : "Observation.component.code",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
              "code" : "abc-behaviour"
            }
          ]
        }
      },
      {
        "id" : "Observation.component:behaviour.value[x]",
        "path" : "Observation.component.value[x]",
        "short" : "Exact description of what was done",
        "min" : 1,
        "type" : [
          {
            "code" : "string"
          }
        ],
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:consequence",
        "path" : "Observation.component",
        "sliceName" : "consequence",
        "min" : 1,
        "max" : "1",
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:consequence.code",
        "path" : "Observation.component.code",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
              "code" : "abc-consequence"
            }
          ]
        }
      },
      {
        "id" : "Observation.component:consequence.value[x]",
        "path" : "Observation.component.value[x]",
        "short" : "Staff response & Outcome",
        "min" : 1,
        "type" : [
          {
            "code" : "string"
          }
        ],
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:duration",
        "path" : "Observation.component",
        "sliceName" : "duration",
        "min" : 0,
        "max" : "1",
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:duration.code",
        "path" : "Observation.component.code",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
              "code" : "abc-duration"
            }
          ]
        }
      },
      {
        "id" : "Observation.component:duration.value[x]",
        "path" : "Observation.component.value[x]",
        "min" : 1,
        "type" : [
          {
            "code" : "Quantity"
          }
        ],
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:duration.value[x].unit",
        "path" : "Observation.component.value[x].unit",
        "patternString" : "min"
      },
      {
        "id" : "Observation.component:duration.value[x].system",
        "path" : "Observation.component.value[x].system",
        "patternUri" : "http://unitsofmeasure.org"
      },
      {
        "id" : "Observation.component:duration.value[x].code",
        "path" : "Observation.component.value[x].code",
        "patternCode" : "min"
      },
      {
        "id" : "Observation.component:intensity",
        "path" : "Observation.component",
        "sliceName" : "intensity",
        "min" : 0,
        "max" : "1",
        "mustSupport" : true
      },
      {
        "id" : "Observation.component:intensity.code",
        "path" : "Observation.component.code",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes",
              "code" : "abc-intensity"
            }
          ]
        }
      },
      {
        "id" : "Observation.component:intensity.value[x]",
        "path" : "Observation.component.value[x]",
        "short" : "1 (Mild) to 10 (Severe)",
        "min" : 1,
        "type" : [
          {
            "code" : "integer"
          }
        ],
        "mustSupport" : true
      }
    ]
  }
}

```
