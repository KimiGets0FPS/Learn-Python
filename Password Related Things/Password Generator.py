import string
from random import *


askT = int(input("How many passwords do you want?? "))
while askT > 0:
    print("A password larger or equal to 10 is unpredictible!!!")
    askd = int(input("How much digits do you want in your password?(number has to be larger than 10!!!) "))
    if askd < 10:
        break
    characters = string.ascii_letters + string.punctuation + string.digits
    password ="".join(choice(characters) for x in range (askd))
    print(password)
    askT = askT - 1
# THIS IS THE BEST PASSWORD GENERATOR EVER!!!!!
