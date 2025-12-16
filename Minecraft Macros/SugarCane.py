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

    # pg.keyDown('space')
    # time.sleep(0.05)
    # pg.keyUp('space')

    # time.sleep(0.01)

    # pg.keyDown('space')
    # time.sleep(0.05)
    # pg.keyUp('space')

    wpt.sleep(0.001)


def macro(times):
    # if times-1 > 30:
    #     os.system("shutdown /s /t 1")
    print(f"{times} times farmed")

    pg.mouseDown(button='left')
    section = 1
    print(f"Section {section}")
    for _ in range(4):
        pg.keyDown('a')
        wpt.sleep(48)
        pg.keyUp('a')

        pg.keyDown('w')
        wpt.sleep(0.2)
        pg.keyUp('w')

        pg.keyDown('s')
        wpt.sleep(48)
        pg.keyUp('s')

        pg.keyDown('d')
        wpt.sleep(0.2)
        pg.keyUp('d')

        section += 1
        print(f"Section {section}")

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
