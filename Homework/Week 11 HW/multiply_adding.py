def homework_1():
    my_list = []
    x = 2
    while x > 0:
        user_input = int(input("What number do you want? "))
        my_list.append(user_input)
        x -= 1
    product = my_list[0] * my_list[1]
    if product < 1000:
        print(product)
    else:
        sum_num = my_list[2] + my_list[1]
        print(sum_num)
    print(list)


homework_1()
