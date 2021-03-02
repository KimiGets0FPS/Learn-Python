import threading
import time
import keyboard
from pynput.keyboard import Listener, KeyCode

start_stop_key = KeyCode(char='=')  # Customize!!!
exit_key = KeyCode(char='-')  # Customize!!!


class StartCounting(threading.Thread):
    def __init__(self, delay=0.01):
        super(StartCounting, self).__init__()
        self.running = False
        self.program_running = True
        self.delay = delay

    def start_counting(self):
        self.running = True

    def stop_counting(self):
        self.running = False

    def exit(self):
        self.stop_counting()
        self.program_running = False

    def run(self):
        user_input = int(input("Give me a number to get started: "))
        while self.program_running and self.running:
            keyboard.press(user_input)
            user_input += 1
            time.sleep(self.delay)


count_thread = StartCounting(delay=float(input("Delay time: ")))
count_thread.start()


def on_press(key):
    if key == start_stop_key:
        if count_thread.running:
            count_thread.stop_counting()
        else:
            count_thread.start_counting()
    elif key == exit_key:
        count_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()
