import time
import pyautogui
import keyboard
import pydirectinput


def automatic():
    start = time.time()
    seconds = 180  # change to the time you can work
    while True:
        current = time.time()
        if current - start > seconds:
            break
        for _ in range(50):
            time.sleep(0.0000001)
            keyboard.press_and_release('e')


def locate_button_1():
    b1 = None
    while b1 is None:
        b1 = pyautogui.locateOnScreen("C:/Users/zhewe/OneDrive/Documents/Coding Projects/Learn-Python/Keyboard and "
                                      "Mouse Projects/Keyboard Simulations/Company Simulator Script/b1.png",
                                      confidence=.65, region=(0, 0, 1920, 1080))  # Change the path to the desired path
        if b1 is not None:
            break
    return b1


def locate_button_2():
    b2 = None
    while b2 is None:
        b2 = pyautogui.locateOnScreen("C:/Users/zhewe/OneDrive/Documents/Coding Projects/Learn-Python/Keyboard and "
                                      "Mouse Projects/Keyboard Simulations/Company Simulator Script/b2.png",
                                      confidence=.65, region=(0, 0, 1920, 1080))  # Change the path to the desired path
        if b2 is not None:
            break
    return b2


def locate_button_3():
    b3 = None
    while b3 is None:
        b3 = pyautogui.locateOnScreen("C:/Users/zhewe/OneDrive/Documents/Coding Projects/Learn-Python/Keyboard and "
                                      "Mouse Projects/Keyboard Simulations/Company Simulator Script/b3.png",
                                      confidence=.65, region=(0, 0, 1920, 1080))  # Change the path to the desired path
        if b3 is not None:
            break
    return b3


while 5:
    print(f"{locate_button_1()[0]}, {locate_button_1()[1]}")
    pydirectinput.click(x=locate_button_1()[0], y=locate_button_1()[1])
    print("b1 found")
    pydirectinput.click(x=locate_button_2()[0], y=locate_button_2()[1])
    print("b2 found")
    automatic()
    pydirectinput.click(x=locate_button_3()[0], y=locate_button_3()[1])
    print("b3 found\n")
