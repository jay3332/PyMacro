# pymacro
PyMacro is a partial wrapper around [pyautogui](https://pypi.org/project/PyAutoGUI/). PyMacro can automate your tasks all inside of Python - give it a try!
## Features
- Object oriented
- Extra utility functions
- Asynchronous support 
## Installation
PyMacro can be easily downloaded with PIP:
```
pip install pymacro
```
You can install the latest version from this repository, too:
```
pip install git+https://github.com/jay3332/PyMacro
```
## Example Usage
### Basic Usage
```py
from pymacro import Macro

macro = Macro()
macro.type("Hello, world!", interval=.15)

macro(wait=2)
```
### Mouse/keyboard Macros
```py
from pymacro import Macro

macro = Macro()
macro.move_mouse_relative((0, 50), seconds=0.5)
macro.click()
macro.key_press("enter")

macro(wait=0.5)
```
### Repeat Macro Indefinitely
```py 
from pymacro import Macro

macro = Macro()
macro.click()

macro(wait=0.5, repeat=0, delay=0.1)

# Wait 0.5 seconds before starting the macro.
# Repeating 0 times tells pymacro to repeat this macro forever without end.
# Delay of 0.1 means to wait 0.1 seconds between every iteration of the loop.
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

macro()
```
### Multiple Macros at once with asyncio
```py
import pymacro
import asyncio

macro1 = pymacro.Macro()
macro2 = pymacro.Macro()

def print_one_to_ten():
    for i in range(1, 11):
        print(i)

macro1.execute(print_one_to_ten)
macro2.execute(print_one_to_ten)

loop = asyncio.get_event_loop()
loop.create_task(macro1.async_run())
loop.create_task(macro2.async_run())
```
## Tips
### Special Functions
```py
import pymacro
macro = pymacro.Macro()

# Functions
macro.execute(function, times=1, interval=0, *args, **kwargs)

# End the macro early 
macro.end(condition=True, wait=0)

macro()
```
