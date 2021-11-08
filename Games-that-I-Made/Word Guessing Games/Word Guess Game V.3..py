from random import *

lives = 5
word_list = ['cat','dog','lion','tiger','zebra','gecko','pig']
word = choice(word_list)
length = len(word)
print ("The word is " + str(length) + " long")
while lives > 0:
    user_guess = input("What's your guess? ")
    i = 0
    hint = ""
    while i != length:
        if word[i] == user_guess[i]:
            hint += (word[i])
        else:
            hint += "-"
        i += 1
    if hint == word:
        print ("You win!!!")
        print ("The word was " + word)
        break
    elif lives == 0 and hint != word:
        print ("You lose!!!")
        print ("The word was " + word)

    print (hint)
