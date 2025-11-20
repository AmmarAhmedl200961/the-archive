#!/usr/bin/env python3
"""
API Configuration for Multi-Agent Research Assistant

This module provides configuration and helper functions for connecting
to various academic paper APIs used by the research assistant.
"""

import os
import json
import logging
from pathlib import Path
from typing import Dict, Any, Optional, List, Union
import requests
import time

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class APIConfig:
    """Configuration for various APIs used by the research assistant."""
    
    def __init__(self, config_file: Optional[str] = None):
        """
        Initialize API configuration.
        
        Args:
            config_file: Path to a JSON configuration file (optional)
        """
        # Default configuration
        self.config = {
            "together": {
                "api_key": os.environ.get("TOGETHER_API_KEY", ""),
                "base_url": "https://api.together.xyz/v1",
                "models": {
                    "llama3_8b": "meta-llama/Llama-3-8B-Instruct",
                    "llama3_70b": "meta-llama/Llama-3.1-70B-Instruct"
                },
                "rate_limit": {
                    "requests_per_minute": 60,
                    "retry_delay": 5
                }
            },
            "semantic_scholar": {
                "api_key": os.environ.get("SEMANTIC_SCHOLAR_API_KEY", ""),
                "base_url": "https://api.semanticscholar.org/graph/v1",
                "rate_limit": {
                    "requests_per_minute": 100,
                    "retry_delay": 2
                }
            },
            "arxiv": {
                "base_url": "http://export.arxiv.org/api/query",
                "rate_limit": {
                    "requests_per_minute": 30,
                    "retry_delay": 3
                }
            },
            "pubmed": {
                "api_key": os.environ.get("PUBMED_API_KEY", ""),
                "base_url": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils",
                "rate_limit": {
                    "requests_per_minute": 10,
                    "retry_delay": 3
                }
            },
            "core": {
                "api_key": os.environ.get("CORE_API_KEY", ""),
                "base_url": "https://api.core.ac.uk/v3",
                "rate_limit": {
                    "requests_per_minute": 30,
                    "retry_delay": 2
                }
            },
            "openai": {
                "api_key": os.environ.get("OPENAI_API_KEY", ""),
                "base_url": "https://api.openai.com/v1",
                "models": {
                    "gpt35": "gpt-3.5-turbo",
                    "gpt4": "gpt-4"
                },
                "rate_limit": {
                    "requests_per_minute": 60,
                    "retry_delay": 5
                }
            }
        }
        
        # Load configuration from file if provided
        if config_file:
            self.load_config(config_file)
        
        # Initialize API wrappers
        self.wrappers = {
            "together": TogetherAPIWrapper(self.config["together"]),
            "semantic_scholar": SemanticScholarWrapper(self.config["semantic_scholar"]),
            "arxiv": ArxivWrapper(self.config["arxiv"]),
            "pubmed": PubMedWrapper(self.config["pubmed"]),
            "core": COREWrapper(self.config["core"])
        }
    
    def load_config(self, config_file: str) -> None:
        """
        Load configuration from a JSON file.
        
        Args:
            config_file: Path to a JSON configuration file
        """
        try:
            with open(config_file, 'r') as f:
                loaded_config = json.load(f)
                
                # Update configuration with loaded values
                for api, settings in loaded_config.items():
                    if api in self.config:
                        self.config[api].update(settings)
                
                logger.info(f"Loaded configuration from {config_file}")
        except Exception as e:
            logger.error(f"Error loading configuration from {config_file}: {e}")
    
    def save_config(self, config_file: str) -> None:
        """
        Save configuration to a JSON file.
        
        Args:
            config_file: Path to save the configuration
        """
        try:
            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(os.path.abspath(config_file)), exist_ok=True)
            
            # Save only non-sensitive information (remove API keys)
            safe_config = {}
            for api, settings in self.config.items():
                safe_config[api] = settings.copy()
                if "api_key" in safe_config[api]:
                    safe_config[api]["api_key"] = "" if not safe_config[api]["api_key"] else "[API KEY SET]"
            
            with open(config_file, 'w') as f:
                json.dump(safe_config, f, indent=2)
                
            logger.info(f"Saved configuration to {config_file}")
        except Exception as e:
            logger.error(f"Error saving configuration to {config_file}: {e}")
    
    def set_api_key(self, api: str, key: str) -> None:
        """
        Set an API key.
        
        Args:
            api: Name of the API (e.g., "together", "semantic_scholar")
            key: API key
        """
        if api in self.config:
            self.config[api]["api_key"] = key
            
            # Also set in environment variables
            os.environ[f"{api.upper()}_API_KEY"] = key
            
            # Update the wrapper if it exists
            if api in self.wrappers:
                self.wrappers[api].config["api_key"] = key
            
            logger.info(f"Set API key for {api}")
        else:
            logger.error(f"Unknown API: {api}")
    
    def get_api_key(self, api: str) -> str:
        """
        Get an API key.
        
        Args:
            api: Name of the API
            
        Returns:
            The API key as a string
        """
        if api in self.config:
            return self.config[api].get("api_key", "")
        else:
            logger.error(f"Unknown API: {api}")
            return ""
    
    def get_wrapper(self, api: str):
        """
        Get an API wrapper.
        
        Args:
            api: Name of the API
            
        Returns:
            The API wrapper object
        """
        return self.wrappers.get(api)

