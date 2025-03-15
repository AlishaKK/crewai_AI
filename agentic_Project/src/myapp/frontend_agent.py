from crewai import Agent, Task
from greeting_agent import greeting_task
from setting import GEMINI_API_KEY

# Front-End Agent
frontend_agent = Agent(
    name="Front-End Agent",
    role="Routes user input to the correct agent",
    goal="Understand user intent and forward messages accordingly",
    backstory="An AI designed to delegate user queries.",
    llm={"provider": "gemini/gemini-1.5-flash", "api_key": GEMINI_API_KEY}
)

# Orchestration Task
orchestration_task = Task(
    description="Identify user intent and route to the Greeting Agent if necessary.",
    agent=frontend_agent,
    expected_output="A response from the Greeting Agent, if the message is a greeting."
)
