"""
CompareAgent Module
This agent is responsible for comparing summaries of papers to identify common themes,
contradictions, and research gaps.
"""

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
import together
import json


class CompareAgent:
    """
    Agent for performing comparative analysis on summarized papers.
    Identifies common themes, contradictions, and research gaps using LLMs.
    """

    def __init__(self, model="meta-llama/Llama-3-8B-hf", api_key=None):
        """
        Initialize the CompareAgent.

        Args:
            model (str): Model ID to use for comparative analysis
            api_key (str): API key for LLM service (e.g., Together.ai)
        """
        self.model = model
        self.api_key = api_key
        self.client = None

        if api_key:
            self.client = together.Together(api_key=api_key)

    def compare_papers(self, summarized_papers, original_query):
        """
        Compare multiple paper summaries to identify patterns, contradictions, and gaps.

        Args:
            summarized_papers (list): List of papers with summaries
            original_query (str): The user's original research query

        Returns:
            dict: Comparative analysis results
        """
        # Extract titles and summaries for comparison
        paper_data = []
        for i, paper in enumerate(summarized_papers):
            paper_data.append(
                {
                    "id": i + 1,
                    "title": paper.get("title", f"Paper {i+1}"),
                    "authors": paper.get("authors", []),
                    "summary": paper.get("summary", "No summary available"),
                    "publish_date": paper.get("publish_date", "Unknown"),
                }
            )

        # Create prompt for comparative analysis
        system_prompt = """You are an expert academic research analyst specialized in synthesizing information across multiple papers.
Your task is to analyze the summaries of several research papers on a given topic and identify:

1. Common Findings: Key conclusions and methods that multiple papers agree on
2. Contradictions: Areas where papers disagree or present conflicting results
3. Research Gaps: Important aspects of the topic that seem underexplored based on these papers
4. Future Directions: Promising research avenues suggested by the collective findings
5. Methodological Insights: Common or innovative research approaches used across papers

Organize your analysis in a structured format with clear sections. Be specific and reference which papers support each point.
Focus on synthesizing insights rather than simply summarizing each paper individually.

Provide your analysis in JSON format with the following structure:
{
  "common_findings": [
    {"finding": "Description of finding", "papers": [paper_ids], "explanation": "Brief explanation"}
  ],
  "contradictions": [
    {"topic": "Topic of contradiction", "papers": [paper_ids], "explanation": "Nature of disagreement"}
  ],
  "research_gaps": [
    {"gap": "Description of research gap", "explanation": "Why this gap is significant"}
  ],
  "future_directions": [
    {"direction": "Potential research direction", "papers": [paper_ids], "explanation": "Reasoning"}
  ],
  "methodological_insights": [
    {"insight": "Description of methodological insight", "papers": [paper_ids], "explanation": "Significance"}
  ],
  "summary": "A brief overall synthesis of the research landscape based on these papers"
}"""

        # Prepare paper information for the prompt
        papers_text = "Research Papers:\n"
        for paper in paper_data:
            papers_text += f"\nPaper {paper['id']}: {paper['title']}\n"
            papers_text += f"Authors: {', '.join(paper['authors']) if isinstance(paper['authors'], list) else paper['authors']}\n"
            papers_text += f"Published: {paper['publish_date']}\n"
            papers_text += f"Summary: {paper['summary']}\n"

        user_prompt = f"""Original Research Query: {original_query}

{papers_text}

Based on these papers, provide a comparative analysis following the format specified in your instructions."""

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_prompt),
        ]

        # Get comparative analysis from LLM
        response = self._generate_from_llm(messages)

        # Parse JSON from response
        try:
            # Extract JSON part from response if needed
            json_content = self._extract_json(response)
            analysis = json.loads(json_content)

            # Add the original response as well
            analysis["full_response"] = response

        except Exception as e:
            print(f"Error parsing comparison results: {e}")
            print(f"Raw response: {response}")

            # Create a fallback structure if JSON parsing fails
            analysis = {
                "common_findings": [],
                "contradictions": [],
                "research_gaps": [],
                "future_directions": [],
                "methodological_insights": [],
                "summary": "Error parsing comparative analysis.",
                "full_response": response,
            }

        return analysis

    def _extract_json(self, text):
        """
        Extract JSON content from text that might contain markdown or other formatting.

        Args:
            text (str): Text that might contain JSON

        Returns:
            str: Extracted JSON string
        """
        import re

        # Try to extract JSON from code blocks
        json_match = re.search(r"```(?:json)?\s*([\s\S]+?)\s*```", text)
        if json_match:
            return json_match.group(1)

        # If no code block, look for parts that look like JSON
        json_match = re.search(r"({[\s\S]+})", text)
        if json_match:
            return json_match.group(1)

        # If all else fails, return the original text
        return text

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
                temperature=0.3,
                max_tokens=2000,
            )
            return response.choices[0].message.content
        else:
            # Use LangChain with OpenAI (fallback)
            llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.3)
            response = llm.invoke(messages)
            return response.content

    def generate_research_report(
        self, comparative_analysis, summarized_papers, original_query, expanded_keywords
    ):
        """
        Generate a comprehensive research report based on comparative analysis and paper summaries.

        Args:
            comparative_analysis (dict): Results from compare_papers method
            summarized_papers (list): List of papers with summaries
            original_query (str): The user's original research query
            expanded_keywords (dict): Expanded keywords from KeywordAgent

        Returns:
            dict: Research report content
        """
        # Create a topic summary based on the query and keyword analysis
        query_analysis = ""
        if (
            "expanded_keywords" in expanded_keywords
            and "query_analysis" in expanded_keywords["expanded_keywords"]
        ):
            query_analysis = expanded_keywords["expanded_keywords"]["query_analysis"]

        # Construct system prompt for report generation
        system_prompt = """You are an expert academic research assistant specialized in creating comprehensive research reports.
Based on the comparative analysis and summaries of key papers provided, create a well-structured academic research report.
The report should be written in a scholarly tone but be accessible to researchers who might not be experts in the specific field.

Structure the report as follows:

# [Title based on research topic]

## 1. Introduction and Topic Overview
- Brief introduction to the research area
- Significance of the topic in the broader field
- Scope of this research report

## 2. Methodology
- Overview of how papers were selected and analyzed
- Description of the analytical approach used

## 3. Key Papers Overview
- Structured overview of the most significant papers reviewed
- For each paper: brief summary of methodology, findings, and contributions

## 4. Comparative Analysis
- Common themes and findings across papers
- Contradictions or disagreements in the literature
- Methodological approaches and their effectiveness

## 5. Research Gaps and Opportunities
- Identified gaps in the current literature
- Emerging questions that require further investigation
- Potential research directions

## 6. Conclusion
- Summary of the current state of knowledge
- Implications for theory and practice
- Final thoughts on the research landscape

Ensure the report synthesizes information rather than simply listing papers. Make connections between works and highlight the evolution of ideas."""

        # Prepare data for the user prompt
        papers_info = "\n\n".join(
            [
                f"Paper: {paper.get('title', 'Untitled')}\n"
                f"Authors: {', '.join(paper.get('authors', ['Unknown']))}\n"
                f"Published: {paper.get('publish_date', 'Unknown date')}\n"
                f"Summary: {paper.get('summary', 'No summary available')}"
                for paper in summarized_papers
            ]
        )

        user_prompt = f"""Original Research Query: {original_query}

Topic Analysis: {query_analysis}

Comparative Analysis Results:
{json.dumps(comparative_analysis, indent=2)}

Paper Summaries:
{papers_info}

Based on this information, please generate a comprehensive research report following the structure in your instructions."""

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_prompt),
        ]

        # Generate report from LLM
        report_content = self._generate_from_llm(messages)

        return {
            "query": original_query,
            "report": report_content,
            "comparative_analysis": comparative_analysis,
        }

    def run(self, inputs):
        """
        Run the compare agent with the given inputs.

        Args:
            inputs (dict): Input dictionary containing summarized papers

        Returns:
            dict: Output dictionary containing comparative analysis and research report
        """
        summarized_papers = inputs.get("summarized_papers", [])
        original_query = inputs.get("original_query", "")
        expanded_keywords = inputs.get("expanded_keywords", {})

        if not summarized_papers:
            return {
                "error": "No summarized papers provided",
                "comparative_analysis": {},
                "research_report": "",
            }

        # Perform comparative analysis
        comparative_analysis = self.compare_papers(summarized_papers, original_query)

        # Generate comprehensive research report
        research_report = self.generate_research_report(
            comparative_analysis, summarized_papers, original_query, expanded_keywords
        )

        return {
            "comparative_analysis": comparative_analysis,
            "research_report": research_report,
        }


