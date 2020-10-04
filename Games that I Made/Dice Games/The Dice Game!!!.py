import random as r

while True:
    numberofdice = int(input('How many dice(s) do you want?'))
    if numberofdice <= 0:
        print ('the number has to be within 1 to 10!!!')
        break
    else:
        num=0
        output=""
        while (num < numberofdice):            
            dice = r.randint (1,6)
            #print(dice)
            output = output + str(dice) + ' ' 
            num = num + 1
        print(output)
