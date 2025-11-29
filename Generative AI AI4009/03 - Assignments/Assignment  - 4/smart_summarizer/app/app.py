"""
Smart Summarizer Streamlit App
This script provides a web interface for the Smart Summarizer using Streamlit.
"""

import os
import sys
import io
import torch
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import from other modules
from models.lora_finetune import SummarizerLoraTrainer
from evaluation.evaluation import SummaryEvaluator

# For PDF processing
import pypdf
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer


class SmartSummarizerApp:
    """A class to handle the Streamlit interface for the Smart Summarizer."""

    def __init__(self, base_model_name, lora_model_dir, together_api_key=None):
        """
        Initialize the app.

        Args:
            base_model_name (str): Name of the base model
            lora_model_dir (str): Directory containing the LoRA model
            together_api_key (str, optional): API key for Together.ai
        """
        self.base_model_name = base_model_name
        self.lora_model_dir = lora_model_dir
        self.together_api_key = together_api_key

        # Models and tokenizers
        self.base_model = None
        self.base_tokenizer = None
        self.lora_model = None
        self.lora_tokenizer = None

        # Evaluator
        self.evaluator = None

        # Set up page configuration
        st.set_page_config(page_title="Smart Summarizer", page_icon="📚", layout="wide")

    def load_models(self):
        """Load the base and LoRA models."""
        with st.spinner("Loading models... This may take a minute."):
            # Load base model and tokenizer
            self.base_tokenizer = AutoTokenizer.from_pretrained(self.base_model_name)
            if self.base_tokenizer.pad_token is None:
                self.base_tokenizer.pad_token = self.base_tokenizer.eos_token

            self.base_model = AutoModelForCausalLM.from_pretrained(
                self.base_model_name,
                load_in_8bit=True,
                device_map="auto",
                torch_dtype=torch.float16,
            )

            # Load LoRA model
            self.lora_tokenizer = AutoTokenizer.from_pretrained(self.lora_model_dir)
            base_model_for_lora = AutoModelForCausalLM.from_pretrained(
                self.base_model_name,
                load_in_8bit=True,
                device_map="auto",
                torch_dtype=torch.float16,
            )
            self.lora_model = PeftModel.from_pretrained(
                base_model_for_lora, self.lora_model_dir
            )

            # Initialize evaluator if Together API key is provided
            if self.together_api_key:
                self.evaluator = SummaryEvaluator(
                    base_model_name=self.base_model_name,
                    lora_model_dir=self.lora_model_dir,
                    together_api_key=self.together_api_key,
                )

        st.success("Models loaded successfully! Ready to summarize.")

    def extract_text_from_pdf(self, pdf_file):
        """
        Extract text from a PDF file.

        Args:
            pdf_file: File object of the PDF

        Returns:
            str: Extracted text
        """
        try:
            pdf_reader = pypdf.PdfReader(pdf_file)
            text = ""

            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"

            return text
        except Exception as e:
            st.error(f"Error extracting text from PDF: {str(e)}")
            return None

    def generate_summary(self, text, model, tokenizer, max_new_tokens=256):
        """
        Generate a summary for the given text using the specified model.

        Args:
            text (str): Text to summarize
            model: Model to use for generation
            tokenizer: Tokenizer to use for tokenization
            max_new_tokens (int): Maximum number of tokens to generate

        Returns:
            str: Generated summary
        """
        # Truncate input if it's too long
        max_input_length = 4096  # Adjust based on model capabilities
        if len(text) > max_input_length:
            text = text[:max_input_length]

        # Tokenize the input text
        inputs = tokenizer(text, return_tensors="pt", truncation=True)
        inputs = {k: v.to(model.device) for k, v in inputs.items()}

        # Generate summary
        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                temperature=0.7,
                top_p=0.9,
                num_beams=4,
                do_sample=True,
                pad_token_id=tokenizer.pad_token_id,
                eos_token_id=tokenizer.eos_token_id,
            )

        # Decode the generated text
        summary = tokenizer.decode(outputs[0], skip_special_tokens=True)

        return summary

    def evaluate_with_llm_judge(self, text, summary):
        """
        Evaluate a summary using LLM-as-a-Judge.

        Args:
            text (str): Original text
            summary (str): Summary to evaluate

        Returns:
            dict: Dictionary containing scores and justifications
        """
        if self.evaluator is None or self.together_api_key is None:
            st.warning(
                "LLM-as-a-Judge evaluation is not available. Please provide a Together.ai API key."
            )
            return None

        # Create prompt for the LLM judge
        prompt = self.evaluator._create_llm_judge_prompt(text, summary)

        # Get judgment from Together.ai
        judgment = self.evaluator._get_judgment_from_together(
            prompt, model_name="Meta-Llama-3.1-70B-Instruct-Turbo"
        )

        # Parse scores
        scores = self.evaluator._parse_scores(judgment)

        # Extract justifications using regex
        import re

        fluency_justification = ""
        factuality_justification = ""
        coverage_justification = ""

        fluency_match = re.search(
            r"Fluency:.*?\n.*?Justification: (.*?)(?=\n\w|$)", judgment, re.DOTALL
        )
        if fluency_match:
            fluency_justification = fluency_match.group(1).strip()

        factuality_match = re.search(
            r"Factuality:.*?\n.*?Justification: (.*?)(?=\n\w|$)", judgment, re.DOTALL
        )
        if factuality_match:
            factuality_justification = factuality_match.group(1).strip()

        coverage_match = re.search(
            r"Coverage:.*?\n.*?Justification: (.*?)(?=\n\w|$)", judgment, re.DOTALL
        )
        if coverage_match:
            coverage_justification = coverage_match.group(1).strip()

        return {
            "scores": scores,
            "justifications": {
                "fluency": fluency_justification,
                "factuality": factuality_justification,
                "coverage": coverage_justification,
            },
            "full_judgment": judgment,
        }

    def render_sidebar(self):
        """Render the sidebar."""
        st.sidebar.title("Smart Summarizer")
        st.sidebar.write(
            "Upload a research paper to summarize it using our fine-tuned model."
        )

        # Add Together.ai API key input
        together_api_key = st.sidebar.text_input(
            "Together.ai API Key (for LLM-as-a-Judge)",
            type="password",
            help="Enter your Together.ai API key to use LLM-as-a-Judge evaluation.",
        )

        if together_api_key:
            self.together_api_key = together_api_key

        # Add GitHub link
        st.sidebar.markdown("---")
        st.sidebar.write("Smart Summarizer is built with fine-tuned LLMs using LoRA.")

        # Add information about the model
        st.sidebar.markdown("---")
        st.sidebar.subheader("Model Information")
        st.sidebar.write(f"Base Model: {self.base_model_name}")
        st.sidebar.write("Fine-tuning: LoRA (Low-Rank Adaptation)")

    def render_main(self):
        """Render the main section of the app."""
        st.title("📚 Smart Summarizer")
        st.write(
            """
        This app uses a fine-tuned LLM to summarize academic research papers.
        Upload a paper (PDF or plain text) and get a concise summary!
        """
        )

        # File upload section
        uploaded_file = st.file_uploader(
            "Upload a research paper (PDF or TXT)", type=["pdf", "txt"]
        )

        # Text input as an alternative
        st.write("--- OR ---")
        input_text = st.text_area("Paste the text you want to summarize", height=200)

        # Get text to summarize
        text_to_summarize = None

        if uploaded_file is not None:
            # Get file content based on type
            if uploaded_file.type == "application/pdf":
                text_to_summarize = self.extract_text_from_pdf(uploaded_file)
                if text_to_summarize:
                    st.success("PDF processed successfully!")
            else:  # txt file
                text_to_summarize = uploaded_file.getvalue().decode("utf-8")
                st.success("Text file processed successfully!")
        elif input_text:
            text_to_summarize = input_text

        # Generate summary
        if text_to_summarize:
            # Add model loading button
            if st.button("Load Models"):
                self.load_models()

            # Check if models are loaded
            if self.base_model is None or self.lora_model is None:
                st.warning("Please load the models first.")
                return

            # Add summarize button
            if st.button("Summarize"):
                with st.spinner("Generating summaries..."):
                    # Generate summary with LoRA model
                    lora_summary = self.generate_summary(
                        text_to_summarize, self.lora_model, self.lora_tokenizer
                    )

                    # Generate summary with base model for comparison
                    base_summary = self.generate_summary(
                        text_to_summarize, self.base_model, self.base_tokenizer
                    )

                # Display the fine-tuned model's summary
                st.subheader("📝 Summary (Fine-tuned Model)")
                st.write(lora_summary)

                # Display the base model's summary in an expandable section
                with st.expander("Compare with Base Model Summary"):
                    st.write(base_summary)

                # Evaluate with LLM-as-a-Judge if API key is provided
                if self.together_api_key:
                    st.subheader("🧠 LLM-as-a-Judge Evaluation")

                    with st.spinner("Evaluating summary quality..."):
                        evaluation = self.evaluate_with_llm_judge(
                            text_to_summarize, lora_summary
                        )

                    if evaluation:
                        # Display scores
                        scores = evaluation["scores"]
                        justifications = evaluation["justifications"]

                        col1, col2, col3 = st.columns(3)

                        with col1:
                            st.metric("Fluency", f"{scores['fluency']}/5")
                            st.write(f"*{justifications['fluency']}*")

                        with col2:
                            st.metric("Factuality", f"{scores['factuality']}/5")
                            st.write(f"*{justifications['factuality']}*")

                        with col3:
                            st.metric("Coverage", f"{scores['coverage']}/5")
                            st.write(f"*{justifications['coverage']}*")

                        # Calculate average score
                        avg_score = (
                            scores["fluency"]
                            + scores["factuality"]
                            + scores["coverage"]
                        ) / 3
                        st.metric("Overall Quality", f"{avg_score:.1f}/5")

    def run(self):
        """Run the Streamlit app."""
        self.render_sidebar()
        self.render_main()


if __name__ == "__main__":
    # Example usage
    base_model_name = "meta-llama/Llama-3-8B"  # Replace with the model you want to use
    lora_model_dir = (
        "../models/lora_summarizer/final_model"  # Replace with your model path
    )

    app = SmartSummarizerApp(base_model_name, lora_model_dir)
    app.run()
