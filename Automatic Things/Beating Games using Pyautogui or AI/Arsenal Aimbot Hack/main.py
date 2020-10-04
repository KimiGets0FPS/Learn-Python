# import keyboard as kb
import threading
from pynput.keyboard import Listener, KeyCode
import time as t
import numpy as np
from PIL import ImageGrab
import cv2
# import pyautogui as pyag

delay = 0
start_stop_key = KeyCode(char='del')
exit_key = KeyCode(char='`')


class Main(threading.Thread):
    def __init__(self, delay):
        super(Main, self).__init__()
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

    def main(self):
        while self.program_running:
            while self.running:
                print_screen = np.array(ImageGrab.grab(bbox=(0, 40, 800, 640)))
                cv2.imshow('Aimbot Hack LMAO', cv2.cvtColor(print_screen, cv2.COLOR_BGR2RGB))
                """
                last_time = t.time()
                print(f"loop took {t.time() - last_time} seconds")
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    cv2.destroyAllWindows()
                    break
                    """


aimbot_thread = Main(delay)
aimbot_thread.start()


def on_press(key):
    if key == start_stop_key:
        if aimbot_thread.running:
            aimbot_thread.stop()
        else:
            aimbot_thread.start()
    elif key == exit_key:
        aimbot_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()
