import pyautogui as pg
import win_precise_time as wpt


def main():
    while True:
        pg.click(button='left')
        wpt.sleep(1)

if __name__ == "__main__":
    wpt.sleep(float(input()))
    main()
