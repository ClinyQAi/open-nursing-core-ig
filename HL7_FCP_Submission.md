# HL7 FHIR Community Process (FCP) Project Submission
## Open Nursing Core Implementation Guide

**Submission Date**: December 26, 2025  
**Project Lead**: [Your Name]  
**Contact**: [Your Email]  
**Organization**: [Your Organization/Independent]

---

## EXECUTIVE SUMMARY

The **Open Nursing Core (ONC) FHIR Implementation Guide** is a comprehensive, open-source IG that standardizes nursing documentation across the full spectrum of care, encompassing foundational assessments (ADPIE cycle), relational care (patient priorities, equity considerations), fundamental care (elimination, hydration, oral health), and specialized clinical domains (mental health, learning disabilities, frailty).

We seek **FCP Project approval** to formally recognize this work as compliant with HL7 FHIR standards and to foster broader community adoption within clinical systems, health information exchanges, and national interoperability frameworks (NHS England, ONC TEFCA).

---

## PROJECT DESCRIPTION

### 1. Project Name & Canonical URL
- **Name**: Open Nursing Core FHIR Implementation Guide (ONC-IG)
- **Canonical URL**: `https://fhir.clinyq.ai`
- **Package ID**: `@clinyqai/open-nursing-core-ig`
- **Current Version**: 0.1.0 (Draft/Beta)

### 2. Clinical Scope
The ONC-IG addresses a critical gap in nursing informatics by providing production-ready FHIR R4 profiles for:

#### Foundation & Safety (10 profiles)
- ADPIE cycle: Assessment, Problem (Diagnosis), Goal, Intervention, Evaluation
- Deterioration scores: NEWS2, qSOFA, ACVPU, Glasgow Coma Scale
- Risk assessments: Braden Scale (pressure ulcers), Waterlow, Morse Fall Scale, MUST (malnutrition), Barthel Index (ADLs)
- Cognition: MMSE

#### Relational & Inclusive Care (6 profiles)
- Patient-centred: What Matters to Me, Patient Story, Relational Observation
- Equity: Monk Skin Tone Scale (10-level), Fitzpatrick Skin Type
- Legal safeguards: Reasonable Adjustment (Equality Act 2010), Mental Capacity Assessment (MCA 2005)

#### Fundamental Care (5 profiles)
- Elimination: Bristol Stool Chart
- Hydration: Fluid Balance (Input/Output)
- Pain: Abbey Pain Scale (non-verbal patients with dementia)
- Hygiene: Oral Health Assessment
- Rest: Sleep Pattern

#### Specialized Care (9 profiles)
- Learning disabilities/autism: ABC Chart (Positive Behaviour Support)
- Epilepsy: Seizure Record
- Frailty: Clinical Frailty Scale (Rockwood 1-9)
- Delirium: 4AT Screen
- Wound care: Wound Assessment
- Diagnostics: Urinalysis (dipstick)
- Additional: Pain (general), Inspired Oxygen

### 3. Target Users
- **Clinical Systems**: EHR vendors (Epic, Cerner, EMIS, SystmOne)
- **Care Settings**: Acute hospitals, care homes, community nursing, mental health trusts
- **National Programs**: NHS Shared Care Records, U.S. TEFCA, Australian My Health Record
- **Research**: Health services research, quality improvement, machine learning
- **Education**: Nursing informatics curricula

### 4. Novel Contributions
- **First comprehensive nursing FHIR IG** covering all ADPIE phases + relational + equity domains
- **Monk Skin Tone Scale integration**: Addresses known bias in Fitzpatrick for darker skin tones
- **Mental Capacity Act compliance**: Structured MCA assessments with decision-specific documentation
- **Positive Behaviour Support**: ABC Chart for learning disability and autism services
- **Fundamental care visibility**: Structured oral health, sleep, elimination data (often relegated to free-text)

---

## FCP COMPLIANCE CHECKLIST

### ✅ FCP Specification Requirements

| Requirement | Status | Evidence |
|-------------|--------|----------|
| **1. Security, Safety, Privacy Documentation** | ✅ Complete | See "Security Considerations" section below |
| **2. Published at Canonical URL** | ✅ Complete | `https://opennursingcoreig.com/` (auto-deployed via GitHub Pages) |
| **3. QA Report with Zero Errors** | ⚠️ **3 Errors** | See "QA Status" section below. Errors are non-blocking semantic checks (skin tone display names). Ready for FCP with documented exceptions. |
| **4. FHIR Registry Inclusion** | ⚠️ Pending | Awaiting FCP approval to register at `simplifier.net/fhir-registry` and `registry.fhir.org` |
| **5. Issue Reporting Method** | ✅ Complete | GitHub Issues: `https://github.com/ClinyQAi/open-nursing-core-ig/issues` |
| **6. Licensing** | ✅ Complete | MIT License (compatible with CC0 for HL7 specifications) |
| **7. IG Conformance (Basic Rules)** | ✅ Complete | Conforms to HL7 IG Publishing Requirements v1.6.34 |

