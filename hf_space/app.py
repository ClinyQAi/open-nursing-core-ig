"""
Relational AI 4 Nursing - Hugging Face Spaces Demo
Fine-tuned Llama-3-8B for person-centred nursing documentation.
"""
import gradio as gr
import torch
import os
from transformers import AutoModelForCausalLM, AutoTokenizer, TextIteratorStreamer
from threading import Thread
from huggingface_hub import login

# Login to Hugging Face (Requires HF_TOKEN secret in Space settings)
if os.getenv("HF_TOKEN"):
    login(token=os.getenv("HF_TOKEN"))

# ============================================
# MODEL CONFIGURATION
# ============================================
MODEL_ID = "NurseCitizenDeveloper/nursing-llama-3-8b-fons"

# Alpaca prompt format (used during training)
ALPACA_TEMPLATE = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
{instruction}

### Input:
{context}

### Response:
"""

# ============================================
# LOAD MODEL (PEFT / Adapter Compatible)
# ============================================
BASE_MODEL = "NousResearch/Meta-Llama-3-8B" # Non-gated alternative to original Meta repo
print(f"🔄 Loading base model: {BASE_MODEL}")

# tokenizer should be loaded from the adapter repo if it has custom tokens
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)

# Load base model (Requires HF_TOKEN secret in Space settings)
model = AutoModelForCausalLM.from_pretrained(
    BASE_MODEL,
    torch_dtype=torch.float16,
    device_map="auto",
    trust_remote_code=True,
)

# Load Adapters
from peft import PeftModel
print(f"🧩 Applying nursing adapters from: {MODEL_ID}")
model = PeftModel.from_pretrained(model, MODEL_ID)

print("✅ Super-Gold Model loaded and ready!")

# ============================================
# GENERATION FUNCTION
# ============================================
def generate_response(instruction: str, context: str, max_tokens: int = 256, temperature: float = 0.7):
    """Generate a response using the fine-tuned model."""
    prompt = ALPACA_TEMPLATE.format(instruction=instruction, context=context)
    
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    
    # Streaming setup
    streamer = TextIteratorStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)
    
    generation_kwargs = dict(
        **inputs,
        max_new_tokens=max_tokens,
        do_sample=True,
        temperature=temperature,
        top_p=0.9,
        streamer=streamer,
    )
    
    # Run generation in a thread for streaming
    thread = Thread(target=model.generate, kwargs=generation_kwargs)
    thread.start()
    
    # Yield tokens as they arrive
    partial_response = ""
    for new_text in streamer:
        partial_response += new_text
        yield partial_response


def chat_interface(message: str, history: list):
    """Chat interface handler."""
    # Use the message as both instruction and context for simple chat
    for response in generate_response(message, "General nursing documentation context."):
        yield response


def rewrite_clinical_note(original_note: str):
    """Rewrite a clinical note using person-centred language."""
    instruction = "Rewrite this clinical note using person-centred, dignified language that respects the patient. Focus on their experience and preferences."
    for response in generate_response(instruction, original_note, max_tokens=300):
        yield response


def skin_tone_assessment(patient_info: str):
    """Generate skin tone-aware pressure ulcer assessment."""
    instruction = "Generate a comprehensive skin assessment for pressure ulcer risk. Include specific guidance for documenting skin tone changes, ensuring the assessment is appropriate for all skin tones including darker complexions."
    for response in generate_response(instruction, patient_info, max_tokens=400):
        yield response


def adpie_generator(clinical_scenario: str):
    """Generate structured ADPIE nursing documentation."""
    instruction = "Structure this clinical scenario using the ADPIE nursing process: Assessment, Diagnosis, Planning, Implementation, and Evaluation. Provide clear, actionable documentation for each step."
    for response in generate_response(instruction, clinical_scenario, max_tokens=500):
        yield response


def semantic_review(note: str):
    """Perform openEHR-inspired semantic analysis on a nursing note."""
    instruction = """Perform a SUPER-GOLD SEMANTIC AUDIT on this nursing note.
    Your goal is to exceed openEHR standards by validating:
    1. ONC Empathy Index (1-5): Score the therapeutic depth of the interaction.
    2. Relief Engagement (1-5): Score the authentic partnership level.
    3. Mandatory Equity Gate: Verify if skin tone or cultural background is documented to guide clinical assessment.
    4. NANDA-I Mapping: Suggest formal Nursing Diagnoses.
    5. ADPIE Integrity: Ensure Assessment leads logically to Implementation.
    
    If any 'Relational' or 'Equity' markers are missing, provide a 'Relational Intervention' to fix it."""
    for response in generate_response(instruction, note, max_tokens=500):
        yield response


# ============================================
# GRADIO UI
# ============================================
# Custom CSS for NHS-inspired theme
custom_css = """
.gradio-container {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
}
.gr-button-primary {
    background-color: #005eb8 !important;
    border-color: #005eb8 !important;
}
.gr-button-primary:hover {
    background-color: #003d7a !important;
}
footer {
    visibility: hidden;
}
"""

# Header HTML
header_html = """
<div style="text-align: center; padding: 20px; background: linear-gradient(135deg, #005eb8 0%, #003d7a 100%); border-radius: 10px; margin-bottom: 20px;">
    <h1 style="color: white; margin: 0; font-size: 2.5em;">🤖 Relational AI 4 Nursing</h1>
    <p style="color: #e8edee; margin-top: 10px; font-size: 1.1em;">
        The first open-source LLM fine-tuned on FONS literature for person-centred, equitable clinical documentation.
    </p>
    <div style="margin-top: 15px;">
        <span style="background: #4c9aff; color: white; padding: 5px 15px; border-radius: 20px; margin: 0 5px; font-size: 0.9em;">🎯 Equity Score: 8/10</span>
        <span style="background: #7c3aed; color: white; padding: 5px 15px; border-radius: 20px; margin: 0 5px; font-size: 0.9em;">💬 Person-Centred: 7.6/10</span>
        <span style="background: #059669; color: white; padding: 5px 15px; border-radius: 20px; margin: 0 5px; font-size: 0.9em;">✅ FONS Aligned</span>
    </div>
