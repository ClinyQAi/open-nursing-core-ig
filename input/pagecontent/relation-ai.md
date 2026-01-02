# Relational Ai for Nursing

**The first open-source LLM fine-tuned on Foundation of Nursing Studies (FONS) literature for person-centred, equitable clinical documentation.**

<div style="background-color: #f0f7ff; border-left: 5px solid #005eb8; padding: 15px; margin-bottom: 20px;">
<strong>🚀 Model Live on Hugging Face:</strong> <a href="https://huggingface.co/NurseCitizenDeveloper/nursing-llama-3-8b-fons" target="_blank">NurseCitizenDeveloper/nursing-llama-3-8b-fons</a>
</div>

## Overview
**Relational Ai for Nursing** is a specialized AI model developed as part of the Open Nursing Core IG. It is designed to assist nurses in writing high-quality, person-centred clinical notes that adhere to professional standards while reducing administrative burden.

Instead of generic medical text, this model is trained to prioritize:
*   **Relational Care:** Focusing on the patient's experience and preferences.
*   **Health Equity:** Specifically trained to ensure inclusive documentation (e.g., correct skin tone assessment).
*   **FONS Principles:** Aligned with the Foundation of Nursing Studies' core values.

## Key Capabilities

### 1. Equitable Skin Tone Assessment
Standard AI models often fail to describe pressure ulcer risks accurately for patients with darker skin tones. **Relation Ai** has been fine-tuned to capture these nuances, achieving an **8/10 score** from expert judges on equity benchmarks.

### 2. Person-Centred Language
The model rewrites clinical jargon into language that respects the patient's dignity.
*   *Before:* "Patient non-compliant with medication."
*   *Relation Ai:* "Patient prefers to take medication with food to avoid nausea; discussed strategies to support adherence."

### 3. FONS Alignment
Trained on **6,698 instruction pairs** from the International Practice Development Journal (IPDJ), the model understands concepts like "flourishing," "authentic partnership," and "values-based practice."

## Evaluation Results
The model was evaluated using a rigorous multi-judge system (GPT-4o, GPT-5, Gemini 3 Pro).

| Metric | Score | Note |
|---|---|---|
| **Clinical Accuracy** | **6.6/10** | Solid baseline for nursing interventions |
| **Person-Centredness** | **7.6/10** | Strong performance in respectful language |
| **Equity (Skin Tone)** | **8.0/10** | **Best-in-class performance** |

## Integration with FHIR
This AI model is designed to work alongside the FHIR profiles defined in this IG.
*   **Input:** Structured data from `Patient`, `Observation` (e.g., Skin Tone), and `Condition` resources.
*   **Output:** Narrative text for `Composition` or `ClinicalImpression` resources.

## Semantic Intelligence (openEHR Inspired)
The Open Nursing Core project leverages **FHIR Logical Models** to define the "Clinical Truth" of nursing concepts—a methodology inspired by openEHR archetypes.

### Clinical Mapping
The **Relational AI** performs real-time semantic audits, mapping clinical findings to international standards:
*   **NANDA-I:** Maps narrative findings to official Nursing Diagnoses.
*   **Logical Model Mapping:** Validates that the "Relational" aspect of care (e.g., patient story) is present in the documentation.

## Usage & License
*   **License:** CC BY-NC 3.0 (Non-Commercial)
*   **Base Model:** Llama-3-8B (Unsloth)
*   **Disclaimer:** This tool is for research and educational purposes. All clinical documentation must be verified by a registered nurse.
