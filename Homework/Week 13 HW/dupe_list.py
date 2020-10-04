import random


def additional_homework_1():
    user_input = int(input("How many times do you want the loop to run? "))
    while user_input > 0:
        random_numbers = random.randint(1, 21, 1)
        list.append(random_numbers)
        user_input -= 1
    print(f"These are the original numbers {list}")
    i = 0
    new_list = []
    dupe_num_list = []
    for numbers in list:
        if i == 0:
            new_list.append(numbers)
        if i >= 1:
            previuos_number = list[i-1]
            if numbers != previuos_number:
                new_list.append(numbers)
            else:
                dupe_num_list.append(numbers)
        i += 1
    print(f"The numbers that have duplicated are {dupe_num_list}")
    print(f"The new list is {new_list}")


additional_homework_1()
