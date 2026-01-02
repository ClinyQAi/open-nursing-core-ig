# Open Nursing Core FHIR Implementation Guide (ONC-IG)

[![Build Status](https://github.com/ClinyQAi/open-nursing-core-ig/actions/workflows/build-publish.yml/badge.svg)](https://github.com/ClinyQAi/open-nursing-core-ig/actions)
[![FHIR R4](https://img.shields.io/badge/FHIR-R4-blue.svg)](https://hl7.org/fhir/R4/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![IG Version](https://img.shields.io/badge/IG-v1.0.0-orange.svg)](https://clinyqai.github.io/open-nursing-core-ig/)
[![AI Powered](https://img.shields.io/badge/AI-Relational%20Core-purple)](https://huggingface.co/NurseCitizenDeveloper/nursing-llama-3-8b-fons)
[![NHS England Aligned](https://img.shields.io/badge/NHS%20England-Aligned-success.svg)](https://www.england.nhs.uk/long-read/towards-a-unified-vision-of-nursing-and-midwifery-documentation/)

---

## 📘 Published Implementation Guide

**🌐 Live IG:** [https://opennursingcoreig.com/](https://opennursingcoreig.com/)

| Resource | Link |
|----------|------|
| **Home** | [Implementation Guide](https://opennursingcoreig.com/index.html) |
| **Artifacts** | [All Profiles & Extensions](https://opennursingcoreig.com/artifacts.html) |
| **Table of Contents** | [ToC](https://opennursingcoreig.com/toc.html) |
| **QA Report** | [Validation Results](https://opennursingcoreig.com/qa.html) |

---

## 🎯 The Mission

The **Open Nursing Core (ONC)** is a nurse-led, open-source initiative to codify the nursing process (**ADPIE** - Assessment, Diagnosis, Planning, Implementation, Evaluation) into rigorous digital standards using HL7 FHIR.

**This independent project aligns with [NHS England's Unified Vision of Nursing Documentation](https://www.england.nhs.uk/long-read/towards-a-unified-vision-of-nursing-and-midwifery-documentation/), providing a practical FHIR-based implementation of their strategic goals.**

> **Note**: This is an independent open-source project and is not officially endorsed by or affiliated with NHS England. It is developed by the nursing informatics community to support the vision outlined in NHS England's guidance.

### 🏥 Alignment with NHS England Vision

This Implementation Guide supports the goals outlined in NHS England's unified vision by:

- ✅ **Standardising nursing documentation** across health and social care
- ✅ **Reducing unwarranted variation** through validated FHIR profiles
- ✅ **Supporting professional judgement** with flexible, evidence-based tools
- ✅ **Enabling digital transformation** with API-ready, interoperable standards
- ✅ **Implementing core assessment tools** recommended by NHS England:
  - NEWS2 (National Early Warning Score)
  - MUST (Malnutrition Universal Screening Tool)
  - Falls Risk Assessment (Morse Fall Scale)
  - Skin Assessment (Waterlow, Wound Assessment)

### Key Features

- ✅ **27 Production-Ready Profiles** covering all major nursing assessments
- ✅ **Full NHS CareConnect Alignment** for NEWS2 with 7 supporting vital signs
- ✅ **Nursing Process Framework** (ADPIE) - Assessment, Diagnosis, Planning, Implementation, Evaluation
- ✅ **Evidence-Based Tools** using standard LOINC and SNOMED codes
- ✅ **Equity Module** - Fitzpatrick and Monk skin tone scales
- ✅ **Safety Module** - Risk assessments (Braden, Waterlow, Morse Fall Scale)
- ✅ **Relational Ai for Nursing** - Fine-tuned LLM for person-centred documentation (Score: 8/10 Equity)
- ✅ **Paired Validator** - NHS Unified Nursing Validator for enforcement

---

## 🤖 Relational Ai for Nursing

**The first open-source LLM fine-tuned on Foundation of Nursing Studies (FONS) literature for person-centred, equitable clinical documentation.**

> **🚀 Live Model**: [Hugging Face: NurseCitizenDeveloper/nursing-llama-3-8b-fons](https://huggingface.co/NurseCitizenDeveloper/nursing-llama-3-8b-fons)

### Why It Matters
Standard AI models often produce generic, task-oriented medical text. **Relational Ai** is different—it's trained on 6,698 examples of high-quality nursing literature to prioritize:

*   **Person-Centredness**: Focusing on what matters to the patient.
*   **Health Equity**: Specifically fine-tuned to document skin tone risks (e.g., pressure ulcers) accurately for all ethnicities.
*   **Relational Care**: Using language that fosters therapeutic relationships.

### Evaluation Highlights
*   **Equity**: **8.0/10** (Skin Tone Sensitivity)
*   **Person-Centredness**: **7.6/10**
*   **Accuracy**: **6.6/10**

---

## 📊 Clinical Assessment Profiles

### Core Risk Assessments (NHS England Recommended)

| Profile | Code | Range | Description |
|---------|------|-------|-------------|
| **NEWS2 Score** | SNOMED 1104051000000101 | 0-20 | National Early Warning Score (full NHS alignment) |
| **MUST Score** | SNOMED 870431003 | 0-6 | Malnutrition Universal Screening Tool |
| **Morse Fall Scale** | LOINC 73830-2 | 0-125 | Falls risk assessment |
| **Waterlow Score** | SNOMED 443846001 | 0-64+ | Pressure ulcer risk |
| **Wound Assessment** | SNOMED 399912005 | - | Pressure ulcer staging & dimensions |

### Neurological & Cognitive Assessments

| Profile | Code | Range | Description |
|---------|------|-------|-------------|
| **Glasgow Coma Scale** | LOINC 9269-2 | 3-15 | Consciousness level (Eye, Verbal, Motor) |
| **MMSE** | LOINC 72106-8 | 0-30 | Mini Mental State Examination |

### Pain & Symptom Management

| Profile | Code | Range | Description |
|---------|------|-------|-------------|
| **Pain Assessment** | LOINC 72514-3 | 0-10 | Numeric Rating Scale (NRS) |

### Critical Care & Sepsis

| Profile | Code | Range | Description |
|---------|------|-------|-------------|
| **qSOFA** | LOINC 96790-1 | 0-3 | Quick Sequential Organ Failure Assessment |

### Functional Assessment

| Profile | Code | Range | Description |
|---------|------|-------|-------------|
| **Barthel Index** | LOINC 83254-5 | 0-100 | Activities of Daily Living (ADL) |

### NEWS2 Supporting Vital Signs (7 Profiles)

| Profile | Code | Description |
|---------|------|-------------|
| **Respiration Rate** | LOINC 9279-1 | Breaths per minute |
| **Oxygen Saturation** | LOINC 59408-5 | SpO2 percentage |
| **Body Temperature** | LOINC 8310-5 | Core temperature |
| **Blood Pressure** | LOINC 85354-9 | Systolic/Diastolic |
| **Heart Rate** | LOINC 8867-4 | Pulse rate |
| **ACVPU** | SNOMED 1104441000000107 | Consciousness level |
| **Inspired Oxygen** | LOINC 3151-8 | Supplemental oxygen |

### Nursing Process Profiles

| Profile | Description |
|---------|-------------|
| **ONCNursingAssessment** | Base profile for all nursing observations |
| **ONCBradenScaleAssessment** | Pressure ulcer risk (Braden Scale) |
| **ONCNursingProblem** | Nursing diagnosis documentation |
| **ONCPatientGoal** | Patient-centered goal setting |
| **ONCNursingIntervention** | Care activity documentation |
| **ONCGoalEvaluation** | Outcome assessment |

### Equity & Inclusivity

| Profile | Description |
|---------|-------------|
| **ONCSkinToneObservation** | Fitzpatrick & Monk skin tone scales |
| **ONCNHSPatient** | NHS patient with ethnic category extension |

---

## 🚀 Getting Started

### Prerequisites
- [Node.js](https://nodejs.org/) (for SUSHI)
- [SUSHI](https://fshschool.org/docs/sushi/) (`npm install -g fsh-sushi`)
- [IG Publisher](https://github.com/HL7/fhir-ig-publisher) (optional, for full IG build)

### Build the IG Locally

```bash
# Clone the repository
git clone https://github.com/ClinyQAi/open-nursing-core-ig.git
cd open-nursing-core-ig

# Run SUSHI to compile FSH to FHIR
sushi .

# (Optional) Run full IG Publisher build
./_genonce.sh   # Mac/Linux
_genonce.bat    # Windows
```

---

## 📂 Project Structure

```
open-nursing-core-ig/
├── input/
│   ├── fsh/                         # FHIR Shorthand source files
│   │   ├── onc-profiles.fsh         # Core nursing process profiles
│   │   ├── onc-news2-full.fsh       # NEWS2 (full NHS alignment)
│   │   ├── onc-clinical-assessments.fsh  # Pain, Wound
│   │   ├── onc-glasgow-coma-scale.fsh    # GCS
│   │   ├── onc-waterlow-score.fsh   # Pressure ulcer risk
│   │   ├── onc-must-score.fsh       # Malnutrition screening
│   │   ├── onc-additional-assessments.fsh # Morse, qSOFA, Barthel
│   │   ├── onc-mmse.fsh             # Cognitive assessment
│   │   ├── onc-equity.fsh           # Equity module
│   │   └── onc-terminology.fsh      # ValueSets & CodeSystems
│   ├── pagecontent/                 # IG content pages
│   └── includes/                    # Menu and includes
├── .spec-kit/                       # Spec-driven development
│   └── specs/                       # Clinical specifications
├── sushi-config.yaml                # SUSHI configuration
└── README.md
```

---

## 🌟 What Makes This IG Unique

1. **Most Comprehensive Nursing IG**: 27 profiles covering all major nursing assessments
2. **NHS-Aligned**: Full CareConnect compatibility, implements NHS England's unified vision
3. **Production-Ready**: All profiles use standard LOINC/SNOMED codes with validation
4. **Paired Validator**: NHS Unified Nursing Validator enforces profile compliance
5. **Community-Driven**: Open framework for clinical contributions
6. **Spec-Driven Development**: Transparent development process with clinical specifications

---

## 🤝 Contributing

We welcome contributions from nurses, informaticians, and developers! 

### How to Contribute Clinical Profiles

1. **Request a Profile**: Open an [issue using our template](https://github.com/ClinyQAi/open-nursing-core-ig/issues/new?template=clinical_profile_request.yml)
2. **Review the Guide**: See [ADDING_PROFILES_GUIDE.md](ADDING_PROFILES_GUIDE.md)
3. **Submit a PR**: Follow our [CONTRIBUTORS.md](CONTRIBUTORS.md) guidelines

### Priority Areas for Contribution

- **Pediatric Assessments**: PEWS, APGAR, FLACC
- **Mental Health**: PHQ-9, GAD-7, C-SSRS
- **Maternal/Neonatal**: MEOWS, Bishop Score
- **Community Care**: Frailty Index, Edmonton Frail Scale

---

## 🎓 Acknowledgements

This implementation is built upon the scholarship and research of nursing innovators:

- **Professor Joanne Bosanquet** (Chief Executive, Foundation of Nursing Studies) - For championing open access to nursing knowledge via the International Practice Development Journal (IPDJ)
- **Dr Clare Cable** (Chief Executive, Burdett Trust for Nursing) - For pioneering work on Relational Intelligence in nursing
- **Kumbi Kariwo** (Nurse Citizen Developer) - For leading the technical integration of Skin Tone Inclusivity and equity measures
- **Robylin 'Tweetie' Diya** - For foundational work on MCINDS (Minimum Core International Nursing Data Set)

**Inspiration & Alignment:**
- **NHS England** - For publishing the unified vision of nursing documentation that inspired this technical implementation

---

## 📚 Related Resources

- [NHS England Unified Vision](https://www.england.nhs.uk/long-read/towards-a-unified-vision-of-nursing-and-midwifery-documentation/)
- [NHS Unified Nursing Validator](https://github.com/ClinyQAi/nhs-unified-nursing-validator)
- [HL7 FHIR R4 Specification](https://hl7.org/fhir/R4/)
- [FHIR Shorthand (FSH)](https://fshschool.org/)

---

## ⚖️ License

This project is licensed under the **MIT License**.

> This work is inspired by research from the Foundation of Nursing Studies (FoNS), 
> the International Practice Development Journal, and NHS England's unified vision 
> of nursing documentation.

---

## 📬 Contact

- **Issues**: [GitHub Issues](https://github.com/ClinyQAi/open-nursing-core-ig/issues)
- **Organization**: [ClinyQAi](https://github.com/ClinyQAi)
- **Live IG**: [https://opennursingcoreig.com/](https://opennursingcoreig.com/)

---

**Built by nurses, for nurses. Open source, open standards, open future.** 🩺✨
