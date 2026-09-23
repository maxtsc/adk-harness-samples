import asyncio
import logging
from pydantic import BaseModel, Field
from google.adk.agents.llm_agent import Agent

async def fast_tool() -> str:
    """Fast tool: pauses for 2 seconds, then returns 'value: 2'."""
    await asyncio.sleep(2)
    return "value: 2"


async def slow_tool() -> str:
    """Slow tool: pauses for 4 seconds, then returns 'value: 4'."""
    await asyncio.sleep(4)
    return "value: 4"

sequential_tool_agent = Agent(
    name="sequential_tool_agent",
    model="gemini-3.8-flash",
    description=(
        "Executes fast_tool and slow_tool sequentially."
    ),
    mode="single_turn",
    tools=[fast_tool, slow_tool],
    instruction="""You are the sequential tool execution agent.
        Execute the tools and parse the results.""",
)

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

root_agent = Agent(
    name="root_agent",
    model="gemini-3.8-flash",
    description=(
        "Root coordinator that delegates tool execution to either the sequential "
        "or parallel agent based on user instruction, and then always calls the "
        "multiplication agent to return the final result."
    ),
    sub_agents=[sequential_tool_agent, parallel_tool_agent, multiplication_agent],
    instruction="""Your workflow:
    1/ If the user specifies "sequential" call `sequential_tool_agent`.
    If the user specifies "parallel" call `parallel_tool_agent`.
    2/ Afterwards, call `multiplication_agent` to multiply the values."""
)
