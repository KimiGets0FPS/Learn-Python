from random import *
my_list = []
i = 0
while True:
    user_input = int(input("How much times do want the dice to be rolled? "))
    while user_input > 0:
        dice_roll = randint(1, 6)
        my_list.append(dice_roll)
        user_input -= 1
    print(my_list)
