import threading


def type_char():
    import keyboard
    while True:
        keyboard.wait('u')
        for _ in range(1500):
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
