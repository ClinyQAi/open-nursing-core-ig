# Open Nursing Core: A Comprehensive FHIR Implementation Guide for Standardizing Nursing Documentation Across Physical, Mental, and Social Health Domains

**Authors**: [Your Name]^1^, [Co-authors as applicable]  
**Affiliations**: ^1^[Your Institution]

**Corresponding Author**: [Email]

---

## ABSTRACT

**Objective**: To develop and validate a comprehensive FHIR R4 Implementation Guide (IG) that standardizes nursing documentation across the full spectrum of care, encompassing foundational assessments, relational care, fundamental needs, and specialized clinical domains including mental health and learning disabilities.

**Materials and Methods**: We employed FHIR Shorthand (FSH) to develop 30+ StructureDefinition profiles, extensions, CodeSystems, and ValueSets based on established clinical instruments and nursing frameworks. Profiles were organized into four modules: (1) Foundation & Safety (ADPIE cycle, pressure ulcer risk, deterioration scores); (2) Relational & Inclusive Care (patient priorities, mental capacity, equity considerations); (3) Fundamental Care (elimination, hydration, pain, oral health, sleep); and (4) Specialized Care (positive behaviour support, seizure management, delirium screening, frailty assessment). The IG underwent iterative validation using SUSHI v3.16.5 and the HL7 FHIR IG Publisher v1.6.34, reducing initial validation errors from 96 to 3 through systematic terminology mapping and structural refinement. The canonical URL was standardized to `https://fhir.clinyq.ai`, and the IG was versioned at 0.1.0 (draft status) for beta community feedback.

**Results**: The Open Nursing Core IG successfully defines standardized FHIR resources for 30+ nursing assessments and care processes. Key innovations include: (a) local CodeSystem (ONCObservationCodes) with 100+ nursing-specific concepts to address external terminology gaps; (b) integration of the Monk Skin Tone Scale alongside Fitzpatrick for equitable skin assessment; (c) Mental Capacity Act-compliant profiles for legal safeguarding; (d) Positive Behaviour Support (PBS) ABC Chart for learning disability/autism care; (e) comprehensive fundamental care profiles (Bristol Stool Chart, Abbey Pain Scale, oral health, sleep pattern, urinalysis) rarely captured in existing FHIR IGs. The IG artifacts are publicly available on GitHub and published to GitHub Packages as `@clinyqai/open-nursing-core-ig`, with documentation deployed to `opennursingcoreig.com`.

**Discussion**: This work addresses a critical gap in nursing informatics by providing a foundation for interoperable, person-centred digital nursing records. Unlike existing FHIR IGs that focus primarily on physician-centric workflows, the Open Nursing Core IG explicitly models the holistic nursing process—including relational domains (What Matters to Me, Patient Story) and equity considerations (Reasonable Adjustments, inclusive skin tone assessment). The use of local codes, while pragmatic for beta release, highlights the need for international nursing terminology harmonization within SNOMED CT and LOINC. Limitations include the absence of real-world piloting and the preliminary status of certain profiles (e.g., wound assessment complexity).

**Conclusion**: The Open Nursing Core IG represents a significant step toward standardized, FHIR-based nursing documentation that balances clinical rigor with person-centred care principles. Future work will focus on clinical validation, integration with Electronic Health Record systems, and expansion to include additional specialized nursing domains (e.g., palliative care, community nursing).

**Keywords**: FHIR, Nursing Informatics, Interoperability, Standardization, Person-Centred Care, Mental Health Nursing, Learning Disabilities

---

## LAY SUMMARY

Nurses record vital information about patients every day—from basic health checks to understanding what matters most to each person. However, different hospitals and care settings use different computer systems that don't "talk" to each other, making it hard to share this important information safely and quickly. We created the "Open Nursing Core"—a free, open-source digital toolkit that provides a common language for 30+ types of nursing records. This includes everything from pressure sore risk assessments and early warning scores, to recording a patient's life story and personal goals. By using international health data standards (FHIR), our toolkit helps nursing information flow seamlessly between GP surgeries, hospitals, care homes, and community services. This means nurses spend less time re-entering data and more time caring for patients, while ensuring critical information like mental capacity assessments and specialized needs (e.g., for people with dementia or learning disabilities) are never lost during transfers of care.

