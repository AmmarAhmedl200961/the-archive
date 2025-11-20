#!/usr/bin/env python3
"""
Model Integration for Multi-Agent Research Assistant

This module provides tools for integrating the fine-tuned summarization 
model with the Multi-Agent Research Assistant.
"""

import os
import torch
import logging
import json
from typing import Dict, Any, Optional, List, Union, Tuple
from pathlib import Path
import requests
import time

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Try to import transformers
try:
    from transformers import AutoModelForCausalLM, AutoTokenizer
    from peft import PeftModel, PeftConfig
    TRANSFORMERS_AVAILABLE = True
except ImportError:
    logger.warning("Transformers package not available. Using fallback methods for summarization.")
    TRANSFORMERS_AVAILABLE = False

class ModelIntegration:
    """Integration with the fine-tuned summarization model."""
    
    def __init__(self, model_path: Optional[str] = None, api_key: Optional[str] = None):
        """
        Initialize model integration.
        
        Args:
            model_path: Path to the fine-tuned model directory
            api_key: Together.ai API key (for fallback method)
        """
        self.model = None
        self.tokenizer = None
        self.model_path = model_path or os.environ.get("FINETUNED_MODEL_PATH", "./fine_tuned_model")
        self.api_key = api_key or os.environ.get("TOGETHER_API_KEY", "")
        self.fallback_mode = False
        
        # Load the model if transformers is available
        if TRANSFORMERS_AVAILABLE:
            self._load_model()
        else:
            logger.info("Using Together.ai as fallback for summarization")
            self.fallback_mode = True
    
    def _load_model(self) -> None:
        """Load the fine-tuned model."""
        try:
            if not os.path.exists(self.model_path):
                logger.warning(f"Model path '{self.model_path}' does not exist. Using fallback method.")
                self.fallback_mode = True
                return
            
            # Check if the model path contains a config.json file indicating it's a LoRA model
            is_lora = os.path.exists(os.path.join(self.model_path, "adapter_config.json"))
            
            # Load the tokenizer
            if is_lora:
                # For LoRA models, we need to load the base model first
                # Try to determine the base model from the LoRA config
                try:
                    with open(os.path.join(self.model_path, "adapter_config.json"), "r") as f:
                        config = json.load(f)
                    base_model_name = config.get("base_model_name_or_path", "mistralai/Mistral-7B-v0.1")
                except:
                    # Default to Mistral if we can't determine the base model
                    base_model_name = "mistralai/Mistral-7B-v0.1"
            else:
                base_model_name = self.model_path
            
            logger.info(f"Loading tokenizer from {base_model_name}")
            self.tokenizer = AutoTokenizer.from_pretrained(base_model_name, trust_remote_code=True)
            
            # Ensure we have a padding token
            if self.tokenizer.pad_token is None:
                self.tokenizer.pad_token = self.tokenizer.eos_token
            
            # Check if CUDA is available
            device = "cuda" if torch.cuda.is_available() else "cpu"
            logger.info(f"Using device: {device}")
            
            # Load the base model
            if is_lora:
                logger.info(f"Loading base model from {base_model_name}")
                base_model = AutoModelForCausalLM.from_pretrained(
                    base_model_name,
                    load_in_4bit=True if torch.cuda.is_available() else False,
                    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
                    device_map="auto" if torch.cuda.is_available() else None,
                    trust_remote_code=True
                )
                
                # Load the LoRA adapter
                logger.info(f"Loading LoRA adapter from {self.model_path}")
                self.model = PeftModel.from_pretrained(base_model, self.model_path)
            else:
                # Direct loading of the full model
                logger.info(f"Loading model from {self.model_path}")
                self.model = AutoModelForCausalLM.from_pretrained(
                    self.model_path,
                    load_in_4bit=True if torch.cuda.is_available() else False,
                    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
                    device_map="auto" if torch.cuda.is_available() else None,
                    trust_remote_code=True
                )
            
            # Set the model to evaluation mode
            self.model.eval()
            logger.info("Model loaded successfully")
        except Exception as e:
            logger.error(f"Error loading model: {e}")
            self.fallback_mode = True
            self.model = None
            self.tokenizer = None
    
    def _summarize_with_model(self, text: str, max_length: int = 300) -> str:
        """
        Generate a summary using the loaded model.
        
        Args:
            text: Text to summarize
            max_length: Maximum length of the summary in tokens
            
        Returns:
            Generated summary
        """
        if self.model is None or self.tokenizer is None:
            return None
        
        try:
            # Create the prompt
            prompt = f"""Summarize the following academic paper:
            
Article: {text}
            
Summary: """
            
            # Tokenize the input
            inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)
            
            # Check if the input is too long for the model's context window
            max_context_length = 2048  # Safe default for most models
            if hasattr(self.model.config, "max_position_embeddings"):
                max_context_length = self.model.config.max_position_embeddings
            
            if inputs.input_ids.shape[1] > max_context_length:
                # If the input is too long, truncate it
                logger.warning(f"Input too long ({inputs.input_ids.shape[1]} tokens), truncating to {max_context_length} tokens")
                inputs.input_ids = inputs.input_ids[:, :max_context_length]
                if hasattr(inputs, "attention_mask"):
                    inputs.attention_mask = inputs.attention_mask[:, :max_context_length]
            
            # Generate the summary
            with torch.no_grad():
                output = self.model.generate(
                    inputs.input_ids,
                    max_new_tokens=max_length,
                    do_sample=True,
                    temperature=0.7,
                    top_p=0.9,
                    repetition_penalty=1.2,
                    pad_token_id=self.tokenizer.eos_token_id
                )
            
            # Decode the output
            summary = self.tokenizer.decode(output[0], skip_special_tokens=True)
            
            # Extract just the summary part (after "Summary:")
            try:
                summary = summary.split("Summary:")[1].strip()
            except IndexError:
                pass  # If "Summary:" is not in the output, use the whole output
            
            return summary
        except Exception as e:
            logger.error(f"Error generating summary with model: {e}")
            return None
    
    def _summarize_with_together(self, text: str, max_tokens: int = 512) -> str:
        """
        Generate a summary using the Together.ai API (fallback method).
        
        Args:
            text: Text to summarize
            max_tokens: Maximum length of the summary in tokens
            
        Returns:
            Generated summary
        """
        if not self.api_key:
            logger.error("No Together.ai API key available for fallback summarization")
            return "Error: No API key available for summarization"
        
        try:
            # Create the prompt
            prompt = f"""Summarize the following academic paper with a focus on the main problem, methods, and key findings.
            
Article: {text}
            
Summary:"""
            
            # Call the Together.ai API
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            json_data = {
                "model": "meta-llama/Llama-3-8B-Instruct",
                "prompt": prompt,
                "max_tokens": max_tokens,
                "temperature": 0.7,
                "top_p": 0.9,
                "top_k": 60,
                "repetition_penalty": 1.1
            }
            
            response = requests.post(
                "https://api.together.xyz/v1/completions",
                headers=headers,
                json=json_data
            )
            
            if response.status_code == 200:
                result = response.json()
                return result["choices"][0]["text"].strip()
            else:
                logger.error(f"Error from Together.ai API: {response.text}")
                return f"Error: {response.status_code} from API"
        except Exception as e:
            logger.error(f"Error generating summary with Together.ai: {e}")
            return f"Error generating summary: {str(e)}"
    
    def summarize(self, text: str, max_length: int = 300) -> str:
        """
        Generate a summary of the given text.
        
        Args:
            text: Text to summarize
            max_length: Maximum length of the summary in tokens
            
        Returns:
            Generated summary
        """
        # If we're in fallback mode, use Together.ai
        if self.fallback_mode:
            return self._summarize_with_together(text, max_length)
        
        # Try to use the loaded model
        summary = self._summarize_with_model(text, max_length)
        
        # If the model fails, fall back to Together.ai
        if summary is None:
            logger.info("Falling back to Together.ai for summarization")
            summary = self._summarize_with_together(text, max_length)
        
        return summary
    
    def is_using_fallback(self) -> bool:
        """
        Check if the integration is using the fallback method.
        
        Returns:
            True if using fallback, False if using the loaded model
        """
        return self.fallback_mode
    
    def get_model_info(self) -> Dict[str, Any]:
        """
        Get information about the loaded model.
        
        Returns:
            Dictionary with model information
        """
        if self.fallback_mode:
            return {
                "status": "fallback",
                "method": "Together.ai API",
                "model": "meta-llama/Llama-3-8B-Instruct",
                "parameters": None
            }
        
        if self.model is None:
            return {
                "status": "error",
                "error": "Model not loaded"
            }
        
        # Try to get model information
        try:
            model_type = type(self.model).__name__
            is_peft = isinstance(self.model, PeftModel) if TRANSFORMERS_AVAILABLE else False
            
            if is_peft:
                base_model_name = self.model.base_model.config._name_or_path
                adapter_name = self.model.active_adapter
                
                return {
                    "status": "loaded",
                    "type": "LoRA fine-tuned model",
                    "base_model": base_model_name,
                    "adapter": adapter_name,
                    "device": str(self.model.device),
                    "parameters": {
                        "total": sum(p.numel() for p in self.model.parameters()),
                        "trainable": sum(p.numel() for p in self.model.parameters() if p.requires_grad)
                    }
                }
            else:
                return {
                    "status": "loaded",
                    "type": "Full model",
                    "model_name": getattr(self.model.config, "_name_or_path", "unknown"),
                    "device": str(next(self.model.parameters()).device),
                    "parameters": sum(p.numel() for p in self.model.parameters())
                }
        except Exception as e:
            logger.error(f"Error getting model info: {e}")
            return {
                "status": "loaded",
                "error": str(e)
            }

