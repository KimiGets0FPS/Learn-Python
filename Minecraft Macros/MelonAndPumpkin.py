"""
Script made by KimiGets0FPS_YT

This macro will work for MELONS AND PUMPKINS

Pitch must be 58.5-59
Speed: 280% (with depth strider 3)
"""


import os
import win_precise_time as wpt

import pyautogui as pg


def warp_garden():
    pg.mouseUp(button='left')
    pg.press('t')
    pg.write('/warp garden')
    pg.press('enter')
    wpt.sleep(0.025)

def start():
    # pg.press('t')
    pg.write('/warp garden')
    pg.press('enter')

    # pg.keyDown('space')
    # time.sleep(0.05)
    # pg.keyUp('space')

    # time.sleep(0.01)

    # pg.keyDown('space')
    # time.sleep(0.05)
    # pg.keyUp('space')

    wpt.sleep(0.001)

def macro(times):
    # if times-1 > 25:  # Computer automatically shuts down after farming 35 times
    #     os.system("shutdown /s /t 1")
    print(f"{times} times farmed 10 sections")

    pg.mouseDown(button='left')
    layer = 1
    print(f"Section {layer}")
    for _ in range(4):
        pg.keyDown('a')
        wpt.sleep(74)
        pg.keyUp('a')

        pg.keyDown('w')
        wpt.sleep(0.45)
        pg.keyUp('w')

        layer += 1
        print(f"Section {layer}")

        pg.keyDown('d')
        wpt.sleep(74)
        pg.keyUp('d')

        pg.keyDown('w')
        wpt.sleep(0.4)
        pg.keyUp('w')
        
        layer += 1
        print(f"Section {layer}")

    # Last Section
    pg.keyDown('a')
    wpt.sleep(74)
    pg.keyUp('a')

    layer += 1
    print(f"Section {layer}")

    pg.keyDown('w')
    wpt.sleep(0.4)
    pg.keyUp('w')

    pg.keyDown('d')
    wpt.sleep(74)
    pg.keyUp('d')

    # Start the process again
    warp_garden()
    macro(times+1)


def countdown(seconds):
    for i in range(seconds):
        print(f"{seconds - i} seconds left")
        wpt.sleep(1)
    print("Starting Macro")

def main():
    countdown(int(input("Seconds to countdown: ")))

    start()
    macro(times = 1)

if __name__ == "__main__":
    main()