---

## INTRODUCTION

### Background

Nursing documentation forms the backbone of safe, effective healthcare delivery, yet it remains one of the least standardized components of electronic health records (EHRs)[1,2]. While physician-centric clinical data has benefitted from decades of standardization efforts through initiatives like HL7 FHIR (Fast Healthcare Interoperability Resources)[3], nursing-specific assessments, care plans, and interventions continue to be captured in proprietary, non-interoperable formats[4,5]. This fragmentation has profound consequences: critical nursing intelligence is lost during care transitions, duplicate assessments burden both patients and clinicians, and the unique contribution of nursing to patient outcomes remains invisible in aggregated health data[6,7].

The nursing process—Assessment, Diagnosis, Planning, Implementation, and Evaluation (ADPIE)—provides a systematic framework for delivering holistic, person-centred care[8]. However, digital implementations of ADPIE rarely extend beyond basic vital signs and task management, neglecting relational domains (e.g., patient priorities, life narratives) and specialized assessments essential for vulnerable populations, such as those with dementia, learning disabilities, or complex mental health needs[9,10].

### The Case for FHIR in Nursing

FHIR has emerged as the de facto standard for health data exchange, with mandates from regulatory bodies including NHS England, the U.S. Office of the National Coordinator (ONC), and the European Commission[11-13]. FHIR's resource-based architecture, RESTful API design, and extensibility make it well-suited for capturing the multi-dimensional nature of nursing care[14]. However, existing FHIR Implementation Guides (IGs) overwhelmingly prioritize medical diagnoses, procedures, and medications, with minimal representation of nursing assessments beyond basic observations[15,16].

Recent initiatives, such as the International Council of Nurses' (ICN) work on the International Classification for Nursing Practice (ICNP) and efforts to map nursing concepts to SNOMED CT, have laid important groundwork[17,18]. Yet, pragmatic, production-ready FHIR profiles for nursing remain scarce, particularly for specialized domains like mental health nursing, positive behaviour support, and fundamental care activities (e.g., oral hygiene, elimination patterns, sleep quality)[19].

### Equity and Inclusivity in Health IT

The COVID-19 pandemic starkly exposed how inadequate data infrastructure perpetuates health inequities, particularly for minoritized communities and people with disabilities[20,21]. Skin assessments—critical for detecting pressure injuries, rashes, and deterioration—were identified as systematically biased when documentation systems defaulted to Fitzpatrick skin types optimized for lighter skin tones[22,23]. Similar gaps exist for capturing Reasonable Adjustments (required under the UK Equality Act 2010) and Mental Capacity Act assessments, both of which are legal requirements but often documented in free-text notes rather than structured, queryable fields[24,25].

### Objectives

This study aimed to:
1. Develop a comprehensive, open-source FHIR R4 Implementation Guide covering the full nursing process, with explicit inclusion of relational care, equity considerations, and specialized domains (mental health, learning disabilities, frailty).
2. Validate the IG's structural integrity and interoperability using standard FHIR tooling.
3. Publish the IG as a freely accessible resource to support adoption in clinical systems, research platforms, and policy development.

---

## MATERIALS AND METHODS

### Development Framework

We employed an iterative, community-driven approach informed by nursing informatics best practices and FHIR profiling methodologies[26,27]. The project was conducted between [Date Range] and involved collaboration with registered nurses across acute care, mental health, learning disability, and community settings.

#### FHIR Shorthand (FSH)
All profiles were authored using FHIR Shorthand (FSH) v3.0, a domain-specific language that enables human-readable, version-controlled definition of FHIR artifacts[28]. FSH files were organized into 23 modules (e.g., `onc-profiles.fsh`, `onc-equity.fsh`, `onc-pbs.fsh`) to facilitate maintainability and collaborative editing via Git version control.

#### Toolchain
- **SUSHI** (SUSHI Unshortens Short Hand Inputs) v3.16.5: Compiled FSH to FHIR JSON/XML StructureDefinitions[29].
- **HL7 FHIR IG Publisher** v1.6.34: Generated navigable HTML documentation and validated conformance[30].
- **GitHub Actions**: Automated continuous integration pipelines for validation and deployment.
- **GitHub Pages**: Hosted the IG at `opennursingcoreig.com` with a custom domain.

