import threading
import keyboard


def type_char():
    while True:
        keyboard.wait('u')
        for _ in range(50):
            keyboard.press_and_release('e')


threads = []
for i in range(50):
    t = threading.Thread(target=type_char())
    t.daemon = True
    threads.append(t)
for i in range(50):
    threads[i].start()
for i in range(50):
    threads[i].join()
