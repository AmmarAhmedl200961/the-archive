"""
RankAgent Module
This agent is responsible for scoring and ranking retrieved papers based on multiple criteria.
"""

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
import together
from datetime import datetime
import numpy as np


class RankAgent:
    """
    Agent for ranking papers based on relevance, citation count, recency, and other factors.
    Uses a multi-criteria ranking approach and LLM-based relevance assessment.
    """

    def __init__(self, model="meta-llama/Llama-3-8B-hf", api_key=None):
        """
        Initialize the RankAgent.

        Args:
            model (str): Model ID to use for relevance assessment
            api_key (str): API key for LLM service (e.g., Together.ai)
        """
        self.model = model
        self.api_key = api_key
        self.client = None

        if api_key:
            self.client = together.Together(api_key=api_key)

        # Ranking weights for different criteria
        self.weights = {
            "relevance_score": 0.6,  # LLM-based relevance assessment
            "recency_score": 0.2,  # How recent the paper is
            "citation_score": 0.2,  # Estimated by author count and categories
        }

    def rank_papers(self, search_results, expanded_keywords):
        """
        Rank papers based on multiple criteria.

        Args:
            search_results (dict): Search results from the SearchAgent
            expanded_keywords (dict): Expanded keywords from the KeywordAgent

        Returns:
            dict: Ranked papers with scores
        """
        if "results" not in search_results or not search_results["results"]:
            return {
                "query": search_results.get("query", ""),
                "ranked_papers": [],
                "error": "No papers found in search results",
            }

        # Extract papers from search results
        papers = search_results["results"]

        # Rank each paper
        ranked_papers = []

        for paper in papers:
            # Calculate scores for different criteria
            recency_score = self._calculate_recency_score(paper.get("publish_date", ""))
            citation_score = self._estimate_citation_score(paper)
            relevance_score = self._calculate_relevance_score(paper, expanded_keywords)

            # Calculate overall score
            overall_score = (
                self.weights["relevance_score"] * relevance_score
                + self.weights["recency_score"] * recency_score
                + self.weights["citation_score"] * citation_score
            )

            # Add scores to paper
            ranked_paper = paper.copy()
            ranked_paper.update(
                {
                    "scores": {
                        "relevance": relevance_score,
                        "recency": recency_score,
                        "citation_estimate": citation_score,
                        "overall": overall_score,
                    }
                }
            )

            ranked_papers.append(ranked_paper)

        # Sort papers by overall score (descending)
        ranked_papers.sort(key=lambda p: p["scores"]["overall"], reverse=True)

        return {
            "query": search_results.get("query", ""),
            "original_count": len(papers),
            "ranked_papers": ranked_papers,
        }

    def _calculate_recency_score(self, publish_date_str):
        """
        Calculate a score based on how recent the paper is.

        Args:
            publish_date_str (str): Publish date string (YYYY-MM-DD)

        Returns:
            float: Recency score (0.0 to 1.0)
        """
        try:
            # Parse publish date
            publish_date = datetime.strptime(publish_date_str, "%Y-%m-%d")

            # Current date
            current_date = datetime.now()

            # Calculate years since publication
            years_diff = (current_date - publish_date).days / 365

            # Score decreases with age (exponential decay)
            recency_score = np.exp(-0.5 * years_diff)  # Half-life of 2 years

            # Ensure score is between 0 and 1
            return max(0.0, min(1.0, recency_score))

        except (ValueError, TypeError):
            # Default to middle score if date is invalid
            return 0.5

    def _estimate_citation_score(self, paper):
        """
        Estimate citation importance based on available metadata.
        In a real system, this would use actual citation counts.

        Args:
            paper (dict): Paper metadata

        Returns:
            float: Estimated citation score (0.0 to 1.0)
        """
        # This is a simplified heuristic without actual citation data
        score = 0.5  # Start with neutral score

        # More authors might indicate a more significant paper
        author_count = len(paper.get("authors", []))
        if author_count > 4:
            score += 0.1
        elif author_count > 2:
            score += 0.05

        # Papers in multiple categories might be more influential
        category_count = len(paper.get("categories", []))
        if category_count > 2:
            score += 0.1

        # Cross-disciplinary papers (cs.* + another field) might be more impactful
        categories = paper.get("categories", [])
        has_cs = any("cs." in cat for cat in categories)
        has_other = any("cs." not in cat for cat in categories)
        if has_cs and has_other and categories:
            score += 0.1

        # Ensure score is between 0 and 1
        return max(0.0, min(1.0, score))

    def _calculate_relevance_score(self, paper, expanded_keywords):
        """
        Calculate a relevance score using LLM-based assessment.

        Args:
            paper (dict): Paper metadata
            expanded_keywords (dict): Expanded keywords from the KeywordAgent

        Returns:
            float: Relevance score (0.0 to 1.0)
        """
        # Extract paper information
        title = paper.get("title", "")
        abstract = paper.get("abstract", "")

        # Truncate abstract if it's too long
        if len(abstract) > 1000:
            abstract = abstract[:1000] + "..."

        # Get original query and keywords
        original_query = expanded_keywords.get("original_query", "")

        # Get expanded keyword lists
        expanded = expanded_keywords.get("expanded_keywords", {})
        core_keywords = expanded.get("core_keywords", [])
        related_keywords = expanded.get("related_keywords", [])

        # Create a short keywords summary for the prompt
        keywords_summary = ", ".join(core_keywords + related_keywords[:3])

        # Create prompt for relevance assessment
        system_prompt = """You are an expert academic research evaluator specialized in assessing the relevance of papers to research queries.
For the given paper title, abstract, and research query, determine how relevant the paper is to the query on a scale of 0.0 to 1.0.

Focus on:
1. Whether the paper directly addresses the core research question
2. How well it aligns with the keywords and concepts in the query
3. Whether it might provide valuable insights even if not directly on-topic

Respond with ONLY a numeric score between 0.0 and 1.0 representing the relevance, where:
- 1.0 means extremely relevant, perfectly aligned with the query
- 0.7 means highly relevant, addresses major aspects of the query
- 0.5 means moderately relevant, touches on the query topic
- 0.3 means somewhat relevant, tangentially related
- 0.1 means minimally relevant, very loosely connected
- 0.0 means not relevant at all

Provide ONLY the numeric score with no explanation or additional text."""

        user_prompt = f"""Research query: {original_query}
Keywords: {keywords_summary}

Paper title: {title}
Paper abstract: {abstract}

Relevance score (0.0 to 1.0):"""

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_prompt),
        ]

        try:
            # Get relevance assessment from LLM
            response = self._generate_from_llm(messages)

            # Extract the numeric score from the response
            score_str = response.strip()
            relevance_score = float(score_str)

            # Ensure score is between 0 and 1
            relevance_score = max(0.0, min(1.0, relevance_score))

            return relevance_score

        except (ValueError, TypeError):
            # Default score if LLM response can't be parsed
            return 0.5

    def _generate_from_llm(self, messages):
        """
        Generate a response from the LLM using the provided messages.

        Args:
            messages (list): List of message objects for the LLM

        Returns:
            str: The generated response
        """
        if self.client:
            # Use Together.ai client
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": m.type, "content": m.content} for m in messages],
                temperature=0.1,  # Low temperature for more deterministic scoring
                max_tokens=10,
            )
            return response.choices[0].message.content
        else:
            # Use LangChain with OpenAI (fallback)
            llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.1)
            response = llm.invoke(messages)
            return response.content

    def select_top_papers(self, ranked_papers_result, top_n=5):
        """
        Select the top N papers from the ranked results.

        Args:
            ranked_papers_result (dict): Results from rank_papers method
            top_n (int): Number of top papers to select

        Returns:
            dict: Selected top papers
        """
        if "ranked_papers" not in ranked_papers_result:
            return {
                "query": ranked_papers_result.get("query", ""),
                "top_papers": [],
                "error": "No ranked papers found",
            }

        ranked_papers = ranked_papers_result["ranked_papers"]
        top_papers = ranked_papers[: min(top_n, len(ranked_papers))]

        return {
            "query": ranked_papers_result.get("query", ""),
            "top_n": len(top_papers),
            "top_papers": top_papers,
        }

    def run(self, inputs):
        """
        Run the ranking agent with the given inputs.

        Args:
            inputs (dict): Input dictionary containing search results and expanded keywords

        Returns:
            dict: Output dictionary containing ranked papers and top selections
        """
        search_results = inputs.get("search_results", {})
        expanded_keywords = inputs.get("expanded_keywords", {})
        top_n = inputs.get("top_n", 5)

        if not search_results or "results" not in search_results:
            return {
                "error": "No search results provided",
                "ranked_papers": [],
                "top_papers": [],
            }

        # Rank papers
        ranked_results = self.rank_papers(search_results, expanded_keywords)

        # Select top papers
        top_papers_result = self.select_top_papers(ranked_results, top_n)

        return {
            "ranked_papers": ranked_results["ranked_papers"],
            "top_papers": top_papers_result["top_papers"],
        }


if __name__ == "__main__":
    # Example usage
    search_results = {
        "query": "LLMs for academic summarization",
        "results": [
            {
                "title": "Sample Paper 1",
                "abstract": "This is an abstract about LLMs in academic summarization",
                "authors": ["Author 1", "Author 2", "Author 3"],
                "publish_date": "2023-05-15",
                "categories": ["cs.CL", "cs.AI"],
            },
            {
                "title": "Sample Paper 2",
                "abstract": "This is an abstract about academic writing",
                "authors": ["Author 4"],
                "publish_date": "2022-10-20",
                "categories": ["cs.CL"],
            },
        ],
    }

    expanded_keywords = {
        "original_query": "LLMs for academic summarization",
        "expanded_keywords": {
            "core_keywords": ["LLM", "academic summarization", "research papers"],
            "related_keywords": ["natural language processing", "text summarization"],
        },
    }

    agent = RankAgent(api_key="YOUR_API_KEY")  # Replace with your API key
    results = agent.run(
        {"search_results": search_results, "expanded_keywords": expanded_keywords}
    )

    print(f"Ranked {len(results['ranked_papers'])} papers")
    print(f"Selected top {len(results['top_papers'])} papers")
