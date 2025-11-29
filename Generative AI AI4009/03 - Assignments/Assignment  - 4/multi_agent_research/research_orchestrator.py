"""
Multi-Agent Academic Research Assistant Orchestrator
This module coordinates the workflow of multiple specialized agents using LangGraph.
"""

import os
import json
from typing import Dict, List, Any, Annotated, TypedDict
from dotenv import load_dotenv

# Import LangGraph for agent orchestration
from langgraph.graph import StateGraph, END
import langgraph.checkpoint as checkpoint

# Import our specialized agents
from agents.keyword_agent import KeywordAgent
from agents.search_agent import SearchAgent
from agents.rank_agent import RankAgent
from agents.summary_agent import SummaryAgent
from agents.compare_agent import CompareAgent

# Load environment variables
load_dotenv()


class ResearchState(TypedDict):
    """TypedDict defining the state schema for the research workflow."""

    query: str
    expanded_keywords: Dict[str, Any]
    search_results: Dict[str, Any]
    ranked_papers: List[Dict[str, Any]]
    top_papers: List[Dict[str, Any]]
    summarized_papers: List[Dict[str, Any]]
    comparative_analysis: Dict[str, Any]
    research_report: Dict[str, Any]
    error: str


def create_research_orchestrator(
    api_key=None, base_model_name=None, lora_model_dir=None
):
    """
    Create a multi-agent research orchestrator using LangGraph.

    Args:
        api_key (str): API key for LLM services (e.g., Together.ai)
        base_model_name (str): Base model name for summarization
        lora_model_dir (str): Directory with LoRA weights for summarization

    Returns:
        graph: The LangGraph state graph for the research workflow
    """
    # Initialize all agents
    keyword_agent = KeywordAgent(api_key=api_key)
    search_agent = SearchAgent(max_results_per_source=20)
    rank_agent = RankAgent(api_key=api_key)
    summary_agent = SummaryAgent(
        base_model_name=base_model_name, lora_model_dir=lora_model_dir
    )
    compare_agent = CompareAgent(api_key=api_key)

    # Define agent execution functions that operate on the state
    def expand_keywords(state: ResearchState) -> ResearchState:
        """Expand the user query into comprehensive keywords."""
        print("🔍 Expanding keywords...")
        result = keyword_agent.run({"query": state["query"]})
        return {"expanded_keywords": result}

    def search_literature(state: ResearchState) -> ResearchState:
        """Search for papers using expanded keywords."""
        print("📚 Searching academic literature...")
        result = search_agent.run({"expanded_keywords": state["expanded_keywords"]})
        return {"search_results": result}

    def rank_papers(state: ResearchState) -> ResearchState:
        """Rank and select top papers from search results."""
        print("⭐ Ranking papers by relevance and importance...")
        result = rank_agent.run(
            {
                "search_results": state["search_results"],
                "expanded_keywords": state["expanded_keywords"],
                "top_n": 5,  # Select top 5 papers
            }
        )
        return {
            "ranked_papers": result.get("ranked_papers", []),
            "top_papers": result.get("top_papers", []),
        }

    def summarize_papers(state: ResearchState) -> ResearchState:
        """Summarize selected papers."""
        print("📝 Generating summaries of top papers...")
        result = summary_agent.run({"top_papers": state["top_papers"]})
        return {"summarized_papers": result.get("summarized_papers", [])}

    def compare_and_report(state: ResearchState) -> ResearchState:
        """Compare papers and generate research report."""
        print("🧠 Analyzing papers and generating research report...")
        result = compare_agent.run(
            {
                "summarized_papers": state["summarized_papers"],
                "original_query": state["query"],
                "expanded_keywords": state["expanded_keywords"],
            }
        )
        return {
            "comparative_analysis": result.get("comparative_analysis", {}),
            "research_report": result.get("research_report", {}),
        }

    # Define conditional edge function
    def should_end_early(state: ResearchState) -> str:
        """Check if workflow should end early due to errors or no results."""
        if state.get("error"):
            return "end"

        if "search_results" in state and (
            not state["search_results"]
            or not state["search_results"].get("results")
            or len(state["search_results"].get("results", [])) == 0
        ):
            state["error"] = (
                "No papers found matching your query. Please try different keywords."
            )
            return "end"

        if "top_papers" in state and len(state["top_papers"]) == 0:
            state["error"] = "Could not rank papers. Please try a different query."
            return "end"

        # Continue to next step
        return "continue"

    # Create the state graph
    workflow = StateGraph(ResearchState)

    # Add nodes for each agent
    workflow.add_node("expand_keywords", expand_keywords)
    workflow.add_node("search_literature", search_literature)
    workflow.add_node("rank_papers", rank_papers)
    workflow.add_node("summarize_papers", summarize_papers)
    workflow.add_node("compare_and_report", compare_and_report)

    # Define the workflow edges
    workflow.set_entry_point("expand_keywords")
    workflow.add_edge("expand_keywords", "search_literature")

    # Add conditional edge after search
    workflow.add_conditional_edges(
        "search_literature", should_end_early, {"continue": "rank_papers", "end": END}
    )

    # Add conditional edge after ranking
    workflow.add_conditional_edges(
        "rank_papers", should_end_early, {"continue": "summarize_papers", "end": END}
    )

    workflow.add_edge("summarize_papers", "compare_and_report")
    workflow.add_edge("compare_and_report", END)

    # Compile the workflow
    return workflow.compile()