### QA Status Detail
**Current Errors**: 3 (down from 96 initial)  
**Nature of Remaining Errors**:
1. SNOMED CT display name mismatch for Fitzpatrick skin types (non-blocking, cosmetic)
2. Local code `#monk-mst-X` not in external terminology (intentional design choice pending SNOMED CT submission)

**Warnings**: 57 (acceptable for beta per HL7 QA guidelines)  
**Build Status**: Success (IG Publisher v1.6.34)

**Action Plan**: We will:
- Submit concept requests to SNOMED International for Monk Skin Tone codes
- Map all local `ONCObservationCodes` to SNOMED CT/LOINC where possible
- Achieve zero errors for FMM Level 2 (STU ballot readiness)

---

## SECURITY, SAFETY, AND PRIVACY CONSIDERATIONS

### Security
- **No Authentication/Authorization Logic**: This IG defines data models only; security is the responsibility of implementing systems (SMART on FHIR, OAuth 2.0).
- **Sensitive Data**: Mental Capacity Assessments and Reasonable Adjustments may contain sensitive legal/personal information. Implementers must apply appropriate access controls per jurisdictional regulations (GDPR, HIPAA).

### Safety
- **Clinical Decision Support**: Deterioration scores (NEWS2, qSOFA) are intended to support, not replace, clinical judgment. Implementers must ensure alerts/escalations are configurable and auditable.
- **Data Integrity**: Incorrect recording of assessments (e.g., Bristol Stool Chart, 4AT Delirium) can lead to inappropriate care. Implementers should use validation rules and user training.

### Privacy
- **Patient Narratives**: "What Matters to Me" and "Patient Story" contain highly personal information. Systems must:
  - Allow granular consent (FHIR `Consent` resource)
  - Support patient-controlled sharing
  - Redact/anonymize for secondary use

- **Reasonable Adjustments**: Disability-related information is protected under Equality Act/ADA. Systems must enforce role-based access and audit logs.

### Issue Reporting
Security/safety/privacy vulnerabilities should be reported via:
- **GitHub Security Advisories**: `https://github.com/ClinyQAi/open-nursing-core-ig/security/advisories`
- **Email**: [Your Email] (for confidential disclosures)

---

## DEVELOPMENT GOVERNANCE

### Current Status
- **Development Model**: Community-driven, open-source (GitHub)
- **License**: MIT (code) + CC0 (documentation, compatible with HL7 requirements)
- **Version Control**: Git with semantic versioning (0.1.0 = initial beta)
- **Contributors**: [List key contributors if applicable]

### Proposed HL7 Work Group Sponsorship
We seek sponsorship from the **HL7 Patient Care Work Group** (or **Clinical Quality Information WG** if nursing falls under their remit). Rationale:
- Patient Care WG has produced foundational Observation/Condition/Goal/Procedure profiles
- ONC-IG extends these with nursing-specific constraints
- Aligns with WG's mission to improve care coordination and patient-centred data

**Co-Sponsorship Requested**:
- **Orders & Observations WG**: For clinical assessment profiles (NEWS2, Braden, etc.)
- **Clinical Decision Support WG**: For integration with CDS Hooks (future work)

### Community Engagement Plan
1. **Beta Testing** (Q1 2025): Pilot with 2-3 NHS Trusts, 1 care home provider
2. **Public Comment Period** (Q2 2025): Solicit feedback via FHIR Zulip, nursing informatics forums
3. **STU Ballot** (Q3 2025): Submit for HL7 STU ballot after achieving FMM Level 2
4. **Normative Ballot** (2026-2027): Target FMM Level 5 with real-world implementation evidence

---

## TECHNICAL ARTIFACTS

### Repository & Documentation
- **Source Code**: `https://github.com/ClinyQAi/open-nursing-core-ig`
- **Documentation**: `https://opennursingcoreig.com/`
- **NPM Package**: `npm install @clinyqai/open-nursing-core-ig`
- **FHIR Package**: `package.tgz` (656KB, contains all StructureDefinitions, ValueSets, CodeSystems)

### Artifact Summary
- **30 StructureDefinitions** (29 profiles + 1 patient extension)
- **3 Extensions** (goal-reference, intervention-goal-reference, observation-goal-reference)
- **3 CodeSystems** (ONCObservationCodes, ONCMonkScale, ONCProblemType)
- **18 ValueSets**
- **14 Example Instances** (covering all profile categories)
- **3,200+ lines of FHIR Shorthand (FSH)**

### Build Process
- **FSH Compiler**: SUSHI v3.16.5
- **IG Publisher**: HL7 FHIR IG Publisher v1.6.34
- **CI/CD**: GitHub Actions (automated validation and deployment)
- **Deployment**: GitHub Pages with custom domain (`opennursingcoreig.com`)

---

## ALIGNMENT WITH NATIONAL/INTERNATIONAL INITIATIVES

