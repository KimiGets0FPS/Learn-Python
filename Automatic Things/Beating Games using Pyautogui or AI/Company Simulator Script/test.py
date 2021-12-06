import time
import threading
import keyboard


def main():
    started = time.time()
    while True:
        if keyboard.is_pressed('u'):
            for _ in range(100):
                keyboard.press_and_release('e')
                time.sleep(0.00000000000000001)
            if time.time()-started >= 5:
                break


threads = []

for i in range(100):
    t = threading.Thread(target=main())
    t.daemon = True
    threads.append(t)

for i in range(100):
    threads[i].start()

for i in range(100):
    threads[i].join()
