"""
Macro made by KimiGets0FPS_YT

This macro will farm superfarm for cactus ONLY

Speed: 470%
Yaw: 90.0/0.0

Make sure that you're not moving left or right when moving foward/backward

REMEMBER TO DO /setspawn to set your spawnpoint on the garden!
"""

import win_precise_time as wpt
import pyautogui as pg

def macro(times):
    pg.mouseDown(button='left')

    for _ in range(10):

        pg.keyDown('a')
        wpt.sleep(23.9)
        pg.keyUp('a')

        pg.keyDown('w')
        wpt.sleep(0.1)
        pg.keyUp('w')

        pg.keyDown('d')
        wpt.sleep(23.9)
        pg.keyUp('d')

        pg.keyDown('w')
        wpt.sleep(0.1)
        pg.keyUp('w')

    pg.keyDown('a')
    wpt.sleep(23.9)
    pg.keyUp('a')

    pg.keyDown('w')
    wpt.sleep(0.1)
    pg.keyUp('w')

    pg.keyDown('d')
    wpt.sleep(23.9)
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
    
    wpt.sleep(0.001)

def countdown(seconds):
    for i in range(seconds):
        print(f"{seconds - i} seconds left")
        wpt.sleep(1)
    print("Starting Macro")

def main():
    countdown(int(input("Seconds to countdown: ")))
    start()
    macro(times=1)


if __name__ == "__main__":
    main()