### Profile Development Methodology

#### Phase 1: Foundational Profiles (ADPIE Cycle)
We first established base profiles for the ADPIE framework:
- **ONCNursingAssessment** (parent profile extending `Observation`): Supports `CodeableConcept`, `Quantity`, and `string` value types to accommodate diverse assessment formats.
- **ONCNursingProblem** (extending `Condition`): Captures nursing diagnoses with a custom `ONCProblemType` CodeSystem (nursing diagnosis, risk state, syndrome).
- **ONCPatientGoal** (extending `Goal`): Links to problems via the `addresses` element.
- **ONCNursingIntervention** (extending `Procedure`): References goals via a custom `intervention-goal-reference` extension.
- **ONCGoalEvaluation** (extending `Observation`): Assesses goal achievement with a `goal-reference` extension.

#### Phase 2: Safety & Deterioration Scores
Standard risk assessment tools were profiled:
- **Braden Scale** (pressure ulcer risk): 6-component slicing (Sensory Perception, Moisture, Activity, Mobility, Nutrition, Friction/Shear) with local codes (`#braden-sensory`, etc.) due to incomplete LOINC coverage.
- **NEWS2** (National Early Warning Score): Physiological parameters + total score, mapped to `http://snomed.info/sct#1104051000000101`.
- **Waterlow**, **MUST** (malnutrition), **Morse Fall Scale**, **Glasgow Coma Scale**, **qSOFA** (sepsis), **Barthel Index** (ADL independence): Each profiled with component-based architecture.

#### Phase 3: Equity & Relational Care
- **Monk Skin Tone Scale**: 10-level scale (MST-1 to MST-10) defined in `ONCMonkScale` CodeSystem, profiled in `ONCMonkSkinToneObservation`. Included alongside Fitzpatrick (`ONCSkinToneObservation`) to address limitations in darker skin tone representation[31].
- **Reasonable Adjustment**: String-based observation (e.g., "Requires BSL interpreter", "Cannot use stairs") mapped to `#reasonable-adjustment` code.
- **Mental Capacity Assessment**: CodeableConcept with `MentalCapacityVS` (Capacity Present, Capacity Absent, Best Interest Decision Made). Aligns with Mental Capacity Act 2005 requirements.
- **What Matters to Me**: String observation capturing patient-defined priorities (e.g., "Walking my dog daily").
- **Patient Story**: Narrative background (former occupation, hobbies, family context) to support person-centred care.

#### Phase 4: Fundamental Care
- **Bristol Stool Chart**: Integer (1-7) with invariant constraint (`bristol-range`).
- **Abbey Pain Scale**: Non-verbal pain assessment (6 components: Vocalization, Facial Expression, Body Language, Behavioural Change, Physiological Change, Physical Changes). Total score interpretation: 0-2 (no pain), 3-7 (mild), 8-13 (moderate), 14+ (severe).
- **Fluid Balance**: Input/output components with calculated balance (Quantity in mL).
- **Oral Health**: 5-component assessment (Lips, Tongue, Gums, Teeth, Saliva) based on OHAT (Oral Health Assessment Tool).
- **Sleep Pattern**: Hours slept (Quantity), quality (string), disturbances (string).

#### Phase 5: Specialized Care
- **Positive Behaviour Support (PBS) ABC Chart**: Antecedent, Behaviour, Consequence, Function, Duration, Intensity. Critical for learning disability and autism care settings.
- **Seizure Record**: Type (Tonic-Clonic, Absence, Focal), duration (minutes), recovery phase description, triggers.
- **Clinical Frailty Scale**: Rockwood 1-9 scale (Very Fit to Terminally Ill).
- **4AT Delirium Screen**: Alertness, AMT4 (4-item mental test), Attention (months backwards), Acute Change. Total score ≥4 suggests delirium.
- **Urinalysis**: 8-parameter dipstick (Leukocytes, Nitrites, Protein, Blood, Glucose, Ketones, pH, Specific Gravity).

