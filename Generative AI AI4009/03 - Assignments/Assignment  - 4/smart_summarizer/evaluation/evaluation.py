"""
Summary Evaluation Module
This script handles the evaluation of generated summaries using both automatic metrics
and the LLM-as-a-Judge approach.
"""

import os
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel
import evaluate
from together import Together
import nltk
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
import re


class SummaryEvaluator:
    """A class to evaluate the quality of generated summaries."""

    def __init__(self, base_model_name, lora_model_dir, together_api_key=None):
        """
        Initialize the evaluator.

        Args:
            base_model_name (str): Name of the base model
            lora_model_dir (str): Directory containing the LoRA model
            together_api_key (str, optional): API key for Together.ai
        """
        self.base_model_name = base_model_name
        self.lora_model_dir = lora_model_dir

        # Initialize Together.ai client if API key is provided
        self.together_client = None
        if together_api_key:
            self.together_client = Together(api_key=together_api_key)

        # Initialize evaluation metrics
        try:
            self.rouge = evaluate.load("rouge")
        except:
            nltk.download("punkt")
            self.rouge = evaluate.load("rouge")

        # Try to load BERTScore, but handle potential issues
        try:
            self.bert_score = evaluate.load("bertscore")
        except:
            print("Warning: Could not load BERTScore. Will use ROUGE and BLEU only.")
            self.bert_score = None

        # Load BLEU smoothing function
        self.smoothing = SmoothingFunction().method1

    def load_tokenizer(self):
        """Load the tokenizer for the base model."""
        return AutoTokenizer.from_pretrained(self.base_model_name)

    def load_base_model(self):
        """Load the base pre-trained model."""
        print("Loading base model...")
        tokenizer = self.load_tokenizer()
        model = AutoModelForCausalLM.from_pretrained(
            self.base_model_name,
            load_in_8bit=True,
            device_map="auto",
            torch_dtype=torch.float16,
        )
        return model, tokenizer

    def load_lora_model(self):
        """Load the LoRA fine-tuned model."""
        print("Loading LoRA fine-tuned model...")
        tokenizer = AutoTokenizer.from_pretrained(self.lora_model_dir)
        base_model = AutoModelForCausalLM.from_pretrained(
            self.base_model_name,
            load_in_8bit=True,
            device_map="auto",
            torch_dtype=torch.float16,
        )
        model = PeftModel.from_pretrained(base_model, self.lora_model_dir)
        return model, tokenizer

    def generate_summary_with_model(self, model, tokenizer, text, max_new_tokens=256):
        """
        Generate a summary using the specified model.

        Args:
            model: The model to use for generation
            tokenizer: The tokenizer to use for tokenization
            text (str): The text to summarize
            max_new_tokens (int): Maximum number of tokens to generate

        Returns:
            str: The generated summary
        """
        # Tokenize the input text
        inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=1024)
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

    def compute_rouge(self, predictions, references):
        """
        Compute ROUGE scores for the given predictions and references.

        Args:
            predictions (list): List of predicted summaries
            references (list): List of reference summaries

        Returns:
            dict: Dictionary containing ROUGE scores
        """
        results = self.rouge.compute(
            predictions=predictions, references=references, use_stemmer=True
        )
        return results

    def compute_bleu(self, predictions, references):
        """
        Compute BLEU scores for the given predictions and references.

        Args:
            predictions (list): List of predicted summaries
            references (list): List of reference summaries

        Returns:
            float: BLEU score
        """
        scores = []
        for pred, ref in zip(predictions, references):
            # Tokenize
            pred_tokens = nltk.word_tokenize(pred.lower())
            ref_tokens = nltk.word_tokenize(ref.lower())

            # Compute BLEU with smoothing
            score = sentence_bleu(
                [ref_tokens], pred_tokens, smoothing_function=self.smoothing
            )
            scores.append(score)

        return sum(scores) / len(scores) if scores else 0

    def compute_bertscore(self, predictions, references):
        """
        Compute BERTScore for the given predictions and references.

        Args:
            predictions (list): List of predicted summaries
            references (list): List of reference summaries

        Returns:
            dict: Dictionary containing BERTScore results
        """
        if self.bert_score is None:
            return {"precision": 0, "recall": 0, "f1": 0}

        results = self.bert_score.compute(
            predictions=predictions, references=references, lang="en"
        )

        # Calculate average scores
        avg_results = {
            "precision": sum(results["precision"]) / len(results["precision"]),
            "recall": sum(results["recall"]) / len(results["recall"]),
            "f1": sum(results["f1"]) / len(results["f1"]),
        }

        return avg_results

    def evaluate_with_metrics(self, texts, ground_truths):
        """
        Evaluate generated summaries using automatic metrics.

        Args:
            texts (list): List of input texts to summarize
            ground_truths (list): List of ground truth summaries

        Returns:
            dict: Dictionary containing evaluation results
        """
        print("Evaluating summaries with automatic metrics...")

        # Load models
        base_model, base_tokenizer = self.load_base_model()
        lora_model, lora_tokenizer = self.load_lora_model()

        # Generate summaries
        base_summaries = []
        lora_summaries = []

        for text in tqdm(texts, desc="Generating summaries"):
            # Generate summary with base model
            base_summary = self.generate_summary_with_model(
                base_model, base_tokenizer, text
            )
            base_summaries.append(base_summary)

            # Generate summary with LoRA model
            lora_summary = self.generate_summary_with_model(
                lora_model, lora_tokenizer, text
            )
            lora_summaries.append(lora_summary)

        # Compute automatic metrics
        results = {
            "base_model": {
                "rouge": self.compute_rouge(base_summaries, ground_truths),
                "bleu": self.compute_bleu(base_summaries, ground_truths),
                "bertscore": self.compute_bertscore(base_summaries, ground_truths),
            },
            "lora_model": {
                "rouge": self.compute_rouge(lora_summaries, ground_truths),
                "bleu": self.compute_bleu(lora_summaries, ground_truths),
                "bertscore": self.compute_bertscore(lora_summaries, ground_truths),
            },
            "summaries": {
                "input_texts": texts,
                "ground_truths": ground_truths,
                "base_summaries": base_summaries,
                "lora_summaries": lora_summaries,
            },
        }

        return results

    def evaluate_with_llm_as_judge(
        self,
        texts,
        ground_truths,
        base_summaries,
        lora_summaries,
        model_name="Meta-Llama-3.1-70B-Instruct-Turbo",
    ):
        """
        Evaluate generated summaries using the LLM-as-a-Judge approach.

        Args:
            texts (list): List of input texts
            ground_truths (list): List of ground truth summaries
            base_summaries (list): List of base model summaries
            lora_summaries (list): List of LoRA model summaries
            model_name (str): Name of the model to use as judge

        Returns:
            dict: Dictionary containing evaluation results
        """
        if self.together_client is None:
            raise ValueError(
                "Together.ai API key is required for LLM-as-a-Judge evaluation"
            )

        print("Evaluating summaries with LLM-as-a-Judge...")

        results = {
            "base_model": {"fluency": [], "factuality": [], "coverage": []},
            "lora_model": {"fluency": [], "factuality": [], "coverage": []},
            "judgments": {"base_model": [], "lora_model": []},
        }

        for i, (text, ground_truth, base_summary, lora_summary) in enumerate(
            zip(texts, ground_truths, base_summaries, lora_summaries)
        ):
            print(f"\nEvaluating summary {i+1}/{len(texts)}")

            # Prepare prompt for base model summary
            base_prompt = self._create_llm_judge_prompt(text, base_summary)

            # Get judgment for base model summary
            base_judgment = self._get_judgment_from_together(base_prompt, model_name)
            results["judgments"]["base_model"].append(base_judgment)

            # Parse scores from the judgment
            base_scores = self._parse_scores(base_judgment)
            results["base_model"]["fluency"].append(base_scores["fluency"])
            results["base_model"]["factuality"].append(base_scores["factuality"])
            results["base_model"]["coverage"].append(base_scores["coverage"])

            # Prepare prompt for LoRA model summary
            lora_prompt = self._create_llm_judge_prompt(text, lora_summary)

            # Get judgment for LoRA model summary
            lora_judgment = self._get_judgment_from_together(lora_prompt, model_name)
            results["judgments"]["lora_model"].append(lora_judgment)

            # Parse scores from the judgment
            lora_scores = self._parse_scores(lora_judgment)
            results["lora_model"]["fluency"].append(lora_scores["fluency"])
            results["lora_model"]["factuality"].append(lora_scores["factuality"])
            results["lora_model"]["coverage"].append(lora_scores["coverage"])

        # Calculate average scores
        for model_type in ["base_model", "lora_model"]:
            for criterion in ["fluency", "factuality", "coverage"]:
                scores = results[model_type][criterion]
                results[model_type][f"avg_{criterion}"] = (
                    sum(scores) / len(scores) if scores else 0
                )

        return results

    def _create_llm_judge_prompt(self, input_text, summary):
        """Create a prompt for the LLM judge."""
        # Truncate the input text if it's too long (for API limits)
        max_length = 6000  # Adjust based on API limits
        input_text_truncated = (
            input_text[:max_length] + "..."
            if len(input_text) > max_length
            else input_text
        )

        prompt = f"""As an expert evaluator, assess the quality of the following summary based on the original text.

Original Text:
{input_text_truncated}

Generated Summary:
{summary}

Evaluate the summary on these three dimensions:
1. Fluency: Is the summary readable and grammatically correct? Rate from 1 (poor) to 5 (excellent).
2. Factuality: Are the statements in the summary correct and do they accurately reflect the source? Rate from 1 (poor) to 5 (excellent).
3. Coverage: Does the summary include the main problem, method, and key findings of the paper? Rate from 1 (poor) to 5 (excellent).

For each dimension, provide a numerical score followed by a brief justification.
Format your response exactly as shown below:
Fluency: [score]
Justification: [1-2 sentence justification]
Factuality: [score]
Justification: [1-2 sentence justification]
Coverage: [score]
Justification: [1-2 sentence justification]
"""
        return prompt

    def _get_judgment_from_together(self, prompt, model_name):
        """Get a judgment from the Together.ai API."""
        response = self.together_client.chat.completions.create(
            model=model_name,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=1000,
        )
        return response.choices[0].message.content

    def _parse_scores(self, judgment):
        """Parse scores from the judgment text."""
        scores = {"fluency": 0, "factuality": 0, "coverage": 0}

        # Regular expressions to extract scores
        fluency_match = re.search(r"Fluency:\s*(\d+)", judgment)
        factuality_match = re.search(r"Factuality:\s*(\d+)", judgment)
        coverage_match = re.search(r"Coverage:\s*(\d+)", judgment)

        if fluency_match:
            scores["fluency"] = int(fluency_match.group(1))
        if factuality_match:
            scores["factuality"] = int(factuality_match.group(1))
        if coverage_match:
            scores["coverage"] = int(coverage_match.group(1))

        return scores

    def plot_automatic_metrics(self, results):
        """
        Plot automatic evaluation metrics.

        Args:
            results (dict): Results from evaluate_with_metrics
        """
        plt.figure(figsize=(15, 10))

        # ROUGE scores
        plt.subplot(2, 2, 1)
        rouge_base = results["base_model"]["rouge"]
        rouge_lora = results["lora_model"]["rouge"]

        rouge_metrics = ["rouge1", "rouge2", "rougeL"]
        base_scores = [rouge_base[m] for m in rouge_metrics]
        lora_scores = [rouge_lora[m] for m in rouge_metrics]

        x = np.arange(len(rouge_metrics))
        width = 0.35

        plt.bar(x - width / 2, base_scores, width, label="Base Model")
        plt.bar(x + width / 2, lora_scores, width, label="LoRA Model")

        plt.xlabel("Metric")
        plt.ylabel("Score")
        plt.title("ROUGE Scores")
        plt.xticks(x, rouge_metrics)
        plt.legend()
        plt.grid(True, linestyle="--", alpha=0.7)

        # BLEU score
        plt.subplot(2, 2, 2)
        bleu_scores = [results["base_model"]["bleu"], results["lora_model"]["bleu"]]

        plt.bar(["Base Model", "LoRA Model"], bleu_scores)
        plt.xlabel("Model")
        plt.ylabel("Score")
        plt.title("BLEU Score")
        plt.grid(True, linestyle="--", alpha=0.7)

        # BERTScore
        plt.subplot(2, 2, 3)
        bertscore_base = results["base_model"]["bertscore"]
        bertscore_lora = results["lora_model"]["bertscore"]

        bert_metrics = ["precision", "recall", "f1"]
        base_bert_scores = [bertscore_base[m] for m in bert_metrics]
        lora_bert_scores = [bertscore_lora[m] for m in bert_metrics]

        x = np.arange(len(bert_metrics))

        plt.bar(x - width / 2, base_bert_scores, width, label="Base Model")
        plt.bar(x + width / 2, lora_bert_scores, width, label="LoRA Model")

        plt.xlabel("Metric")
        plt.ylabel("Score")
        plt.title("BERTScore")
        plt.xticks(x, bert_metrics)
        plt.legend()
        plt.grid(True, linestyle="--", alpha=0.7)

        plt.tight_layout()
        plt.savefig("automatic_metrics.png")
        plt.close()

    def plot_llm_judge_scores(self, results):
        """
        Plot LLM-as-a-Judge scores.

        Args:
            results (dict): Results from evaluate_with_llm_as_judge
        """
        plt.figure(figsize=(10, 6))

        criteria = ["fluency", "factuality", "coverage"]
        base_scores = [results["base_model"][f"avg_{c}"] for c in criteria]
        lora_scores = [results["lora_model"][f"avg_{c}"] for c in criteria]

        x = np.arange(len(criteria))
        width = 0.35

        plt.bar(x - width / 2, base_scores, width, label="Base Model")
        plt.bar(x + width / 2, lora_scores, width, label="LoRA Model")

        plt.xlabel("Criterion")
        plt.ylabel("Average Score (1-5)")
        plt.title("LLM-as-a-Judge Evaluation Scores")
        plt.xticks(x, [c.capitalize() for c in criteria])
        plt.ylim(0, 5)
        plt.legend()
        plt.grid(True, linestyle="--", alpha=0.7)

        plt.tight_layout()
        plt.savefig("llm_judge_scores.png")
        plt.close()

    def save_results(self, auto_results, llm_judge_results, output_dir):
        """
        Save evaluation results to files.

        Args:
            auto_results (dict): Results from evaluate_with_metrics
            llm_judge_results (dict): Results from evaluate_with_llm_as_judge
            output_dir (str): Directory to save results to
        """
        os.makedirs(output_dir, exist_ok=True)

        # Save summaries
        summaries = {
            "input_texts": auto_results["summaries"]["input_texts"],
            "ground_truths": auto_results["summaries"]["ground_truths"],
            "base_summaries": auto_results["summaries"]["base_summaries"],
            "lora_summaries": auto_results["summaries"]["lora_summaries"],
        }

        with open(os.path.join(output_dir, "summaries.json"), "w") as f:
            json.dump(summaries, f, indent=2)

        # Save automatic metrics
        auto_metrics = {
            "base_model": {
                "rouge": auto_results["base_model"]["rouge"],
                "bleu": auto_results["base_model"]["bleu"],
                "bertscore": auto_results["base_model"]["bertscore"],
            },
            "lora_model": {
                "rouge": auto_results["lora_model"]["rouge"],
                "bleu": auto_results["lora_model"]["bleu"],
                "bertscore": auto_results["lora_model"]["bertscore"],
            },
        }

        with open(os.path.join(output_dir, "automatic_metrics.json"), "w") as f:
            json.dump(auto_metrics, f, indent=2)

        # Save LLM judge results
        with open(os.path.join(output_dir, "llm_judge_results.json"), "w") as f:
            json.dump(llm_judge_results, f, indent=2)

        # Create CSV for easy viewing
        summaries_df = pd.DataFrame(
            {
                "Text Index": list(range(len(summaries["input_texts"]))),
                "Ground Truth": summaries["ground_truths"],
                "Base Model": summaries["base_summaries"],
                "LoRA Model": summaries["lora_summaries"],
            }
        )

        summaries_df.to_csv(os.path.join(output_dir, "summaries.csv"), index=False)

        # Create CSV for LLM judge scores
        llm_scores = []
        for i in range(len(llm_judge_results["base_model"]["fluency"])):
            llm_scores.append(
                {
                    "Text Index": i,
                    "Base Fluency": llm_judge_results["base_model"]["fluency"][i],
                    "Base Factuality": llm_judge_results["base_model"]["factuality"][i],
                    "Base Coverage": llm_judge_results["base_model"]["coverage"][i],
                    "LoRA Fluency": llm_judge_results["lora_model"]["fluency"][i],
                    "LoRA Factuality": llm_judge_results["lora_model"]["factuality"][i],
                    "LoRA Coverage": llm_judge_results["lora_model"]["coverage"][i],
                }
            )

        llm_scores_df = pd.DataFrame(llm_scores)
        llm_scores_df.to_csv(
            os.path.join(output_dir, "llm_judge_scores.csv"), index=False
        )


if __name__ == "__main__":
    # Example usage
    base_model_name = "meta-llama/Llama-3-8B"
    lora_model_dir = "../models/lora_summarizer/final_model"

    evaluator = SummaryEvaluator(
        base_model_name=base_model_name,
        lora_model_dir=lora_model_dir,
        together_api_key="your-together-api-key",  # Replace with your API key
    )

    # Load test data
    # For demonstration purposes, assume we have test data loaded
    texts = ["Sample text 1", "Sample text 2"]
    ground_truths = ["Ground truth 1", "Ground truth 2"]

    # Evaluate with automatic metrics
    auto_results = evaluator.evaluate_with_metrics(texts, ground_truths)

    # Evaluate with LLM as judge
    llm_judge_results = evaluator.evaluate_with_llm_as_judge(
        texts,
        ground_truths,
        auto_results["summaries"]["base_summaries"],
        auto_results["summaries"]["lora_summaries"],
    )

    # Plot results
    evaluator.plot_automatic_metrics(auto_results)
    evaluator.plot_llm_judge_scores(llm_judge_results)

    # Save results
    evaluator.save_results(auto_results, llm_judge_results, "evaluation_results")
