import math
def sum(user_input):
    y = user_input
    sum = 0
    for x in y:
        sum = sum + x
    return sum


def product(user_input):
    y = user_input
    product = 1
    for x in y:
        product = product * x
    return product


def median(user_input):
    y = user_input
    i = 0
    for x in y:
        add_sum = sum (y)
        i += 1
    actual_median = add_sum/i
    return actual_median


def do():
    list = []
    while True:
        user_input = int(input("Choose a number(Enter 0 to stop): "))
        if user_input == 0:
            print ("The sum in the my_list is ",sum(list))
            print ("The product in the my_list is ",product(list))
            print ("The median of the my_list is ",median(list))
            break
        else:
            list.append(user_input)


do()
