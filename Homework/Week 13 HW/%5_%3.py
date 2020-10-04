import pyautogui


def additional_homework_3():
    user_input = int(input("Enter any number: "))
    if user_input == 0:
        print("Hello, you aren't suppose to see this so get our right now or else I'm calling in the FBI")
        joke = pyautogui.confirm('Should I call the FBI on you?', buttons=["Yes", "No"])
        if joke == "Yes":
            print("FBI! Open up!!!")
        else:
            print("LOL, did you think that I'm going to call the FBI on you?")
    else:
        """This is the part where we tell if its divisible by 3 or 5 or nothing or both"""
        if user_input % 5 == 0 and user_input % 3 == 0:
            print(f"The number {user_input} is divisible by 3 and 5!!!")
        if user_input % 3 == 0 or user_input % 5 == 0:
            if user_input % 3 == 0:
                print(f"The number that you entered ({user_input}) is divisible by 3!!!")
            if user_input % 5 == 0:
                print(f"The number that you entered ({user_input}) is divisible by 5!!!")
            else:
                print(f"The number that you entered ({user_input}) isn't divisible by 3 or 5!!!")


additional_homework_3()
