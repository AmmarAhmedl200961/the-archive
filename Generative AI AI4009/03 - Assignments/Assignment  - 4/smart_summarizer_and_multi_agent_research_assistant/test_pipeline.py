#!/usr/bin/env python3
"""
Test Pipeline for Multi-Agent Research Assistant

This script tests the entire research pipeline with sample keywords.
"""

import os
import sys
import json
import logging
import time
from datetime import datetime
from typing import List, Dict, Any, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("pipeline_test.log")
    ]
)
logger = logging.getLogger(__name__)

# Import API configuration
try:
    from api_config import APIConfig, test_api_connections
except ImportError:
    logger.error("Failed to import APIConfig. Make sure api_config.py is in the current directory.")
    sys.exit(1)

# Import model integration
try:
    from model_integration import ModelIntegration
except ImportError:
    logger.error("Failed to import ModelIntegration. Make sure model_integration.py is in the current directory.")
    sys.exit(1)

# Try to import agent components from the notebook
# These will be imported when running the test through the notebook
# If running standalone, we'll create simple mock agents
try:
    from multi_agent_research import (
        KeywordAgent, SearchAgent, RankAgent, SummaryAgent, CompareAgent, ResearchWorkflow
    )
    NOTEBOOK_IMPORTS = True
    logger.info("Successfully imported agents from notebook")
except ImportError:
    logger.warning("Failed to import agents from notebook. Using mock implementations.")
    NOTEBOOK_IMPORTS = False

# Import LLM components if available
try:
    from langchain_openai import ChatOpenAI
    LANGCHAIN_AVAILABLE = True
except ImportError:
    logger.warning("langchain_openai not available. Using simple LLM implementation.")
    LANGCHAIN_AVAILABLE = False

class MockLLM:
    """Mock LLM implementation for testing without langchain."""
    
    def __init__(self, api_key=None):
        """Initialize the mock LLM."""
        self.api_key = api_key or os.environ.get("TOGETHER_API_KEY", "")
    
    def invoke(self, prompt):
        """Generate a response for the given prompt."""
        try:
            import together
            together.api_key = self.api_key
            
            response = together.Complete.create(
                prompt=prompt if isinstance(prompt, str) else prompt["prompt"],
                model="meta-llama/Llama-3-8B-Instruct",
                max_tokens=512,
                temperature=0.7,
                top_p=0.9
            )
            
            return response['output']['choices'][0]['text']
        except Exception as e:
            logger.error(f"Error calling Together.ai API: {e}")
            return f"Error: {e}"

