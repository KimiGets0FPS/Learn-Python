"""
Macro made by KimiGets0FPS_YT

This macro will farm superfarm for SUGAR CANE

Speed: 327%
Yaw: 135.0/0.0

REMEMBER TO DO /setspawn to set your spawnpoint on the garden!
"""

import win_precise_time as wpt

import pyautogui as pg


def warp_garden():
    pg.mouseUp(button='left')
    pg.press('t')
    pg.write('/warp garden')
    pg.press('enter')

def start():
    pg.press('t')
    pg.write('/warp garden')
    pg.press('enter')

    wpt.sleep(0.001)


def macro(times):
    # if times-1 > 30:
    #     os.system("shutdown /s /t 1")
    print(f"{times} times farmed")

    pg.mouseDown(button='left')
    section = 1
    print(f"Section {section}")
    for _ in range(14):
        pg.keyDown('s')
        wpt.sleep(20)
        pg.keyUp('s')

        pg.keyDown('a')
        wpt.sleep(20)
        pg.keyUp('a')

        section += 1
        print(f"Section {section}")

    pg.keyDown('s')
    wpt.sleep(20)
    pg.keyUp('s')
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

    macro(times=1)


if __name__ == "__main__":
    main()
