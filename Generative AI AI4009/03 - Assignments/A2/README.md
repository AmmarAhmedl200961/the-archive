# Computer Vision & AI Project Suite

A comprehensive project implementing two cutting-edge computer vision applications: **Face Anti-Spoofing Detection** and **AI-Powered Visual Search** using state-of-the-art deep learning models.

## 🚀 Project Overview

This repository contains two main components:

### 🔒 Part 1: Face Anti-Spoofing Detection
A deep learning solution for detecting face spoofing attacks using Vision Transformer (ViT) architecture. The model can distinguish between real and spoofed faces with high accuracy.

### 🔍 Part 2: AI-Powered Visual Search
An intelligent image search system powered by CLIP (Contrastive Language-Image Pre-Training) that enables natural language queries to find relevant images in large datasets.

## 📂 Repository Structure

```
├── l200961_A2.ipynb              # Main Jupyter notebook with complete implementation
├── l200961_A2_report.pdf         # Detailed project report
├── generated_images.zip          # Generated/test images for evaluation
└── README.md                     # This file
```

## 🛠️ Features

### Face Anti-Spoofing Detection
- **Model Architecture**: Fine-tuned Vision Transformer (ViT-base-patch16-224)
- **Dataset**: CelebA-Spoof dataset for face anti-spoofing
- **Performance Metrics**: Accuracy, Precision, Recall, F1-Score
- **Training Framework**: PyTorch Lightning with Weights & Biases logging
- **Binary Classification**: Real vs. Spoof face detection

### AI-Powered Visual Search
- **Model**: OpenAI's CLIP (ViT-Base-Patch32)
- **Dataset**: COCO validation dataset (1000+ images)
- **Search Capabilities**: Natural language image queries
- **Features**: Top-K similar image retrieval with confidence scores
- **Demonstrations**: Multiple search examples including:
  - "A person riding a horse"
  - "A dog playing in the snow"
  - "A pizza on a table"
  - "People playing basketball"
  - "A cat sleeping on a couch"

## 🔧 Technology Stack

- **Deep Learning Frameworks**: PyTorch, PyTorch Lightning, Transformers (Hugging Face)
- **Computer Vision**: OpenCV, PIL, matplotlib
- **Data Processing**: NumPy, pandas, scikit-learn
- **Model Architectures**: Vision Transformer (ViT), CLIP
- **Experiment Tracking**: Weights & Biases (wandb)
- **Datasets**: CelebA-Spoof, COCO validation set

## 📊 Model Performance

### Face Anti-Spoofing Detection
- **Training Epochs**: 3
- **Batch Size**: 8
- **Learning Rate**: 2e-5
- **Optimizer**: AdamW
- **Model Size**: 85.8M parameters
- **Metrics**: Comprehensive evaluation with accuracy, precision, recall, and F1-score

### Visual Search System
- **Feature Extraction**: CLIP image and text encoders
- **Similarity Metric**: Cosine similarity
- **Search Results**: Top-5 most relevant images
- **Processing**: Batch processing for efficient encoding

## 🚀 Getting Started

### Prerequisites
```bash
pip install torch torchvision transformers pytorch-lightning
pip install datasets huggingface_hub wandb matplotlib pillow
pip install scikit-learn numpy pandas tqdm wget
```

### Usage

1. **Face Spoofing Detection**:
   ```python
   # Load the trained model
   from transformers import ViTImageProcessor, ViTForImageClassification
   
   processor = ViTImageProcessor.from_pretrained("./vit-face-spoofing-lightning")
   model = ViTForImageClassification.from_pretrained("./vit-face-spoofing-lightning")
   
   # Detect spoofing
   detect_and_plot("path/to/image.jpg")
   ```

2. **Visual Search**:
   ```python
   # Search for images using natural language
   query = "A person riding a horse"
   similarities, images = search_images(query, image_features, dataset)
   plot_results(query, images, similarities)
   ```

## 📈 Results & Visualizations

The project includes comprehensive visualizations:
- **Training Progress**: Loss curves and validation metrics
- **Spoofing Detection**: Side-by-side comparison of input and prediction
- **Search Results**: Top-5 most similar images with confidence scores
- **Model Performance**: Detailed evaluation metrics

## 🎯 Key Achievements

- ✅ Successfully implemented and trained a robust face anti-spoofing detector
- ✅ Built an efficient visual search engine using state-of-the-art CLIP model
- ✅ Achieved high-quality results on both tasks with comprehensive evaluation
- ✅ Demonstrated practical applications with real-world examples
- ✅ Integrated experiment tracking and model versioning

## 📚 Academic Context

This project was developed as part of an advanced computer vision and generative AI course, demonstrating proficiency in:
- Deep learning model fine-tuning and training
- Multi-modal AI systems (vision + language)
- Practical implementation of research papers
- Comprehensive model evaluation and validation

## 🔗 Links & Resources

- **Weights & Biases Project**: [ViT-Celeba Experiments](https://wandb.ai/ammar-90/ViT-Celeba)
- **Models Used**:
  - Vision Transformer: `google/vit-base-patch16-224`
  - CLIP: `openai/clip-vit-base-patch32`
- **Datasets**:
  - CelebA-Spoof: `nguyenkhoa/celeba-spoof-for-face-antispoofing-test`
  - COCO Validation 2017


## 📄 License

This project is developed for academic purposes as part of coursework in Generative AI and Computer Vision.

---

*This project showcases the practical implementation of cutting-edge computer vision techniques, demonstrating both technical proficiency and real-world application potential.*