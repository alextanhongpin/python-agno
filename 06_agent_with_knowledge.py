from agno.agent import Agent
from agno.embedder.ollama import OllamaEmbedder
from agno.knowledge.url import UrlKnowledge
from agno.models.ollama import Ollama
from agno.tools.reasoning import ReasoningTools
from agno.vectordb.lancedb import LanceDb, SearchType

# Load Agno documentation in a knowledge base
knowledge = UrlKnowledge(
    urls=["https://docs.agno.com/introduction/agents.md"],
    vector_db=LanceDb(
        uri="tmp/lancedb",
        table_name="agno_docs",
        search_type=SearchType.hybrid,
        # Use Ollama for embeddings
        embedder=OllamaEmbedder(id="llama3.2", dimensions=3072),
    ),
)

agent = Agent(
    name="Agno Assist",
    model=Ollama(id="llama3.2", host="http://localhost:11434"),
    instructions=[
        "Use tables to display data.",
        "Include sources in your response.",
        # "Search your knowledge before answering the question.",
        "Use the search tool to answer the question.",
        "Only include the output in your response. No other text.",
    ],
    knowledge=knowledge,
    tools=[ReasoningTools(add_instructions=True)],
    add_datetime_to_instructions=True,
    markdown=True,
)

if __name__ == "__main__":
    # Load the knowledge base, comment out after first run
    # Set recreate to True to recreate the knowledge base if needed
    agent.knowledge.load(recreate=False)
    agent.print_response(
        "What are Agents?",
        stream=True,
        show_full_reasoning=True,
        stream_intermediate_steps=True,
    )
