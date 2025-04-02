from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
import os
import dotenv

dotenv.load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")

agent = Agent(
    model=Gemini(id="gemini-2.0-flash"),
    tools=[DuckDuckGo()],
    markdown=True,
)

agent.print_response(
    "Tell me about this image and give me the latest news about it.",
    images=["https://upload.wikimedia.org/wikipedia/commons/b/bf/Krakow_-_Kosciol_Mariacki.jpg"],
    stream=True,
)