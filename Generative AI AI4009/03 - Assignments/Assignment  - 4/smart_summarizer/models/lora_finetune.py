"""
LoRA Fine-tuning for Summarization Model
This script handles LoRA-based fine-tuning of a pre-trained LLM for paper summarization.
"""

import os
import torch
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from tqdm.auto import tqdm
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    TrainingArguments,
    Trainer,
    DataCollatorForSeq2Seq,
    get_scheduler,
)
from peft import prepare_model_for_kbit_training, LoraConfig, get_peft_model, TaskType
from torch.utils.data import DataLoader, TensorDataset
from torch.optim import AdamW


class SummarizerLoraTrainer:
    """A class to handle LoRA fine-tuning of a pre-trained LLM for summarization."""

    def __init__(
        self,
        model_name,
        data_dir,
        output_dir,
        lora_r=8,
        lora_alpha=16,
        lora_dropout=0.1,
        device=None,
    ):
        """
        Initialize the trainer.

        Args:
            model_name (str): Name of the pre-trained model
            data_dir (str): Directory containing the processed data
            output_dir (str): Directory to save the fine-tuned model
            lora_r (int): LoRA rank
            lora_alpha (int): LoRA alpha parameter
            lora_dropout (float): Dropout probability for LoRA layers
            device (str): Device to use for training ('cuda' or 'cpu')
        """
        self.model_name = model_name
        self.data_dir = data_dir
        self.output_dir = output_dir
        self.lora_r = lora_r
        self.lora_alpha = lora_alpha
        self.lora_dropout = lora_dropout

        # Set device
        self.device = (
            device if device else ("cuda" if torch.cuda.is_available() else "cpu")
        )
        print(f"Using device: {self.device}")

        # Initialize tokenizer and model
        self.tokenizer = None
        self.model = None
        self.peft_model = None

        # Training history
        self.train_losses = []
        self.val_losses = []

    def load_data(self):
        """Load the preprocessed data splits."""
        print("Loading preprocessed data...")

        # Load train, validation, and test data
        splits = {}
        for split_name in ["train", "validation", "test"]:
            split_dir = os.path.join(self.data_dir, split_name)
            split_data = {}

            for key in ["input_ids", "attention_mask", "labels"]:
                file_path = os.path.join(split_dir, f"{key}.pt")
                split_data[key] = torch.load(file_path)

            splits[split_name] = split_data

        self.train_data = splits["train"]
        self.val_data = splits["validation"]
        self.test_data = splits["test"]

        print(f"Loaded {len(self.train_data['input_ids'])} training samples")
        print(f"Loaded {len(self.val_data['input_ids'])} validation samples")
        print(f"Loaded {len(self.test_data['input_ids'])} test samples")

        return splits

    def setup_model(self):
        """Set up the pre-trained model with LoRA integration."""
        print("Loading pre-trained model and tokenizer...")

        # Load tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)

        # Ensure the tokenizer has padding and EOS tokens
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token

        # Load model with quantization for efficiency
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_name,
            load_in_8bit=True,  # Use 8-bit quantization
            device_map="auto",
            torch_dtype=torch.float16,
        )

        # Prepare model for k-bit training
        self.model = prepare_model_for_kbit_training(self.model)

        # Define LoRA configuration
        lora_config = LoraConfig(
            r=self.lora_r,  # Rank
            lora_alpha=self.lora_alpha,  # Alpha parameter
            lora_dropout=self.lora_dropout,  # Dropout probability
            bias="none",  # Don't apply LoRA to bias terms
            task_type=TaskType.CAUSAL_LM,  # Task type (causal language modeling)
            target_modules=[
                "q_proj",
                "v_proj",
            ],  # Only apply LoRA to query and value projection matrices
        )

        # Apply LoRA to the model
        self.peft_model = get_peft_model(self.model, lora_config)

        # Print trainable parameters info
        self.print_trainable_parameters()

        return self.peft_model

    def print_trainable_parameters(self):
        """Print the number of trainable parameters in the model."""
        trainable_params = 0
        all_params = 0

        for _, param in self.peft_model.named_parameters():
            num_params = param.numel()
            all_params += num_params
            if param.requires_grad:
                trainable_params += num_params

        print(f"Total parameters: {all_params:,}")
        print(f"Trainable parameters: {trainable_params:,}")
        print(
            f"Percentage of trainable parameters: {100 * trainable_params / all_params:.4f}%"
        )

    def create_dataloaders(self, batch_size=8):
        """Create dataloaders for training and validation."""
        print("Creating dataloaders...")

        # Create tensor datasets
        train_dataset = TensorDataset(
            self.train_data["input_ids"],
            self.train_data["attention_mask"],
            self.train_data["labels"],
        )

        val_dataset = TensorDataset(
            self.val_data["input_ids"],
            self.val_data["attention_mask"],
            self.val_data["labels"],
        )

        # Create dataloaders
        self.train_dataloader = DataLoader(
            train_dataset, batch_size=batch_size, shuffle=True
        )

        self.val_dataloader = DataLoader(
            val_dataset, batch_size=batch_size, shuffle=False
        )

        return self.train_dataloader, self.val_dataloader

    def train(
        self,
        epochs=5,
        batch_size=8,
        learning_rate=2e-4,
        weight_decay=0.01,
        grad_accumulation_steps=8,
    ):
        """
        Train the model using LoRA for efficient fine-tuning.

        Args:
            epochs (int): Number of training epochs
            batch_size (int): Batch size for training
            learning_rate (float): Learning rate
            weight_decay (float): Weight decay for regularization
            grad_accumulation_steps (int): Number of gradient accumulation steps
        """
        print("Starting training...")

        # Create dataloaders
        self.create_dataloaders(batch_size=batch_size)

        # Set up optimizer
        optimizer = AdamW(
            self.peft_model.parameters(), lr=learning_rate, weight_decay=weight_decay
        )

        # Set up learning rate scheduler
        total_steps = len(self.train_dataloader) * epochs // grad_accumulation_steps
        lr_scheduler = get_scheduler(
            name="cosine",
            optimizer=optimizer,
            num_warmup_steps=100,
            num_training_steps=total_steps,
        )

        # Training loop
        self.peft_model.train()

        for epoch in range(epochs):
            print(f"\nEpoch {epoch+1}/{epochs}")

            # Training phase
            self.peft_model.train()
            train_loss = 0
            train_steps = 0

            progress_bar = tqdm(self.train_dataloader, desc=f"Training epoch {epoch+1}")

            for step, batch in enumerate(progress_bar):
                batch = tuple(t.to(self.device) for t in batch)
                input_ids, attention_mask, labels = batch

                # Forward pass
                outputs = self.peft_model(
                    input_ids=input_ids, attention_mask=attention_mask, labels=labels
                )

                loss = outputs.loss / grad_accumulation_steps
                loss.backward()

                train_loss += loss.item() * grad_accumulation_steps
                train_steps += 1

                # Update parameters after accumulating gradients
                if (step + 1) % grad_accumulation_steps == 0 or step == len(
                    self.train_dataloader
                ) - 1:
                    optimizer.step()
                    lr_scheduler.step()
                    optimizer.zero_grad()

                # Update progress bar
                progress_bar.set_postfix(
                    {"loss": loss.item() * grad_accumulation_steps}
                )

            # Calculate average training loss for the epoch
            avg_train_loss = train_loss / train_steps
            self.train_losses.append(avg_train_loss)

            # Validation phase
            self.peft_model.eval()
            val_loss = 0
            val_steps = 0

            with torch.no_grad():
                progress_bar = tqdm(
                    self.val_dataloader, desc=f"Validation epoch {epoch+1}"
                )

                for batch in progress_bar:
                    batch = tuple(t.to(self.device) for t in batch)
                    input_ids, attention_mask, labels = batch

                    # Forward pass
                    outputs = self.peft_model(
                        input_ids=input_ids,
                        attention_mask=attention_mask,
                        labels=labels,
                    )

                    loss = outputs.loss
                    val_loss += loss.item()
                    val_steps += 1

                    # Update progress bar
                    progress_bar.set_postfix({"loss": loss.item()})

            # Calculate average validation loss for the epoch
            avg_val_loss = val_loss / val_steps
            self.val_losses.append(avg_val_loss)

            print(
                f"Epoch {epoch+1} - Train loss: {avg_train_loss:.4f}, Val loss: {avg_val_loss:.4f}"
            )

            # Save checkpoint after each epoch
            self.save_checkpoint(epoch + 1)

        # Plot training and validation loss curves
        self.plot_loss_curves()

        # Save the fine-tuned model
        self.save_model()

        return self.train_losses, self.val_losses

    def save_checkpoint(self, epoch):
        """Save a checkpoint of the model."""
        checkpoint_dir = os.path.join(self.output_dir, f"checkpoint-epoch-{epoch}")
        os.makedirs(checkpoint_dir, exist_ok=True)

        # Save model checkpoint
        self.peft_model.save_pretrained(checkpoint_dir)

        # Save training and validation losses
        loss_data = {"train_losses": self.train_losses, "val_losses": self.val_losses}
        torch.save(loss_data, os.path.join(checkpoint_dir, "loss_history.pt"))

        print(f"Checkpoint saved at {checkpoint_dir}")

    def save_model(self):
        """Save the final fine-tuned model."""
        final_model_dir = os.path.join(self.output_dir, "final_model")
        os.makedirs(final_model_dir, exist_ok=True)

        # Save the model
        self.peft_model.save_pretrained(final_model_dir)

        # Save the tokenizer
        self.tokenizer.save_pretrained(final_model_dir)

        # Save model info
        model_info = {
            "base_model": self.model_name,
            "lora_r": self.lora_r,
            "lora_alpha": self.lora_alpha,
            "lora_dropout": self.lora_dropout,
            "train_losses": self.train_losses,
            "val_losses": self.val_losses,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        torch.save(model_info, os.path.join(final_model_dir, "model_info.pt"))

        print(f"Final model saved at {final_model_dir}")

    def plot_loss_curves(self):
        """Plot training and validation loss curves."""
        plt.figure(figsize=(10, 6))
        plt.plot(self.train_losses, label="Training Loss")
        plt.plot(self.val_losses, label="Validation Loss")
        plt.xlabel("Epoch")
        plt.ylabel("Loss")
        plt.title("Training and Validation Loss")
        plt.legend()
        plt.grid(True)

        # Save the plot
        os.makedirs(self.output_dir, exist_ok=True)
        plt.savefig(os.path.join(self.output_dir, "loss_curves.png"))
        plt.close()

        print(
            f"Loss curves saved to {os.path.join(self.output_dir, 'loss_curves.png')}"
        )

    def generate_summary(self, text, max_new_tokens=256):
        """
        Generate a summary for the given text using the fine-tuned model.

        Args:
            text (str): Text to summarize
            max_new_tokens (int): Maximum number of tokens to generate

        Returns:
            str: Generated summary
        """
        # Tokenize the input text
        inputs = self.tokenizer(
            text, return_tensors="pt", truncation=True, max_length=1024
        )
        inputs = {k: v.to(self.device) for k, v in inputs.items()}

        # Generate summary
        with torch.no_grad():
            outputs = self.peft_model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                temperature=0.7,
                top_p=0.9,
                num_beams=4,
                do_sample=True,
                pad_token_id=self.tokenizer.pad_token_id,
                eos_token_id=self.tokenizer.eos_token_id,
            )

        # Decode the generated text
        summary = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        return summary


if __name__ == "__main__":
    # Example usage
    model_name = "meta-llama/Llama-3-8B"  # Replace with the model you want to use
    data_dir = "../data/processed_data"
    output_dir = "./lora_summarizer"

    # Initialize trainer
    trainer = SummarizerLoraTrainer(
        model_name=model_name, data_dir=data_dir, output_dir=output_dir
    )

    # Load data
    trainer.load_data()

    # Set up model
    trainer.setup_model()

    # Train model
    trainer.train(epochs=5, batch_size=8)
