# Open Nursing Core FHIR Implementation Guide

Welcome to the **Open Nursing Core FHIR Implementation Guide (ONC-IG)**.

This Implementation Guide provides foundational FHIR R4 profiles for documenting the nursing process (ADPIE - Assessment, Diagnosis, Planning, Implementation, Evaluation), with a focus on **Safety** and **Equity** in nursing care.

## Overview

The ONC-IG defines standardized FHIR profiles for:

- **Patient Assessment** - Nursing observations and assessments
- **Nursing Diagnosis** - Problem identification and categorization  
- **Patient Goals** - Goal setting and outcome evaluation
- **Nursing Interventions** - Care activities and procedures
- **Safety Assessments** - Braden Scale for pressure ulcer risk
- **Equity Considerations** - Skin tone documentation for equitable care

## Key Profiles

| Profile | Description |
|---------|-------------|
| [ONC Nursing Assessment](StructureDefinition-onc-nursing-assessment.html) | Base profile for all nursing observations |
| [Braden Scale Assessment](StructureDefinition-onc-braden-scale-assessment.html) | Pressure ulcer risk assessment |
| [Nursing Problem](StructureDefinition-onc-nursing-problem.html) | Nursing diagnosis documentation |
| [Patient Goal](StructureDefinition-onc-patient-goal.html) | Patient-centered goal setting |
| [Nursing Intervention](StructureDefinition-onc-nursing-intervention.html) | Care activity documentation |
| [Goal Evaluation](StructureDefinition-onc-goal-evaluation.html) | Outcome assessment |
| [Skin Tone Observation](StructureDefinition-onc-skintone-observation.html) | Fitzpatrick skin type for equitable assessment |

## Getting Started

- Browse the [Artifacts](artifacts.html) for all profiles, extensions, and examples
- Download the [full package](package.tgz) for use in your FHIR server

## License

This Implementation Guide is released under the MIT License.

## Contact

For questions or contributions, visit our [GitHub repository](https://github.com/ClinyQAi/open-nursing-core-ig).
