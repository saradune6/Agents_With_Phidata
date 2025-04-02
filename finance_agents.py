from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools

import os
import dotenv

dotenv.load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

finance_agent = Agent(
    name="Finance Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)
finance_agent.print_response("Summarize analyst recommendations for NVDA", stream=True)