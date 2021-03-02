import threading
# import sys
import numpy as np
from PIL import ImageGrab
import cv2
# from pynput.mouse import Controller
from pynput.keyboard import KeyCode, Listener

stop_key = KeyCode(char='|')


class AimBot(threading.Thread):
    def __init__(self, delay=0):
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

    def look_screen(self):
        RED = 138, 25, 18
        while self.program_running:
            image = ImageGrab.grab()
            while True:
                print_screen = np.array(ImageGrab.grab(bbox=(0, 40, 800, 640)))
                cv2.imshow("Let's Go AimBot", cv2.cvtColor(print_screen, cv2.COLOR_BGR2RGB))
                # Checking if there is red on the team.
                for y in range(0, 100, 10):
                    for x in range(0, 100, 10):
                        if image.getpixel((x, y)) == RED:
                            print("yay")
                # if cv2.waitKey(25) & 0xFF == ord('q'):
                #     cv2.destroyAllWindows()
                #     break


# Color Red RGB value: 138, 25, 18

# mouse = Controller

aimbot = AimBot()


def on_press(key):
    if key == 't':
        aimbot.exit()
    else:
        if aimbot.running:
            aimbot.stop()
        else:
            aimbot.start()
            aimbot.look_screen()


if __name__ == '__main__':
    on_press('t')

with Listener(on_press=on_press) as listener:
    listener.join()
