import random as r
# guesses is the times you can guess
guesses = 3


def play():
    global guesses
    dice = r.randint(1, 6)
    while True:
        guess = int(input("Guess the dice number: "))
        # if the guess is right
        if guess == dice:
            print ("You win!!!")
            break
        # if you guess it wrong

        if guesses == 1:
            print("You lose!!!")
            print("The number was " + str(dice))
            break
        else:
            print("You guessed it wrong!!!")
            guesses = guesses - 1
            print('You still have ' + str(guesses) + " lives left!!!")


play()
