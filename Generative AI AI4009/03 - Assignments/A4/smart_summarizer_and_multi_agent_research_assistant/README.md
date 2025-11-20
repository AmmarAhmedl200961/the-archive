# Smart Summarizer and Multi-Agent Research Assistant

This project implements an intelligent summarization system by fine-tuning a Large Language Model (LLM) using Low-Rank Adaptation (LoRA) to understand and summarize academic research papers. Additionally, it creates a multi-agent autonomous research assistant that can retrieve, rank, summarize, and compare academic papers.

## Project Structure

The project consists of two main components:

1. **Smart Summarizer**: A fine-tuned LLM that can generate accurate and readable summaries of academic papers.
2. **Multi-Agent Research Assistant**: A system built with LangGraph/LangChain that automates the academic research process.

## Environment Setup

### Requirements

- Python 3.8+
- PyTorch 2.0+
- CUDA-compatible GPU (recommended for fine-tuning)
- Together.ai API key (for LLM-as-a-Judge evaluation)

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/smart-summarizer.git
   cd smart-summarizer
   ```

2. Run the environment setup script:
   ```bash
   chmod +x setup_environment.sh
   ./setup_environment.sh
   ```

3. Activate the virtual environment:
   ```bash
   source smartsummarizer_env/bin/activate
   ```

4. Set up your Together.ai API key:
   ```bash
   python together_api_setup.py --save
   ```

5. Check your hardware configuration:
   ```bash
   python check_gpu.py
   ```

6. Configure hardware settings for training:
   ```bash
   python hardware_config.py
   ```

## Smart Summarizer Implementation

The entire implementation of the Smart Summarizer is contained in a single notebook:

- `smart_summarizer.ipynb`: This notebook includes data preprocessing, model fine-tuning, inference, evaluation, and the Streamlit interface development.

The notebook follows these steps:

1. **Data Preprocessing**: Loading and preparing the arXiv summarization dataset.
2. **LoRA-Based Fine-Tuning**: Fine-tuning a pre-trained LLM (Mistral 7B) using LoRA.
3. **Inference and Output**: Generating summaries using both the fine-tuned and base models.
4. **Model Evaluation**: Evaluating the summaries using both automatic metrics and LLM-as-a-Judge.
5. **Streamlit Interface**: Developing a user-friendly interface for the summarization system.

## Multi-Agent Research Assistant

The Multi-Agent Research Assistant implementation will be provided in a separate notebook:

- `multi_agent_research.ipynb`: This notebook will implement the complete multi-agent system using LangGraph/LangChain.

## Hardware Configuration

The `hardware_config.py` script detects your system's hardware capabilities and provides optimal configuration settings for model fine-tuning. It considers:

- GPU availability and memory
- CPU cores
- Available RAM
- Optimal batch sizes, precision settings, and sequence lengths

The configuration is saved to `hardware_config.json`, which can be loaded in the training notebooks.

## API Configuration

The `together_api_setup.py` script helps you set up and test your Together.ai API key, which is required for the LLM-as-a-Judge evaluation component.

## Running the Streamlit App

After running the Smart Summarizer notebook, you can launch the Streamlit interface:

```bash
streamlit run app.py
```

## Usage

1. Open and run the `smart_summarizer.ipynb` notebook to fine-tune the model and create the summarization system.
2. Use the Streamlit interface to test the summarization system with your own academic papers.
3. Open and run the `multi_agent_research.ipynb` notebook to implement and test the multi-agent research assistant.

## License

[MIT License](LICENSE)

## Acknowledgements

- [arXiv summarization dataset](https://huggingface.co/datasets/ccdv/arxiv-summarization)
- [Mistral AI](https://mistral.ai/) for the Mistral 7B model
- [Meta AI](https://ai.meta.com/) for the LLaMA 3 model
- [LangChain](https://www.langchain.com/) and [LangGraph](https://python.langchain.com/docs/langgraph) for agent orchestration
- [Together.ai](https://www.together.ai/) for LLM-as-a-Judge evaluation