class MockKeywordAgent:
    """Mock implementation of KeywordAgent."""
    
    def __init__(self, llm):
        self.llm = llm
    
    def process(self, query):
        """Expand the query into keywords."""
        logger.info(f"Expanding query: {query}")
        
        if isinstance(self.llm, MockLLM):
            prompt = f"""You are an expert research assistant. Given the following research query, generate an expanded list of 5-8 related keywords and phrases that would be useful for finding relevant academic papers.

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
            response = self.llm.invoke(prompt)
            
            try:
                # Try to parse the JSON response
                import re
                json_match = re.search(r'({.*})', response.replace('\n', ' '), re.DOTALL)
                if json_match:
                    result = json.loads(json_match.group(1))
                    return result
            except:
                pass
        
        # Fallback result
        return {
            "original_query": query,
            "expanded_keywords": [
                {"keyword": query, "relevance": 1.0},
                {"keyword": f"{query} research", "relevance": 0.9},
                {"keyword": f"{query} applications", "relevance": 0.8},
                {"keyword": f"{query} methods", "relevance": 0.7},
                {"keyword": f"{query} techniques", "relevance": 0.6}
            ]
        }

class MockSearchAgent:
    """Mock implementation of SearchAgent."""
    
    def __init__(self, api_config=None):
        self.api_config = api_config
    
    def process(self, keyword_set):
        """Search for papers using the keywords."""
        logger.info(f"Searching for papers with keywords: {keyword_set}")
        
        papers = []
        
        # Use actual API if available
        if self.api_config:
            # Try to use the arXiv API wrapper
            arxiv_wrapper = self.api_config.get_wrapper("arxiv")
            if arxiv_wrapper:
                try:
                    # Search using the original query
                    query = keyword_set["original_query"]
                    results = arxiv_wrapper.search(query, max_results=5)
                    
                    if "items" in results:
                        for item in results["items"]:
                            paper = {
                                "id": item["id"],
                                "title": item["title"],
                                "abstract": item["abstract"],
                                "authors": item["authors"],
                                "year": item.get("published", "")[:4] if item.get("published") else None,
                                "url": item.get("arxiv_url"),
                                "pdf_url": item.get("pdf_url"),
                                "citation_count": None,
                                "source": "arxiv"
                            }
                            papers.append(paper)
                except Exception as e:
                    logger.error(f"Error searching arXiv: {e}")
        
        # If we didn't get any papers from the API, use mock data
        if not papers:
            logger.info("Using mock paper data")
            # Generate mock papers
            papers = [
                {
                    "id": "2201.12345",
                    "title": f"Advances in {keyword_set['original_query']}",
                    "abstract": f"This paper presents recent advances in {keyword_set['original_query']}.",
                    "authors": [{"name": "Smith, J."}, {"name": "Johnson, A."}],
                    "year": 2023,
                    "url": "https://arxiv.org/abs/2201.12345",
                    "pdf_url": "https://arxiv.org/pdf/2201.12345.pdf",
                    "citation_count": 42,
                    "source": "arxiv"
                },
                {
                    "id": "2202.67890",
                    "title": f"A Survey of {keyword_set['original_query']}",
                    "abstract": f"This survey provides a comprehensive overview of {keyword_set['original_query']}.",
                    "authors": [{"name": "Brown, M."}, {"name": "Davis, L."}],
                    "year": 2022,
                    "url": "https://arxiv.org/abs/2202.67890",
                    "pdf_url": "https://arxiv.org/pdf/2202.67890.pdf",
                    "citation_count": 86,
                    "source": "arxiv"
                }
            ]
            
            # Add papers for top keywords
            for keyword in keyword_set["expanded_keywords"][:3]:
                papers.append({
                    "id": f"mock_{len(papers)}",
                    "title": f"Research on {keyword['keyword']}",
                    "abstract": f"This paper investigates various aspects of {keyword['keyword']}.",
                    "authors": [{"name": "Researcher, A."}, {"name": "Academic, B."}],
                    "year": 2023,
                    "url": f"https://example.com/papers/{len(papers)}",
                    "pdf_url": f"https://example.com/papers/{len(papers)}.pdf",
                    "citation_count": int(keyword["relevance"] * 100),
                    "source": "mock"
                })
        
        logger.info(f"Found {len(papers)} papers")
        return papers

class MockRankAgent:
    """Mock implementation of RankAgent."""
    
    def __init__(self, llm):
        self.llm = llm
    
    def process(self, papers, keyword_set):
        """Rank the papers based on relevance, citations, and recency."""
        logger.info(f"Ranking {len(papers)} papers")
        
        # Calculate scores for each paper
        ranked_papers = []
        for paper in papers:
            # Simple relevance score based on keyword matching
            relevance_score = self._calculate_relevance(paper, keyword_set["original_query"])
            
            # Citation score
            citation_score = self._calculate_citation_score(paper.get("citation_count"))
            
            # Recency score
            recency_score = self._calculate_recency_score(paper.get("year"))
            
            # Overall score
            rank_score = (relevance_score * 0.6) + (citation_score * 0.25) + (recency_score * 0.15)
            
            # Add ranked paper
            ranked_paper = dict(paper)
            ranked_paper.update({
                "rank_score": rank_score,
                "relevance_score": relevance_score,
                "citation_score": citation_score,
                "recency_score": recency_score
            })
            
            ranked_papers.append(ranked_paper)
        
        # Sort by rank score
        ranked_papers.sort(key=lambda p: p["rank_score"], reverse=True)
        
        logger.info(f"Ranked {len(ranked_papers)} papers")
        return ranked_papers
    
    def _calculate_relevance(self, paper, query):
        """Calculate relevance score based on query matching."""
        # Simple keyword matching for testing
        query_lower = query.lower()
        title_lower = paper.get("title", "").lower()
        abstract_lower = paper.get("abstract", "").lower()
        
        # Count occurrences in title (weighted higher)
        title_count = title_lower.count(query_lower) * 2
        
        # Count occurrences in abstract
        abstract_count = abstract_lower.count(query_lower)
        
        # Normalize score between 0 and 1
        score = min(1.0, (title_count + abstract_count) / 10)
        
        # Ensure a minimum score for all papers
        return max(0.3, score)
    
    def _calculate_citation_score(self, citation_count):
        """Calculate score based on citation count."""
        if citation_count is None:
            return 0.5
        
        # Log-based scoring to handle papers with very high citation counts
        import math
        if citation_count == 0:
            return 0.1
        return min(1.0, 0.1 + 0.3 * math.log10(citation_count + 1))
    
    def _calculate_recency_score(self, year):
        """Calculate score based on publication recency."""
        if year is None:
            return 0.5
        
        current_year = datetime.now().year
        
        # Linear decay from current year (1.0) to 10 years ago (0.1)
        years_ago = current_year - int(year)
        if years_ago <= 0:
            return 1.0
        elif years_ago >= 10:
            return 0.1
        else:
            return 1.0 - (0.9 * years_ago / 10.0)

class MockSummaryAgent:
    """Mock implementation of SummaryAgent."""
    
    def __init__(self, model_integration=None, llm=None):
        self.model_integration = model_integration
        self.llm = llm
    
    def process(self, ranked_papers, top_n=3):
        """Generate summaries for the top-ranked papers."""
        # Select the top N papers
        top_papers = ranked_papers[:top_n]
        logger.info(f"Summarizing {len(top_papers)} papers")
        
        paper_summaries = []
        for i, paper in enumerate(top_papers):
            logger.info(f"Summarizing paper {i+1}/{len(top_papers)}: {paper['title']}")
            
            # Try to use the model integration
            summary = None
            if self.model_integration:
                try:
                    summary = self.model_integration.summarize(paper["abstract"])
                except Exception as e:
                    logger.error(f"Error using model integration: {e}")
            
            # If that failed, try to use the LLM
            if not summary and self.llm:
                try:
                    if isinstance(self.llm, MockLLM):
                        prompt = f"""Summarize the following academic paper:
                        