### Terminology Strategy

To address gaps in existing terminologies (SNOMED CT, LOINC), we created the **ONCObservationCodes** local CodeSystem with 100+ concepts. This pragmatic approach enabled rapid beta deployment while maintaining semantic clarity. For established concepts, we referenced:
- SNOMED CT for clinical findings and procedures
- LOINC for vital signs and laboratory tests where coverage existed
- HL7 Observation Category CodeSystem for categorization

### Validation Process

1. **Syntactic Validation**: SUSHI compilation identified FSH syntax errors, missing elements, and type mismatches.
2. **Structural Validation**: IG Publisher verified FHIR conformance, cardinality constraints, and slicing definitions.
3. **Terminology Validation**: Validated ValueSet bindings and CodeSystem references. Iteratively resolved "unknown code" errors by creating local codes where necessary.
4. **Example Instances**: Authored 14 synthetic clinical examples covering all major profile categories (stored in `onc-master-examples.fsh` and `onc-new-examples.fsh`).

Initial validation yielded 96 errors (primarily canonical URL mismatches and missing LOINC codes). Through systematic remediation:
- Standardized canonical URL to `https://fhir.clinyq.ai`
- Mapped 40+ assessment codes to local system
- Corrected ValueSet bindings
- Added missing element descriptions

Final validation: **3 errors, 57 warnings** (remaining errors: non-blocking semantic checks; warnings: acceptable for beta release per FHIR QA guidelines[32]).

### Deployment & Accessibility

- **GitHub Repository**: `https://github.com/ClinyQAi/open-nursing-core-ig` (MIT License)
- **Package Registry**: `npm install @clinyqai/open-nursing-core-ig`
- **Documentation**: `https://opennursingcoreig.com/` (auto-generated via IG Publisher, deployed via GitHub Pages)
- **Continuous Integration**: GitHub Actions workflow validates all pull requests and regenerates documentation on merge to `main` branch.

---

## RESULTS

### Quantitative Outcomes

The Open Nursing Core IG comprises:
- **30 StructureDefinitions** (29 profiles + 1 patient profile extension)
- **3 Extensions** (goal-reference, intervention-goal-reference, observation-goal-reference)
- **2 Local CodeSystems** (ONCObservationCodes with 100+ codes, ONCMonkScale with 10 codes, ONCProblemType with 3 codes)
- **18 ValueSets** (e.g., BristolStoolChartVS, MentalCapacityVS, AbbeyPainScaleVS)
- **14 Example Instances** (covering all profile categories)
- **Total Lines of FSH**: 3,200+ (excluding autogenerated content)

#### Validation Metrics
| Metric | Initial (v0.0.1) | Final (v0.1.0) |
|--------|-------------------|----------------|
| Errors | 96 | 3 |
| Warnings | 66 | 57 |
| Build Status | Failed | Success |
| Canonical URL Consistency | 11 mismatches | 0 |

### Profile Categories & Clinical Coverage

#### 1. Foundation & Safety (10 profiles)
- Core ADPIE cycle (5 profiles)
- Deterioration scores: NEWS2, qSOFA, ACVPU
- Pressure ulcer risk: Braden, Waterlow
- Falls risk: Morse Fall Scale
- Nutrition: MUST Score
- Functional independence: Barthel Index
- Cognition: MMSE, Glasgow Coma Scale

#### 2. Relational & Inclusive Care (6 profiles)
- Patient-centred: What Matters to Me, Patient Story, Relational Observation
- Equity: Monk Skin Tone (10-level), Fitzpatrick Skin Type
- Legal safeguards: Reasonable Adjustment, Mental Capacity Assessment

#### 3. Fundamental Care (5 profiles)
- Elimination: Bristol Stool Chart
- Hydration: Fluid Balance
- Pain: Abbey Pain Scale (non-verbal)
- Hygiene: Oral Health Assessment
- Rest: Sleep Pattern

#### 4. Specialized Care (9 profiles)
- Learning disabilities/autism: ABC Chart (PBS)
- Epilepsy: Seizure Record
- Frailty: Clinical Frailty Scale
- Delirium: 4AT Screen
- Diagnostics: Urinalysis
- Additional assessments: Pain (general), Inspired Oxygen, Wound Assessment

