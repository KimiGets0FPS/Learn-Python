def fabonacci_number():
    """This is about Fabonacci numbers!"""
    while True:
        i = 0
        start_num = 1
        user_input = int(input("0 to stop the loop\nHow many fibonnici numbers do you want? "))
        if user_input == 0:
            break
        else:
            while user_input > 0:
                if start_num == 1:
                    print(start_num)
                    list.append(start_num)
                    print(start_num)
                    list.append(start_num)
                    start_num += 1
                if start_num >= 2:
                    c_num = list[i-1] + list[i-2]
                    print(c_num)
                    list.append(c_num)
                user_input -= 1


fabonacci_number()