Title: {paper['title']}
Authors: {', '.join(author['name'] for author in paper['authors'])}
Abstract: {paper['abstract']}

Summary:"""
                        summary = self.llm.invoke(prompt)
                    else:
                        # For langchain LLM
                        from langchain.prompts import PromptTemplate
                        prompt_template = PromptTemplate(
                            input_variables=["title", "authors", "abstract"],
                            template="""Summarize the following academic paper:
                            
Title: {title}
Authors: {authors}
Abstract: {abstract}

Summary:"""
                        )
                        prompt = prompt_template.format(
                            title=paper['title'],
                            authors=', '.join(author['name'] for author in paper['authors']),
                            abstract=paper['abstract']
                        )
                        summary = self.llm.invoke(prompt)
                except Exception as e:
                    logger.error(f"Error using LLM for summarization: {e}")
            
            # If both methods failed, use a mock summary
            if not summary:
                summary = f"This paper presents research on {paper['title']}. The authors investigate various aspects and provide insights into the topic."
            
            # Extract structured information
            structured_info = self._extract_structured_information(summary)
            
            # Create paper summary
            paper_summary = {
                "paper_id": paper["id"],
                "title": paper["title"],
                "authors": [author["name"] for author in paper["authors"]],
                "summary": summary,
                "methodology": structured_info.get("methodology", "Not specified"),
                "contributions": structured_info.get("contributions", "Not specified"),
                "limitations": structured_info.get("limitations", "Not specified")
            }
            
            paper_summaries.append(paper_summary)
        
        logger.info(f"Generated {len(paper_summaries)} summaries")
        return paper_summaries
    
    def _extract_structured_information(self, summary):
        """Extract structured information from the summary."""
        # Try to use the LLM for extraction
        if self.llm:
            try:
                if isinstance(self.llm, MockLLM):
                    prompt = f"""Extract and structure the information from the following paper summary into specific sections.

