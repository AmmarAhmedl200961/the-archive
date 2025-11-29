"""
Data Preprocessing for arXiv Summarization Dataset
This script handles loading, preprocessing, and splitting the arXiv dataset for fine-tuning.
"""

import os
import numpy as np
import pandas as pd
from datasets import load_dataset
from transformers import AutoTokenizer
from sklearn.model_selection import train_test_split
import torch
from tqdm import tqdm


def load_arxiv_dataset(subset_size=5000, random_seed=42):
    """
    Load the arXiv summarization dataset and select a subset of samples.

    Args:
        subset_size (int): Number of samples to select from the dataset
        random_seed (int): Random seed for reproducibility

    Returns:
        dataset: HuggingFace dataset object containing the selected samples
    """
    print("Loading arXiv summarization dataset...")
    # Load the dataset from Hugging Face
    dataset = load_dataset("ccdv/arxiv-summarization")

    # Select a subset of samples
    if subset_size and subset_size < len(dataset["train"]):
        # Set random seed for reproducibility
        np.random.seed(random_seed)

        # Sample indices
        indices = np.random.choice(len(dataset["train"]), subset_size, replace=False)

        # Select the samples
        subset = dataset["train"].select(indices)
        print(f"Selected {len(subset)} samples from the dataset.")
        return subset
    else:
        print(f"Using the entire dataset with {len(dataset['train'])} samples.")
        return dataset["train"]


def prepare_dataset(dataset, tokenizer, max_input_length=1024, max_target_length=256):
    """
    Prepare the dataset for training by extracting input and target texts and tokenizing them.

    Args:
        dataset: Dataset to prepare
        tokenizer: Tokenizer to use for tokenization
        max_input_length (int): Maximum input sequence length
        max_target_length (int): Maximum target sequence length

    Returns:
        inputs: Tokenized input sequences
        targets: Tokenized target sequences
    """
    print("Extracting input and target texts...")
    inputs = []
    targets = []

    for item in tqdm(dataset, desc="Processing samples"):
        # Extract article text as input
        input_text = item["article"]

        # Extract abstract as target
        target_text = item["abstract"]

        inputs.append(input_text)
        targets.append(target_text)

    print("Tokenizing inputs and targets...")
    # Tokenize inputs
    tokenized_inputs = tokenizer(
        inputs,
        max_length=max_input_length,
        padding="max_length",
        truncation=True,
        return_tensors="pt",
    )

    # Tokenize targets
    tokenized_targets = tokenizer(
        targets,
        max_length=max_target_length,
        padding="max_length",
        truncation=True,
        return_tensors="pt",
    )

    # Prepare labels for the model
    labels = tokenized_targets["input_ids"].clone()
    # Replace padding token id's with -100 so they are ignored in the loss
    labels[labels == tokenizer.pad_token_id] = -100

    return {
        "input_ids": tokenized_inputs["input_ids"],
        "attention_mask": tokenized_inputs["attention_mask"],
        "labels": labels,
    }


def split_dataset(
    dataset, train_size=0.8, val_size=0.1, test_size=0.1, random_state=42
):
    """
    Split the dataset into training, validation, and test sets.

    Args:
        dataset: HuggingFace Dataset object with 'article' and 'abstract' fields
        train_size (float): Proportion of data for training
        val_size (float): Proportion of data for validation
        test_size (float): Proportion of data for testing
        random_state (int): Random seed for reproducibility

    Returns:
        dict: Dictionary containing the split datasets
    """
    print("Splitting dataset into train, validation, and test sets...")

    # Get the total number of samples
    num_samples = len(dataset)

    # Generate indices for the splits
    indices = np.arange(num_samples)

    # First split: separate out test set
    train_val_indices, test_indices = train_test_split(
        indices, test_size=test_size, random_state=random_state
    )

    # Second split: separate train set from validation set
    # Calculate the validation proportion relative to the remaining data
    relative_val_size = val_size / (train_size + val_size)

    train_indices, val_indices = train_test_split(
        train_val_indices, test_size=relative_val_size, random_state=random_state
    )

    # Create the split datasets using 'article' and 'abstract'
    splits = {}
    splits["train"] = dataset.select(train_indices)
    splits["validation"] = dataset.select(val_indices)
    splits["test"] = dataset.select(test_indices)

    print(f"Train set: {len(splits['train'])} samples")
    print(f"Validation set: {len(splits['validation'])} samples")
    print(f"Test set: {len(splits['test'])} samples")

    return splits


def save_splits(splits, output_dir):
    """
    Save the split datasets to disk.

    Args:
        splits (dict): Dictionary containing the split datasets
        output_dir (str): Directory to save the splits to
    """
    print(f"Saving splits to {output_dir}...")
    os.makedirs(output_dir, exist_ok=True)

    # Save each split as a PyTorch tensor
    for split_name, split_data in splits.items():
        split_dir = os.path.join(output_dir, split_name)
        os.makedirs(split_dir, exist_ok=True)

        for key, tensor in split_data.items():
            torch.save(tensor, os.path.join(split_dir, f"{key}.pt"))

    print("Splits saved successfully.")


def preprocess_arxiv_dataset(model_name, subset_size=5000, output_dir="processed_data"):
    """
    Main function to preprocess the arXiv dataset.

    Args:
        model_name (str): Name of the model to use for tokenization
        subset_size (int): Number of samples to select from the dataset
        output_dir (str): Directory to save the processed data to
    """
    # Load the tokenizer for the specified model
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Ensure the tokenizer has padding and EOS tokens
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    # Load the dataset
    dataset = load_arxiv_dataset(subset_size=subset_size)

    # Prepare the dataset for training
    tokenized_dataset = prepare_dataset(dataset, tokenizer)

    # Split the dataset
    splits = split_dataset(tokenized_dataset)

    # Save the splits
    save_splits(splits, output_dir)

    return tokenizer, splits


if __name__ == "__main__":
    # Example usage
    model_name = "meta-llama/Llama-3-8B"  # Replace with the model you want to use
    preprocess_arxiv_dataset(model_name, subset_size=5000)
