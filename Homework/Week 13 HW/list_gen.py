import random


def random_list_generators():
    list_1 = []
    list_2 = []
    new_list = []
    user_input = int(input("How many times do you want this code to run? "))
    if user_input == 0:
        print("Just why did you enter 0 :(")
    else:
        while user_input > 0:
            random_number = random.randint(1, 101)
            random_number_2 = random.randint(1, 101)
            random_num = str(random_number)
            random_num_2 = str(random_number_2)
            new_list.append(random_num)
            new_list.append(random_num_2)
            """This is for my_list one"""
            if random_number % 2 == 0:
                list_1.append(random_number)
            """This is for my_list two"""
            if random_number_2 % 2 != 0:
                list_2.append(random_number_2)
            user_input -= 1
        print("The output for the 1st list is even numbers\nThe output for the 2nd list is odd numbers")
        print(f"This is the 1st list: {list_1}\nThis is the 2nd list {list_2}")
        print(f"And together, they get the new list: {list_2}")


random_list_generators()
