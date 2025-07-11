from agno.agent import Agent
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.manager import MemoryManager
from agno.memory.v2.memory import Memory
from agno.models.ollama import Ollama
from rich.pretty import pprint

user_id = "john_doe"
memory = Memory(
    db=SqliteMemoryDb(table_name="memory", db_file="tmp/memory.db"),
    model=Ollama(id="llama3.2", host="http://localhost:11434"),
)
memory.clear()


agent = Agent(
    model=Ollama(id="llama3.2", host="http://localhost:11434"),
    user_id=user_id,
    memory=memory,
    # Enable the agent to dynamically create and manager user memories.
    enable_agentic_memory=True,
    add_datetime_to_instructions=True,
    markdown=True,
)

if __name__ == "__main__":
    agent.print_response("My name is John Doe and I like to eat carrots.")
    memories = memory.get_user_memories(user_id=user_id)
    print(f"Memories about {user_id}:")
    pprint(memories)
    agent.print_response("What is my favorite food?")
    agent.print_response("My best friend is Jemima Puddleduck.")
    print(f"Memories about {user_id}:")
    pprint(memories)
    agent.print_response("Recommend a good lunch meal, who should i invite?")
