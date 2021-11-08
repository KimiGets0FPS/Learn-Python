from random import * 
def play():  
    name = input("What is your name? ")
    print("Bad Luck ! ", name) 
    words = ['rainbow','computer','science','cat','python','hello','player','condition','reverse','water','board','joemama']
    word = choice(words) 
    print("Guess the word!")
    guesses = '' 
    chances = 12
    while chances > 0:
        fails = 0
        guess = input("guess a character:")   
        guesses += guess
        for joemama in word:  
            if joemama in guesses:  
                print(joemama) 
            else:  
                print("-")
                fails += 1
        if guess != word:
            chances-= 1  
            print("Wrong")  
            print("You have", + chances, 'more guesses')
        if fails == 0: 
            print("You Win")
            print("The word is: ", word)  
            break
        if chances == 0:
            print ("You Loose, ha you're bad kid")
            print ("The word was obviously " + word)
    
