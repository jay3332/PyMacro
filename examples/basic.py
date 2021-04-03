import pymacro

macro = pymacro.Macro()
macro.move_mouse((1024, 700), seconds=0.5)
macro.click("left")

macro.run(repeat=1, delay=0.1, speed=0.01)

# In async situations:
import asyncio

async def run():
    await macro.async_run()

asyncio.run(run())
