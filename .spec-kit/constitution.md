# Open Nursing Core IG - Constitution

## Status
- [x] Specify
- [x] Plan
- [x] Tasks
- [ ] Implement

## Project Vision
The Open Nursing Core Implementation Guide (ONC-IG) establishes the **gold standard** for digitising nursing practice into HL7 FHIR, with an unwavering commitment to **clinical equity** and **computational rigour**.

---

## Core Principles

### 1. Equity First
> "This is the only FHIR standard in the world that prevents you from training racist AI models."

- **Mandatory Skin Tone Context**: No wound assessment without linked skin tone observation
- **Inclusive Terminology**: Codes and displays reflect diverse patient populations
- **Anti-Bias by Design**: Data structures that prevent AI training on inequitable data

### 2. Nursing Process Integrity (ADPIE)
- **Assessment**: Structured, validated observations with mandatory coding
- **Diagnosis**: Explicit Nursing Problem profile, distinct from medical diagnosis
- **Planning**: CarePlan as the "spine" linking conditions, goals, and interventions
- **Implementation**: Task-driven workflow with status tracking
- **Evaluation**: Closed-loop Goal Evaluation with outcome measurement

### 3. Computational Rigour
- **No Free Text**: All diagnoses and interventions must use coded values
- **CQL Integration**: Embedded clinical logic for auto-calculation (NEWS2, Waterlow, Braden)
- **Invariants**: Hard-coded validation rules that reject non-compliant data
- **Terminology Binding**: Strict ValueSets with SNOMED CT and LOINC

### 4. NHS Alignment
- **UK Core Compatibility**: Profiles extend NHS Digital UK Core base profiles
- **PRSB Conformance**: Logical models map to PRSB Nursing Care Needs Standard
- **RCP Standards**: NEWS2 implementation matches Royal College of Physicians specification

### 5. Open Development
- **MIT License**: Free to use, modify, and redistribute
- **Community Governance**: Contributions welcome via GitHub
- **Transparent Versioning**: Semantic versioning with clear change logs

---

## Technical Governance

### Code Quality Standards
- All FSH files must compile with 0 warnings
- All profiles must have complete examples
- All ValueSets must use established terminologies (SNOMED CT, LOINC, dm+d)

### Testing Requirements
- Validator must accept all examples
- 3+ independent implementations required for FMM 2
- Clinical review by nursing professionals before release

### Documentation Requirements
- Every profile must have clinical context documentation
- Every invariant must have rationale and error messages
- ADPIE mapping must be explicit

---

## Success Metrics

| Metric | Target |
|--------|--------|
| FHIR Maturity (FMM) | Level 3+ |
| Profile Coverage | 100% ADPIE stages |
| Terminology Binding | 100% coded values |
| Equity Profiles | Skin tone, communication, cultural context |
| Independent Implementations | 3+ NHS Trusts |