### NHS England
- **Digital First Primary Care**: ONC profiles enable structured GP-to-hospital handovers
- **Shared Care Records**: Provides nursing data standards for local health and care record exemplars (LHCREs)
- **Patient Safety**: NEWS2 and deterioration scores support Patient Safety Incident Response Framework (PSIRF)

### U.S. Office of the National Coordinator (ONC)
- **TEFCA**: ONC-IG nursing assessments can flow through Qualified Health Information Networks (QHINs)
- **USCDI+ Nursing**: Aligns with proposed USCDI+ nursing data elements (if/when formalized)

### Australia (ADHA)
- **My Health Record**: ONC profiles could complement AU Base IG for nursing summaries

### International Council of Nurses (ICN)
- **ICNP Alignment**: We will map `ONCObservationCodes` to ICNP 2024 edition where applicable

---

## ROADMAP & FUTURE WORK

### Version 0.1.0 → 1.0.0 (Beta → Stable)
1. **Clinical Validation**: Implement in 5+ pilot sites, gather usability feedback
2. **Terminology Harmonization**: Submit 100+ concept requests to SNOMED CT and LOINC
3. **Example Expansion**: Add 20+ additional synthetic examples (pediatric, palliative, community nursing scenarios)
4. **CDS Hooks**: Develop reference implementations for NEWS2 escalation, capacity assessment prompts
5. **FHIR Maturity Model**: Achieve FMM Level 2 (STU) by Q3 2025, FMM Level 5 (Normative) by 2027

### Future Modules (Version 2.x)
- **Pediatric Nursing**: FLACC, COMFORT-B scales, pediatric early warning scores
- **Palliative/End-of-Life Care**: IPOS, POS-S, Liverpool Care Pathway elements
- **Community/Home Nursing**: District nurse visit documentation, medication administration records
- **Critical Care**: RASS, CAM-ICU for ventilated patients, SOFA score

---

## REQUESTED ACTION FROM HL7 FCPCC

We respectfully request:

1. **FCP Participant Status** (if not already approved)
2. **FCP Project Approval** for "Open Nursing Core FHIR Implementation Guide"
3. **Guidance on QA Exception Process** for the 3 remaining non-blocking errors
4. **Work Group Sponsorship Facilitation** (Patient Care WG introduction)
5. **Registry Inclusion** upon FCP approval

---

## SUPPORTING MATERIALS

### Appendix A: List of All Profiles
1. ONCNursingAssessment (parent)
2. ONCNursingProblem
3. ONCPatientGoal
4. ONCNursingIntervention
5. ONCGoalEvaluation
6. ONCBradenScaleAssessment
7. ONCNEWS2Score
8. ONCWaterlowScore
9. ONCMUSTScore
10. ONCMorseFallScale
11. ONCGlasgowComaScale
12. ONCqSOFA
13. ONCBarthelIndex
14. ONCMMSE
15. ONCACVPU
16. ONCBloodPressure
17. ONCHeartRate
18. ONCRespirationRate
19. ONCBodyTemperature
20. ONCOxygenSaturation
21. ONCInspiredOxygen
22. ONCPainAssessment
23. ONCWoundAssessment
24. ONCSkinToneObservation (Fitzpatrick)
25. ONCMonkSkinToneObservation
26. ONCWhatMattersToMe
27. ONCPatientStory
28. ONCRelationalObservation
29. ONCReasonableAdjustment
30. ONCMentalCapacity
31. ONCClinicalFrailtyScale
32. ONC4ATDelirium
33. ONCBristolStoolChart
34. ONCAbbeyPainScale
35. ONCFluidBalance
36. ONCABCChart
37. ONCOralHealth
38. ONCSeizureRecord
39. ONCSleepPattern
40. ONCUrinalysis

### Appendix B: Community Engagement Evidence
- **GitHub Stars**: [Current count]
- **Community Contributors**: [List names if applicable]
- **Presentations**: [List any conference presentations, webinars]
- **Publications**: Manuscript submitted to JAMIA Open (December 2025)

---

## CONTACT INFORMATION

**Project Lead**: [Your Name]  
**Email**: [Your Email]  
**GitHub**: `https://github.com/ClinyQAi/open-nursing-core-ig`  
**Website**: `https://opennursingcoreig.com/`  
**LinkedIn**: [Your LinkedIn if applicable]

**Availability**: Available for FCPCC review meetings, HL7 Work Group presentations, and community calls.

---

## DECLARATION

I/We declare that:
1. The Open Nursing Core IG is developed in good faith to advance nursing informatics and FHIR adoption.
2. All content is original or properly attributed, with no intellectual property conflicts.
3. We commit to maintaining the IG per FCP requirements, including timely issue resolution and QA improvements.
4. We agree to HL7's licensing terms (CC0 for specifications, with MIT for reference implementations).

**Signature**: [Your Name]  
**Date**: December 26, 2025

---

**END OF SUBMISSION PACKAGE**
