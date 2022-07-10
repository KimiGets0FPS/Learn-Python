import time
from pyautogui import moveTo, mouseDown, mouseUp, keyDown, keyUp
import threading
from pynput.keyboard import Listener, KeyCode

e = "e"
start_stop_key = KeyCode(char='u')
exit_key = KeyCode(char='o')
delay = 0.001
button = 'e'


class Macro(threading.Thread):
    def __init__(self, delay, button):  # variable delay and button is useless, but it's needed for the thread thing
        super(Macro, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_macro(self):
        self.running = True

    def stop_macro(self):
        self.running = False

    def exit(self):
        self.stop_macro()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouseDown()

                # Top Layer

                while ...:
                    keyDown("w")
                    time.sleep(40)
                    keyUp("w")
                    keyDown("s")
                    time.sleep(40)
                    keyUp("s")
                    keyDown("d")
                    time.sleep(0.25)
                    keyUp("d")

                # Bottom Layer

                keyDown("shift")
                time.sleep(0.15)
                keyUp("shift")

                while ...:
                    ...
        mouseUp()


macro = Macro(delay, button)
macro.start()


def on_press(key):
    if key == start_stop_key:
        if macro.running:
            macro.stop_macro()
        else:
            macro.start_macro()
    elif key == exit_key:
        macro.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()
