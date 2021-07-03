import pyautogui
import time


def additional_homework_5():
    def do_1():
        count = 0
        user_input = int(input("Enter any integer and I'll tell you how many digits there are: "))
        while user_input > 0:
            user_input = user_input // 10
            count = count + 1
        print(f"There are {count} digits in the number {user_input}")
    """Or I could do it like this LMAO"""
    def do_2():
        user_input = int(input("Enter any integer and I'll tell you how many digits there are: "))
        print(f"There are {len(str(abs(user_input)))} digits in the number {user_input}")

    user_input = input("Type in 1 for 1\nType in 2 for 2\nWhich one do you want to use? ")
    if user_input == "1":
        do_1()
    if user_input == "2":
        do_2()
    else:
        pyautogui.alert("FBI OPEN UP!!!")
        time.sleep(3)


additional_homework_5()
