import random


def random_list_generators():
    new_list = []
    list_1 = []
    user_input = int(input("How many times do you want this code to run? "))
    if user_input == 0:
        print("Just why did you enter 0,brb :(")
    else:
        while user_input > 0:
            random_number = random.randint(1, 101)
            random_number_2 = random.randint(1, 101)
            random_num = str(random_number)
            random_num_2 = str(random_number_2)
            list.append(random_num)
            list_1.append(random_num_2)
            """This is for list one"""
            if random_number % 2 == 0:
                new_list.append(random_number)
            """This is for list two"""
            if random_number_2 % 2 != 0:
                new_list.append(random_number_2)
            user_input -= 1
        print("The output for the 1st list is even numbers\nThe output for the 2nd list is odd numbers")
        print(f"This is the 1st list: {list}\nThis is the 2nd list {list_1}")
        print(f"And together, they get the new list: {new_list}")


random_list_generators()
