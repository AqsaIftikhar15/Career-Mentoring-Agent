from configuration import config
from agents_needed.career_agent import CareerAgent
from chainlit import on_message , Message
from agents import Runner
import os
import chainlit as cl

@on_message
async def on_message(msg):
    runner = Runner()  
    result = await runner.run(
        starting_agent=CareerAgent,
        input=msg.content,
        max_turns=150
    )
    await Message(content=result.final_output).send()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    cl.run(port=port, host="0.0.0.0")