class RateLimiter:
    """Rate limiter for API requests."""
    
    def __init__(self, requests_per_minute: int, retry_delay: int = 2):
        """
        Initialize rate limiter.
        
        Args:
            requests_per_minute: Maximum number of requests per minute
            retry_delay: Delay in seconds before retrying after rate limit is hit
        """
        self.requests_per_minute = requests_per_minute
        self.retry_delay = retry_delay
        self.interval = 60.0 / requests_per_minute
        self.last_request_time = 0
    
    def wait_if_needed(self) -> None:
        """Wait if needed to respect rate limits."""
        current_time = time.time()
        elapsed = current_time - self.last_request_time
        
        if elapsed < self.interval:
            wait_time = self.interval - elapsed
            time.sleep(wait_time)
        
        self.last_request_time = time.time()

class BaseAPIWrapper:
    """Base class for API wrappers."""
    
    def __init__(self, config: Dict[str, Any]):
        """
        Initialize the API wrapper.
        
        Args:
            config: Configuration dictionary
        """
        self.config = config
        self.rate_limiter = RateLimiter(
            config.get("rate_limit", {}).get("requests_per_minute", 60),
            config.get("rate_limit", {}).get("retry_delay", 2)
        )
    
    def _make_request(self, method: str, endpoint: str, params: Dict[str, Any] = None, 
                     headers: Dict[str, str] = None, data: Any = None, json_data: Any = None) -> requests.Response:
        """
        Make an HTTP request to the API.
        
        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint
            params: URL parameters
            headers: HTTP headers
            data: Form data
            json_data: JSON data
            
        Returns:
            Response object
        """
        # Apply rate limiting
        self.rate_limiter.wait_if_needed()
        
        # Create URL
        url = f"{self.config['base_url']}/{endpoint.lstrip('/')}"
        
        # Set default headers
        if headers is None:
            headers = {}
        
        # Add API key to headers if available
        api_key = self.config.get("api_key")
        if api_key and "api_key" not in headers:
            headers["api_key"] = api_key
        
        # Make the request
        try:
            response = requests.request(
                method=method,
                url=url,
                params=params,
                headers=headers,
                data=data,
                json=json_data
            )
            
            # Check for rate limiting errors
            if response.status_code == 429:  # Too Many Requests
                logger.warning(f"Rate limit hit for {url}. Retrying after {self.rate_limiter.retry_delay} seconds.")
                time.sleep(self.rate_limiter.retry_delay)
                return self._make_request(method, endpoint, params, headers, data, json_data)
            
            # Raise for other errors
            response.raise_for_status()
            
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"Error making request to {url}: {e}")
            raise

