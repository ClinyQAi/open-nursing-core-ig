"""
Evaluation Script for Fine-Tuned Nursing LLM
Uses Azure OpenAI (GPT-4o) as an "Expert Judge" to score model responses.
"""
import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from langchain_core.messages import HumanMessage
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel
import torch

load_dotenv()

# Configuration
HF_MODEL_ID = "NurseCitizenDeveloper/nursing-llama-3-8b-fons"
BASE_MODEL_ID = "unsloth/llama-3-8b-bnb-4bit"

def load_model_from_hf():
    """Load the fine-tuned LoRA adapter from Hugging Face."""
    print(f"🔄 Loading model from Hugging Face: {HF_MODEL_ID}...")
    
    # Load tokenizer
    tokenizer = AutoTokenizer.from_pretrained(HF_MODEL_ID)
    
    # Load base model + adapter
    model = AutoModelForCausalLM.from_pretrained(
        HF_MODEL_ID,
        torch_dtype=torch.float16,
        device_map="auto",
        trust_remote_code=True,
    )
    
    print("✅ Model loaded successfully!")
    return model, tokenizer

def get_azure_judge():
    """Initialize Azure OpenAI as the expert judge."""
    return AzureChatOpenAI(
        azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    )

def evaluate_response(llm, instruction, input_text, model_output):
    """Use Azure GPT-4o to evaluate the model's response."""
    prompt = f"""You are an expert nursing educator evaluating an AI assistant trained on FONS (Foundation of Nursing Studies) principles.

Evaluate the following response on a scale of 1-10 for each criterion:
1. **Clinical Accuracy** (1-10): Is the information clinically correct?
2. **Person-Centred Language** (1-10): Does it use respectful, dignified language?
3. **FONS Alignment** (1-10): Does it reflect FONS principles (relational care, practice development)?

**Instruction Given**: {instruction}
**Context**: {input_text}
**Model Response**: {model_output}

Provide scores and a brief rationale for each, then an overall recommendation."""
    
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content

def run_evaluation():
    """Main evaluation loop."""
    # Test cases covering key nursing domains
    test_cases = [
        {
            "instruction": "Summarize the key nursing interventions for a patient with delirium.",
            "input": "Patient is an 85-year-old male with acute confusion, fluctuating consciousness, and visual hallucinations. History of dementia."
        },
        {
            "instruction": "What are the FONS principles for person-centred care?",
            "input": "A nurse is documenting care for a patient with dementia."
        },
        {
            "instruction": "Explain why skin tone documentation is important in pressure ulcer risk assessment.",
            "input": "Using the Braden Scale for a patient with darker skin."
        },
        {
            "instruction": "How should a nurse communicate bad news to a family member?",
            "input": "The patient's condition has deteriorated significantly overnight."
        },
    ]
    
    alpaca_prompt = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
{}

### Input:
{}

### Response:
{}"""

    # Load model and judge
    model, tokenizer = load_model_from_hf()
    llm = get_azure_judge()
    
    print("\n" + "="*60)
    print("🏁 Relational Ai for Nursing Evaluation")
    print("="*60)
    
    total_scores = {"accuracy": 0, "person_centred": 0, "fons": 0}
    
    for i, case in enumerate(test_cases, 1):
        print(f"\n--- Test Case {i}/{len(test_cases)} ---")
        print(f"📝 Instruction: {case['instruction']}")
        
        # Generate response
        prompt = alpaca_prompt.format(case["instruction"], case["input"], "")
        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
        
        with torch.no_grad():
            outputs = model.generate(**inputs, max_new_tokens=200, do_sample=True, temperature=0.7)
        
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        response = response.split("### Response:")[-1].strip() if "### Response:" in response else response
        
        print(f"🤖 Model Response: {response[:300]}...")
        
        # Evaluate with Azure Judge
        evaluation = evaluate_response(llm, case["instruction"], case["input"], response)
        print(f"\n⚖️ Expert Evaluation:\n{evaluation}")
        print("-" * 50)
    
    print("\n" + "="*60)
    print("✅ Evaluation Complete!")
    print("="*60)

if __name__ == "__main__":
    run_evaluation()