Paper summary: {summary}

Extract the following components from the summary:
1. Methodology: What research methods or techniques were used?
2. Key Contributions: What are the main findings or contributions of the paper?
3. Limitations or Gaps: What limitations, open questions, or research gaps were identified?

Respond with a JSON object in the following format:
{{
  "methodology": "description of methodology",
  "contributions": "key contributions and findings",
  "limitations": "limitations and research gaps"
}}
"""
                    response = self.llm.invoke(prompt)
                    
                    try:
                        # Try to parse the JSON response
                        import re
                        json_match = re.search(r'({.*})', response.replace('\n', ' '), re.DOTALL)
                        if json_match:
                            return json.loads(json_match.group(1))
                    except:
                        pass
                else:
                    # For langchain LLM
                    from langchain.prompts import PromptTemplate
                    prompt_template = PromptTemplate(
                        input_variables=["summary"],
                        template="""Extract and structure the information from the following paper summary into specific sections.

Paper summary: {summary}

Extract the following components from the summary:
1. Methodology: What research methods or techniques were used?
2. Key Contributions: What are the main findings or contributions of the paper?
3. Limitations or Gaps: What limitations, open questions, or research gaps were identified?

Respond with a JSON object in the following format:
{{
  "methodology": "description of methodology",
  "contributions": "key contributions and findings",
  "limitations": "limitations and research gaps"
}}
"""
                    )
                    prompt = prompt_template.format(summary=summary)
                    response = self.llm.invoke(prompt)
                    
                    try:
                        # Try to parse the JSON response
                        import re
                        json_match = re.search(r'({.*})', response.replace('\n', ' '), re.DOTALL)
                        if json_match:
                            return json.loads(json_match.group(1))
                    except:
                        pass
            except Exception as e:
                logger.error(f"Error extracting structured information: {e}")
        
        # Fallback: return simple structured information
        return {
            "methodology": "The paper employs various research methods to investigate the topic.",
            "contributions": "The paper contributes to the understanding of the topic and provides valuable insights.",
            "limitations": "The study has some limitations that could be addressed in future research."
        }

class MockCompareAgent:
    """Mock implementation of CompareAgent."""
    
    def __init__(self, llm):
        self.llm = llm
    
    def process(self, paper_summaries):
        """Perform comparative analysis on the paper summaries."""
        logger.info(f"Performing comparative analysis on {len(paper_summaries)} paper summaries")
        
        # Try to use the LLM for comparison
        if self.llm:
            try:
                # Format the summaries
                formatted_summaries = ""
                for i, summary in enumerate(paper_summaries):
                    formatted_summaries += f"Paper {i+1}: {summary['title']}\n"
                    formatted_summaries += f"Authors: {', '.join(summary['authors'])}\n"
                    formatted_summaries += f"Summary: {summary['summary']}\n"
                    formatted_summaries += f"Methodology: {summary['methodology']}\n"
                    formatted_summaries += f"Key Contributions: {summary['contributions']}\n"
                    formatted_summaries += f"Limitations/Gaps: {summary['limitations']}\n\n"
                
                if isinstance(self.llm, MockLLM):
                    prompt = f"""You are an expert academic researcher analyzing multiple papers on a related topic. Perform a comparative analysis of the following paper summaries to identify common themes, contradictions, research gaps, and future directions.

Paper Summaries:
{formatted_summaries}

