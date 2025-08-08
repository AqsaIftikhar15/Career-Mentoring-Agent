from configuration import config
from agents_needed.career_agent import CareerAgent
from chainlit import on_message , Message
from agents import Runner

@on_message
async def on_message(msg):
    runner = Runner()  # no arguments
    result = await runner.run(
        starting_agent=CareerAgent,
        input=msg.content,
        max_turns=150
    )
    await Message(content=result.final_output).send()