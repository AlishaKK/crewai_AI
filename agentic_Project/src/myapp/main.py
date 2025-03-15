 
from fastapi import FastAPI
from pydantic import BaseModel
from frontend_agent import frontend_agent, orchestration_task
from greeting_agent import greeting_agent, greeting_task

app = FastAPI()

# Define request body model
class UserMessage(BaseModel):
    message: str

@app.post("/chat")
def chat(user_input: UserMessage):
    """Handles user messages and routes them to the correct agent."""
    message = user_input.message.lower()

    greetings = ["hello", "hi", "good morning", "good evening", "how are you"]
    
    if any(greet in message for greet in greetings):
        response = greeting_task.execute()
    else:
        response = "I only handle greetings right now."

    return {"response": response}
