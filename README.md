🦜🕸️ LangGraph & Complex AI Agents in Python

Welcome to my LangGraph & AI Agents repository! 🚀 This project contains hands-on code, workflows, and stateful multi-agent systems built while following the LangGraph Complete Course for Beginners by freeCodeCamp.

📌 Overview

This project explores building production-grade, stateful, multi-agent LLM applications using LangGraph and Python. LangGraph extends LangChain to enable cyclic graphs, flexible state management, human-in-the-loop interactions, and robust agent orchestration.

✨ Features & Concepts Covered

🧠 Stateful Agent Workflows: Persistent state management across multiple execution cycles.

🔄 Cyclic & Multi-Agent Graphs: Nodes, edges, and conditional routing for complex decision-making loops.

🛠️ Tool Integration & Calling: Equipping agents with external custom tools and APIs.

👤 Human-in-the-Loop (HITL): Interrupting graph execution for human approval/validation.

💾 Persistence & Checkpointing: Resuming conversations and workflow states effortlessly.

🔀 Conditional Routing: Dynamic paths based on intermediate agent outputs.

🛠️ Tech Stack & Prerequisites

Language: Python 3.10+ 🐍

Frameworks & Libraries:

langgraph 🦜🕸️

langchain / langchain-community

langchain-openai / langchain-anthropic (or local LLM integrations)

pydantic (Data validation & structured output)

🚀 Quick Start

1. Clone the Repository

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name


2. Set Up Virtual Environment

python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate


3. Install Dependencies

pip install -r requirements.txt


4. Configure Environment Variables

Create a .env file in the root directory:

OPENAI_API_KEY=your_openai_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here  # Optional for web search tool
LANGCHAIN_TRACING_V2=true                 # Optional for LangSmith debugging
LANGCHAIN_API_KEY=your_langsmith_key


5. Run the Project

python main.py


📂 Project Structure

.
├── agents/             # Custom agent definitions and prompts
├── tools/              # Custom tools & utilities for agents
├── workflows/          # LangGraph graph definitions (nodes, edges, state)
├── main.py             # Entry point for execution
├── requirements.txt    # Project dependencies
├── .env.example        # Environment variable template
└── README.md           # Project documentation


🎓 Acknowledgments & Resources

📺 Course Video: LangGraph Complete Course for Beginners – Complex AI Agents with Python (freeCodeCamp)

📚 LangGraph Documentation: langchain-ai.github.io/langgraph

⭐ If you find this repository helpful, feel free to give it a star!
