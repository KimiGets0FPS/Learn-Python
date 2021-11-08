import random as r
import time as t


def main():
    user_lives = 3
    # user_takes_the_L = 0
    pc_lives = 3
    pc_takes_the_l = 0
    while user_lives > 0 and pc_lives > 0:
        user_input = int(input("1. Rock\n2. Paper\n3. Scissors\nChoose a number: "))
        if user_input == 1 or user_input == 2 or user_input == 3:
            pc_choice = r.randint(1, 4)
            if pc_choice == 1:
                pcw_choice = "Rock"
            elif pc_choice == 2:
                pcw_choice = "Paper"
            elif pc_choice == 3:
                pcw_choice = "Scissors"
            t.sleep(0.5)
            # When user win
            if user_input == 1 and pc_choice == 3:
                print("You won!!!")
                print(f"The computer chose: {pcw_choice}!")
                pc_lives -= 1
                print(f"The computer only has {pc_lives} lives left!")

            elif user_input == 2 and pc_choice == 1:
                print("You won!!!")
                print(f"The computer chose: {pcw_choice}!")
                pc_lives -= 1
                print(f"The computer only has {pc_lives} lives left!")

            elif user_input == 3 and pc_choice == 2:
                print("You won!!!")
                print(f"The computer chose: {pcw_choice}!")
                pc_lives -= 1
                print(f"The computer only has {pc_lives} lives left!")

                """1 is Rock, 2 is Paper, 3 is Scissors"""
            # When user lose
            elif user_input == 2 and pc_choice == 3:
                print("You lost!!!")
                print(f"The computer chose: {pcw_choice}!")
                user_lives -= 1
                print(f"You only have {user_lives} lives left!!!")
            elif user_input == 1 and pc_choice == 2:
                print("You lost!!!")
                print(f"The computer chose: {pcw_choice}!")
                user_lives -= 1
                print(f"You only have {user_lives} lives left!!!")
            elif user_input == 3 and pc_choice == 1:
                print("You lost!!!")
                print(f"The computer chose: {pcw_choice}!")
                user_lives -= 1
                print(f"You only have {user_lives} lives left!!!")
            # Draw
            elif user_input == pc_choice:
                print("Draw!")
        # if the user decides not to obey the rules
        else:
            print("Choose 1, 2, or 3!")

        if user_lives == 0:
            print(f"You lost!\nYou won {pc_takes_the_l} times")
        elif pc_lives == 0:
            print(f"You Won!\nYou lost {pc_lives} times!")


main()
