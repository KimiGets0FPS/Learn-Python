def fabonacci_number():
    usr_input = int(input("Where do you want the number to stop (starts at 1): "))
    num_1, num_2 = 0, 1
    while num_1 < usr_input:
        print(num_1)
        num_1, num_2 = num_2, num_1 + num_2


fabonacci_number()
