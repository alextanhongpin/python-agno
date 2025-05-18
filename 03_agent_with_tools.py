from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.tools.yfinance import YFinanceTools

agent = Agent(
    # https://docs.agno.com/reference/models/ollama#ollama
    model=Ollama(id="llama3.2", host="http://localhost:11434"),
    tools=[YFinanceTools(stock_price=True)],
    markdown=True,
)

agent.print_response(
    "What is the stock price of Apple?",
    stream=True,
    show_full_reasoning=True,
    stream_intermediate_steps=True,
)
