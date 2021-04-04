from inspect import iscoroutinefunction
from functools import partial
from .errors import *
from .effects import *
import pyautogui
import asyncio
import typing
import time


def _calc_coordinates(coords):
    if coords == ():
        return None, None
    if len(coords) == 1:
        coords = (coords[0], None)
    if len(coords) > 2:
        coords = coords[:2]
    return coords


class _EndRunner:
    def __init__(self, condition, wait):
        self.condition, self.wait = condition, wait


class Macro:
    def __init__(self):
        self.tasks = []
        self._register_aliases()

    def _register_aliases(self):
        self.hotkey = self.shortcut
        self.sleep = self.delay
        self.press = self.key_press
        self.scroll_y = self.scroll
        self.move = self.move_mouse
        self.move_rel = self.move_mouse_relative

    def delay(self, seconds: float = 1.):
        def _wrapper():
            time.sleep(seconds)

        self.tasks.append(_wrapper)
        return self

    def key_down(self, key):
        def _wrapper():
            pyautogui.keyDown(key)

        self.tasks.append(_wrapper)
        return self

    def key_up(self, key):
        def _wrapper():
            pyautogui.keyUp(key)

        self.tasks.append(_wrapper)
        return self

    def key_press(self, key, *, interval=0., presses=1):
        def _wrapper():
            pyautogui.press(key, interval=interval, presses=presses)

        self.tasks.append(_wrapper)
        return self

    def shortcut(self, *keys):
        def _wrapper():
            pyautogui.hotkey(*keys)

        self.tasks.append(_wrapper)
        return self

    def type(self, text, *, interval=0.):
        def _wrapper():
            pyautogui.typewrite(text, interval)

        self.tasks.append(_wrapper)
        return self

    def move_mouse(self, coordinates=(), seconds=0., effect=linear):
        def _wrapper():
            pyautogui.moveTo(*_calc_coordinates(coordinates), seconds, tween=effect)

        self.tasks.append(_wrapper)
        return self

    def move_mouse_relative(self, coordinates=(), seconds=0., effect=linear):
        def _wrapper():
            pyautogui.move(*_calc_coordinates(coordinates), seconds, tween=effect)

        self.tasks.append(_wrapper)
        return self

    def drag(self, coordinates=(), seconds=0., button="primary", effect=linear, *, mouse_down_up=True):
        def _wrapper():
            pyautogui.dragTo(*_calc_coordinates(coordinates), seconds, effect, button, mouse_down_up)

        self.tasks.append(_wrapper)
        return self

    def drag_relative(self, coordinates=(), seconds=0., button="primary", effect=linear, *, mouse_down_up=True):
        def _wrapper():
            pyautogui.dragRel(*_calc_coordinates(coordinates), seconds, effect, button, mouse_down_up)

        self.tasks.append(_wrapper)
        return self

    def mouse_down(self, button="primary", coordinates=(), effect=linear):
        def _wrapper():
            pyautogui.mouseDown(*_calc_coordinates(coordinates), button=button, tween=effect)

        self.tasks.append(_wrapper)
        return self

    def mouse_up(self, button="primary", coordinates=(), effect=linear):
        def _wrapper():
            pyautogui.mouseUp(*_calc_coordinates(coordinates), button=button, tween=effect)

        self.tasks.append(_wrapper)
        return self

    def click(self, button="primary", clicks: int = 1, interval=0., coordinates=(), effect=linear):
        def _wrapper():
            pyautogui.click(*_calc_coordinates(coordinates), clicks=clicks, interval=interval, button=button, tween=effect)

        self.tasks.append(_wrapper)
        return self

    def scroll(self, distance, coordinates=()):
        def _wrapper():
            pyautogui.scroll(distance, *_calc_coordinates(coordinates))

        self.tasks.append(_wrapper)
        return self

    def scroll_x(self, distance, coordinates=()):
        def _wrapper():
            pyautogui.hscroll(distance, *_calc_coordinates(coordinates))

        self.tasks.append(_wrapper)
        return self

    def execute(self, callback, times=1, interval=0., *args, **kwargs):
        def _wrapper():
            for _ in range(times):
                if iscoroutinefunction(callback):
                    _loop = asyncio.get_event_loop()
                    _loop.create_task(callback(*args, **kwargs))
                callback(*args, **kwargs)
                if interval > 0:
                    time.sleep(interval)

        self.tasks.append(_wrapper)
        return self


    def end(self, condition=True, wait=0.):
        self.tasks.append(_EndRunner(condition, wait))
        return self


    def run(self, *,
            repeat: int = 1,
            wait: typing.Union[float, int] = 0.,
            delay: typing.Union[float, int] = 0.,
            speed: typing.Union[float, int] = None,
            suppress: bool = True):
        """
        Runs the macro in it's current state.
        """
        if speed is not None and speed <= 0:
            raise SpeedError("Macro speed should be greater than 0.")

        if delay < 0:
            raise ValueError("Macro delay should be at least 0.")

        if wait < 0:
            raise ValueError("Macro wait should be at least 0.")

        if repeat < 0:
            raise ValueError("Macro repeat value should be positive, or 0 to repeat forever.")

        def _runner():
            for _task in self.tasks:
                if not isinstance(_task, _EndRunner):
                    _task()
                else:
                    if _task.condition:
                        if _task.wait > 0:
                            time.sleep(wait)
                        raise TaskEndError("Task ended early.")
                if speed is not None:
                    time.sleep(speed)
            if delay > 0:
                time.sleep(delay)

        try:
            if wait > 0:
                time.sleep(wait)
            if repeat == 1:
                _runner()
            elif repeat > 1:
                for _ in range(repeat):
                    _runner()
            elif repeat <= 0:
                while True:
                    _runner()
        except Exception as e:
            if suppress:
                return self
            raise TaskException(e)
        return self

    async def async_run(self, *args, **kwargs):
        _loop = asyncio.get_event_loop()
        _partial = partial(self.run, *args, **kwargs)
        return await _loop.run_in_executor(None, _partial)

    def __iter__(self):
        return iter(self.tasks)

    def __add__(self, other):
        if isinstance(other, Macro):
            return [*self.tasks, *other.tasks]

    def __iadd__(self, other):
        if isinstance(other, Macro):
            self.tasks.extend(other.tasks)
            return self.tasks

    def __call__(self, *args, **kwargs):
        self.run(*args, **kwargs)