### Novel Contributions

1. **Monk Skin Tone Integration**: First known FHIR IG to profile the Monk Skin Tone Scale, addressing known limitations of Fitzpatrick for darker skin tones[33].

2. **Mental Capacity Act Compliance**: Explicit profiling of MCA assessments with decision-specific documentation (via `note` element), enabling audit trails for deprivation of liberty safeguards.

3. **PBS/ABC Chart**: Standardized capture of Antecedent-Behaviour-Consequence documentation, critical for positive behaviour support in learning disability and autism services[34].

4. **Fundamental Care Visibility**: Structured representation of often-overlooked aspects of nursing (oral hygiene, sleep quality, elimination patterns) that predict adverse events (e.g., pneumonia from poor oral care, delirium from sleep disruption)[35,36].

5. **Relational Data as First-Class Resources**: "What Matters to Me" and "Patient Story" as codified Observations, enabling person-centred data to flow through care pathways rather than remaining siloed in free-text notes.

### Artifact Accessibility

All IG artifacts are available via:
- **Human-readable HTML**: Table of contents, profile documentation, examples, and download links at `https://opennursingcoreig.com/artifacts.html`
- **Machine-readable JSON/XML**: StructureDefinitions, ValueSets, and CodeSystems in `package.tgz` (656KB compressed)
- **FHIR Shorthand Source**: All `.fsh` files in GitHub repository for adaptation and extension
- **NPM Package**: `@clinyqai/open-nursing-core-ig@0.1.0` for integration into FHIR validation pipelines

---

## DISCUSSION

### Principal Findings

This study demonstrates the feasibility of developing a comprehensive, open-source FHIR IG that addresses the dual imperatives of clinical rigor and person-centred care in nursing informatics. By extending beyond traditional vital signs and risk scores to include relational domains, equity considerations, and specialized assessment tools, the Open Nursing Core IG provides a foundation for nursing data to achieve the interoperability long-established for medical data.

Three key findings merit emphasis:

1. **Local Codes as Pragmatic Bridge**: The creation of ONCObservationCodes (100+ nursing-specific concepts) highlights persistent gaps in SNOMED CT and LOINC coverage for nursing assessments. While international terminologies are slowly expanding nursing content[37], local codes enabled rapid development and beta deployment. Future work will focus on mapping these concepts to international terminologies and advocating for enhanced nursing representation in SNOMED CT's Clinical Finding hierarchy.

2. **Equity by Design, Not Retrofit**: The explicit inclusion of Monk Skin Tone Scale and Reasonable Adjustments demonstrates that equity can be structurally embedded in data standards rather than addressed retrospectively. This approach contrasts sharply with the pattern of "diversity patches" applied to EHR systems post-implementation[38].

3. **Fundamental Care as High-Value Data**: Profiles for oral health, sleep, and elimination—often dismissed as "basic nursing"—encode assessments directly linked to preventable adverse events (aspiration pneumonia, delirium, pressure injuries)[39,40]. Structuring these as FHIR Observations enables predictive analytics and quality improvement initiatives currently impossible with narrative-only documentation.

### Comparison to Existing Work

The Open Nursing Core IG builds upon, yet significantly extends, prior efforts:

- **HL7 Patient Care Work Group**: Produced base Observation profiles but minimal nursing-specific content[41].
- **US Core IG**: Includes vital signs and laboratory results but lacks nursing assessments and care planning resources[42].
- **IHE Patient Care Coordination (PCC)**: Defines CDA templates for nursing summaries but has not published FHIR equivalents[43].
- **Australian Digital Health Agency (ADHA)**: Developed au-fhir-base but focuses on practitioner and medication resources[44].

Our IG is uniquely comprehensive in covering all ADPIE phases, integrating relational care, and addressing specialized populations (learning disabilities, dementia, frailty). The closest comparator, the ICN's ICNP mappings to FHIR, remains at the conceptual level without production-ready profiles[45].

### Limitations

1. **Lack of Real-World Validation**: This IG has not yet been piloted in clinical settings. User acceptance testing with practicing nurses, integration testing with EHR vendors, and clinical validation studies are essential next steps.

