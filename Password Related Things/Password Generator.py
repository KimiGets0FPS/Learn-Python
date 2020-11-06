import string
from random import *


number_of_passwords = int(input("How many passwords do you want?? "))
while number_of_passwords > 0:
    print("A password larger or equal to 10 is unpredictable!!!")
    nums_of_value = int(input("How much digits do you want in your password?(number has to be larger than 10!!!) "))
    if nums_of_value > 10:
        characters = string.ascii_letters + string.punctuation + string.digits
        password = ''.join(choice(characters) for x in range(nums_of_value))
        print(password)
        askT = number_of_passwords - 1
    else:
        print("The number that you just inputted has to be bigger than 10!!")
