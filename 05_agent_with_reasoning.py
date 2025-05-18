from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.tools.reasoning import ReasoningTools
from agno.tools.yfinance import YFinanceTools

agent = Agent(
    # https://docs.agno.com/reference/models/ollama#ollama
    model=Ollama(id="llama3.2", host="http://localhost:11434"),
    tools=[
        ReasoningTools(add_instructions=True),
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            company_info=True,
            company_news=True,
        ),
    ],
    instructions=[
        "Use tables to display data.",
        "Include sources in your response",
        "Only include the report in your response. No other text.",
    ],
    markdown=True,
)

agent.print_response(
    "Write a report on AAPL",
    stream=True,
    show_full_reasoning=True,
    stream_intermediate_steps=True,
)
