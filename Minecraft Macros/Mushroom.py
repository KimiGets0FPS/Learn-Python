import win_precise_time as wpt
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

    wpt.sleep(0.001)

def macro(times):
    # if times-1 > 25:  # Computer automatically shuts down after farming 35 times
    #     os.system("shutdown /s /t 1")
    print(f"{times} times farmed 5 layers")

    pg.mouseDown(button='left')
    layer = 1
    print(f"Layer {layer}")

    pg.keyDown('d')
    wpt.sleep(227)
    pg.keyUp('d')

    pg.keyDown('w')
    wpt.sleep(1.25)
    pg.keyUp('w')

    pg.keyDown('a')
    wpt.sleep(227)
    pg.keyUp('a')
    
    layer += 1
    print(f"Layer {layer}")

    pg.keyDown('d')
    wpt.sleep(227)
    pg.keyUp('d')

    pg.keyDown('s')
    wpt.sleep(1.9)
    pg.keyUp('s')

    pg.keyDown('a')
    wpt.sleep(227)
    pg.keyUp('a')

    layer += 1
    print(f"Layer {layer}")

    pg.keyDown('d')
    wpt.sleep(227)
    pg.keyUp('d')

    pg.keyDown('w')
    wpt.sleep(1.25)
    pg.keyUp('w')

    pg.keyDown('a')
    wpt.sleep(227)
    pg.keyUp('a')

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
