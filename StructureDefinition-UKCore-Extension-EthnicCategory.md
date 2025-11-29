# UK Core Ethnic Category - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **UK Core Ethnic Category**

## Extension: UK Core Ethnic Category 

| | |
| :--- | :--- |
| *Official URL*:https://fhir.hl7.org.uk/StructureDefinition/UKCore-Extension-EthnicCategory | *Version*:1.0.0 |
| Active as of 2025-11-29 | *Computable Name*:UKCoreEthnicCategory |

**Context of Use**

**Usage info**

**Usages:**

* Use this Extension: [ONC NHS Patient](StructureDefinition-onc-nhs-patient.md)
* Examples for this Extension: [Patient/patient-example-jane](Patient-patient-example-jane.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/onc.ig|current/StructureDefinition/UKCore-Extension-EthnicCategory)

### Formal Views of Extension Content

 [Description of Profiles, Differentials, Snapshots, and how the XML and JSON presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-UKCore-Extension-EthnicCategory.csv), [Excel](StructureDefinition-UKCore-Extension-EthnicCategory.xlsx), [Schematron](StructureDefinition-UKCore-Extension-EthnicCategory.sch) 

#### Constraints



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "UKCore-Extension-EthnicCategory",
  "url" : "https://fhir.hl7.org.uk/StructureDefinition/UKCore-Extension-EthnicCategory",
  "version" : "1.0.0",
  "name" : "UKCoreEthnicCategory",
  "title" : "UK Core Ethnic Category",
  "status" : "active",
  "date" : "2025-11-29T22:52:23+00:00",
  "fhirVersion" : "4.0.1",
  "mapping" : [
    {
      "identity" : "rim",
      "uri" : "http://hl7.org/v3",
      "name" : "RIM Mapping"
    }
  ],
  "kind" : "complex-type",
  "abstract" : false,
  "context" : [
    {
      "type" : "element",
      "expression" : "Element"
    }
  ],
  "type" : "Extension",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Extension",
  "derivation" : "constraint",
  "differential" : {
    "element" : [
      {
        "id" : "Extension",
        "path" : "Extension",
        "short" : "UK Core Ethnic Category"
      },
      {
        "id" : "Extension.extension",
        "path" : "Extension.extension",
        "max" : "0"
      },
      {
        "id" : "Extension.url",
        "path" : "Extension.url",
        "fixedUri" : "https://fhir.hl7.org.uk/StructureDefinition/UKCore-Extension-EthnicCategory"
      },
      {
        "id" : "Extension.value[x]",
        "path" : "Extension.value[x]",
        "type" : [
          {
            "code" : "CodeableConcept"
          }
        ]
      }
    ]
  }
}

```