</div>
"""

with gr.Blocks(css=custom_css, title="Relational AI 4 Nursing") as demo:
    gr.HTML(header_html)
    
    with gr.Tabs():
        # Tab 1: Chat Interface
        with gr.TabItem("💬 Chat Assistant"):
            gr.Markdown("### Ask questions about nursing practice, care planning, or clinical documentation.")
            chatbot = gr.ChatInterface(
                fn=chat_interface,
                examples=[
                    "What are the key principles of person-centred care?",
                    "How should I document a patient's refusal of medication?",
                    "Explain the importance of relational care in nursing.",
                    "What is the FONS approach to practice development?",
                ],
                retry_btn=None,
                undo_btn=None,
            )
        
        # Tab 2: Language Rewriter
        with gr.TabItem("✨ Language Rewriter"):
            gr.Markdown("""
            ### Transform Clinical Jargon into Person-Centred Language
            Paste a clinical note written in traditional medical language, and Relational AI will rewrite it 
            using dignified, person-centred language that respects the patient's experience.
            """)
            
            with gr.Row():
                with gr.Column():
                    original_input = gr.Textbox(
                        label="Original Clinical Note",
                        placeholder="e.g., 'Patient non-compliant with medication. Refused to ambulate. Agitated and uncooperative.'",
                        lines=5,
                    )
                    rewrite_btn = gr.Button("✨ Rewrite with Relational AI", variant="primary")
                
                with gr.Column():
                    rewritten_output = gr.Textbox(
                        label="Person-Centred Version",
                        lines=8,
                        interactive=False,
                    )
            
            rewrite_btn.click(
                fn=rewrite_clinical_note,
                inputs=original_input,
                outputs=rewritten_output,
            )
            
            gr.Examples(
                examples=[
                    ["Patient is non-compliant with medication regimen. Refused physiotherapy session. Combative when staff attempted to assist with personal care."],
                    ["Elderly female, confused and agitated. Fall risk. Requires 1:1 supervision. Not eating."],
                    ["Patient is a poor historian. Unable to provide reliable information about symptoms."],
                ],
                inputs=original_input,
            )
        
        # Tab 3: Skin Tone Assessment
        with gr.TabItem("🎨 Equity: Skin Assessment"):
            gr.Markdown("""
            ### Equitable Skin Tone Assessment
            Standard pressure ulcer tools (like the Braden Scale) often fail to capture risks for patients with darker skin tones.
            This tool generates assessments that account for **all skin tones**, ensuring equitable care.
            
            > **Why this matters:** Early signs of pressure damage (erythema) appear differently on darker skin. 
            > Relational AI was specifically trained to address this gap.
            """)
            
            patient_info_input = gr.Textbox(
                label="Patient Information",
                placeholder="e.g., 'Mrs. Johnson, 78 years old, limited mobility, dark brown skin tone (Fitzpatrick V), admitted for hip fracture.'",
                lines=3,
            )
            skin_btn = gr.Button("🔍 Generate Equitable Assessment", variant="primary")
            skin_output = gr.Textbox(label="Skin Assessment", lines=10, interactive=False)
            
            skin_btn.click(
                fn=skin_tone_assessment,
                inputs=patient_info_input,
                outputs=skin_output,
            )
            
            gr.Examples(
                examples=[
                    ["78-year-old woman with dark skin (Fitzpatrick Type V), admitted for stroke rehabilitation, limited mobility, incontinent."],
                    ["65-year-old man, South Asian heritage, diabetic, peripheral neuropathy, using wheelchair."],
                ],
                inputs=patient_info_input,
            )
        
        # Tab 4: ADPIE Generator
        with gr.TabItem("📋 ADPIE Generator"):
            gr.Markdown("""
            ### Structure Your Documentation Using ADPIE
            Enter a clinical scenario, and Relational AI will help you organize it using the nursing process:
            - **A**ssessment
            - **D**iagnosis
            - **P**lanning
            - **I**mplementation
            - **E**valuation
            """)
            
            scenario_input = gr.Textbox(
                label="Clinical Scenario",
                placeholder="e.g., 'Patient reports difficulty sleeping due to pain in left hip. Pain score 7/10. Currently on paracetamol PRN.'",
                lines=4,
            )
            adpie_btn = gr.Button("📋 Generate ADPIE Documentation", variant="primary")
            adpie_output = gr.Textbox(label="Structured ADPIE Notes", lines=15, interactive=False)
            
            adpie_btn.click(
                fn=adpie_generator,
                inputs=scenario_input,
                outputs=adpie_output,
            )

        # Tab 5: Semantic Review
        with gr.TabItem("🧠 Semantic Review"):
            gr.Markdown("""
            ### Clinical Semantic Analysis (openEHR Inspired)
            This tool performs a deep audit of your nursing documentation. It checks the note against 
            the **ONC Relational Care Logical Model** and suggests formal **NANDA-I** mappings.
            
            > **Goal:** To ensure documentation is not just "data" but high-quality **Clinical Knowledge**.
            """)
            
            with gr.Row():
                with gr.Column():
                    review_input = gr.Textbox(
                        label="Patient Progress Note",
                        placeholder="Paste a note for a semantic audit...",
                        lines=5,
                    )
                    review_btn = gr.Button("🧠 Perform Semantic Review", variant="primary")
                
                with gr.Column():
                    review_output = gr.Textbox(
                        label="Semantic Audit & Mapping Suggestions",
                        lines=12,
                        interactive=False,
                    )
            
            review_btn.click(
                fn=semantic_review,
                inputs=review_input,
                outputs=review_output,
            )
            
            gr.Examples(
                examples=[
                    ["Patient seems isolated today. Minimal eye contact. Did not participate in group activity."],
                    ["Mrs. Singh (dark skin tone) has area of hyperpigmentation on sacrum. Patient prefers to be called 'Dadi'."],
                ],
                inputs=review_input,
            )
    
    # Footer
    gr.Markdown("""
    ---
    **Model:** [NurseCitizenDeveloper/nursing-llama-3-8b-fons](https://huggingface.co/NurseCitizenDeveloper/nursing-llama-3-8b-fons) | 
    **License:** CC BY-NC 3.0 | 
    **IG:** [opennursingcoreig.com](https://opennursingcoreig.com)
    
    > ⚠️ **Disclaimer:** This tool is for research and educational purposes only. All clinical documentation must be verified by a registered nurse.
    """)

# Launch
if __name__ == "__main__":
    demo.queue().launch()
