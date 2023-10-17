"""
Macro made by KimiGets0FPS_YT

This macro will farm superfarm for WHEAT, CARROTS, POTATOES, AND NETHER WARTS

Speed: 93%

REMEMBER TO DO /setspawn to set your spawnpoint on the garden!
"""

import os
import time
import pyautogui as pg


def warp_garden():
    pg.mouseUp(button='left')
    pg.press('t')
    pg.write('/warp garden')
    pg.press('enter')

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

    time.sleep(0.001)


def macro1(times): # Farming wheat, carrots, and potatoes
    print(f"{times} times farmed 5 layers")

    pg.mouseDown(button='left')
    for _ in range(2):
        pg.keyDown('d')
        time.sleep(119.5)
        pg.keyUp('d')
        pg.keyDown('a')
        time.sleep(119.5)
        pg.keyUp('a')

    # Last Layer
    pg.keyDown('d')
    time.sleep(119.5)
    pg.keyUp('d')

    # Start the process again
    warp_garden()
    macro1(times+1)


def macro2(times):  # Farming netherwart
    if times == 15:
        pg.hotkey('alt', 'f4')
        os.system('shutdown /s /t 0')
    print(f"{times} times farmed 5 layers")

    pg.mouseDown(button='left')
    for _ in range(2):
        pg.keyDown('a')
        time.sleep(119.5)
        pg.keyUp('a')
        pg.keyDown('d')
        time.sleep(119.5)
        pg.keyUp('d')

    # Last Layer
    pg.keyDown('a')
    time.sleep(119.5)
    pg.keyUp('a')

    # Start the process again
    warp_garden()
    macro2(times+1)


def countdown(seconds):
    for i in range(seconds):
        print(f"{seconds - i} seconds left")
        time.sleep(1)
    print("Starting Macro")

def main():
    netherwart = input("Are you farming netherwart? (y/n): ").lower() == "y"
    countdown(int(input("Seconds to countdown: ")))

    start()
    if netherwart:
        macro2(times=1)
    else:
        macro1(times=1)

if __name__ == "__main__":
    main()
