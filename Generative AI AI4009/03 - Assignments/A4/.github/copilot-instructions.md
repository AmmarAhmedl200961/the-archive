# Copilot Instructions

This project involves building a **Smart Summarizer** and a **Multi-Agent Autonomous Research Assistant**.

**Application Name:** Smart Summarizer and Multi-Agent Autonomous Research Assistant

**Application Purpose:**
The Smart Summarizer focuses on fine-tuning a Large Language Model (LLM) using LoRA for accurate and efficient summarization of academic research papers. The Multi-Agent Autonomous Research Assistant uses a multi-agent system orchestrated with LangGraph to automate the academic research process, including keyword expansion, paper retrieval, ranking, summarization (using the fine-tuned model), and comparative analysis.

**Technologies Used:**
* Large Language Models (LLMs)
* LoRA (Low-Rank Adaptation)
* HuggingFace PEFT library
* Streamlit or Gradio (for UI)
* LangChain
* LangGraph
* Academic Search APIs (e.g., arXiv, Semantic Scholar, PubMed)
* arxiv api test https://export.arxiv.org/api/query?search_query=all:LLM&start=0&max_results=10
* Together.ai API (for LLM-as-a-Judge and possibly other LLM calls)
* ROUGE, BLEU, BERTScore (for evaluation metrics)
* Python Notebook (Jupyter)

**Best Practices:**

**General:**
* Write clear, concise, and well-documented code.
* Use meaningful variable and function names.
* Break down complex tasks into smaller, manageable functions or modules.
* Implement error handling and validation where necessary.
* Write unit tests for critical components.

** Keep in mind the following **Helping** topics that i found on YouTube(do not apply just know them)**
* Report mAIstro: Multi-agent research and report writing
  Research + Summarization was the most popular agent use case in our recent State of AI Agents survey of 1300 professionals. But how do you design agents for high-quality research and report distillation? In this video, we share key insights and show how we built Report mAIstro, an agent capable of web research and high quality report writing. 

    Report mAIstro simply:
    1. Takes a topic (and optional report structure)
    2. Builds an outline
    3. Parallelizes research + writing across sections

    You'll see various report examples and learn how to configure assistants for different report types.

    Code:
    https://github.com/langchain-ai/open_deep_research

* LangGraph: Multi-Agent Workflows
  LangGraph makes it easy to construct multi-agent workflows, where each agent is a node, and the edges define how they communicate. In this video we will walk through three examples of multi-agent workflows 
  https://github.com/langchain-ai/langgraph/tree/main/examples/multi_agent

* 🌟 *Langchain Agents: Advanced Multi-Agent Workflow w/ LangGraph & LangSmith Tavily Search Tool & Memory* 🌟

    🚀 Welcome to this in-depth tutorial on creating *Advanced Multi-Agent Workflows* using *LangGraph**, **LangSmith**, and powerful tools like **Tavily Search* and **Memory Integration**. In this video, I break down a sophisticated agent orchestration that leverages reflection workflows to create high-quality, well-researched outputs. If you're diving into **Langchain Agents**, this video is a must-watch!

    ---

    🔍 *What You'll Learn:*

    1️⃣ **Understanding the Multi-Agent Workflow**:
    Explore the *Reflection Agent Orchestration* through a detailed diagram (see above).
    Learn how tasks are divided among specialized agents:
    **Planner Agent**: Breaks down tasks into actionable plans.
    **Plan Researcher**: Fetches real-time data using the **Tavily Search Tool**.
    **Generate Agent**: Produces content like essays or reports (powered by **GPT-4o**).
    **Reflection Agent**: Refines the output iteratively for optimal results.

    2️⃣ **Workflow Explained**:
    Understand *normal edges* and *conditional edges* that define agent flows.
    Learn how *task and plan data* flow seamlessly between agents.
    Dive into the *iteration loop* where the Reflection Agent enhances outputs based on critiques and revisions.

    3️⃣ **Building the Orchestration**:
    Step-by-step guide to setting up the orchestration using *LangGraph* methods and classes.
    Use Langchain v0.3+ to create modular and maintainable workflows.

    4️⃣ **Integrating Tools and Memory**:
    How to connect the *Tavily Search Tool* for real-time web data retrieval.
    Add *memory nodes* to provide contextual understanding for agents during iterations.

    5️⃣ **Verbose Reporting and Debugging**:
    Custom verbose functions to visualize the agent's actions and thought process.
    Use *LangSmith* for enhanced debugging and workflow tracing.

    6️⃣ **Live Demo in Google Colab**:
    Hands-on demonstration of the agent orchestration in action.
    Watch how the workflow generates, critiques, and refines outputs based on real-world scenarios.

    ---

    💡 **Key Features of This Orchestration**:
    **Dynamic Task Management**: Efficient division of tasks among specialized agents.
    **Reflection-Based Workflow**: Iterative improvements ensure high-quality outputs.
    **Memory Integration**: Adds context and continuity to multi-step tasks.
    **Web Data Retrieval**: Seamless integration of search tools for real-time insights.

    ---

