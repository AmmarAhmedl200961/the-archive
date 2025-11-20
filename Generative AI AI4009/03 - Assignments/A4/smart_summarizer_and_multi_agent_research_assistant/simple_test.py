#!/usr/bin/env python3
"""
Simple test script for API connections.

This script tests the API connections without requiring imports from other files.
"""

import os
import sys
import json
import logging
import requests
import time
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def test_arxiv_api():
    """Test the arXiv API."""
    logger.info("Testing arXiv API...")
    
    query = "machine learning"
    url = f"http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results=2"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        # Simple check for success
        if "<entry>" in response.text:
            logger.info("arXiv API test successful!")
            return True
        else:
            logger.error("arXiv API returned unexpected response")
            logger.debug(f"Response: {response.text[:200]}...")
            return False
    except Exception as e:
        logger.error(f"Error testing arXiv API: {e}")
        return False

def test_semantic_scholar_api():
    """Test the Semantic Scholar API."""
    logger.info("Testing Semantic Scholar API...")
    
    api_key = os.environ.get("SEMANTIC_SCHOLAR_API_KEY", "")
    url = "https://api.semanticscholar.org/graph/v1/paper/search"
    params = {
        "query": "machine learning",
        "limit": 2,
        "fields": "title,authors,abstract,year"
    }
    
    headers = {}
    if api_key:
        headers["x-api-key"] = api_key
    
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        
        data = response.json()
        
        if "data" in data:
            logger.info("Semantic Scholar API test successful!")
            return True
        else:
            logger.error("Semantic Scholar API returned unexpected response")
            logger.debug(f"Response: {data}")
            return False
    except Exception as e:
        logger.error(f"Error testing Semantic Scholar API: {e}")
        return False

def test_together_api():
    """Test the Together.ai API."""
    logger.info("Testing Together.ai API...")
    
    api_key = os.environ.get("TOGETHER_API_KEY", "")
    if not api_key:
        logger.error("Together.ai API key not found in environment variables")
        return False
    
    url = "https://api.together.xyz/v1/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "meta-llama/Llama-3-8B-Instruct",
        "prompt": "Write a one-sentence summary of machine learning.",
        "max_tokens": 100,
        "temperature": 0.7
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        
        result = response.json()
        
        if "choices" in result:
            logger.info("Together.ai API test successful!")
            logger.info(f"Response: {result['choices'][0]['text']}")
            return True
        else:
            logger.error("Together.ai API returned unexpected response")
            logger.debug(f"Response: {result}")
            return False
    except Exception as e:
        logger.error(f"Error testing Together.ai API: {e}")
        return False

def test_pubmed_api():
    """Test the PubMed API."""
    logger.info("Testing PubMed API...")
    
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": "machine learning",
        "retmax": 2,
        "retmode": "json"
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        data = response.json()
        
        if "esearchresult" in data:
            logger.info("PubMed API test successful!")
            return True
        else:
            logger.error("PubMed API returned unexpected response")
            logger.debug(f"Response: {data}")
            return False
    except Exception as e:
        logger.error(f"Error testing PubMed API: {e}")
        return False

def run_api_tests():
    """Run all API tests."""
    print("Testing API connections...")
    
    results = {
        "arxiv": test_arxiv_api(),
        "semantic_scholar": test_semantic_scholar_api(),
        "together": test_together_api(),
        "pubmed": test_pubmed_api()
    }
    
    print("\nTest Results:")
    for api, success in results.items():
        status = "✅ Connected" if success else "❌ Connection failed"
        print(f"  {api}: {status}")
    
    # Check if any test was successful
    if any(results.values()):
        print("\nAt least one API connection was successful.")
        return True
    else:
        print("\nAll API connections failed.")
        return False

def simple_keyword_test():
    """Run a simple test to expand keywords using Together.ai API."""
    print("\nRunning simple keyword expansion test...")
    
    api_key = os.environ.get("TOGETHER_API_KEY", "")
    if not api_key:
        print("Together.ai API key not found. Skipping keyword test.")
        return False
    
    query = "machine learning in healthcare"
    
    url = "https://api.together.xyz/v1/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    prompt = f"""You are an expert research assistant. Given the following research query, generate an expanded list of 5 related keywords and phrases.

Research query: {query}

Please respond with a JSON object in the following format:
{{
  "original_query": "{query}",
  "expanded_keywords": [
    {{"keyword": "first keyword", "relevance": 0.9}},
    {{"keyword": "second keyword", "relevance": 0.8}},
    ... and so on
  ]
}}
"""
    
    data = {
        "model": "meta-llama/Llama-3-8B-Instruct",
        "prompt": prompt,
        "max_tokens": 300,
        "temperature": 0.7
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        
        result = response.json()
        generated_text = result["choices"][0]["text"]
        
        print(f"\nKeyword expansion results:\n{generated_text}")
        return True
    except Exception as e:
        print(f"Error in keyword test: {e}")
        return False

if __name__ == "__main__":
    # Get API keys from environment or user
    if not os.environ.get("TOGETHER_API_KEY"):
        key = input("Enter your Together.ai API key (press Enter to skip): ")
        if key:
            os.environ["TOGETHER_API_KEY"] = key
    
    if not os.environ.get("SEMANTIC_SCHOLAR_API_KEY"):
        key = input("Enter your Semantic Scholar API key (press Enter to skip): ")
        if key:
            os.environ["SEMANTIC_SCHOLAR_API_KEY"] = key
    
    # Run tests
    api_test_success = run_api_tests()
    
    if api_test_success:
        simple_keyword_test()
    
    print("\nTest complete.")