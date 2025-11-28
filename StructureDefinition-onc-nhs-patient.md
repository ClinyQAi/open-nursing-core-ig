# ONC NHS Patient - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **ONC NHS Patient**

## Resource Profile: ONC NHS Patient 

| | |
| :--- | :--- |
| *Official URL*:https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/onc-nhs-patient | *Version*:1.0.0 |
| Active as of 2025-11-28 | *Computable Name*:ONCNHSPatient |

**Usages:**

* Examples for this Profile: [Patient/patient-example-jane](Patient-patient-example-jane.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/onc.ig|current/StructureDefinition/onc-nhs-patient)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-onc-nhs-patient.csv), [Excel](StructureDefinition-onc-nhs-patient.xlsx), [Schematron](StructureDefinition-onc-nhs-patient.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "onc-nhs-patient",
  "url" : "https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/onc-nhs-patient",
  "version" : "1.0.0",
  "name" : "ONCNHSPatient",
  "title" : "ONC NHS Patient",
  "status" : "active",
  "date" : "2025-11-28T01:13:19+00:00",
  "fhirVersion" : "4.0.1",
  "mapping" : [
    {
      "identity" : "rim",
      "uri" : "http://hl7.org/v3",
      "name" : "RIM Mapping"
    },
    {
      "identity" : "cda",
      "uri" : "http://hl7.org/v3/cda",
      "name" : "CDA (R2)"
    },
    {
      "identity" : "w5",
      "uri" : "http://hl7.org/fhir/fivews",
      "name" : "FiveWs Pattern Mapping"
    },
    {
      "identity" : "v2",
      "uri" : "http://hl7.org/v2",
      "name" : "HL7 v2 Mapping"
    },
    {
      "identity" : "loinc",
      "uri" : "http://loinc.org",
      "name" : "LOINC code for the element"
    }
  ],
  "kind" : "resource",
  "abstract" : false,
  "type" : "Patient",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Patient",
  "derivation" : "constraint",
  "differential" : {
    "element" : [
      {
        "id" : "Patient",
        "path" : "Patient"
      },
      {
        "id" : "Patient.extension",
        "path" : "Patient.extension",
        "slicing" : {
          "discriminator" : [
            {
              "type" : "value",
              "path" : "url"
            }
          ],
          "ordered" : false,
          "rules" : "open"
        },
        "min" : 1
      },
      {
        "id" : "Patient.extension:ethnicCategory",
        "path" : "Patient.extension",
        "sliceName" : "ethnicCategory",
        "min" : 1,
        "max" : "1",
        "type" : [
          {
            "code" : "Extension",
            "profile" : [
              "https://fhir.hl7.org.uk/StructureDefinition/UKCore-Extension-EthnicCategory"
            ]
          }
        ],
        "mustSupport" : true
      }
    ]
  }
}

```
