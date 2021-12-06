import threading
import keyboard
import time
import pyautogui


def press():
    while True:
        if keyboard.is_pressed('u'):
            for _ in range(100):
                keyboard.press_and_release('e')
                time.sleep(0.0000000000000000001**5)


threads = []
for i in range(50):
    t = threading.Thread(target=press())
    t.daemon = True
    threads.append(t)

for i in range(50):
    threads[i].start()

for i in range(50):
    threads[i].join()