class TogetherAPIWrapper(BaseAPIWrapper):
    """Wrapper for Together.ai API."""
    
    def complete(self, prompt: str, model: str = None, max_tokens: int = 1024, 
                temperature: float = 0.7, top_p: float = 0.9) -> Dict[str, Any]:
        """
        Generate a completion using the Together.ai API.
        
        Args:
            prompt: Text prompt
            model: Model name (defaults to llama3_8b)
            max_tokens: Maximum number of tokens to generate
            temperature: Sampling temperature
            top_p: Top-p sampling parameter
            
        Returns:
            API response as a dictionary
        """
        # Get the model name
        if model is None:
            model = self.config["models"]["llama3_8b"]
        elif model in self.config["models"]:
            model = self.config["models"][model]
        
        # Prepare the request
        headers = {
            "Authorization": f"Bearer {self.config['api_key']}",
            "Content-Type": "application/json"
        }
        
        json_data = {
            "model": model,
            "prompt": prompt,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "top_p": top_p,
            "top_k": 60,
            "repetition_penalty": 1.1
        }
        
        # Make the request
        try:
            response = self._make_request(
                method="POST",
                endpoint="/completions",
                headers=headers,
                json_data=json_data
            )
            
            return response.json()
        except Exception as e:
            logger.error(f"Error calling Together.ai API: {e}")
            return {"error": str(e)}

class SemanticScholarWrapper(BaseAPIWrapper):
    """Wrapper for Semantic Scholar API."""
    
    def search(self, query: str, limit: int = 10, fields: List[str] = None) -> Dict[str, Any]:
        """
        Search for papers on Semantic Scholar.
        
        Args:
            query: Search query
            limit: Maximum number of results
            fields: Fields to include in the response
            
        Returns:
            Search results as a dictionary
        """
        # Default fields if not specified
        if fields is None:
            fields = ["title", "authors", "abstract", "year", "url", "citationCount", "influentialCitationCount"]
        
        # Prepare parameters
        params = {
            "query": query,
            "limit": limit,
            "fields": ",".join(fields)
        }
        
        # Set headers
        headers = {}
        if self.config.get("api_key"):
            headers["x-api-key"] = self.config["api_key"]
        
        # Make the request
        try:
            response = self._make_request(
                method="GET",
                endpoint="/paper/search",
                params=params,
                headers=headers
            )
            
            return response.json()
        except Exception as e:
            logger.error(f"Error searching Semantic Scholar: {e}")
            return {"error": str(e), "data": []}
    
    def get_paper(self, paper_id: str, fields: List[str] = None) -> Dict[str, Any]:
        """
        Get details of a paper by ID.
        
        Args:
            paper_id: Semantic Scholar paper ID
            fields: Fields to include in the response
            
        Returns:
            Paper details as a dictionary
        """
        # Default fields if not specified
        if fields is None:
            fields = ["title", "authors", "abstract", "year", "url", "citations", "references", "tldr"]
        
        # Prepare parameters
        params = {
            "fields": ",".join(fields)
        }
        
        # Set headers
        headers = {}
        if self.config.get("api_key"):
            headers["x-api-key"] = self.config["api_key"]
        
        # Make the request
        try:
            response = self._make_request(
                method="GET",
                endpoint=f"/paper/{paper_id}",
                params=params,
                headers=headers
            )
            
            return response.json()
        except Exception as e:
            logger.error(f"Error getting paper from Semantic Scholar: {e}")
            return {"error": str(e)}