def test_model_integration(model_path: Optional[str] = None, api_key: Optional[str] = None) -> None:
    """
    Test the model integration with a sample text.
    
    Args:
        model_path: Path to the fine-tuned model directory
        api_key: Together.ai API key
    """
    # Create the integration
    integration = ModelIntegration(model_path, api_key)
    
    # Print model info
    model_info = integration.get_model_info()
    print("\nModel Information:")
    for key, value in model_info.items():
        print(f"  {key}: {value}")
    
    # Sample text to summarize
    sample_text = """
    Recent advances in large language models (LLMs) have demonstrated their remarkable ability in
    following instructions, performing in-context learning, and generating human-like responses.
    However, existing work has primarily focused on evaluating LLMs via multiple-choice questions
    or short-form free-text generation. In this paper, we introduce FActScore, a new evaluation
    framework for measuring the factual precision of long-form text generated by LLMs. FActScore
    decomposes generated text into a set of atomic facts, each of which is then verified by a
    question-answering (QA) system. We validate that FActScore has a strong correlation with human
    evaluation on two existing datasets. We further create a new long-form generation dataset for
    evaluating factuality, covering diverse topics including science, finance, medicine, and
    history. Through our evaluation framework, we reveal that some widely used techniques for
    improving generations, such as Chain-of-Thought prompting, can lead to reduced factuality.
    Furthermore, we demonstrate that stronger LLMs do not always produce more factual text.
    Additionally, we find that model-based fact-checking can effectively identify and reduce factual
    errors in model generations.
    """
    
    # Test the integration
    print("\nGenerating summary...")
    summary = integration.summarize(sample_text)
    print("\nSummary:")
    print(summary)
    
    # Check if using fallback
    if integration.is_using_fallback():
        print("\nUsing fallback method (Together.ai API)")
    else:
        print("\nUsing loaded model for summarization")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Test model integration")
    parser.add_argument("--model_path", type=str, help="Path to fine-tuned model")
    parser.add_argument("--api_key", type=str, help="Together.ai API key")
    
    args = parser.parse_args()
    
    # Get API key from environment if not provided
    if not args.api_key:
        args.api_key = os.environ.get("TOGETHER_API_KEY", "")
    
    # Test the integration
    test_model_integration(args.model_path, args.api_key)