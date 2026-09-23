import asyncio
import logging
from pydantic import BaseModel, Field
from google.adk.agents.llm_agent import Agent
from google.adk.agents.sequential_agent import SequentialAgent

async def fast_tool() -> str:
    """Fast tool: pauses for 2 seconds, then returns 'value: 2'."""
    await asyncio.sleep(2)
    return "value: 2"


async def slow_tool() -> str:
    """Slow tool: pauses for 4 seconds, then returns 'value: 4'."""
    await asyncio.sleep(4)
    return "value: 4"

parallel_tool_agent = Agent(
    name="parallel_tool_agent",
    model="gemini-3.8-flash",
    description=(
        "Executes fast_tool and slow_tool in parallel."
    ),
    mode="single_turn",
    tools=[fast_tool, slow_tool],
    instruction="In a single turn, trigger BOTH `fast_tool` and `slow_tool`.",
)

multiplication_agent = Agent(
    name="multiplication_agent",
    model="gemini-3.8-flash",
    description="Multiplies value1 and value2.",
    mode="single_turn",
    instruction="Read and multiply the gathered values.",
)

root_agent = SequentialAgent(
    name="root_agent",
    sub_agents=[parallel_tool_agent, multiplication_agent],
)
