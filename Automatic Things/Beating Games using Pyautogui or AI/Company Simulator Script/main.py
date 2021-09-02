import threading
import keyboard
import pyautogui


def find_1():
    ...


def find_2():
    ...


def find_3():
    ...


def press():
    for _ in range(100):
        keyboard.press_and_release('e')


if __name__ == '__main__':
    while True:
        pyautogui.click(find_1())
        pyautogui.click(find_2())
        threads = []
        for i in range(50):
            t = threading.Thread(target=press())
            t.daemon = True
            threads.append(t)
        for i in range(50):
            threads[i].start()
        for i in range(50):
            threads[i].join()
        pyautogui.click(find_3())
