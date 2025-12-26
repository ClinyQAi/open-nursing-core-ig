# Open Nursing Core FHIR Implementation Guide

Welcome to the **Open Nursing Core FHIR Implementation Guide (ONC-IG)**.

This IG provides **Standardized Nursing Data Models** for the NHS and beyond, focusing on the complete nursing process (ADPIE) and specialized care needs.

## 🌟 Core Philosophy
- **Holistic**: Covers physical, mental, and social needs.
- **Relational**: Captures "What Matters to Me" and patient stories.
- **Equitable**: Includes Safe Skin Tone (Monk Scale) and Reasonable Adjustments.

---

## 📚 Profile Library

### 1. Foundation & Safety 🛡️
Base profiles for standard nursing operations.
- [OncNursingAssessment](StructureDefinition-onc-nursing-assessment.html)
- [OncNursingProblem](StructureDefinition-onc-nursing-problem.html) (Diagnosis)
- [OncPatientGoal](StructureDefinition-onc-patient-goal.html)
- [OncNursingIntervention](StructureDefinition-onc-nursing-intervention.html)
- [Braden Scale](StructureDefinition-onc-braden-scale-assessment.html) (Pressure Ulcer Risk)
- [Waterlow Score](StructureDefinition-onc-waterlow-score.html)
- [NEWS2](StructureDefinition-onc-news2-score.html) (Deterioration)

### 2. Relational & Inclusive Care ❤️
Capturing the person behind the patient.
- [What Matters To Me](StructureDefinition-onc-what-matters.html)
- [Patient Story](StructureDefinition-onc-patient-story.html)
- [Reasonable Adjustment](StructureDefinition-onc-reasonable-adjustment.html) (Equality Act)
- [Mental Capacity Assessment](StructureDefinition-onc-mental-capacity.html)
- [Skin Tone Observation](StructureDefinition-onc-skintone-observation.html) (Monk/Fitzpatrick)

### 3. Fundamental Care 💧
The essentials of daily nursing care.
- [Bristol Stool Chart](StructureDefinition-onc-bristol-stool-chart.html) (Elimination)
- [Fluid Balance](StructureDefinition-onc-fluid-balance.html) (Hydration)
- [Abbey Pain Scale](StructureDefinition-onc-abbey-pain-scale.html) (Non-verbal pain)
- [Oral Health](StructureDefinition-onc-oral-health.html)
- [Sleep Pattern](StructureDefinition-onc-sleep-pattern.html)

### 4. Specialized & Mental Health 🧠
Tools for Learning Disabilities, Mental Health, and Geriatrics.
- [ABC Chart](StructureDefinition-onc-abc-chart.html) (Positive Behaviour Support)
- [Seizure Record](StructureDefinition-onc-seizure-record.html) (Epilepsy)
- [Clinical Frailty Scale](StructureDefinition-onc-clinical-frailty-scale.html)
- [4AT Delirium Screen](StructureDefinition-onc-4at-delirium.html)
- [Urinalysis](StructureDefinition-onc-urinalysis.html)

---

## 🚀 Getting Started

1. **Browse Artifacts**: See the [Artifacts Page](artifacts.html) for all JSON definitions.
2. **Download Package**: `npm install @clinyqai/open-nursing-core-ig`
3. **Contribute**: Visit [GitHub](https://github.com/ClinyQAi/open-nursing-core-ig).

---
*Built with ❤️ by the Open Nursing Community*
