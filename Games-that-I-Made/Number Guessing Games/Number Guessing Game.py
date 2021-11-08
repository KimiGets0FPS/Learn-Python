from random import *
while True:    
    u_lives = 10
    user_input = str(input("dO yOu wAnT tO tRy oUt oUr nEw mOdEl oF gUeSsInG nUmBeR gAmE???(Yes/No): "))
    if user_input.lower() == 'no':
        break
    elif user_input.lower() == 'yes':
        a_number = randint(0, 51)
        while True:
            # actual number
            ask_user = int(input("What do think the number is?(0 to 50) "))
            if ask_user == a_number:
                print("Wow, you got it!!!You won!!!")
                break
            elif ask_user > a_number:
                u_lives = u_lives - 1
                print("THE NUMBER IS TOO BIG!!!!")
                print("You still have " + str(u_lives) + " lives")
            elif ask_user < a_number:
                u_lives = u_lives - 1
                print("the number is too small!!!")
                print("You still have " + str(u_lives) + " lives")
            if u_lives == 0:
                print("Bruh, you suck...YOU LOST!!!")
                print("The number was " + str(a_number))
                break
    else:
        print("BRUH")
        break

