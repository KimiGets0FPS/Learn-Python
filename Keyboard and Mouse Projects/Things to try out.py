import keyboard as kb
import time as t


def enter():
    return kb.press_and_release("enter")


def pls_beg():
    return kb.write("pls beg")


def pls_hunt():
    return kb.write("pls hunt")


kb.wait('delete')
num_of_sec = 0
while True:
    if num_of_sec == 0:
        pls_beg()
        enter()
        pls_hunt()
    else:
        if num_of_sec // 40:
            pls_beg()
            enter()
        if num_of_sec // 50:
            pls_hunt()
            enter()
