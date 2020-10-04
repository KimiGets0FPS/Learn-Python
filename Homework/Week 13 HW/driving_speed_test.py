import pyautogui


def additional_homework_4():
    """The points are bad and if the driver get 12 points, they get their driver's license suspended"""
    points = 0
    while True:
        if points == 12:
            print("FBI OPEN UP!!!")
            break
        print("\nOver 70 MPH is over the speed limit")
        user_input = int(input("What speed are you driving at right now? "))
        if user_input == 0:
            joke = pyautogui.confirm('Have you made it home?', buttons=["Yes", "No"])
            if joke == "Yes":
                print("\nYou're safe...at least for now")
            if joke == "No":
                print("\nJust stay there, I bet you that the police will come XD")
            break
        if user_input <= 70:
            print("Good, you are not over the speed limit")
        elif 80 >= user_input > 70:
            print("You're speeding! Plus 2 points!!!")
            points += 2
            points_left = 12 - points
            print(f"Now you have {points} points!!!\nAnd you still have {points_left} points left!!!")
        elif 100 >= user_input > 80:
            print("Oh boi, the police is chasing you! plus 4 points!!!")
            points += 4
            points_left = 12 - points
            print(f"You have {points} points now!!!\nAnd you still have {points_left} points left!!!")
        elif user_input > 100:
            print("Bro, what are you playing?GTA 10 million? Why do you have to that fast???")
            print("FBI OPEN UP!!!\nLOL that's just the police, plus 6 points LMAO")
            points += 6
            points_left = 12 - points
            print(f"You have {points} points now!!!\nAnd you still have {points_left} points left!!!")


additional_homework_4()
