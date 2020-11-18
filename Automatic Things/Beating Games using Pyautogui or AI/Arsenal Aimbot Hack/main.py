import threading
from mouse import on_click
import sys
import numpy as np
from PIL import ImageGrab
import cv2
from pynput.mouse import Controller
from pynput.keyboard import KeyCode, Listener


delay = 0
stop_key = KeyCode(char='|')


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

    def on_click(self, x, y, button, pressed):
        if pressed:
            print("Pressed.")

    def screen_looks_at_you_while_you_sleep(self):
        color_to_look_at = 138, 25, 18
        while self.program_running:
            image = ImageGrab.grab()
            while True:
                print_screen = np.array(ImageGrab.grab(bbox=(0, 40, 800, 640)))
                cv2.imshow("Let's Go AimBot", cv2.cvtColor(print_screen, cv2.COLOR_BGR2RGB))
                #* Checking if there is red on the team.
                for y in range(0, 100, 10):
                    for x in range(0, 100, 10):
                        color = image.getpixel((x, y))
                        if color == color_to_look_at:
                            print("yay")
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    cv2.destroyAllWindows()
                    break
# Color #!Red
#! 138, 25, 18

# mouse = Controller
aimbot_start = AimBot(delay=0)


def on_press(key):
    if stop_key == '|':
        aimbot_start.exit()
        listener.stop()
    else:
        if aimbot_start.running:
            aimbot_start.stop()
        else:
            aimbot_start.start()

if __name__ == '__main__':
    aimbot_start.start()


    
"""
def on_press(key):
    if key == start_stop_key:
        if aimbot_thread.running:
            aimbot_thread.stop()
        else:
            aimbot_thread.start()
    elif key == exit_key:
        aimbot_thread.exit()
        listener.stop()"""


with Listener(on_press=on_press, on_click=on_click) as listener:
    listener.join()

# with Listener(on_click=on_click) as listener:
# listener.join()
