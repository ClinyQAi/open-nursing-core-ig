# example-reasonable-adjustment - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **example-reasonable-adjustment**

## Example Observation: example-reasonable-adjustment

Profile: [Reasonable Adjustment](StructureDefinition-onc-reasonable-adjustment.md)

**status**: Final

**category**: Survey

**code**: Reasonable Adjustment

**subject**: [Jane Doe Female, DoB Unknown](Patient-patient-example-jane.md)

**performer**: [Practitioner Nightingale](Practitioner-practitioner-example.md)

**value**: Requires large print documents (Font size 16+).



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "example-reasonable-adjustment",
  "meta" : {
    "profile" : [
      "https://opennursingcoreig.com/StructureDefinition/onc-reasonable-adjustment"
    ]
  },
  "status" : "final",
  "category" : [
    {
      "coding" : [
        {
          "system" : "http://terminology.hl7.org/CodeSystem/observation-category",
          "code" : "survey"
        }
      ]
    }
  ],
  "code" : {
    "coding" : [
      {
        "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
        "code" : "reasonable-adjustment"
      }
    ]
  },
  "subject" : {
    "reference" : "Patient/patient-example-jane"
  },
  "performer" : [
    {
      "reference" : "Practitioner/practitioner-example"
    }
  ],
  "valueString" : "Requires large print documents (Font size 16+)."
}

```
