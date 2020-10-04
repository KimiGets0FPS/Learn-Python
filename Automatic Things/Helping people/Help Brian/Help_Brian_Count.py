import threading
import time
from pynput.keyboard import Listener, KeyCode

delay = 0.01  # Edit the delay here
start_stop_key = KeyCode(char='=')  # Costimize!!!
exit_key = KeyCode(char='-')  # Costimize!!!


class Start_Counting(threading.Thread):
    def __init__(self):
        super(Start_Counting, self).__init__()
        self.running = False
        self.program_running = True

    def start_counting(self):
        self.running = True

    def stop_counting(self):
        self.running = False

    def exit(self):
        self.stop_counting()
        self.program_running = False

    def run(self):
        user_input = int(input("Give me a number to get started: "))
        while self.program_running:
            while self.running:
                print(user_input)
                user_input += 1
                time.sleep(delay)


count_thread = Start_Counting()
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
