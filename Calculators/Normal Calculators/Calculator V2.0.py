from math import *


numList = []
def piperi():
    while True:
        num = float(input("What do you want for your pi perimeter problem(put 0 is you want to stop): "))
        print(2 * num * pi)
def piarea():
    while True:
        num = float(input("What do you want for your pi area problem(put 0 is you want to stop): "))
        print(num * num * pi)
def addition():
    while True:
        num = float(input("What do you want for your addition problem(put 0 is you want to stop): "))
        if num == 0:
            break
        else:
            numList.append(num)
    print("The sum is ", sum(numList))
def subtraction():
    while True:
        num = float(input("What do you want for your subtraction problem(put 0 is you want to stop): "))
        if num == 0:
            break
        else:
            numList.append(num)
    diff=numList[0]
    i = 1
    while i < len(numList):
        diff = diff - numList[i]
        i = i + 1
    print('The difference is ', diff)
def multiplication():
    while True:
        num = float(input("What do you want for your multiplication problem(put 0 is you want to stop): "))
        if num == 0:
            break
    product = ''
    for x in numList:
        product = product * x         
    print ('The product was: ', str(product))


# Running the code
multiplication()
piperi()
piarea()
addition()
subtraction()
