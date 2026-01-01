# Spec 15: Equity Skin Tone Profile

## Status
- [x] Specify
- [ ] Plan
- [ ] Tasks
- [ ] Implement

## Clinical Context
Traditional wound and pressure ulcer assessments often fail patients with darker skin tones because clinical signs like "redness," "blanching," and "pallor" are less visible. This profile ensures skin tone is captured as **mandatory clinical context** for any skin integrity assessment.

## The Problem
- Pressure ulcer detection algorithms trained on predominantly white patient populations
- "Redness" as a gold-standard indicator disadvantages darker-skinned patients
- AI models trained on uncontextualised wound data perpetuate health disparities

## The Solution
Create a mandatory linkage where **no Wound Assessment can exist without a corresponding Skin Tone Observation**.

---

## Clinical Requirements

### Assessment Tool
- **Name**: Skin Tone Observation
- **Scale**: Fitzpatrick scale (I-VI) or NHS Monk Skin Tone Scale
- **Purpose**: Contextualise skin assessments for equitable clinical decisions

### SNOMED Coding
- **Skin Tone**: `406157005` - Skin type (observable entity)
- **Fitzpatrick Scale**: To be mapped to specific SNOMED concepts

### Fitzpatrick Scale Values
| Type | Description | SNOMED Concept |
|------|-------------|----------------|
| I | Light, pale white | TBD |
| II | White, fair | TBD |
| III | Medium, white to olive | TBD |
| IV | Olive, moderate brown | TBD |
| V | Brown, dark brown | TBD |
| VI | Very dark brown to black | TBD |

---

## FHIR Structure

### Profile: ONCEquitySkinTone

```fsh
Profile: ONCEquitySkinTone
Parent: Observation
Id: onc-equity-skin-tone
Title: "ONC Equity Skin Tone Observation"
Description: "Captures patient skin tone for equitable skin integrity assessment."

* status MS
* code = http://snomed.info/sct#406157005 "Skin type"
* subject only Reference(Patient)
* valueCodeableConcept from ONCFitzpatrickScaleVS (required)
* effectiveDateTime MS
```

### ValueSet: FitzpatrickScaleVS

```fsh
ValueSet: ONCFitzpatrickScaleVS
Id: onc-fitzpatrick-scale-vs
Title: "Fitzpatrick Skin Type Scale"
Description: "Skin phototype classification I-VI"

* include codes from system http://snomed.info/sct where concept is-a #406157005
```

---

## Critical Innovation: Mandatory Invariant

### The "Data Quality Gate"

```fsh
Invariant: onc-equity-skin-tone-required
Description: "Wound assessments MUST have an associated skin tone observation"
Expression: "Observation.hasMember.exists(resolve().code.coding.where(code = '443846001')) implies Observation.hasMember.exists(resolve().code.coding.where(code = '406157005'))"
Severity: #error
```

### Implementation Pattern

```fsh
Profile: ONCBradenScore
Parent: Observation
Id: onc-braden-score

* obeys onc-equity-skin-tone-required
* hasMember ^slicing.discriminator.type = #pattern
* hasMember ^slicing.discriminator.path = "resolve().code"
* hasMember contains skinTone 1..1 MS
* hasMember[skinTone] only Reference(ONCEquitySkinTone)
```

---

## AI Safety Certification

### Why This Matters for AI
```
WITHOUT Skin Tone Context:
Training Data → Biased Model → Inequitable Care Recommendations

WITH Skin Tone Context:
Training Data + Skin Tone → Fair Model → Equitable, Contextualised Recommendations
```

### Certification Badge
Data generated using ONC-IG equity profiles can claim:
> "AI Training Safe: Equity Context Included"

---

## Success Metrics
- [ ] Skin Tone profile compiles without errors
- [ ] Invariant correctly rejects Braden/Waterlow without linked Skin Tone
- [ ] Invariant correctly accepts Braden/Waterlow with linked Skin Tone
- [ ] Example instances demonstrate correct linking pattern
- [ ] Clinical review confirms terminology appropriateness

---

## References
- NHS England: Addressing racial inequalities in wound care
- Kumbi Kariwo (Nurse Citizen Developer): Skin Tone Inclusivity Lead
- Monk Skin Tone Scale: Google's 10-point alternative to Fitzpatrick
