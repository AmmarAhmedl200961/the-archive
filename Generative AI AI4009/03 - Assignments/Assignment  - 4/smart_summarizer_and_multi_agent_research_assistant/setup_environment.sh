#!/bin/bash

# Exit script on error
set -e

echo "Setting up environment for Smart Summarizer and Multi-Agent Research Assistant..."

# Create and activate a virtual environment
echo "Creating virtual environment..."
python3 -m venv smartsummarizer_env
source smartsummarizer_env/bin/activate

# Install required packages
echo "Installing required packages..."
pip install --upgrade pip
pip install -r requirements.txt

# Check for GPU availability
if python -c "import torch; print(torch.cuda.is_available())"; then
    echo "GPU is available for computation."
    # Install CUDA-specific packages if necessary
    pip install flash-attn --no-build-isolation
else
    echo "WARNING: No GPU detected. Fine-tuning a 7B parameter model will be very slow on CPU."
    echo "Consider using a machine with GPU acceleration."
fi

# Setup Together.ai API environment
echo "Setting up Together.ai API..."
echo "export TOGETHER_API_KEY=\"YOUR_API_KEY_HERE\"" >> ~/.bashrc
echo ""
echo "NOTE: Please replace 'YOUR_API_KEY_HERE' in ~/.bashrc with your actual Together.ai API key."
echo "You can get a free API key with $1 credit at https://www.together.ai/"

# Create directories for saved models and outputs
echo "Creating directories for models and outputs..."
mkdir -p models
mkdir -p outputs
mkdir -p logs

echo ""
echo "Environment setup complete!"
echo "To activate the environment, run: source smartsummarizer_env/bin/activate"
echo "Before running the notebooks, make sure to set your Together.ai API key."