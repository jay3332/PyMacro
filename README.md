# pymacro
PyMacro is a partial wrapper around [pyautogui](https://pypi.org/project/PyAutoGUI/). PyMacro can automate your tasks all inside of Python - give it a try!
## Features
- Object oriented
- Extra utility functions
- Asynchronous support 
### Example Usage
```py
from pymacro import Macro

macro = Macro()
macro.type("Hello, world!", interval=.15)

macro.run(wait=2)
```
### Async Usage
```py
import asyncio
from pymacro import Macro

macro = Macro()
macro.type("Hello, world!", interval=.15)

async def run_macro():
    await macro.async_run(wait=2)

asyncio.run(run_macro())
```
### Executing Functions
```py
from pymacro import Macro

def fn():
    print("This function is running.")

macro = Macro()
macro.execute(fn, times=5)  # execute this function 5 times 

macro.run()
```