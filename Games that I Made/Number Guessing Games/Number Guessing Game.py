from random import *
while True:    
    ulives = 10
    user_input = str(input("""Do YoU WaNt To TrY OuT OuR NeW MoDeL Of
GuEsSiNg NuMbER GaMe???(Yes/No)"""))
    if user_input == 'No' or user_input == 'no':
        break
    elif user_input == 'Yes' or user_input == 'yes':
        anumber = randint (0,51)

        while True:
            # actual number
            ask_user = int(input("What do think the number is?(0 to 50) "))
            if ask_user == anumber:
                print("Wow, you got it!!!You won!!!")
                break
            elif ask_user > anumber:
                ulives = ulives - 1
                print ("THE NUMBER IS TOO BIG!!!!")
                print("You still have " + str(ulives) + " lives")
            elif ask_user < anumber:
                ulives = ulives - 1
                print ("the number is too small!!!")
                print("You still have " + str(ulives) + " lives")
            if ulives == 0:
                print ("Bruh, you suck...YOU LOST!!!")
                print ("The number was " + str(anumber))
                break
    else:
        print ("BRUH")
        break
            