class ArxivWrapper(BaseAPIWrapper):
    """Wrapper for arXiv API."""
    
    def search(self, query: str, max_results: int = 10, start: int = 0, 
              sort_by: str = "relevance", sort_order: str = "descending") -> Dict[str, Any]:
        """
        Search for papers on arXiv.
        
        Args:
            query: Search query
            max_results: Maximum number of results
            start: Start index
            sort_by: Sort criterion (relevance, lastUpdatedDate, submittedDate)
            sort_order: Sort order (ascending, descending)
            
        Returns:
            Search results as a dictionary
        """
        # Prepare parameters
        params = {
            "search_query": f"all:{query}",
            "start": start,
            "max_results": max_results,
            "sortBy": sort_by,
            "sortOrder": sort_order
        }
        
        # Make the request
        try:
            response = self._make_request(
                method="GET",
                endpoint="",  # arXiv API doesn't have endpoints
                params=params
            )
            
            # Parse XML response
            import feedparser
            feed = feedparser.parse(response.content)
            
            # Convert to a dictionary
            results = {
                "totalResults": len(feed.entries),
                "startIndex": start,
                "itemsPerPage": max_results,
                "items": []
            }
            
            for entry in feed.entries:
                # Extract authors
                authors = []
                for author in entry.get("authors", []):
                    if "name" in author:
                        authors.append({"name": author["name"]})
                
                # Extract the PDF URL
                pdf_url = None
                for link in entry.get("links", []):
                    if link.get("type") == "application/pdf":
                        pdf_url = link.get("href")
                        break
                
                # Create item
                item = {
                    "id": entry.get("id", "").split("/")[-1],
                    "title": entry.get("title", ""),
                    "abstract": entry.get("summary", ""),
                    "authors": authors,
                    "published": entry.get("published", ""),
                    "updated": entry.get("updated", ""),
                    "pdf_url": pdf_url,
                    "arxiv_url": entry.get("link", "")
                }
                
                results["items"].append(item)
            
            return results
        except Exception as e:
            logger.error(f"Error searching arXiv: {e}")
            return {"error": str(e), "items": []}

class PubMedWrapper(BaseAPIWrapper):
    """Wrapper for PubMed API."""
    
    def search(self, query: str, max_results: int = 10, retstart: int = 0) -> Dict[str, Any]:
        """
        Search for papers on PubMed.
        
        Args:
            query: Search query
            max_results: Maximum number of results
            retstart: Start index
            
        Returns:
            Search results as a dictionary
        """
        # Prepare parameters for esearch
        params = {
            "db": "pubmed",
            "term": query,
            "retmax": max_results,
            "retstart": retstart,
            "retmode": "json",
            "sort": "relevance"
        }
        
        if self.config.get("api_key"):
            params["api_key"] = self.config["api_key"]
        
        # Make the esearch request
        try:
            response = self._make_request(
                method="GET",
                endpoint="/esearch.fcgi",
                params=params
            )
            
            search_result = response.json()
            id_list = search_result.get("esearchresult", {}).get("idlist", [])
            
            if not id_list:
                return {"count": 0, "articles": []}
            
            # Prepare parameters for efetch
            fetch_params = {
                "db": "pubmed",
                "id": ",".join(id_list),
                "retmode": "xml",
                "rettype": "abstract"
            }
            
            if self.config.get("api_key"):
                fetch_params["api_key"] = self.config["api_key"]
            
            # Make the efetch request
            fetch_response = self._make_request(
                method="GET",
                endpoint="/efetch.fcgi",
                params=fetch_params
            )
            
            # Parse XML response
            import xml.etree.ElementTree as ET
            root = ET.fromstring(fetch_response.content)
            
            # Convert to a dictionary
            articles = []
            
            for article_node in root.findall(".//PubmedArticle"):
                # Extract article data
                pmid = article_node.find(".//PMID").text if article_node.find(".//PMID") is not None else ""
                
                title_node = article_node.find(".//ArticleTitle")
                title = title_node.text if title_node is not None else ""
                
                abstract_nodes = article_node.findall(".//AbstractText")
                abstract = " ".join(node.text for node in abstract_nodes if node.text) if abstract_nodes else ""
                
                # Extract authors
                authors = []
                for author_node in article_node.findall(".//Author"):
                    last_name = author_node.find("LastName")
                    fore_name = author_node.find("ForeName")
                    
                    if last_name is not None and fore_name is not None:
                        authors.append({
                            "name": f"{fore_name.text} {last_name.text}"
                        })
                
                # Extract year
                year_node = article_node.find(".//PubDate/Year")
                year = year_node.text if year_node is not None else ""
                
                # Create article object
                article = {
                    "id": pmid,
                    "title": title,
                    "abstract": abstract,
                    "authors": authors,
                    "year": year,
                    "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
                }
                
                articles.append(article)
            
            return {
                "count": len(articles),
                "articles": articles
            }
        except Exception as e:
            logger.error(f"Error searching PubMed: {e}")
            return {"error": str(e), "articles": []}

