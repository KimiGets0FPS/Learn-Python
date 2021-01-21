import random as r


def in_one_not_other():
    list_1 = []
    list_2 = []
    """In one my_list, but not in the other my_list"""
    user_input = int(input("Tell me how many numbers should be in the my_list "))
    while user_input > 0:
        list_1.append(r.randint(1, 101))
        list_2.append(r.randint(1, 101))
        user_input -= 1
    print(f"\nThis is my_list 1:{list_1}\nThis is my_list 2:{list_2}")
    new_list = []
    for num in list_1:
        if num in list_2:
            pass
        else:
            new_list.append(num)
    for num in list_2:
        if num in list_1:
            pass
        else:
            new_list.append(num)
    print(f"This is the new my_list:{new_list}")


in_one_not_other()
