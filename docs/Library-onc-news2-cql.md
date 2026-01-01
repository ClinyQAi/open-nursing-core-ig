# ONC NEWS2 Auto-Calculation Logic - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **ONC NEWS2 Auto-Calculation Logic**

## Library: ONC NEWS2 Auto-Calculation Logic (Experimental) 

| | |
| :--- | :--- |
| *Official URL*:http://opennursingcore.org/Library/ONC-NEWS2-CQL | *Version*:0.1.0 |
| Active as of 2026-01-01 | *Computable Name*:ONC_NEWS2_Logic |

 
Logic library for calculating National Early Warning Score 2 (NEWS2) from FHIR Observations. 

* * **Content:**text/cql: ````````: **Id:**
  * ?: onc-news2-cql
* * **Content:**text/cql: ````````: **Version:**
  * ?: 0.1.0
* * **Content:**text/cql: ````````: **Url:**
  * ?: [ONC NEWS2 Auto-Calculation Logic](Library-onc-news2-cql.md)
* * **Content:**text/cql: ````````: **Experimental:**
  * ?: true
* * **Content:**text/cql: ````````: **Date:**
  * ?: 2026-01-01 13:37:23+0000
* * **Content:**text/cql: ````````: **Description:**
  * ?: Logic library for calculating National Early Warning Score 2 (NEWS2) from FHIR Observations.



## Resource Content

```json
{
  "resourceType" : "Library",
  "id" : "onc-news2-cql",
  "url" : "http://opennursingcore.org/Library/ONC-NEWS2-CQL",
  "version" : "0.1.0",
  "name" : "ONC_NEWS2_Logic",
  "title" : "ONC NEWS2 Auto-Calculation Logic",
  "status" : "active",
  "experimental" : true,
  "type" : {
    "coding" : [
      {
        "system" : "http://terminology.hl7.org/CodeSystem/library-type",
        "code" : "logic-library"
      }
    ]
  },
  "date" : "2026-01-01T13:37:23+00:00",
  "description" : "Logic library for calculating National Early Warning Score 2 (NEWS2) from FHIR Observations.",
  "content" : [
    {
      "contentType" : "text/cql",
      "url" : "input/cql/ONC_NEWS2_Logic.cql"
    }
  ]
}

```
