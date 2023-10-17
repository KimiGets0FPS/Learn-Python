"""
Macro made by KimiGets0FPS_YT

This macro will farm superfarm for Cactus ONLY

Speed: 400%

REMEMBER TO DO /setspawn to set your spawnpoint on the garden!
"""

import time
import pyautogui as pg

def macro(times):
    pg.mouseDown(button='left')

    # 28 seconds
    pg.keyDown('a')
    time.sleep(28)
    pg.keyUp('a')

    for _ in range(11):
        pg.keyDown('w')
        time.sleep(0.3)
        pg.keyUp('w')

        pg.keyDown('d')
        time.sleep(28)
        pg.keyUp('d')

        pg.keyDown('w')
        time.sleep(0.3)
        pg.keyUp('w')
    
    pg.keyDown('d')
    time.sleep(28)
    pg.keyUp('d')

    warp_garden()
    macro(times+1)

def warp_garden():
    pg.mouseUp(button='left')
    pg.press('t')
    pg.write('/warp garden')
    pg.press('enter')

def start():
    # pg.press('t')
    pg.write('/warp garden')
    pg.press('enter')
    
    time.sleep(0.001)

def countdown(seconds):
    for i in range(seconds):
        print(f"{seconds - i} seconds left")
        time.sleep(1)
    print("Starting Macro")

def main():
    countdown(int(input("Seconds to countdown: ")))
    start()
    macro(times=1)


if __name__ == "__main__":
    main()
