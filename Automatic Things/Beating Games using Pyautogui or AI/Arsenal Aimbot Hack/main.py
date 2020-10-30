import threading
import time as t
import numpy as np
from PIL import ImageGrab
import cv2
from mouse import on_click
from pynput.mouse import Controller
from pynput.keyboard import Listener, KeyCode


delay = 0
start_stop_key = KeyCode(char='`')
exit_key = KeyCode(char='~')


class AimBot(threading.Thread):
    def __init__(self, delay):
        super(AimBot, self).__init__()
        self.delay = delay
        self.running = False
        self.program_running = True

    def start(self):
        self.running = True

    def stop(self):
        self.running = False

    def exit(self):
        self.stop()
        self.program_running = False
        cv2.destroyAllWindows()

    def on_click(self, x, y, button, pressed):  # must need 4 args
        while self.program_running:
            while self.running:
                if pressed:
                    print(f"Mouse clicked at ({x}, {y}) with {button}")

    def screen_looks_at_you_while_you_sleep(self):
        while True:
            print_screen = np.array(ImageGrab.grab(bbox=(0, 40, 800, 640)))
            cv2.imshow('Aimbot Hack LMAO', cv2.cvtColor(print_screen, cv2.COLOR_BGR2RGB))
            last_time = t.time()
            print(f"loop took {t.time() - last_time} seconds")
            """if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break"""


mouse = Controller
aimbot_thread = AimBot(delay)
aimbot_thread.start()


def on_press(key):
    if key == start_stop_key:
        if aimbot_thread.running:
            aimbot_thread.stop()
        aimbot_thread.start()
    elif key == exit_key:
        aimbot_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()

with Listener(on_click=on_click) as listener:
    listener.join()