Based on these summaries, provide a comprehensive comparative analysis in the following JSON format:
{{
  "common_findings": [
    "Common finding 1",
    "Common finding 2",
    ... (at least 3-5 items)
  ],
  "contradictions": [
    "Contradiction 1",
    "Contradiction 2",
    ... (identify any contradictions between papers)
  ],
  "research_gaps": [
    "Research gap 1",
    "Research gap 2",
    ... (identify areas that need further research, at least 3-4 items)
  ],
  "future_directions": [
    "Future direction 1",
    "Future direction 2",
    ... (suggest future research directions, at least 3-4 items)
  ]
}}
"""
                    response = self.llm.invoke(prompt)
                    
                    try:
                        # Try to parse the JSON response
                        import re
                        json_match = re.search(r'({.*})', response.replace('\n', ' '), re.DOTALL)
                        if json_match:
                            return json.loads(json_match.group(1))
                    except:
                        pass
                else:
                    # For langchain LLM
                    from langchain.prompts import PromptTemplate
                    prompt_template = PromptTemplate(
                        input_variables=["summaries"],
                        template="""You are an expert academic researcher analyzing multiple papers on a related topic. Perform a comparative analysis of the following paper summaries to identify common themes, contradictions, research gaps, and future directions.

Paper Summaries:
{summaries}

Based on these summaries, provide a comprehensive comparative analysis in the following JSON format:
{{
  "common_findings": [
    "Common finding 1",
    "Common finding 2",
    ... (at least 3-5 items)
  ],
  "contradictions": [
    "Contradiction 1",
    "Contradiction 2",
    ... (identify any contradictions between papers)
  ],
  "research_gaps": [
    "Research gap 1",
    "Research gap 2",
    ... (identify areas that need further research, at least 3-4 items)
  ],
  "future_directions": [
    "Future direction 1",
    "Future direction 2",
    ... (suggest future research directions, at least 3-4 items)
  ]
}}
"""
                    )
                    prompt = prompt_template.format(summaries=formatted_summaries)
                    response = self.llm.invoke(prompt)
                    
                    try:
                        # Try to parse the JSON response
                        import re
                        json_match = re.search(r'({.*})', response.replace('\n', ' '), re.DOTALL)
                        if json_match:
                            return json.loads(json_match.group(1))
                    except:
                        pass
            except Exception as e:
                logger.error(f"Error performing comparative analysis: {e}")
        
        # Fallback: return simple comparative analysis
        return {
            "common_findings": [
                "All papers acknowledge the importance of the research topic.",
                "Several papers mention similar methodologies.",
                "Most papers identify similar key challenges in the field."
            ],
            "contradictions": [
                "Papers differ in their assessment of the effectiveness of certain approaches.",
                "There are conflicting views on the future direction of the field."
            ],
            "research_gaps": [
                "Limited research on practical applications.",
                "Insufficient attention to ethical considerations.",
                "Need for more comprehensive evaluation metrics."
            ],
            "future_directions": [
                "Develop more integrated research frameworks.",
                "Investigate real-world applications and case studies.",
                "Address ethical and societal implications."
            ]
        }

class MockResearchWorkflow:
    """Mock implementation of ResearchWorkflow."""
    
    def __init__(self, api_config=None, model_integration=None, llm=None):
        """Initialize the research workflow."""
        self.api_config = api_config
        self.model_integration = model_integration
        self.llm = llm
        
        # Initialize agents
        self.keyword_agent = MockKeywordAgent(llm)
        self.search_agent = MockSearchAgent(api_config)
        self.rank_agent = MockRankAgent(llm)
        self.summary_agent = MockSummaryAgent(model_integration, llm)
        self.compare_agent = MockCompareAgent(llm)
    
    def run(self, query, top_n=3):
        """Run the complete research workflow."""
        logger.info(f"Starting research workflow for query: {query}")
        
        # State to store results at each step
        state = {
            "query": query,
            "keyword_set": None,
            "papers": [],
            "ranked_papers": [],
            "paper_summaries": [],
            "comparative_analysis": None,
            "research_report": None
        }
        
        # 1. Expand Keywords
        logger.info("Step 1: Expanding keywords")
        keyword_set = self.keyword_agent.process(query)
        state["keyword_set"] = keyword_set
        logger.info(f"Expanded keywords: {[k['keyword'] for k in keyword_set['expanded_keywords']]}")
        
        # 2. Search Papers
        logger.info("Step 2: Searching papers")
        papers = self.search_agent.process(keyword_set)
        state["papers"] = papers
        logger.info(f"Found {len(papers)} papers")
        
        # 3. Rank Papers
        logger.info("Step 3: Ranking papers")
        ranked_papers = self.rank_agent.process(papers, keyword_set)
        state["ranked_papers"] = ranked_papers
        logger.info(f"Ranked {len(ranked_papers)} papers")
        
        # 4. Summarize Papers
        logger.info("Step 4: Summarizing papers")
        paper_summaries = self.summary_agent.process(ranked_papers, top_n)
        state["paper_summaries"] = paper_summaries
        logger.info(f"Generated {len(paper_summaries)} paper summaries")
        
        # 5. Compare Papers
        logger.info("Step 5: Comparing papers")
        comparative_analysis = self.compare_agent.process(paper_summaries)
        state["comparative_analysis"] = comparative_analysis
        logger.info("Comparative analysis completed")
        
        # 6. Generate Research Report
        logger.info("Step 6: Generating research report")
        research_report = self._generate_research_report(state)
        state["research_report"] = research_report
        logger.info("Research report generated")
        
        return research_report
    
    def _generate_research_report(self, state):
        """Generate the final research report."""
        # Generate topic summary
        topic_summary = self._generate_topic_summary(
            state["query"],
            state["keyword_set"]["expanded_keywords"]
        )
        
        # Create the research report
        research_report = {
            "topic": state["query"],
            "topic_summary": topic_summary,
            "expanded_keywords": [k["keyword"] for k in state["keyword_set"]["expanded_keywords"]],
            "paper_summaries": state["paper_summaries"],
            "comparative_analysis": state["comparative_analysis"],
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        return research_report
    
    def _generate_topic_summary(self, query, keywords):
        """Generate a summary of the research topic."""
        logger.info("Generating topic summary")
        
        if self.llm:
            try:
                # Format keywords
                keywords_str = ", ".join([k["keyword"] for k in keywords])
                
                if isinstance(self.llm, MockLLM):
                    prompt = f"""You are an expert academic researcher writing a brief overview of a research topic.

