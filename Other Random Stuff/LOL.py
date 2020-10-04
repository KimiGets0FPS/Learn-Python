
def say_hello(animal):
    print('I mean... I do like,'+animal+'they are my friend,I like to play with them')

import random

words = ['dogs','cats','horses','snakes','rabbits','alligators','crocdiles','hamsters','John Cenas']
def pickWord():
    while True:
        animal = random.choice(words)
        print('I do not like '+animal)
        if  animal == 'John Cenas':
            return animal
say_hello(pickWord())

def add(n1, n2,n3):
    return n1+n2+n3

print (add(10,90,1234567890))

def dev(e1,e2,e3):
    return e1/e2/e3
print (dev(12,6,1,))

def mul(x1,x2,x3):
    return x1*x2*x3
print (mul(12,13,19))

def sub (y1,y2,y3):
    return y1-y2-y3
print(sub(99654,230,98654))
