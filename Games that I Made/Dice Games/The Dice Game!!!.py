import random as r

while True:
    number_of_dice = int(input('How many dice(s) do you want?'))
    if number_of_dice <= 0:
        print('the number has to be within 1 to 10!!!')
        break
    else:
        num = 0
        output = ""
        while num < number_of_dice:
            dice = r.randint(1, 6)
            # print(dice)
            output = output + str(dice) + ' ' 
            num = num + 1
        print(output)
