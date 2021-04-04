from pymacro import Macro

macro = Macro()
macro.type("hello")
macro.press("enter")

macro.run(repeat=0, delay=1, wait=5)
