from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
import os
from dotenv import load_dotenv
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise ValueError(":x: GROQ_API_KEY is missing. Please set it in the .env file.")

web_agent = Agent(
    name="Web Agent",
    role="Search the web for information",
    model=Groq(id="llama-70b-8192", api_key=groq_api_key),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)
# Finance Agent using Groq
finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=Groq(id="llama-70b-8192", api_key=groq_api_key),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)
# Create a team of agents
agent_team = Agent(
    team=[web_agent, finance_agent],
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)
# Test the agent team
try:
    agent_team.print_response("Summarize analyst recommendations and share the latest news for NVDA", stream=True)
except Exception as e:
    print(":x: Error while fetching data:", e)