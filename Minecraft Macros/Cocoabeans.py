"""
Macro made by KimiGets0FPS_YT

This macro will farm superfarm for cocoabeans ONLY

Speed: 155%
Pitch: 45
TOGGLESPRINT: OFF

REMEMBER TO DO /setspawn to set your spawnpoint on the garden!
"""


import win_precise_time as wpt
import pyautogui as pg


def macro(times):

    pg.mouseDown(button='left')
    
    for _ in range(12):

        # Walk straight
        pg.keyDown('w')
        wpt.sleep(72)
        pg.keyUp('w')

        # Move to the right
        pg.keyDown('d')
        wpt.sleep(0.3)
        pg.keyUp('d')

        # Walk back
        pg.keyDown('s')
        wpt.sleep(72)
        pg.keyUp('s')

        # Move to the right
        pg.keyDown('d')
        wpt.sleep(0.45)
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
