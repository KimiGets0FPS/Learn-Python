from pynput.mouse import Listener, Controller


class OnClick:
    def __init__(self):
        pass
    def on_click(self, x, y, button, pressed):
        if pressed:
            return True


on_click = OnClick()

with Listener(on_click=on_click) as listener:
    listener.join()
