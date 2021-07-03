import os
import time
import sys
import math
from pynput.keyboard import KeyCode, Listener

# IMPORTANT: MUST RUN ON CMD/TERMINAL

BORDER = '⬜'
BORDERS = [[0, 0], ]
SNAKE_HEAD = ''
SNAKE_BODY = ''
FOOD = 'O'


def dialogue(message: str, delay: float, sleep_time: float, if_clear=True):
    for i in message:
        print(i, end='')
        sys.stdout.flush()
        time.sleep(delay)
    time.sleep(sleep_time)
    if if_clear:
        clear()


def dialogue_input(message: str, delay: float, sleep_time: float):
    output = input(dialogue(message, delay, sleep_time))
    return output


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def update():
    ...


first_time = True
while True:
    if first_time:
        clear()
        dialogue('Running...', 0.1, 2)
        dialogue('Hey you!', 0.06, 2.5)
        dialogue('Yeah YOU!!!', 0.07, 2)
        dialogue("Let's play a round of the classic snake game!!!!", 0.03, 2)
        first_time = False
    elif first_time is False:
        clear()
        dialogue("That was a good game!", 0.05, 2.5)
        again = input(dialogue("Do you want to play again? (Yes or no): ", 0.03, 10000, if_clear=False))
        # again = dialogue_input("Do you want to play again? (Yes or No): ", 0.05, 99)
        # getting user input, so use inf on user                                 ^^^
        if again.lower() == 'no':
            break


def on_press(key):
    if key == 'w':
        print("Pressed 'W'")
    elif key == 'a':
        print("Pressed 'A'")
    elif key == 's':
        print("Pressed 'W'")
    elif key == 'd':
        print("Pressed 'W'")


with Listener(on_press=on_press) as listener:
    listener.join()
