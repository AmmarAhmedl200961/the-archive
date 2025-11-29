"""
KeywordAgent Module
This agent is responsible for expanding user-provided research keywords to improve search coverage.
"""

from langchain_core.messages import HumanMessage, SystemMessage
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import together


class KeywordAgent:
    """
    Agent for expanding user queries into comprehensive search terms.
    Uses LLMs to generate related keywords and research concepts.
    """

    def __init__(self, model="meta-llama/Llama-3-8B-hf", api_key=None):
        """
        Initialize the KeywordAgent.

        Args:
            model (str): Model ID to use for keyword expansion
            api_key (str): API key for LLM service (e.g., Together.ai)
        """
        self.model = model
        self.api_key = api_key
        self.client = None

        if api_key:
            self.client = together.Together(api_key=api_key)

    def expand_keywords(self, query):
        """
        Expand a user query into a comprehensive set of search terms.

        Args:
            query (str): The user's original research query

        Returns:
            dict: Dictionary containing expanded keywords and query analysis
        """
        # Define the system prompt for keyword expansion
        system_prompt = """You are an expert academic research assistant specializing in keyword expansion.
Your task is to analyze the user's research query and expand it into a comprehensive set of search terms.
These should include:
1. Core concepts from the original query
2. Related academic terminology and synonyms
3. Broader conceptual areas that encompass the query
4. Narrower, more specific subtopics relevant to the query
5. Methodological terms that might be relevant
6. Key authors or seminal papers in this field (if applicable)

Format your response as a structured JSON with these sections:
- core_keywords: List of the most important keywords from the original query
- related_keywords: List of synonyms and closely related concepts
- broader_concepts: List of more general areas that include this topic
- narrower_concepts: List of more specific subtopics
- methodological_terms: List of research methods or approaches relevant to this area
- query_analysis: A brief analysis of the research domain and what makes it significant

Keep each list to 3-5 high-value terms that would yield the most relevant search results.
"""

        # Create the prompt for the model
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=f"Research query: {query}"),
        ]

        response = self._generate_from_llm(messages)

        # Extract JSON data from response
        try:
            import json
            import re

            # Look for JSON-like structure in the response
            json_match = re.search(r"```json\n(.*?)\n```", response, re.DOTALL)
            if json_match:
                json_str = json_match.group(1)
            else:
                json_str = response

            # Clean up any markdown or non-JSON content
            json_str = re.sub(r"^```json\s*", "", json_str)
            json_str = re.sub(r"\s*```$", "", json_str)

            expanded_keywords = json.loads(json_str)

        except Exception as e:
            print(f"Error parsing JSON from LLM response: {e}")
            print(f"Raw response: {response}")

            # If JSON parsing fails, create a simple structured response
            expanded_keywords = {
                "core_keywords": query.split(),
                "related_keywords": [],
                "broader_concepts": [],
                "narrower_concepts": [],
                "methodological_terms": [],
                "query_analysis": "Failed to parse detailed analysis from LLM.",
            }

        return {"original_query": query, "expanded_keywords": expanded_keywords}

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
                temperature=0.2,
                max_tokens=1000,
            )
            return response.choices[0].message.content
        else:
            # Use LangChain with OpenAI (fallback)
            llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.2)
            response = llm.invoke(messages)
            return response.content

    def run(self, inputs):
        """
        Run the keyword expansion agent with the given inputs.

        Args:
            inputs (dict): Input dictionary containing the query

        Returns:
            dict: Output dictionary containing expanded keywords and analysis
        """
        query = inputs.get("query", "")
        if not query:
            return {"error": "No query provided", "expanded_keywords": {}}

        result = self.expand_keywords(query)
        return result


if __name__ == "__main__":
    # Example usage
    agent = KeywordAgent(api_key="YOUR_API_KEY")  # Replace with your API key
    result = agent.run({"query": "LLMs for academic summarization"})
    print(result)
