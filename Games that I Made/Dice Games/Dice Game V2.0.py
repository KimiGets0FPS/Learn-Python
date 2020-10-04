import random as r


while True:
    print ('Enter 0 if you want to exit the program!!!')
    numberofdice = int(input('How many dices do you want in this game? '))
    if numberofdice <= 0:
        print ('The number has to be bigger than 0!!!')
        break
    x = 0
    output = ""
    while (numberofdice > x):
        dice = r.randint(1,6)
        output = output + str(dice) + ' '
        numberofdice = numberofdice - 1
    print (output)
    
    