def run_research_workflow(
    query: str, api_key=None, base_model_name=None, lora_model_dir=None
):
    """
    Execute the research workflow for a given query.

    Args:
        query (str): Research query to process
        api_key (str): API key for LLM services
        base_model_name (str): Base model for summarization
        lora_model_dir (str): Directory with LoRA weights

    Returns:
        dict: Final state containing research results
    """
    print(f"Starting research on: '{query}'")

    # Create the workflow graph
    app = create_research_orchestrator(
        api_key=api_key, base_model_name=base_model_name, lora_model_dir=lora_model_dir
    )

    # Set up initial state
    initial_state = {
        "query": query,
        "expanded_keywords": {},
        "search_results": {},
        "ranked_papers": [],
        "top_papers": [],
        "summarized_papers": [],
        "comparative_analysis": {},
        "research_report": {},
        "error": "",
    }

    # Run the workflow
    try:
        result = app.invoke(initial_state)

        # Check for errors
        if result.get("error"):
            print(f"❌ Error: {result['error']}")
            return result

        # Log successful completion
        if "research_report" in result and result["research_report"]:
            print("✅ Research workflow completed successfully!")
            report_length = len(result["research_report"].get("report", ""))
            print(f"📊 Generated research report with {report_length} characters")

            summarized_papers = result.get("summarized_papers", [])
            print(f"📑 Analyzed {len(summarized_papers)} papers in depth")

        return result

    except Exception as e:
        print(f"❌ Error running research workflow: {str(e)}")
        return {
            "query": query,
            "error": f"Workflow error: {str(e)}",
        }


def save_research_results(results, output_dir):
    """
    Save research results to disk.

    Args:
        results (dict): Research results to save
        output_dir (str): Directory to save results to
    """
    os.makedirs(output_dir, exist_ok=True)

    # Save research report
    if "research_report" in results and results["research_report"]:
        report_path = os.path.join(output_dir, "research_report.md")
        with open(report_path, "w", encoding="utf-8") as f:
            f.write(results["research_report"].get("report", ""))
        print(f"Research report saved to {report_path}")

    # Save all results as JSON
    results_path = os.path.join(output_dir, "research_results.json")
    with open(results_path, "w", encoding="utf-8") as f:
        # Remove any large or redundant data from results
        slim_results = results.copy()
        # Remove raw search results to keep file size manageable
        if "search_results" in slim_results:
            search_count = len(slim_results["search_results"].get("results", []))
            slim_results["search_results"] = {
                "query": slim_results["search_results"].get("query", ""),
                "total_results": search_count,
                "sources_searched": slim_results["search_results"].get(
                    "sources_searched", []
                ),
                "result_count": search_count,
            }

        json.dump(slim_results, f, indent=2)
    print(f"Complete research results saved to {results_path}")


if __name__ == "__main__":
    import argparse

    # Parse arguments
    parser = argparse.ArgumentParser(description="Run the academic research assistant.")
    parser.add_argument(
        "--query", type=str, required=True, help="Research query to process"
    )
    parser.add_argument(
        "--api_key", type=str, help="API key for LLM service (e.g., Together.ai)"
    )
    parser.add_argument(
        "--base_model",
        type=str,
        default="meta-llama/Llama-3-8B",
        help="Base model for summarization",
    )
    parser.add_argument(
        "--lora_model",
        type=str,
        default="../smart_summarizer/models/lora_summarizer/final_model",
        help="Path to LoRA model",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="research_output",
        help="Output directory for results",
    )

    args = parser.parse_args()

    # Get API key from environment if not provided
    api_key = args.api_key or os.environ.get("TOGETHER_API_KEY")

    # Run the workflow
    results = run_research_workflow(
        query=args.query,
        api_key=api_key,
        base_model_name=args.base_model,
        lora_model_dir=args.lora_model,
    )

    # Save results
    save_research_results(results, args.output)
