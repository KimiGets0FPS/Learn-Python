import math

print(math.pi)

while True:  # accept the input for operation
    print("Select an operation.")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    # Take input from the user
    choice = input("Enter choice(1/2/3/4): ")
    numList = []
    while True:
        num1 = float(input("Enter a number(Put in 0 only if you want to stop): "))
        if num1 == 0:
            break
        else:
            numList.append(num1)
    # calculation

    if choice == '1':
        print('The sum was: ', sum(numList))
    if choice == '2':

        diff = numList[0]
        i = 1
        while i < len(numList):
            diff = diff - numList[i]
            i = i + 1
        print('The difference is: ', diff)

    if choice == '3':
        pro = 1
        for x in numList:
            pro = pro * x
        print('the product was: ', pro)

    if choice == '4':
        quotient = numList[0]
        i = 1
        while i < len(numList):
            quotient = quotient / numList[i]
            i = i + 1
        print('The quotient is: ', quotient)
