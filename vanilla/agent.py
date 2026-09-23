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

root_agent = Agent(
    model='gemini-3.8-flash',
    name='root_agent',
    description='vanilla agent',
    tools=[fast_tool, slow_tool],
    instruction="Call both tools,"
    "then multiply the results,"
    "and present the final answer to the user"
)