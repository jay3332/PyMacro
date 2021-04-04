from pymacro import Macro

macro = Macro()
(
    macro
    .move_mouse_relative((50, 100), seconds=.5)
    .move_mouse_relative((-50, 100), seconds=.5)
    .move_mouse_relative((50, 100), seconds=.5)
    .move_mouse_relative((-50, 100), seconds=.5)
    .move_mouse_relative((50, 100), seconds=.5)
    .move_mouse_relative((-50, 100), seconds=.5)
    .move_mouse_relative((50, 100), seconds=.5)
    .move_mouse_relative((-50, 100), seconds=.5)
)

macro.run()