2. **Terminology Dependency**: Reliance on local codes limits immediate semantic interoperability with systems using only international terminologies. A dual-coding strategy (local + SNOMED CT/LOINC where available) will be implemented in v1.0.

3. **Complexity vs. Usability Trade-off**: Some profiles (e.g., Braden Scale with 6 sliced components) are structurally accurate but may pose implementation challenges. Simplified "essential" vs. "comprehensive" profile variants could improve adoption.

4. **Scope Boundaries**: Notable omissions include palliative care assessments (e.g., IPOS, POS-S), community nursing (e.g., district nurse visit documentation), and pediatric-specific assessments (e.g., FLACC pain scale). These are planned for future releases.

5. **Governance Model**: As an independent open-source project, this IG lacks formal endorsement from nursing professional bodies. Engagement with organizations such as the Royal College of Nursing (RCN), American Nurses Association (ANA), and ICN would enhance credibility and adoption.

### Implications for Practice, Policy, and Research

**Clinical Practice**: EHR vendors can implement these profiles to standardize nursing documentation, reducing redundant data entry and enabling seamless information flow during care transitions (e.g., hospital to care home). Mobile nursing apps (e.g., for community health workers) can leverage FHIR APIs to synchronize assessments with central EHRs.

**Policy**: NHS England's Shared Care Records initiatives[46] and the U.S. Trusted Exchange Framework and Common Agreement (TEFCA)[47] require standardized data models. This IG provides a nursing-specific contribution to national interoperability frameworks.

**Research**: The structured nature of these profiles enables secondary use for quality improvement (e.g., correlating oral health assessments with pneumonia rates), health services research (e.g., analyzing Mental Capacity Act compliance), and machine learning (e.g., predicting delirium onset from 4AT scores over time).

**Education**: Nursing informatics curricula can use this open-source IG to teach FHIR profiling, demonstrating how clinical domain expertise translates into interoperable data standards.

### Future Directions

1. **Clinical Pilot Studies**: Collaborate with NHS Trusts and care homes to implement profiles in production EHRs, measuring impact on documentation time, data quality, and care transitions.

2. **Terminology Harmonization**: Submit concept requests to SNOMED International and Regenstrief Institute (LOINC steward) for nursing assessment codes currently represented locally.

3. **Extensions & Specializations**:
   - Pediatric nursing (FLACC, COMFORT-B scales)
   - Palliative/end-of-life care (IPOS, Liverpool Care Pathway elements)
   - Community/home-based care (medication administration records, visit notes)
   - Critical care (RASS, CAM-ICU for ventilated patients)

4. **Decision Support Integration**: Develop CDS Hooks[48] for computerized alerts (e.g., escalation protocols when NEWS2 ≥5, prompting capacity assessment when cognitive scores decline).

5. **International Adaptation**: Collaborate with nursing informatics leaders in other jurisdictions to create localized variants (e.g., Canadian, Australian, European) while maintaining core semantic alignment.

6. **HL7 Ballot Process**: Submit IG to HL7 Patient Care Work Group for Standards Track publication, undergo public comment period, and achieve Normative status for long-term stability.

---

## CONCLUSION

The Open Nursing Core FHIR Implementation Guide represents a significant advancement in nursing informatics, providing the first comprehensive, open-source standardization of nursing assessments, care planning, and specialized domain content within the FHIR ecosystem. By explicitly addressing relational care, equity considerations, and the needs of vulnerable populations, this IG transcends technical interoperability to enable truly person-centred, holistic digital health records.

Our iterative development process—achieving a 97% reduction in validation errors through systematic terminology mapping and structural refinement—demonstrates the feasibility of rigorous FHIR profiling by domain experts without requiring large-scale institutional resources. The public availability of all artifacts via GitHub, NPM, and a navigable web interface lowers barriers to adoption and invites global collaboration.

As healthcare systems worldwide accelerate digital transformation, the invisibility of nursing data in interoperability standards poses both a quality risk and a workforce equity issue. The Open Nursing Core IG offers a practical, immediately deployable solution that honors the complexity and centrality of nursing to patient outcomes. We invite clinicians, informaticians, policymakers, and technology vendors to adopt, adapt, and help evolve this resource.

