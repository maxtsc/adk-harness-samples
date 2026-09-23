from google.adk.agents.llm_agent import Agent
from google.adk.agents.parallel_agent import ParallelAgent
from google.adk.agents.sequential_agent import SequentialAgent

security_reviewer = Agent(
    name="security_reviewer",
    model="gemini-3.8-flash",
    mode="single_turn",
    output_key="security_notes",
    instruction="List 1 security risk in the snippet in under 15 words.",
)

performance_reviewer = Agent(
    name="performance_reviewer",
    model="gemini-3.8-flash",
    mode="single_turn",
    output_key="perf_notes",
    instruction="List 1 latency bottleneck in the snippet in under 15 words.",
)

parallel_review = ParallelAgent(
    name="parallel_review",
    sub_agents=[security_reviewer, performance_reviewer],
)

synthesizer = Agent(
    name="synthesizer",
    model="gemini-3.8-flash",
    mode="single_turn",
    instruction="Combine findings:\nSecurity: {security_notes}\nPerf: {perf_notes}",
)

root_agent = SequentialAgent(
    name="root_agent",
    sub_agents=[parallel_review, synthesizer],
)