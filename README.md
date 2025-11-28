# Open Nursing Core FHIR Implementation Guide (ONC-IG)

**Status:** Release 1.0.0 ??
**Live Standard:** [https://clinyqai.github.io/open-nursing-core-ig/](https://clinyqai.github.io/open-nursing-core-ig/)

## ?? The Mission
The Open Nursing Core (ONC) is a nurse-led, open-source initiative to codify the nursing process (**ADPIE**) into rigorous digital standards (FHIR).

We are building the digital infrastructure to ensure nursing care is:
*   **Visible:** Captured in standardized data, not free text.
*   **Interoperable:** Readable by any EMR or AI system.
*   **Equitable:** Includes Skin Tone and Social Determinants by default.

## ?? What is in this IG?
This repository contains the source code (FHIR Shorthand) for the following profiles:
*   **Assessments:** Braden Scale, NEWS2, Skin Tone, Housing Status.
*   **Clinical Logic:** Nursing Problems, Goals, Interventions, and Care Plans.
*   **Equity:** UK Core Ethnicity and Fitzpatrick Skin Tone integration.

## ??? How to Build Locally
Prerequisites: [Node.js](https://nodejs.org/), [Java 17+](https://adoptium.net/), and [Jekyll](https://jekyllrb.com/).

1.  **Install SUSHI:**
    \
pm install -g fsh-sushi\
2.  **Download Publisher:**
    Download the latest [publisher.jar](https://github.com/HL7/fhir-ig-publisher/releases)
3.  **Run the Build:**
    \java -jar publisher.jar -ig .\

## ?? License
This project is licensed under the MIT License.
