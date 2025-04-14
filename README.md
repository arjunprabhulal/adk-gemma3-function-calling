# 🤖 Gemma 3 Function Calling with Google ADK

A practical implementation demonstrating function calling (tool use) with Google's Gemma 3 model using the Google AI Development Kit (ADK) and Ollama. This project enables Gemma 3 to perform web searches using CrewAI tools wrapped for ADK compatibility.

![Gemma 3 Function Calling Demo](Images/adk-gemma3-functioncalling-demo.gif)

## 📚 Table of Contents

* [Introduction](#-introduction)
* [Architecture](#-architecture)
  * [Core Components](#-core-components)
  * [Technology Highlights](#-technology-highlights)
* [Features](#-features)
* [Core Concepts](#-core-concepts)
  * [ADK - Agent Development Kit](#adk---agent-development-kit)
  * [Agents in ADK](#agents-in-adk)
  * [Tools in ADK](#tools-in-adk)
  * [Ollama Integration](#ollama-integration)
* [Requirements](#-requirements)
* [Getting Started](#-getting-started)
  * [Installation Steps](#1-installation-steps)
  * [Setup](#2-setup)
  * [Usage](#3-usage)
* [How It Works](#-how-it-works)
* [Project Structure](#-project-structure)
* [Key Considerations](#-key-considerations)
* [Troubleshooting](#-troubleshooting)
* [Repository](#-repository)
* [Author](#-author)
* [License](#-license)

## 🔍 Introduction

This project showcases how to leverage Google's ADK (Agent Development Kit) to build an agent powered by Gemma 3, Google's latest large language model. It demonstrates how to:

- Connect to locally-hosted Gemma 3 via Ollama
- Implement function calling for web search capabilities
- Create a conversational agent that can access external data

## 🏗️ Architecture

### 🧩 Core Components

* **Google ADK** - Provides the agent framework
* **Gemma 3 (27B)** - Powers the language understanding and generation
* **Ollama** - Hosts the Gemma model locally
* **CrewAI Tools** - Provides web search capabilities
* **Python 3.12+** - Base runtime environment

### ✨ Technology Highlights

* **Google ADK**  
  Manages conversation flow and tool orchestration.
* **Gemma 3 via Ollama**  
  Delivers high-quality text generation with function calling capabilities.
* **LiteLlm Integration**  
  Connects ADK to Ollama-hosted models seamlessly.
* **Brave Search API**  
  Provides access to real-time web data through [Brave's Search API](https://brave.com/search/api/).

## 🚀 Features

* **Local LLM Integration** - Run Gemma 3 locally using Ollama
* **Function Calling** - Enable the model to use external tools
* **Web Search Capability** - Connect to Brave Search for real-time information
* **ADK Framework** - Leverage Google's agent development toolkit
* **Simple Command Line Interface** - Easy to use with straightforward queries

## 🧠 Core Concepts

### ADK - Agent Development Kit

**Agent Development Kit (ADK)** is an open-source, code-first Python toolkit for building intelligent AI agents. It provides the infrastructure needed to create agents that can interact with users, reason about tasks, and use tools to complete goals.

### Agents in ADK

An **Agent** in ADK acts as the orchestrator for AI interactions. In this project, we use **LlmAgent**, which is a core component in ADK acting as the "thinking" part of your application. According to [Google's ADK documentation](https://google.github.io/adk-docs/agents/llm-agents/), an LlmAgent:

- Leverages a Large Language Model (LLM) for reasoning and understanding
- Is non-deterministic (unlike workflow agents that follow predefined paths)
- Dynamically decides how to proceed and which tools to use
- Can be configured with an identity, instructions, and tools

The four key components of an LlmAgent are:

1. **Identity and Purpose** - Defined through `name`, `description`, and `model`
2. **Instructions** - Detailed guidance through the `instruction` parameter
3. **Tools** - Capabilities for external interactions via the `tools` parameter
4. **Configuration** - Fine-tuning with parameters like `generate_content_config`

### Tools in ADK

**Tools** in ADK are capabilities that agents can use to interact with external systems. In this project:

- We use **CrewaiTool** - A wrapper that adapts CrewAI's BraveSearchTool for use with ADK
- The tool has a clear name and description to help the model understand when and how to use it
- Our implementation follows best practices by providing detailed guidance on tool usage in the agent instructions

This implementation follows the [official Google ADK documentation for third-party tools](https://google.github.io/adk-docs/tools/third-party-tools/#2-using-crewai-tools), which provides guidance on integrating tools from frameworks like CrewAI into ADK agents.

### Ollama Integration

**Ollama** provides a way to run Gemma 3 and other large language models locally. Google ADK connects to Ollama through:

- **LiteLlm** - A wrapper that standardizes communication with different LLM providers
- The LiteLlm implementation uses the `litellm` library to communicate with Ollama

## 📋 Requirements

- Python 3.12+
- Ollama installed locally
- Gemma 3 (27B) model pulled via Ollama
- [Brave Search API](https://brave.com/search/api/) key (free tier available with 2,000 queries/month)

## 🚦 Getting Started

### 1. Installation Steps

Clone this repository:
```bash
git clone https://github.com/arjunprabhulal/adk-gemma3-function-calling.git
cd adk-gemma3-function-calling
```

### 2. Setup

#### Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### Install dependencies:
```bash
pip install google-adk
pip install "google-adk[extensions]"
```
# Note: This will install:
# - google-adk - Core Agent Development Kit
# - google-adk[extensions] - Additional extensions for ADK functionality

#### Set up your Brave Search API key:
```bash
export BRAVE_API_KEY=your_api_key_here
```
You can get your API key by signing up at [Brave Search API](https://brave.com/search/api/) - a free tier is available with up to 2,000 queries per month.

#### Pull the Gemma 3 model:
```bash
ollama pull gemma3:27b
```

### 3. Usage

There are multiple ways to interact with your agent:

#### Option 1: Web-based UI (Recommended for debugging)
Run the agent using ADK's browser-based developer UI:
```bash
# Navigate to the parent directory of the gemma3 package
cd adk-gemma3-function-calling

# Start the web interface
adk web
```

Then open the URL provided (usually `http://localhost:8000`) in your browser.
- Select "gemma3" from the dropdown menu in the top-left corner
- Type your query in the chat interface
- You can inspect function calls, model responses, and see detailed execution flow

This is particularly useful for debugging as it provides a visual representation of tool calls and responses.

#### Option 2: Terminal with ADK CLI (Recommended)
Run the agent directly in the terminal using ADK's command line interface:
```bash
# Navigate to the parent directory of the gemma3 package
cd adk-gemma3-function-calling

# Run the agent using ADK's CLI
adk run gemma3
```

This will start an interactive chat session in your terminal. Type your questions and the agent will respond, indicating when it's using tools.

To exit, use Cmd/Ctrl+C.

#### Option 3: API Server
Start a FastAPI server to interact with your agent via HTTP requests:
```bash
# Navigate to the parent directory of the gemma3 package
cd adk-gemma3-function-calling

# Start the API server
adk api_server
```

This enables you to test local cURL requests or integrate with other applications, which is useful for development and testing before deployment.

## 🔄 How It Works

The implementation follows these steps:

1. **Agent Initialization**:
   - Creates an LlmAgent with a reference to the Ollama-hosted Gemma 3 model
   - Configures the agent with appropriate instructions
   - Adds the web search tool to the agent's capabilities

2. **Tool Definition**:
   - Defines a BraveSearchTool instance from CrewAI
   - Wraps it with CrewaiTool for ADK compatibility using the pattern:
     ```python
     from google.adk.tools.crewai_tool import CrewaiTool
     from crewai_tools import BraveSearchTool
     
     # Instantiate the CrewAI tool (requires BRAVE_API_KEY env var)
     search_tool_instance = BraveSearchTool()
     
     # Wrap it with CrewaiTool for ADK, providing name and description
     search_tool = CrewaiTool(
         name="web_search",
         description="Searches the internet using Brave Search to find current information.",
         tool=search_tool_instance
     )
     ```
   - The ADK documentation emphasizes providing clear name and description to help the model understand when to use the tool

3. **Query Processing**:
   - User query is passed to the agent
   - Gemma 3 decides whether to use the search tool based on the query
   - If needed, the model formulates an appropriate search query
   - Results are incorporated into the final response

4. **Response Generation**:
   - The agent processes all information and generates a coherent response
   - Output is returned to the user in natural language

## 📁 Project Structure

Following the structure recommended in the [ADK documentation](https://google.github.io/adk-docs/get-started/quickstart/):

```
adk-gemma3-function-calling/
├── gemma3/
│   ├── __init__.py         # Package initialization (imports agent.py)
│   └── agent.py            # Agent implementation with ADK
├── .gitignore              # Git ignore file
├── README.md               # Project documentation
└── requirements.txt        # Dependencies
```

## 🔄 Key Considerations

1. **Model Selection**
   - Gemma 3 (27B) provides a good balance of performance and efficiency for local deployment.
   - Ensure your system has adequate GPU resources to run the model effectively.

2. **Tool Description**
   - The quality of tool use depends on clear, concise tool descriptions.
   - For best results, make sure tool descriptions explain exactly what the tool does and when to use it.

3. **API Credentials**
   - Keep your Brave Search API key secure.
   - Consider using a proper secrets management approach for production deployments.

4. **Ollama Configuration**
   - Ensure Ollama is running and accessible before starting the agent.
   - Monitor Ollama's resource usage, especially for the 27B parameter model.

## ⚠️ Troubleshooting

1. **Model Loading Issues**:
   - Ensure Ollama is running: `ollama list` should show the gemma3:27b model.
   - If the model fails to load, try: `ollama pull gemma3:27b` again.

2. **API Key Issues**:
   - Verify your Brave API key is correctly set in the environment.
   - Test the API key independently to ensure it's valid.

3. **Memory Constraints**:
   - The 27B model requires significant RAM/VRAM.
   - Consider using a smaller model like gemma3:7b if experiencing memory issues.

4. **Function Calling Problems**:
   - If the model doesn't use tools properly, try making the tool description more explicit.
   - Ensure your query clearly requires external information.

5. **LiteLLM/Ollama KeyError Bug**:
   - There's a known issue with Ollama's JSON format responses and LiteLLM's parsing that can cause a KeyError: 'name' error.
   - This happens when Ollama returns JSON format that isn't specifically a tool call format.
   - Error looks like: `KeyError: 'name'` in `litellm/llms/ollama/completion/transformation.py`
   - A fix has been submitted in [PR #9966](https://github.com/BerriAI/litellm/pull/9966) for the LiteLLM package but is still pending approval and merging.
   - This bug might cause your application to crash or enter an infinite loop when using function calling with Ollama models.
   - **Temporary workarounds**:
     - Manually patch your local LiteLLM installation with the changes from PR #9966
     - Avoid using `format=json` in Ollama requests if possible
     - Wait for the PR to be merged and update to the next LiteLLM release that includes the fix

## 📦 Repository

This project is available on GitHub at [arjunprabhulal/adk-gemma3-function-calling](https://github.com/arjunprabhulal/adk-gemma3-function-calling).

For another related project on ADK with MCP, check out [arjunprabhulal/adk-python-mcp-client](https://github.com/arjunprabhulal/adk-python-mcp-client).

## 👨‍💻 Author

Created by Arjun Prabhulal. For more articles on AI/ML and Generative AI, follow [Arjun Prabhulal on Medium](https://medium.com/@arjun-prabhulal).

## 📄 License

MIT 