if __name__ == "__main__":
    # Example usage
    summarized_papers = [
        {
            "title": "Fine-tuning Large Language Models for Summarization",
            "authors": ["Author 1", "Author 2"],
            "publish_date": "2023-01-15",
            "summary": "This paper explores techniques for fine-tuning LLMs specifically for academic summarization tasks. The authors find that parameter-efficient methods like LoRA provide performance comparable to full fine-tuning at a fraction of the computational cost.",
        },
        {
            "title": "Evaluating LLM-generated Summaries of Scientific Papers",
            "authors": ["Author 3", "Author 4", "Author 5"],
            "publish_date": "2023-03-22",
            "summary": "The authors introduce novel evaluation metrics for assessing LLM-generated summaries of scientific papers, focusing on factual accuracy and coverage of key findings. They found that existing metrics like ROUGE correlate poorly with human judgments of quality.",
        },
    ]

    original_query = "LLMs for academic summarization"
    expanded_keywords = {
        "original_query": "LLMs for academic summarization",
        "expanded_keywords": {
            "core_keywords": ["LLM", "academic summarization", "research papers"],
            "related_keywords": ["natural language processing", "text summarization"],
            "query_analysis": "This research area focuses on applying Large Language Models to academic summarization tasks, which requires both high accuracy and preservation of complex information.",
        },
    }

    agent = CompareAgent(api_key="YOUR_API_KEY")  # Replace with your API key
    results = agent.run(
        {
            "summarized_papers": summarized_papers,
            "original_query": original_query,
            "expanded_keywords": expanded_keywords,
        }
    )

    print("Comparative analysis completed!")
    print(
        f"Research report generated with {len(results['research_report']['report'])} characters"
    )
