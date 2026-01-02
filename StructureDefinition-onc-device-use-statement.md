# Device Use Statement - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Device Use Statement**

## Resource Profile: Device Use Statement 

| | |
| :--- | :--- |
| *Official URL*:https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/onc-device-use-statement | *Version*:0.1.0 |
| Draft as of 2026-01-02 | *Computable Name*:ONCDeviceUseStatement |

 
Documentation of mobility aids or other devices used by the patient. 

**Usages:**

* This Profile is not used by any profiles in this Implementation Guide

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/onc.ig|current/StructureDefinition/onc-device-use-statement)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-onc-device-use-statement.csv), [Excel](StructureDefinition-onc-device-use-statement.xlsx), [Schematron](StructureDefinition-onc-device-use-statement.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "onc-device-use-statement",
  "url" : "https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/onc-device-use-statement",
  "version" : "0.1.0",
  "name" : "ONCDeviceUseStatement",
  "title" : "Device Use Statement",
  "status" : "draft",
  "date" : "2026-01-02T16:06:53+00:00",
  "description" : "Documentation of mobility aids or other devices used by the patient.",
  "fhirVersion" : "4.0.1",
  "mapping" : [
    {
      "identity" : "workflow",
      "uri" : "http://hl7.org/fhir/workflow",
      "name" : "Workflow Pattern"
    },
    {
      "identity" : "quick",
      "uri" : "http://siframework.org/cqf",
      "name" : "Quality Improvement and Clinical Knowledge (QUICK)"
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
      "identity" : "rim",
      "uri" : "http://hl7.org/v3",
      "name" : "RIM Mapping"
    }
  ],
  "kind" : "resource",
  "abstract" : false,
  "type" : "DeviceUseStatement",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/DeviceUseStatement",
  "derivation" : "constraint",
  "differential" : {
    "element" : [
      {
        "id" : "DeviceUseStatement",
        "path" : "DeviceUseStatement"
      },
      {
        "id" : "DeviceUseStatement.subject",
        "path" : "DeviceUseStatement.subject",
        "type" : [
          {
            "code" : "Reference",
            "targetProfile" : ["http://hl7.org/fhir/StructureDefinition/Patient"]
          }
        ]
      },
      {
        "id" : "DeviceUseStatement.timing[x]",
        "path" : "DeviceUseStatement.timing[x]",
        "mustSupport" : true
      },
      {
        "id" : "DeviceUseStatement.bodySite",
        "path" : "DeviceUseStatement.bodySite",
        "mustSupport" : true
      }
    ]
  }
}

```
