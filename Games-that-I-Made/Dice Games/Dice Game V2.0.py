import random as r


while True:
    print('Enter 0 if you want to exit the program!!!')
    number_of_dice = int(input('How many dices do you want in this game? '))
    if number_of_dice <= 0:
        print('The number has to be bigger than 0!!!')
        break
    x = 0
    output = ""
    while number_of_dice > x:
        dice = r.randint(1, 6)
        output = output + str(dice) + ' '
        number_of_dice = number_of_dice - 1
    print(output)