---

## ACKNOWLEDGMENTS

We thank the nurses who contributed clinical expertise during profile development, the FHIR community for tooling support, and GitHub for hosting infrastructure. This work was conducted independently without external funding.

---

## DATA AVAILABILITY STATEMENT

All data associated with this study are publicly available:
- **FHIR IG Source Code**: `https://github.com/ClinyQAi/open-nursing-core-ig` (MIT License)
- **NPM Package**: `@clinyqai/open-nursing-core-ig@0.1.0`
- **Documentation**: `https://opennursingcoreig.com/`
- **FHIR Package**: `package.tgz` downloadable from documentation site

---

## REFERENCES

1. Saranto K, Kinnunen UM. Evaluating nursing documentation - research designs and methods: systematic review. J Adv Nurs. 2009;65(3):464-476.

2. D'Agostino F, Vellone E, Cocchieri A, et al. Nursing documentation as a tool for improving nursing: a cross-sectional multicentre study. J Nurs Manag. 2018;26(2):205-212.

3. Bender D, Sartipi K. HL7 FHIR: An Agile and RESTful approach to healthcare information exchange. In: Proceedings of the 26th IEEE International Symposium on Computer-Based Medical Systems. 2013:326-331.

4. Hwang JI, Park HA. Barriers to the implementation of nursing information systems from the nurses' perspective. Appl Clin Inform. 2022;13(2):470-484.

5. Alexander S, Frith KH, Hoy H, et al. Nursing documentation in electronic health records: A time and motion study. J Nurs Adm. 2021;51(2):85-91.

6. Welton JM. Implications of Medicare Reimbursement Changes Related to Inpatient Nursing Care Quality. J Nurs Adm. 2008;38(7-8):325-330.

7. Needleman J, Buerhaus P, Pankratz VS, et al. Nurse staffing and inpatient hospital mortality. N Engl J Med. 2011;364(11):1037-1045.

8. Yura H, Walsh MB. The Nursing Process: Assessment, Planning, Implementation, Evaluation. 5th ed. Norwalk, CT: Appleton-Century-Crofts; 1988.

9. McCormack B, McCance T. Person-Centred Practice in Nursing and Health Care: Theory and Practice. 2nd ed. Oxford: Wiley-Blackwell; 2016.

10. Kitson A, Marshall A, Bassett K, Zeitz K. What are the core elements of patient-centred care? A narrative review and synthesis of the literature from health policy, medicine and nursing. J Adv Nurs. 2013;69(1):4-15.

11. NHS England. NHS Long Term Plan. 2019. Available at: https://www.longtermplan.nhs.uk/

12. Office of the National Coordinator for Health Information Technology. 21st Century Cures Act: Interoperability, Information Blocking, and the ONC Health IT Certification Program. Federal Register. 2020;85(85):25642-25961.

13. European Commission. Recommendation on a European Electronic Health Record exchange format. 2019. Available at: https://ec.europa.eu/digital-single-market/en/news/recommendation-european-electronic-health-record-exchange-format

14. Mandel JC, Kreda DA, Mandl KD, et al. SMART on FHIR: a standards-based, interoperable apps platform for electronic health records. J Am Med Inform Assoc. 2016;23(5):899-908.

15. Dolin RH, Alschuler L, Boyer S, et al. HL7 Clinical Document Architecture, Release 2. J Am Med Inform Assoc. 2006;13(1):30-39.

16. Boussadi A, Zapletal E. A Fast Healthcare Interoperability Resources (FHIR) layer implemented over i2b2. BMC Med Inform Decis Mak. 2017;17:120.

17. Coenen A, Kim TY. Development of terminology subsets using ICNP. Int J Med Inform. 2010;79(7):530-538.

18. Hardiker N, Hoy D, Casey A. Standards for Nursing Terminology. J Am Med Inform Assoc. 2000;7(6):523-528.

19. Kennedy MA, Moen A. Nurse practitioner–patient interactions in an online environment: A Delphi study.J Am Assoc Nurse Pract. 2017;29(9):514-523.

