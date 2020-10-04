def hours_to_seconds():  # and seconds to hours
    while True:
        user_input_which_one = input("\n1. Seconds to hour\n2. Hour to seconds\nType in 1 or 2:(Enter 'q' to quit) ")
        if user_input_which_one != 'q':
            user_input_which_one = int(user_input_which_one)
            if user_input_which_one != 1 and user_input_which_one != 2:
                print("It has to be '1' or '2'")
            elif user_input_which_one == 1 or user_input_which_one == 2:
                if user_input_which_one == 1:
                    user_input_seconds = int(input("How much seconds do you want to convert to hours? "))
                    user_input_seconds /= 3600
                    print(f"It is {user_input_seconds} hours")
                elif user_input_which_one == 2:
                    user_input_hours = int(input(f"How much hours do you want to convert to seconds? "))
                    user_input_hours *= 3600
                    print(f"It is {user_input_hours} seconds")
                else:
                    print("You are not supposed to get this message LMAO")
        elif user_input_which_one == 'q':
            break
        else:
            print("ok I'll just do nothing I guess")
            break


hours_to_seconds()
