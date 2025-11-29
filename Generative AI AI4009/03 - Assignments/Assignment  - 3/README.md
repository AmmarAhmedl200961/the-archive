# PEFT Techniques Comparison: Transformer Fine-Tuning Study

A comprehensive comparison of Parameter Efficient Fine-Tuning (PEFT) techniques for transformer-based models on sentiment classification tasks.

## 🔍 Overview

This project implements and compares four different fine-tuning approaches for transformer models using the IMDb movie review sentiment classification dataset:

- **Full Fine-Tuning** - Traditional approach updating all model parameters
- **LoRA (Low-Rank Adaptation)** - Efficient fine-tuning using low-rank matrices
- **QLoRA (Quantized LoRA)** - Memory-optimized LoRA with 4-bit quantization
- **Adapter Tuning (IA3)** - Lightweight adaptation using Infused Adapter by Inhibiting and Amplifying Inner Activations

## 🎯 Key Features

- **Comprehensive Benchmarking**: Evaluation across accuracy, training time, memory usage, and parameter efficiency
- **Memory Optimization**: GPU memory tracking and optimization techniques
- **Visualization**: Beautiful comparative charts and performance metrics
- **Production Ready**: Well-documented code with best practices

## 📊 Results Summary

| Method | Accuracy | Trainable Parameters | Training Time | Peak Memory |
|--------|----------|---------------------|---------------|-------------|
| Full Fine-tuning | 100% | 124M+ | 593s | 2,423 MB |
| LoRA | 100% | ~1M | 500s | 926 MB |
| QLoRA | 100% | 739K | 233s | 892 MB |
| IA3 Adapter | 100% | 675K | 517s | 1,239 MB |

## 🚀 Quick Start

### Prerequisites

```bash
pip install transformers datasets evaluate accelerate peft bitsandbytes torch wandb
```

### Usage

1. Clone this repository
2. Open `l200961_A3.ipynb` in Jupyter Notebook or VS Code
3. Run all cells to reproduce the experiments
4. Check the generated comparison charts and metrics

## 🛠️ Technical Implementation

### Model Architecture
- **Base Model**: RoBERTa-base (124M parameters)
- **Task**: Binary sentiment classification
- **Dataset**: IMDb movie reviews (3K training, 2K evaluation samples)

### PEFT Configurations
- **LoRA**: rank=8, alpha=16, dropout=0.1
- **QLoRA**: 4-bit quantization + LoRA adaptation
- **IA3**: Adapter tuning with minimal parameter injection

### Optimization Features
- Gradient checkpointing for memory efficiency
- Mixed precision training
- Dynamic batching with padding
- WandB integration for experiment tracking

## 📈 Key Findings

1. **Performance**: All PEFT methods achieved perfect accuracy (100%) on the test set
2. **Efficiency**: PEFT techniques reduced trainable parameters by 100x while maintaining performance
3. **Memory**: QLoRA achieved the lowest memory footprint (892 MB vs 2,423 MB for full fine-tuning)
4. **Speed**: QLoRA was the fastest training method (233s vs 593s for full fine-tuning)

## 🎨 Visualizations

The notebook generates comprehensive comparison charts including:
- Accuracy comparison across methods
- Trainable parameters (log scale)
- Training time analysis
- Peak memory usage visualization

## 📁 Repository Structure

```
├── l200961_A3.ipynb           # Main experiment notebook
├── PEFT_Report.pdf            # Detailed technical report
└── README.md                  # This file
```

## 🔬 Research Implications

This study demonstrates that Parameter Efficient Fine-Tuning techniques can:
- Maintain model performance while drastically reducing computational requirements
- Enable fine-tuning of large models on consumer hardware
- Provide practical solutions for resource-constrained environments
- Achieve faster training times with minimal accuracy trade-offs

## 💡 Applications

- **Resource-Constrained Environments**: Deploy large models on limited hardware
- **Multi-Task Learning**: Efficiently adapt models for multiple downstream tasks
- **Rapid Prototyping**: Quick experimentation with different model configurations
- **Cost Optimization**: Reduce training costs in production environments

## 🤝 Contributing

This is an academic project, but feedback and suggestions are welcome. Please feel free to open issues or submit pull requests.

## 📄 License

This project is for educational purposes. Please cite appropriately if using for research.

---

*Built with ❤️ using PyTorch, Transformers, and PEFT*
