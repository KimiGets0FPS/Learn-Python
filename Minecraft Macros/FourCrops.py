"""
Macro made by KimiGets0FPS_YT

This macro will farm superfarm for WHEAT, CARROTS, POTATOES, AND NETHER WARTS

Speed: 93%

REMEMBER TO DO /setspawn to set your spawn point on the garden!
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

def macro1(times): # Farming wheat, carrots, and potatoes
    # if times-1 > 30:
    #     os.system("shutdown /s /t 1")
    print(f"{times} times farmed 5 layers")

    pg.mouseDown(button='left')
    layer = 1
    print(f"Layer {layer}")
    for _ in range(2):
        pg.keyDown('d')
        wpt.sleep(119.3)
        pg.keyUp('d')

        layer += 1
        print(f"Layer {layer}")
        
        pg.keyDown('a')
        wpt.sleep(119.3)
        pg.keyUp('a')

        layer += 1
        print(f"Layer {layer}")

    # Last Layer
    pg.keyDown('d')
    wpt.sleep(119.3)
    pg.keyUp('d')

    # Start the process again
    warp_garden()
    macro1(times+1)

def macro2(times):  # Farming netherwart
    # if times-1 > 25:  # Computer automatically shuts down after farming 35 times
    #     os.system("shutdown /s /t 1")
    print(f"{times} times farmed 5 layers")

    pg.mouseDown(button='left')
    layer = 1
    print(f"Layer {layer}")
    for _ in range(2):
        pg.keyDown('a')
        wpt.sleep(119.3)
        pg.keyUp('a')

        layer += 1
        print(f"Layer {layer}")
        pg.keyDown('d')
        wpt.sleep(119.3)
        pg.keyUp('d')
        
        layer += 1
        print(f"Layer {layer}")

    # Last Layer
    pg.keyDown('a')
    wpt.sleep(119.3)
    pg.keyUp('a')

    # Start the process again
    warp_garden()
    macro2(times+1)

def countdown(seconds):
    for i in range(seconds):
        print(f"{seconds - i} seconds left")
        wpt.sleep(1)
    print("Starting Macro")

def main():
    netherwart = input("Is 'A' supposed to be pressed? (y/n): ").lower() == "y"
    countdown(int(input("Seconds to countdown: ")))

    start()
    if netherwart:
        macro2(times = 1)
    else:
        macro1(times = 1)

if __name__ == "__main__":
    main()
