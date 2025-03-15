import chainlit as cl
from frontend_agent import frontend_agent, orchestration_task
from greeting_agent import greeting_task

@cl.on_message
async def chat(message):
    """Handles chat interaction in Chainlit."""
    user_message = message.content.lower()

    # Check if message is a greeting
    greetings = ["hello", "hi", "good morning", "good evening", "how are you"]
    
    if any(greet in user_message for greet in greetings):
        response = greeting_task.execute()
    else:
        response = "I only handle greetings right now."

    await cl.Message(content=response).send()
