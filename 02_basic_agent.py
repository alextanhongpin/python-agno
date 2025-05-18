from agno.agent import Agent
from agno.models.ollama import Ollama

agent = Agent(
    # https://docs.agno.com/reference/models/ollama#ollama
    model=Ollama(id="llama3.2", host="http://localhost:11434"),
    markdown=True,
)

agent.print_response(
    "What is the stock price of Apple?",
    stream=True,
    show_full_reasoning=True,
    stream_intermediate_steps=True,
)
