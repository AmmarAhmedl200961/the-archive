"""
SummaryAgent Module
This agent is responsible for generating summaries of academic papers using the fine-tuned LoRA model.
"""

import sys
import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel
import requests
import re


class SummaryAgent:
    """
    Agent for summarizing academic papers using a fine-tuned LoRA model.
    """

    def __init__(self, base_model_name=None, lora_model_dir=None):
        """
        Initialize the SummaryAgent.

        Args:
            base_model_name (str): Name of the base model
            lora_model_dir (str): Directory containing the LoRA model weights
        """
        self.base_model_name = base_model_name or "meta-llama/Llama-3-8B"
        self.lora_model_dir = lora_model_dir
        self.model = None
        self.tokenizer = None

        # Flag to track if model is loaded
        self.model_loaded = False

    def load_model(self):
        """
        Load the fine-tuned model for summarization.
        """
        if self.model_loaded:
            return

        print("Loading summarization model...")

        try:
            # Load tokenizer
            self.tokenizer = AutoTokenizer.from_pretrained(
                self.lora_model_dir
                if os.path.exists(self.lora_model_dir)
                else self.base_model_name
            )

            if self.tokenizer.pad_token is None:
                self.tokenizer.pad_token = self.tokenizer.eos_token

            # Load base model
            base_model = AutoModelForCausalLM.from_pretrained(
                self.base_model_name,
                load_in_8bit=True,
                device_map="auto",
                torch_dtype=torch.float16,
            )

            # Load LoRA weights if available
            if self.lora_model_dir and os.path.exists(self.lora_model_dir):
                self.model = PeftModel.from_pretrained(base_model, self.lora_model_dir)
                print(f"Loaded fine-tuned LoRA model from {self.lora_model_dir}")
            else:
                self.model = base_model
                print(f"LoRA model not found, using base model {self.base_model_name}")

            self.model_loaded = True

        except Exception as e:
            print(f"Error loading model: {str(e)}")
            # Fallback to base model if LoRA loading fails
            try:
                if self.model is None:
                    self.tokenizer = AutoTokenizer.from_pretrained(self.base_model_name)
                    if self.tokenizer.pad_token is None:
                        self.tokenizer.pad_token = self.tokenizer.eos_token

                    self.model = AutoModelForCausalLM.from_pretrained(
                        self.base_model_name,
                        load_in_8bit=True,
                        device_map="auto",
                        torch_dtype=torch.float16,
                    )
                    self.model_loaded = True
                    print(f"Fallback: Loaded base model {self.base_model_name}")
            except Exception as e2:
                print(f"Error loading fallback model: {str(e2)}")

    def download_paper_content(self, paper):
        """
        Download or extract the content of a paper from its URL or ID.
        Currently supports arXiv IDs extracted from URLs.

        Args:
            paper (dict): Paper metadata including URL

        Returns:
            str: Paper content (abstract if full text not available)
        """
        # If we already have the abstract, use it as a fallback
        abstract = paper.get("abstract", "")

        # Try to extract arXiv ID from the URL
        arxiv_id = None
        url = paper.get("url", "")

        if "arxiv.org" in url:
            # Try different patterns to extract arXiv ID
            patterns = [
                r"arxiv\.org/abs/([0-9v\.]+)",
                r"arxiv\.org/pdf/([0-9v\.]+)",
                r"arxiv\.org/[a-z]+/([0-9v\.]+)",
            ]

            for pattern in patterns:
                match = re.search(pattern, url)
                if match:
                    arxiv_id = match.group(1)
                    break

        # If we found an arXiv ID, try to get the abstract from the API
        if arxiv_id:
            try:
                api_url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"
                response = requests.get(api_url)

                if response.status_code == 200:
                    # Parse XML to extract abstract
                    import xml.etree.ElementTree as ET

                    root = ET.fromstring(response.content)
                    namespace = {"atom": "http://www.w3.org/2005/Atom"}

                    # Find entry and extract abstract
                    entry = root.find(".//atom:entry", namespace)
                    if entry:
                        abstract_elem = entry.find("atom:summary", namespace)
                        if abstract_elem is not None and abstract_elem.text:
                            abstract = abstract_elem.text.strip()
            except Exception as e:
                print(f"Error fetching arXiv content: {str(e)}")

        # Return the best content we have (currently just abstract)
        # In a more complete implementation, this would attempt to download and parse PDFs
        return abstract

    def generate_summary(self, text, max_length=256):
        """
        Generate a summary for the given text.

        Args:
            text (str): Text to summarize
            max_length (int): Maximum length of the summary

        Returns:
            str: Generated summary
        """
        if not self.model_loaded:
            self.load_model()

        if not self.model_loaded:
            return "Error: Could not load summarization model."

        # Truncate input if it's too long
        max_input_length = 1024  # Adjust based on model capabilities
        if len(text) > max_input_length:
            text = text[:max_input_length]

        # Prepare the prompt for summarization
        prompt = f"Please summarize the following academic paper:\n\n{text}\n\nSummary:"

        # Tokenize the input text
        inputs = self.tokenizer(prompt, return_tensors="pt", truncation=True)
        inputs = {k: v.to(self.model.device) for k, v in inputs.items()}

        # Generate summary
        try:
            with torch.no_grad():
                outputs = self.model.generate(
                    **inputs,
                    max_new_tokens=max_length,
                    temperature=0.7,
                    top_p=0.9,
                    num_beams=4,
                    do_sample=True,
                    pad_token_id=self.tokenizer.pad_token_id,
                    eos_token_id=self.tokenizer.eos_token_id,
                )

            # Decode the generated text
            summary = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

            # Extract just the summary part (after our prompt)
            summary = summary.split("Summary:")[-1].strip()

            return summary

        except Exception as e:
            print(f"Error generating summary: {str(e)}")
            return f"Error generating summary: {str(e)}"

    def analyze_paper_structure(self, text):
        """
        Analyze the structure of a paper to identify key sections.

        Args:
            text (str): Paper text

        Returns:
            dict: Dictionary containing identified sections
        """
        # This is a simplified implementation that would be expanded in a real system
        # to extract proper sections from papers

        # For now, we'll just return the text as a whole
        return {"whole_text": text}

    def summarize_paper(self, paper):
        """
        Download and summarize a paper.

        Args:
            paper (dict): Paper metadata

        Returns:
            dict: Paper with added summary
        """
        # Get paper content (abstract or full text)
        content = self.download_paper_content(paper)

        # If we couldn't get any content, return the paper as is
        if not content:
            return {
                **paper,
                "summary": "Could not retrieve paper content for summarization.",
            }

        # Analyze paper structure to identify key sections
        structured_content = self.analyze_paper_structure(content)

        # Generate summary
        summary = self.generate_summary(content)

        # Add summary to paper metadata
        summarized_paper = {
            **paper,
            "summary": summary,
            "content_used": (
                "abstract" if content == paper.get("abstract", "") else "full_text"
            ),
        }

        return summarized_paper

    def summarize_papers(self, papers):
        """
        Summarize multiple papers.

        Args:
            papers (list): List of paper metadata

        Returns:
            list: List of papers with added summaries
        """
        summarized_papers = []

        for i, paper in enumerate(papers):
            print(
                f"Summarizing paper {i+1}/{len(papers)}: {paper.get('title', 'Untitled')}"
            )
            summarized_paper = self.summarize_paper(paper)
            summarized_papers.append(summarized_paper)

        return summarized_papers

    def run(self, inputs):
        """
        Run the summary agent with the given inputs.

        Args:
            inputs (dict): Input dictionary containing papers to summarize

        Returns:
            dict: Output dictionary containing summarized papers
        """
        # Get papers to summarize
        papers = inputs.get("top_papers", [])

        if not papers:
            return {
                "error": "No papers provided for summarization",
                "summarized_papers": [],
            }

        # Summarize papers
        summarized_papers = self.summarize_papers(papers)

        return {"summarized_papers": summarized_papers}


if __name__ == "__main__":
    # Example usage
    agent = SummaryAgent(
        base_model_name="meta-llama/Llama-3-8B",
        lora_model_dir="../../smart_summarizer/models/lora_summarizer/final_model",
    )

    # Example paper (just using the abstract as content for this example)
    paper = {
        "title": "Sample Paper Title",
        "abstract": "This is a sample abstract for testing the summarization agent. It would typically contain information about the paper's methodology, findings, and conclusions.",
        "url": "https://arxiv.org/abs/2104.12369",
    }

    result = agent.run({"top_papers": [paper]})
    print(f"Generated summary: {result['summarized_papers'][0]['summary']}")
