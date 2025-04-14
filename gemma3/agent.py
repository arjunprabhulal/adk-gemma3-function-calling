from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
from crewai_tools import BraveSearchTool
from google.adk.tools.crewai_tool import CrewaiTool


# Instantiate the CrewAI tool
search_tool_instance = BraveSearchTool() # Assumes SERPAPI_API_KEY is in env

# Wrap it with CrewaiTool for ADK, providing name and description
search_tool = CrewaiTool(
    name="web_search",
    description="Searches the internet using SerpApi.",
    tool=search_tool_instance
)

# Define the ADK agent (Main focus of this file)
root_agent = LlmAgent(
    name="crewai_search_agent",
    model=LiteLlm(model="ollama/gemma3:27b"), 
    description="Agent to answer questions using Google Search.",
    instruction="Use the `search_tool` tool if needed to find current information, then concisely summarize the findings to answer the user; do not output raw tool data.",
    tools=[search_tool]
)