Research topic: {query}

Related keywords: {keywords_str}

Write a concise (150-200 words) but comprehensive overview of this research topic that explains its significance, key aspects, and relevance in its field.
"""
                    return self.llm.invoke(prompt)
                else:
                    # For langchain LLM
                    from langchain.prompts import PromptTemplate
                    prompt_template = PromptTemplate(
                        input_variables=["query", "keywords"],
                        template="""You are an expert academic researcher writing a brief overview of a research topic.

Research topic: {query}

Related keywords: {keywords}

Write a concise (150-200 words) but comprehensive overview of this research topic that explains its significance, key aspects, and relevance in its field.
"""
                    )
                    prompt = prompt_template.format(query=query, keywords=keywords_str)
                    return self.llm.invoke(prompt)
            except Exception as e:
                logger.error(f"Error generating topic summary: {e}")
        
        # Fallback: return simple topic summary
        return f"This research topic focuses on {query}. It is an important area of study with various applications and implications. The field encompasses several related concepts including {', '.join([k['keyword'] for k in keywords[:3]])}."

def setup_environment():
    """Set up the environment for testing."""
    # Check for API keys
    together_api_key = os.environ.get("TOGETHER_API_KEY", "")
    if not together_api_key:
        logger.warning("No Together.ai API key found. Some features may not work.")
        
        # Try to get the API key from the user
        try:
            together_api_key = input("Enter your Together.ai API key (press Enter to skip): ")
            if together_api_key:
                os.environ["TOGETHER_API_KEY"] = together_api_key
        except:
            pass
    
    # Initialize API configuration
    api_config = APIConfig()
    
    # Test API connections
    logger.info("Testing API connections...")
    connection_results = test_api_connections(api_config)
    
    # Log results
    for api, status in connection_results.items():
        if status is None:
            logger.info(f"API {api}: Not tested (API key not provided)")
        elif status:
            logger.info(f"API {api}: Connected")
        else:
            logger.warning(f"API {api}: Connection failed")
    
    # Initialize model integration
    logger.info("Initializing model integration...")
    model_path = os.environ.get("FINETUNED_MODEL_PATH", "./fine_tuned_model")
    model_integration = ModelIntegration(model_path, together_api_key)
    
    # Get model info
    model_info = model_integration.get_model_info()
    logger.info(f"Model status: {model_info.get('status', 'unknown')}")
    
    # Initialize LLM
    logger.info("Initializing LLM...")
    if LANGCHAIN_AVAILABLE:
        try:
            llm = ChatOpenAI(
                model="gpt-3.5-turbo",
                temperature=0.3,
                api_key=os.environ.get("OPENAI_API_KEY", "")
            )
            logger.info("Using ChatOpenAI LLM")
        except:
            logger.warning("Failed to initialize ChatOpenAI LLM. Using MockLLM instead.")
            llm = MockLLM(together_api_key)
    else:
        logger.info("Using MockLLM with Together.ai API")
        llm = MockLLM(together_api_key)
    
    return api_config, model_integration, llm

def run_test_pipeline(query="Large Language Models", top_n=3, notebook_agents=False):
    """Run the test pipeline with the given query."""
    # Set up the environment
    api_config, model_integration, llm = setup_environment()
    
    # Create the research workflow
    if notebook_agents and NOTEBOOK_IMPORTS:
        logger.info("Using agents from notebook")
        
        # Initialize agents from the notebook
        keyword_agent = KeywordAgent(llm)
        search_agent = SearchAgent()
        rank_agent = RankAgent(llm)
        summary_agent = SummaryAgent(model=model_integration.model,
                                     tokenizer=model_integration.tokenizer,
                                     llm=llm)
        compare_agent = CompareAgent(llm)
        
        # Create the workflow
        workflow = ResearchWorkflow(llm)
    else:
        logger.info("Using mock agents")
        workflow = MockResearchWorkflow(api_config, model_integration, llm)
    
    # Run the workflow
    logger.info(f"Running research workflow for query: {query}")
    start_time = time.time()
    
    try:
        research_report = workflow.run(query, top_n)
        
        # Calculate execution time
        execution_time = time.time() - start_time
        logger.info(f"Workflow completed in {execution_time:.2f} seconds")
        
        # Save the report
        report_file = f"research_report_{query.replace(' ', '_').lower()}.json"
        with open(report_file, "w") as f:
            json.dump(research_report, f, indent=2)
        
        logger.info(f"Research report saved to {report_file}")
        
        # Print summary
        print("\n===== Research Report Summary =====")
        print(f"Topic: {research_report['topic']}")
        print(f"Keywords: {', '.join(research_report['expanded_keywords'][:5])}")
        print(f"Papers analyzed: {len(research_report['paper_summaries'])}")
        print("\nTop papers:")
        for i, summary in enumerate(research_report['paper_summaries']):
            print(f"{i+1}. {summary['title']}")
        
        print("\nCommon findings:")
        for finding in research_report['comparative_analysis']['common_findings'][:2]:
            print(f"- {finding}")
        
        print("\nResearch gaps:")
        for gap in research_report['comparative_analysis']['research_gaps'][:2]:
            print(f"- {gap}")
        
        print(f"\nFull report saved to {report_file}")
        
        return research_report
    except Exception as e:
        logger.error(f"Error running workflow: {e}", exc_info=True)
        execution_time = time.time() - start_time
        logger.info(f"Workflow failed after {execution_time:.2f} seconds")
        return None

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Test the research pipeline")
    parser.add_argument("--query", type=str, default="Large Language Models", help="Research query")
    parser.add_argument("--top_n", type=int, default=3, help="Number of top papers to analyze")
    parser.add_argument("--notebook", action="store_true", help="Use agents from notebook")
    
    args = parser.parse_args()
    
    # Run the test pipeline
    report = run_test_pipeline(args.query, args.top_n, args.notebook)