* In this video, we walk through a powerful use case of LangGraph Intro – Multi Agent Research Pipelines and Report Writing with LangGraph, where multiple AI agents work together in a research pipeline. From asking questions to collecting data and generating structured reports, you’ll see how to coordinate autonomous agents using the map-reduce pattern and LangGraph’s flexible pipeline design.

  Perfect for anyone exploring how to build AI agents, this is part of the “Building AI Agents with LangGraph: A Beginner’s Guide | Agentic AI Course.” We’ll use concepts like mapReduce, pipeline logic, multi-agent systems, and LangGraph Studio, all while sticking to a generic agent architecture.

  Whether you’re learning langgraph, diving into ai agent tutorials, or curious about what is langchain, this is a hands-on guide you don’t want to miss.

    00:00 – Intro to the Research Pipeline  
    02:06 – Defining the Analyst Role  
    04:17 – Creating Analyst Team via LLM  
    09:31 – Expert Interview Subgraph  
    18:38 – Mapping Step: Running Interviews in Parallel  
    21:34 – Reduce Step: Technical Writer Agent  
    23:35 – Running the Full Graph  


**LLMs and Fine-tuning:**
* Carefully manage data preprocessing and tokenization to ensure compatibility with the chosen LLM.
* Monitor training progress using metrics like loss curves.
* Experiment with LoRA configuration parameters if needed, but start with the recommended values (r=8, alpha=16, dropout=0.1, apply to q and v).
* Save model checkpoints regularly during training.
* Be mindful of computational resources and consider using techniques like gradient accumulation or mixed precision training if necessary.

**LangChain/LangGraph:**
* Clearly define the roles and responsibilities of each agent in the multi-agent system.
* Design the graph structure in LangGraph to represent the flow of information and tasks between agents.
* Use clear and specific prompts for LLM calls within agents to guide their behavior.
* Implement robust parsing of agent outputs to ensure correct data flow.

**Streamlit/Gradio:**
* Keep the user interface simple and intuitive.
* Provide clear instructions for users.
* Handle file uploads securely and efficiently.
* Display results clearly and allow for easy comparison where applicable.

**Evaluation:**
* Implement both automatic (ROUGE, BLEU, BERTScore) and qualitative (LLM-as-a-Judge) evaluation methods.
* Use a consistent and well-defined prompt format for the LLM-as-a-Judge.
* Carefully select the LLM to be used as the judge, considering its capabilities and cost.

**Documentation Search:**
* To search the documentation for specific libraries or concepts, use the `#fetch` command followed by the URL. For example, to search the LangChain documentation, you could use `#fetch<https://python.langchain.com/docs/get_started/introduction>` (replace with the actual relevant URL). Similarly for LangGraph or other libraries.