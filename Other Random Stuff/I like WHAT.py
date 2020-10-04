import random


def say_hello(animal):
    print(animal+' are my friend')


def pick_word(words):
    return random.choice(words)


say_hello(pick_word(['dogs', 'cats', 'horses', 'snakes', 'rabbits', 'alligators', 'crocodiles', 'NoObS', 'Pros']))
