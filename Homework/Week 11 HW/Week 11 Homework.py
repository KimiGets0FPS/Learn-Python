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


def homework_2():
    i = 0
    my_list = []
    random_number = 10
    while random_number > 0:
        user_input = int(input("Want number do you want?(You only have to do this 10 times) "))
        my_list.append(user_input)
        random_number -= 1
    for _ in my_list:
        if i == 0:
            print("The current number is ", my_list[i])
        else:
            previous_number = my_list[i - 1]
            sum_num = previous_number + my_list[i]
            print(f"The current number is{my_list[i]}and the previous number is {previous_number} and the sum is "
                  f"{sum_num}")
        i += 1


homework_2()


def homework_3():
    while True:
        i = 0
        user_input = input("Enter any word you want(Enter'=' to stop): ")
        word_length = len(user_input)
        if user_input == '=':
            print("Thank you for using machine 10000! Hope you enjoyed XD")
            break
        else:
            for _ in user_input:
                if i >= word_length:
                    break
                else:
                    print(user_input[i])
                i += 2


homework_3()


def homework_4():
    while True:
        user_input = str(input("Enter any word you want: "))
        i = len(user_input)
        print(f"The number has to be smaller or equal to {i}")
        number = int(input("Enter any number you want: "))
        if number > i:
            print("Enter again, but this time, enter smaller than {i}")
        else:
            print("The word has changed...")
            new_input = user_input[number:]
            print(f"It's now called '{new_input}':/ \nWow I think you created a new word...")


homework_4()


def homework_5():
    my_list = []
    while True:
        user_input = int(input("Enter any number you want(0 to stop loop) "))
        if user_input == 0:
            if my_list[0] == my_list[-1]:
                print("This is true!")
            else:
                print("This is false!")
            break
        my_list.append(user_input)


homework_5()


def additional_hw():
    i = 0
    my_list = []
    print("you have to do like this : 1,2,3,4,5 \nand ill put it like this: '1','2','3','4','5',")
    user_input = input("Please do not put spaces between the numbers!\nWhat set of numbers do you want? ")
    split = user_input.split(",")
    for x in split:
        final = f'{split[i]}'
        my_list.append(final)
        i += 1
    print(my_list)


additional_hw()
