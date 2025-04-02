from phi.agent import Agent
from phi.model.google import Gemini
from phi.storage.agent.sqlite import SqlAgentStorage
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from phi.model.groq import Groq
from phi.playground import Playground, serve_playground_app


import os
import dotenv

dotenv.load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")


web_agent = Agent(
    name="Web Agent",
    model=Groq(id="gemma2-9b-it"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    storage=SqlAgentStorage(table_name="web_agent", db_file="agents.db"),
    add_history_to_messages=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    instructions=["Use tables to display data"],
    storage=SqlAgentStorage(table_name="finance_agent", db_file="agents.db"),
    add_history_to_messages=True,
    markdown=True,
)

app = Playground(agents=[finance_agent, web_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)