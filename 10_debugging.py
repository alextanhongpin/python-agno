from agno.agent import Agent
from agno.models.ollama import Ollama

agent = Agent(markdown=True, model=Ollama(id="llama3.2"), debug_mode=True)
agent.print_response("Share a 2 sentence horror story")
