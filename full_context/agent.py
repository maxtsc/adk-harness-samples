from google.adk.agents.llm_agent import Agent
from google.adk.agents.sequential_agent import SequentialAgent

async def fetch_verbose_logs() -> str:
    """Simulates a 50,000-character raw log dump."""
    return "INFO: ok\n" * 5000 + "ERROR: Database timeout on shard 4\n"

incident_responder = Agent(
    name="incident_responder",
    model="gemini-3.8-flash",
    tools=[fetch_verbose_logs],
    mode="single_turn",
    # Drops the 50,000-character tool history from the model request
    include_contents="none",
    instruction="Propose a 1-sentence fix for this error.",
)

root_agent = SequentialAgent(
    name="root_agent",
    sub_agents=[incident_responder],
)