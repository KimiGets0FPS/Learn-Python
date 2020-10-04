def ten_eight():
    user_input = int(input("Put in a number: "))
    try:
        pass
    except ValueError:
        print("You entered a letter or a symbol! ")
    else:
        user_input = int(input("Put in another number: "))
    try:
        num_sum = user_input + user_input
    except ValueError:
        print("You entered a letter or a symbol! ")
    else:
        print(f"The sum is {num_sum}")


ten_eight()
