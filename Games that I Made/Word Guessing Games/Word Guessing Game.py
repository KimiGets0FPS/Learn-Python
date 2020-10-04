import random

words=['','Turkey','Poland','Greenland','England','California','China','Shanghai','Supercalifragilisticexpeliaoducis','Supercalifragilisticexpeliadoucis','Supercalifragilisticexpeliadoucis']
guessTimes = 5
guessLetters = ""

def pickWord():
    return random.choice(words)

def play():
    print ('Guess the country!!!(province + states) ')
    word = pickWord()
    while True:
        guess = getGuess(word)
        if processGuess(guess,word):
            print ('Dude, you totally lost')
            print ('The word was: '+ word)
            break
        
        if guessTimes == 0:
            print ("You're Bad Kid")
            print ('BRUH, you literlly had 15 chances to win')
            print ('How bad can you get??? ')
            print ('The word was obviously:' + word)

def getGuess(word):
    printWordWithBlanks(word)
    print ('There are only '+ str (guessTimes)+ ' time(s) to guess kid!!!')
    guess = input ('Guess a letter and hurry UP KID!!!')
    return guess

def processGuess(guess,word):
    global guessTimes
    global guessLetters
    guessTimes = guessTimes -1
    guessLetters = guessLetters + guess

    for letter in word:
        if guessLetters.find(letter)== -1:
            return False
    return True
def printWordWithBlanks(word):
    displayWord=""
    for letter in word:
        if guessLetters.find(letter)> -1:
            #letter FOUND OOOOOOOOOOO SSSSSSSHHHHHHHOOOOOOOTTTTTTTTTT
            displayWord = displayWord + letter
            #Letter Not FOUND YYYYYYYYYYYYYYYYYYYYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYYYYYYYYYYYYYYYYYYYYYYYY
        else:
            displayWord = displayWord+'-'
    print (displayWord)

play()

