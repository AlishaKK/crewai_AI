from crewai import Agent, Task
import google.generativeai as genai
from setting import GEMINI_API_KEY

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# Greeting Agent
greeting_agent = Agent(
    name="Greeting Agent",
    role="Handles greeting requests",
    goal="Respond to user greetings in natural language",
    backstory="An AI specialized in recognizing and responding to greetings.",
    llm={"provider": "gemini/gemini-1.5-flash", "api_key": GEMINI_API_KEY}
)

# Greeting Task
greeting_task = Task(
    description="Respond to greetings like 'Hello', 'Hi', 'Good morning'.",
    agent=greeting_agent
)
