"""
SearchAgent Module
This agent is responsible for searching academic databases to find relevant papers
based on expanded keywords.
"""

import requests
import urllib.parse
import xml.etree.ElementTree as ET
import json
import time
from typing import List, Dict, Any


class SearchAgent:
    """
    Agent for retrieving academic papers from various sources based on keywords.
    Currently supports arXiv, with extensibility for other sources.
    """

    def __init__(self, max_results_per_source=20):
        """
        Initialize the SearchAgent.

        Args:
            max_results_per_source (int): Maximum number of results to fetch per source
        """
        self.max_results_per_source = max_results_per_source

    def search(self, expanded_keywords):
        """
        Search academic sources using expanded keywords.

        Args:
            expanded_keywords (dict): Expanded keywords from KeywordAgent

        Returns:
            dict: Search results from various sources
        """
        results = {}

        # Search arXiv
        arxiv_results = self.search_arxiv(expanded_keywords)
        results["arxiv"] = arxiv_results

        # In a complete implementation, you would add more sources here
        # such as Semantic Scholar, PubMed, etc.

        # Combine all results
        all_results = []
        for source, source_results in results.items():
            for result in source_results:
                result["source"] = source
                all_results.append(result)

        return {
            "query": expanded_keywords.get("original_query", ""),
            "sources_searched": list(results.keys()),
            "total_results": len(all_results),
            "results": all_results,
        }

    def search_arxiv(self, expanded_keywords):
        """
        Search arXiv for papers using expanded keywords.

        Args:
            expanded_keywords (dict): Expanded keywords from KeywordAgent

        Returns:
            list: List of paper metadata from arXiv
        """
        # Extract keywords from different categories
        keywords = []

        # Add core keywords (highest priority)
        if (
            "expanded_keywords" in expanded_keywords
            and "core_keywords" in expanded_keywords["expanded_keywords"]
        ):
            keywords.extend(expanded_keywords["expanded_keywords"]["core_keywords"])

        # Add related keywords
        if (
            "expanded_keywords" in expanded_keywords
            and "related_keywords" in expanded_keywords["expanded_keywords"]
        ):
            keywords.extend(expanded_keywords["expanded_keywords"]["related_keywords"])

        # Add narrower concepts if we need more terms
        if (
            len(keywords) < 5
            and "expanded_keywords" in expanded_keywords
            and "narrower_concepts" in expanded_keywords["expanded_keywords"]
        ):
            keywords.extend(expanded_keywords["expanded_keywords"]["narrower_concepts"])

        # If no expanded keywords, use the original query
        if not keywords and "original_query" in expanded_keywords:
            keywords = [expanded_keywords["original_query"]]

        # Create search query from keywords
        search_query = " AND ".join(
            [f"all:{keyword}" for keyword in keywords[:5]]
        )  # Limit to 5 terms

        # Build arXiv API URL
        base_url = "http://export.arxiv.org/api/query?"
        params = {
            "search_query": search_query,
            "start": 0,
            "max_results": self.max_results_per_source,
            "sortBy": "relevance",
            "sortOrder": "descending",
        }

        query_url = base_url + urllib.parse.urlencode(params)

        try:
            # Fetch results from arXiv API
            response = requests.get(query_url)
            response.raise_for_status()  # Raise an exception for HTTP errors

            # Parse XML response
            return self._parse_arxiv_response(response.content)

        except requests.RequestException as e:
            print(f"Error fetching results from arXiv: {e}")
            return []

    def _parse_arxiv_response(self, xml_content):
        """
        Parse arXiv API XML response into structured paper metadata.

        Args:
            xml_content (bytes): XML content from arXiv API

        Returns:
            list: List of paper dictionaries with metadata
        """
        # Parse XML
        root = ET.fromstring(xml_content)

        # Define namespace
        namespace = {
            "atom": "http://www.w3.org/2005/Atom",
            "arxiv": "http://arxiv.org/schemas/atom",
        }

        # Extract entries
        entries = root.findall(".//atom:entry", namespace)

        results = []
        for entry in entries:
            # Skip if this is the "OpenSearch" entry that describes the search itself
            if entry.find("atom:title", namespace).text == "arXiv Query:":
                continue

            # Extract paper metadata
            paper = {
                "title": entry.find("atom:title", namespace).text.strip(),
                "abstract": entry.find("atom:summary", namespace).text.strip(),
                "authors": [
                    author.find("atom:name", namespace).text
                    for author in entry.findall("atom:author", namespace)
                ],
                "publish_date": entry.find("atom:published", namespace).text.split("T")[
                    0
                ],  # Just get the date part
                "url": next(
                    (
                        link.get("href")
                        for link in entry.findall("atom:link", namespace)
                        if link.get("rel") == "alternate"
                    ),
                    "",
                ),
                "id": entry.find("atom:id", namespace).text,
            }

            # Try to extract categories/topics
            categories = entry.findall("atom:category", namespace)
            if categories:
                paper["categories"] = [cat.get("term") for cat in categories]
            else:
                paper["categories"] = []

            # Try to extract arxiv-specific fields
            arxiv_comment = entry.find("arxiv:comment", namespace)
            if arxiv_comment is not None:
                paper["comment"] = arxiv_comment.text

            results.append(paper)

        return results

    def run(self, inputs):
        """
        Run the search agent with the given inputs.

        Args:
            inputs (dict): Input dictionary containing expanded keywords

        Returns:
            dict: Output dictionary containing search results
        """
        expanded_keywords = inputs.get("expanded_keywords", {})
        if not expanded_keywords:
            return {"error": "No expanded keywords provided", "results": []}

        results = self.search(expanded_keywords)
        return results


if __name__ == "__main__":
    # Example usage
    expanded_keywords = {
        "original_query": "LLMs for academic summarization",
        "expanded_keywords": {
            "core_keywords": ["LLM", "academic summarization", "research papers"],
            "related_keywords": ["natural language processing", "text summarization"],
        },
    }

    agent = SearchAgent(max_results_per_source=10)
    results = agent.run({"expanded_keywords": expanded_keywords})
    print(
        f"Found {results['total_results']} papers from {results['sources_searched']} sources"
    )
