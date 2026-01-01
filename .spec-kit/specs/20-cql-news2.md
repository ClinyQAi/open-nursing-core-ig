# Spec 20: CQL NEWS2 Auto-Calculation

## Status
- [x] Specify
- [ ] Plan
- [ ] Tasks
- [ ] Implement

## Clinical Context
NEWS2 (National Early Warning Score 2) is the NHS-mandated standard for detecting patient deterioration. Currently, nurses manually calculate the score from individual observations. This specification adds **computable logic** to auto-calculate NEWS2 from constituent observations.

## The Problem
- Manual calculation is error-prone
- Delays in recognition of clinical deterioration
- Inconsistent application of score thresholds
- No automated escalation triggers

## The Solution
Embed CQL (Clinical Quality Language) logic directly into the Implementation Guide, enabling automatic NEWS2 calculation from raw vital signs.

---

## Clinical Requirements

### NEWS2 Components (Royal College of Physicians)
| Parameter | Score 3 | Score 2 | Score 1 | Score 0 | Score 1 | Score 2 | Score 3 |
|-----------|---------|---------|---------|---------|---------|---------|---------|
| Respiration Rate | ≤8 | - | 9-11 | 12-20 | - | 21-24 | ≥25 |
| SpO2 Scale 1 | ≤91 | 92-93 | 94-95 | ≥96 | - | - | - |
| SpO2 Scale 2 | ≤83 | 84-85 | 86-87 | 88-92 or ≥93 on air | 93-94 on O2 | 95-96 on O2 | ≥97 on O2 |
| Supplemental O2 | - | Yes | - | No | - | - | - |
| Systolic BP | ≤90 | 91-100 | 101-110 | 111-219 | - | - | ≥220 |
| Pulse | ≤40 | - | 41-50 | 51-90 | 91-110 | 111-130 | ≥131 |
| Consciousness | - | - | - | Alert | - | - | CVPU |
| Temperature | ≤35.0 | - | 35.1-36.0 | 36.1-38.0 | 38.1-39.0 | ≥39.1 | - |

### LOINC Codes
- **NEWS2 Total**: `1104051000000101` (UK SNOMED extension)
- **Respiration Rate**: `9279-1`
- **Oxygen Saturation**: `59408-5`
- **Systolic BP**: `8480-6`
- **Pulse Rate**: `8867-4`
- **Temperature**: `8310-5`
- **Consciousness (ACVPU)**: To be mapped

---

## CQL Logic

### Library: ONC_NEWS2_Logic

```cql
library ONC_NEWS2_Logic version '1.0.0'

using FHIR version '4.0.1'

include FHIRHelpers version '4.0.1'

context Patient

// Get most recent observation within last hour
define "Most Recent Respiratory Rate":
  Last([Observation: "9279-1"] O
    where O.status = 'final'
    sort by effective.as(dateTime))

define "Respiratory Rate Score":
  case
    when "Most Recent Respiratory Rate".value.as(Quantity).value <= 8 then 3
    when "Most Recent Respiratory Rate".value.as(Quantity).value between 9 and 11 then 1
    when "Most Recent Respiratory Rate".value.as(Quantity).value between 12 and 20 then 0
    when "Most Recent Respiratory Rate".value.as(Quantity).value between 21 and 24 then 2
    when "Most Recent Respiratory Rate".value.as(Quantity).value >= 25 then 3
    else null
  end

// Similar definitions for other parameters...

define "NEWS2 Total Score":
  "Respiratory Rate Score" 
  + "SpO2 Score" 
  + "Supplemental O2 Score"
  + "Systolic BP Score"
  + "Pulse Score"
  + "Consciousness Score"
  + "Temperature Score"

define "NEWS2 Clinical Risk":
  case
    when "NEWS2 Total Score" >= 7 then 'High'
    when "NEWS2 Total Score" between 5 and 6 then 'Medium'
    when exists("Single Parameter Score 3") then 'Low-Medium'
    when "NEWS2 Total Score" >= 1 then 'Low'
    else 'None'
  end
```

---

## FHIR Integration

### Library Resource

```json
{
  "resourceType": "Library",
  "id": "onc-news2-cql",
  "url": "http://opennursingcore.org/Library/ONC-NEWS2-CQL",
  "version": "1.0.0",
  "name": "ONC_NEWS2_Logic",
  "title": "ONC NEWS2 Auto-Calculation Logic",
  "status": "active",
  "type": {
    "coding": [{
      "system": "http://terminology.hl7.org/CodeSystem/library-type",
      "code": "logic-library"
    }]
  },
  "content": [{
    "contentType": "text/cql",
    "data": "<base64-encoded-cql>"
  }]
}
```

### PlanDefinition for Alerting

```fsh
Instance: NEWS2-Escalation-Plan
InstanceOf: PlanDefinition
Title: "NEWS2 Escalation Protocol"

* status = #active
* action[0].title = "High NEWS2 Alert"
* action[0].condition.kind = #applicability
* action[0].condition.expression.language = #text/cql
* action[0].condition.expression.expression = "NEWS2 Total Score >= 7"
* action[0].dynamicValue.path = "communication.payload.text"
* action[0].dynamicValue.expression.expression = "'URGENT: NEWS2 score is ' + ToString(NEWS2 Total Score)"
```

---

## Success Metrics
- [ ] CQL library compiles without errors
- [ ] All NEWS2 component scores calculated correctly
- [ ] Total score matches manual calculation in test cases
- [ ] Clinical risk classification aligns with RCP thresholds
- [ ] PlanDefinition triggers alerts at correct thresholds

---

## References
- Royal College of Physicians: NEWS2 Guidance
- HL7 CPG-on-FHIR: CQL Integration Patterns
- NHS England: Early Warning Score Implementation