class COREWrapper(BaseAPIWrapper):
    """Wrapper for CORE API."""
    
    def search(self, query: str, limit: int = 10, offset: int = 0) -> Dict[str, Any]:
        """
        Search for papers on CORE.
        
        Args:
            query: Search query
            limit: Maximum number of results
            offset: Start index
            
        Returns:
            Search results as a dictionary
        """
        # Prepare the request
        headers = {
            "Authorization": f"Bearer {self.config.get('api_key', '')}",
            "Content-Type": "application/json"
        }
        
        json_data = {
            "q": query,
            "limit": limit,
            "offset": offset,
            "stats": True
        }
        
        # Make the request
        try:
            response = self._make_request(
                method="POST",
                endpoint="/search/works",
                headers=headers,
                json_data=json_data
            )
            
            return response.json()
        except Exception as e:
            logger.error(f"Error searching CORE: {e}")
            return {"error": str(e), "results": []}

# Initialize default configuration
api_config = APIConfig()

# Function to get API key from environment or prompt
def get_api_key(api_name: str, prompt: bool = True) -> str:
    """
    Get an API key from environment or prompt the user.
    
    Args:
        api_name: Name of the API
        prompt: Whether to prompt the user if the key is not found
        
    Returns:
        API key as a string
    """
    # Try to get from environment
    key = os.environ.get(f"{api_name.upper()}_API_KEY", "")
    
    # Prompt if needed
    if not key and prompt:
        try:
            key = input(f"Enter your {api_name} API key: ")
            if key:
                os.environ[f"{api_name.upper()}_API_KEY"] = key
        except:
            pass
    
    return key

# Function to test API connections
def test_api_connections(config: APIConfig) -> Dict[str, bool]:
    """
    Test connections to all configured APIs.
    
    Args:
        config: API configuration object
        
    Returns:
        Dictionary mapping API names to connection status
    """
    results = {}
    
    # Test Together.ai API
    if config.get_api_key("together"):
        try:
            wrapper = config.get_wrapper("together")
            response = wrapper.complete("Hello, world!", max_tokens=10)
            results["together"] = "error" not in response
        except Exception as e:
            logger.error(f"Error testing Together.ai API: {e}")
            results["together"] = False
    else:
        results["together"] = None  # API key not provided
    
    # Test Semantic Scholar API
    try:
        wrapper = config.get_wrapper("semantic_scholar")
        response = wrapper.search("machine learning", limit=1)
        results["semantic_scholar"] = "error" not in response
    except Exception as e:
        logger.error(f"Error testing Semantic Scholar API: {e}")
        results["semantic_scholar"] = False
    
    # Test arXiv API
    try:
        wrapper = config.get_wrapper("arxiv")
        response = wrapper.search("machine learning", max_results=1)
        results["arxiv"] = "error" not in response
    except Exception as e:
        logger.error(f"Error testing arXiv API: {e}")
        results["arxiv"] = False
    
    # Test PubMed API
    try:
        wrapper = config.get_wrapper("pubmed")
        response = wrapper.search("machine learning", max_results=1)
        results["pubmed"] = "error" not in response
    except Exception as e:
        logger.error(f"Error testing PubMed API: {e}")
        results["pubmed"] = False
    
    # Test CORE API
    if config.get_api_key("core"):
        try:
            wrapper = config.get_wrapper("core")
            response = wrapper.search("machine learning", limit=1)
            results["core"] = "error" not in response
        except Exception as e:
            logger.error(f"Error testing CORE API: {e}")
            results["core"] = False
    else:
        results["core"] = None  # API key not provided
    
    return results

if __name__ == "__main__":
    # Create configuration
    config = APIConfig()
    
    # Get API keys
    for api in ["together", "semantic_scholar", "pubmed", "core"]:
        key = get_api_key(api)
        if key:
            config.set_api_key(api, key)
    
    # Test connections
    print("Testing API connections...")
    results = test_api_connections(config)
    
    # Print results
    print("\nAPI Connection Status:")
    for api, status in results.items():
        if status is None:
            print(f"  {api}: Not tested (API key not provided)")
        elif status:
            print(f"  {api}: ✅ Connected")
        else:
            print(f"  {api}: ❌ Connection failed")
    
    # Save configuration
    config.save_config("api_config.json")