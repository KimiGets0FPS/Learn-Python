from keyboard import press
from time import sleep
import pyautogui
import os


def end():
    print("exited")
    exit(0)


def main():
    os.system('cls')
    spam = input("Enter your spam text:\n-> ")
    num = input(
        "\nNumber of times to spam (Leave it for if you want it to spam forever):\n-> ")  # sets number of time to spam
    if num == "":  # if num is blank sets num to 999999... you won't let this loop that many times would you ?
        num = 999999

    print('\nThe spam will begin in 10 seconds... BRACE YOURSELF !!!\n')  # BRACE YOURSELF !!!!
    print("Return to this window and press 'ctrl/cmd + c' to stop the spam anytime\n\n")  # how to stop the chaos
    sleep(10)  # gives time for lazy users to point towards the input box

    for _ in range(int(num)):
        sleep(0.3)
        pyautogui.typewrite(spam)
        press('enter')

    end()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Stopping the script')
        end()