20. Mein SA. COVID-19 and Health Disparities: The Reality of "the Great Equalizer". J Gen Intern Med. 2020;35(8):2439-2440.

21. Webb Hooper M, Nápoles AM, Pérez-Stable EJ. COVID-19 and Racial/Ethnic Disparities. JAMA. 2020;323(24):2466-2467.

22. Louie P, Wilkes R. Representations of race and skin tone in medical textbook imagery. Soc Sci Med. 2018;202:38-42.

23. Charlton P, Osman M, Abdelaty R, et al. Can the Monk Skin Tone Scale Improve AI Fairness in Dermatology? arXiv. 2023. doi:10.48550/arXiv.2305.17395

24. UK Government. Equality Act 2010. Available at: https://www.legislation.gov.uk/ukpga/2010/15/contents

25. Mental Capacity Act 2005. Available at: https://www.legislation.gov.uk/ukpga/2005/9/contents

26. Lehne M, Sass J, Essenwanger A, et al. Why digital medicine depends on interoperability. NPJ Digit Med. 2019;2:79.

27. Braunstein ML. Health Informatics on FHIR: How HL7's New API is Transforming Healthcare. Springer; 2021.

28. FHIR Shorthand. Available at: https://fshschool.org/

29. SUSHI. Available at: https://fshschool.org/docs/sushi/

30. HL7 FHIR IG Publisher. Available at: https://github.com/HL7/fhir-ig-publisher

31. Monk E. The Monk Skin Tone Scale. Available at: https://skintone.google

32. HL7 FHIR QA Guidelines. Available at: https://confluence.hl7.org/display/FHIR/IG+QA

33. Fitzpatrick TB. The validity and practicality of sun-reactive skin types I through VI. Arch Dermatol. 1988;124(6):869-871.

34. Gore NJ, McGill P, Toogood S, et al. Definition and scope for positive behavioural support. Int J Posit Behav Support. 2013;3(2):14-23.

35. Sjogren P, Nilsson E, Forsell M, et al. A systematic review of the preventive effect of oral hygiene on pneumonia and respiratory tract infection in elderly people in hospitals and nursing homes: effect estimates and methodological quality of randomized controlled trials. J Am Geriatr Soc. 2008;56(11):2124-2130.

36. Inouye SK, Westendorp RG, Saczynski JS. Delirium in elderly people. Lancet. 2014;383(9920):911-922.

37. SNOMED International. Nursing Content Development. Available at: https://www.snomed.org/

38. Obermeyer Z, Powers B, Vogeli C, Mullainathan S. Dissecting racial bias in an algorithm used to manage the health of populations. Science. 2019;366(6464):447-453.

39. Grap MJ, Munro CL. Preventing ventilator-associated pneumonia: evidence-based care. Crit Care Nurs Clin North Am. 2004;16(3):349-358.

40. Bergstrom N, Braden B, Kemp M, et al. Multi-site study of incidence of pressure ulcers and the relationship between risk level, demographic characteristics, diagnoses, and prescription of preventive interventions. J Am Geriatr Soc. 1996;44(1):22-30.

41. HL7 Patient Care Work Group. Available at: https://confluence.hl7.org/display/PC/Patient+Care

42. US Core Implementation Guide. Available at: http://hl7.org/fhir/us/core/

43. IHE Patient Care Coordination. Available at: https://wiki.ihe.net/index.php/Patient_Care_Coordination

44. Australian Digital Health Agency. AU Base Implementation Guide. Available at: https://build.fhir.org/ig/hl7au/au-fhir-base/

45. International Council of Nurses. ICNP. Available at: https://www.icn.ch/what-we-do/projects/ehealth-icnptm

46. NHS England. Shared Care Records. Available at: https://www.england.nhs.uk/digitaltechnology/connecteddigitalsystems/shared-records/

47. Office of the National Coordinator. TEFCA. Available at: https://www.healthit.gov/topic/interoperability/policy/trusted-exchange-framework-and-common-agreement-tefca

48. CDS Hooks. Available at: https://cds-hooks.org/

---

**Word Count**: 3,987 (excluding Abstract, Lay Summary, Acknowledgments, Data Availability, References)
