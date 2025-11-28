# Monk Skin Tone Scale - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Monk Skin Tone Scale**

## CodeSystem: Monk Skin Tone Scale 

| | |
| :--- | :--- |
| *Official URL*:https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-monk-scale | *Version*:1.0.0 |
| Active as of 2025-11-28 | *Computable Name*:ONCMonkScale |

 
The Monk Skin Tone (MST) Scale is a 10-shade scale designed to represent a broader range of skin tones for AI and equity applications. 

 This Code system is referenced in the content logical definition of the following value sets: 

* [ONCMonkScaleVS](ValueSet-onc-monk-scale-vs.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "onc-monk-scale",
  "url" : "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-monk-scale",
  "version" : "1.0.0",
  "name" : "ONCMonkScale",
  "title" : "Monk Skin Tone Scale",
  "status" : "active",
  "date" : "2025-11-28T02:23:26+00:00",
  "description" : "The Monk Skin Tone (MST) Scale is a 10-shade scale designed to represent a broader range of skin tones for AI and equity applications.",
  "content" : "complete",
  "count" : 10,
  "concept" : [
    {
      "code" : "MST-01",
      "display" : "Monk Scale 01",
      "definition" : "Lightest skin tone"
    },
    {
      "code" : "MST-02",
      "display" : "Monk Scale 02"
    },
    {
      "code" : "MST-03",
      "display" : "Monk Scale 03"
    },
    {
      "code" : "MST-04",
      "display" : "Monk Scale 04"
    },
    {
      "code" : "MST-05",
      "display" : "Monk Scale 05"
    },
    {
      "code" : "MST-06",
      "display" : "Monk Scale 06"
    },
    {
      "code" : "MST-07",
      "display" : "Monk Scale 07"
    },
    {
      "code" : "MST-08",
      "display" : "Monk Scale 08"
    },
    {
      "code" : "MST-09",
      "display" : "Monk Scale 09"
    },
    {
      "code" : "MST-10",
      "display" : "Monk Scale 10",
      "definition" : "Darkest skin tone"
    }
  ]
}

```
