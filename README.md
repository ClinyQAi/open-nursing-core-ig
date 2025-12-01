# Open Nursing Core FHIR Implementation Guide (ONC-IG)

**Status:** Release 1.0.0 🚀
**Live Standard:** [https://clinyqai.github.io/open-nursing-core-ig/toc.html](https://clinyqai.github.io/open-nursing-core-ig/toc.html)

## The Mission
The Open Nursing Core (ONC) is a nurse-led, open-source initiative to codify the nursing process (**ADPIE**) into rigorous digital standards (FHIR).

## 📂 Project Structure

This repository is organized into modular components for scalability and maintainability:

*   **`core/`**: Core logic including configuration, authentication, validator, and logging.
*   **`db/`**: Database models, migrations, and connection handling.
*   **`ml/`**: Machine Learning modules (predictive, anomaly detection) and analytics dashboards.
*   **`visualizations/`**: Visualization components for Streamlit.
*   **`scripts/`**: Utility scripts for data ingestion and knowledge base construction.
*   **`app.py`**: Legacy application entry point (Phase 1).
*   **`app_phase2.py`**: Modern application entry point (Phase 2) with database integration.

## 🚀 Getting Started

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/clinyqai/open-nursing-core-ig.git
    cd open-nursing-core-ig
    ```

2.  **Set up environment:**
    Copy the example environment file and configure your credentials.
    ```bash
    cp .env.example .env
    ```
    **Important:** Update `.env` with your actual Azure OpenAI credentials and secure passwords. Never commit `.env` to version control.

3.  **Run with Docker (Recommended):**
    ```bash
    docker-compose up --build
    ```

4.  **Run Locally:**
    Install dependencies and run the Streamlit app.
    ```bash
    pip install -r requirements.txt
    streamlit run app_phase2.py
    ```

## Acknowledgements & Leadership
This technical implementation is built upon the scholarship, leadership, and research of the following nursing innovators:

*   **Professor Joanne Bosanquet (Chief Executive, Foundation of Nursing Studies):** For championing open access to nursing knowledge via the **International Practice Development Journal (IPDJ)**.
*   **Dr Clare Cable (Chief Executive, Burdett Trust for Nursing):** For pioneering work on **Relational Intelligence** in nursing.
*   **Kumbi Kariwo (Nurse Citizen Developer):** For leading the technical integration of **Skin Tone Inclusivity** and equity measures.

## 🎓 Acknowledgements and Relationship to MCINDS
This project aims to create a public, open-source set of FHIR profiles and technical assets for nursing documentation. The clinical concepts and data models contained herein are inspired by and seek to align with the foundational principles of the **Minimum Core International Nursing Data Set (MCINDS)**, the academic and research work for which is led by **Robylin 'Tweetie' Diya**.

##  Scope
This repository contains the source code (FHIR Shorthand) for:
*   **Assessments:** Braden Scale, NEWS2, Skin Tone, Housing Status.
*   **Clinical Logic:** Nursing Problems, Goals, Interventions, and Care Plans.
*   **Equity:** UK Core Ethnicity and Fitzpatrick Skin Tone integration.


## ⚖️ Licensing & Commercial Use

The code in this repository is licensed under MIT (you can use it freely).

However, the **FoNS Knowledge Graph** (`chroma_db_fons`) is built upon academic work from the *International Practice Development Journal*, which is licensed under **CC BY-NC 3.0**.

**You may not use the FoNS-derived database for commercial purposes without a direct agreement with the Foundation of Nursing Studies.**
