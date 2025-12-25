# Open Nursing Core FHIR Implementation Guide (ONC-IG)

[![Build Status](https://github.com/ClinyQAi/open-nursing-core-ig/actions/workflows/build-publish.yml/badge.svg)](https://github.com/ClinyQAi/open-nursing-core-ig/actions)
[![FHIR R4](https://img.shields.io/badge/FHIR-R4-blue.svg)](https://hl7.org/fhir/R4/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![IG Version](https://img.shields.io/badge/IG-v1.0.0-orange.svg)](https://clinyqai.github.io/open-nursing-core-ig/)

---

## 📘 Published Implementation Guide

**🌐 Live IG:** [https://clinyqai.github.io/open-nursing-core-ig/](https://clinyqai.github.io/open-nursing-core-ig/)

| Resource | Link |
|----------|------|
| **Home** | [Implementation Guide](https://clinyqai.github.io/open-nursing-core-ig/index.html) |
| **Artifacts** | [All Profiles & Extensions](https://clinyqai.github.io/open-nursing-core-ig/artifacts.html) |
| **Table of Contents** | [ToC](https://clinyqai.github.io/open-nursing-core-ig/toc.html) |
| **QA Report** | [Validation Results](https://clinyqai.github.io/open-nursing-core-ig/qa.html) |

---

## 🎯 The Mission

The **Open Nursing Core (ONC)** is a nurse-led, open-source initiative to codify the nursing process (**ADPIE** - Assessment, Diagnosis, Planning, Implementation, Evaluation) into rigorous digital standards using HL7 FHIR.

### Key Features

- ✅ **Safety Module** - Braden Scale for pressure ulcer risk assessment
- ✅ **Equity Module** - Fitzpatrick and Monk skin tone scales for equitable assessment
- ✅ **Care Planning** - Nursing problems, goals, interventions, and evaluations
- ✅ **UK Core Compatible** - NHS ethnic category extension support

---

## 📊 FHIR Profiles

| Profile | Description |
|---------|-------------|
| `ONCNursingAssessment` | Base profile for all nursing observations |
| `ONCBradenScaleAssessment` | Pressure ulcer risk assessment (Braden Scale) |
| `ONCNursingProblem` | Nursing diagnosis documentation |
| `ONCPatientGoal` | Patient-centered goal setting |
| `ONCNursingIntervention` | Care activity documentation |
| `ONCGoalEvaluation` | Outcome assessment |
| `ONCSkinToneObservation` | Fitzpatrick skin type for equitable assessment |
| `ONCNHSPatient` | NHS patient with ethnic category extension |

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

### Run the Validation App

```bash
# Set up environment
cp .env.example .env
# Edit .env with your credentials

# Run with Docker (Recommended)
docker-compose up --build

# Or run locally
pip install -r requirements.txt
streamlit run app_phase2.py
```

---

## 📂 Project Structure

```
open-nursing-core-ig/
├── input/
│   ├── fsh/                    # FHIR Shorthand source files
│   │   ├── onc-profiles.fsh    # Core profiles
│   │   ├── onc-equity.fsh      # Equity module
│   │   └── onc-terminology.fsh # ValueSets & CodeSystems
│   ├── pagecontent/            # IG content pages
│   └── includes/               # Menu and includes
├── core/                       # Validation app core logic
├── db/                         # Database models
├── ml/                         # Machine Learning modules
├── sushi-config.yaml           # SUSHI configuration
└── README.md
```

---

## 🎓 Acknowledgements

This implementation is built upon the scholarship and research of nursing innovators:

- **Professor Joanne Bosanquet** (Chief Executive, Foundation of Nursing Studies) - For championing open access to nursing knowledge via the International Practice Development Journal (IPDJ)
- **Dr Clare Cable** (Chief Executive, Burdett Trust for Nursing) - For pioneering work on Relational Intelligence in nursing
- **Kumbi Kariwo** (Nurse Citizen Developer) - For leading the technical integration of Skin Tone Inclusivity and equity measures
- **Robylin 'Tweetie' Diya** - For foundational work on MCINDS (Minimum Core International Nursing Data Set)

---

## ⚖️ License

The code in this repository is licensed under the **MIT License** - you can use it freely.

> **Note:** The FoNS Knowledge Graph (`chroma_db_fons`) is built upon academic work from the *International Practice Development Journal*, licensed under **CC BY-NC 3.0**. Commercial use requires agreement with the Foundation of Nursing Studies.

---

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## 📬 Contact

- **Issues**: [GitHub Issues](https://github.com/ClinyQAi/open-nursing-core-ig/issues)
- **Organization**: [ClinyQAi](https://github.com/ClinyQAi)
