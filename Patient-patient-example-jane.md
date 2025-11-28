# patient-example-jane - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **patient-example-jane**

## Example Patient: patient-example-jane

Profile: [ONC NHS Patient](StructureDefinition-onc-nhs-patient.md)

Jane Doe Female, DoB Unknown

-------

| | |
| :--- | :--- |
| [UK Core Ethnic Category](StructureDefinition-UKCore-Extension-EthnicCategory.md) | British, Mixed British |



## Resource Content

```json
{
  "resourceType" : "Patient",
  "id" : "patient-example-jane",
  "meta" : {
    "profile" : [
      "https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition/onc-nhs-patient"
    ]
  },
  "extension" : [
    {
      "url" : "https://fhir.hl7.org.uk/StructureDefinition/UKCore-Extension-EthnicCategory",
      "valueCodeableConcept" : {
        "coding" : [
          {
            "system" : "https://fhir.hl7.org.uk/CodeSystem/UKCore-EthnicCategory",
            "code" : "A",
            "display" : "British, Mixed British"
          }
        ]
      }
    }
  ],
  "name" : [
    {
      "family" : "Doe",
      "given" : ["Jane"]
    }
  ],
  "gender" : "female"
}

```
