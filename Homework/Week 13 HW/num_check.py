def num_check():
    old_input = input("Enter any number you want to be reversed and checked ")
    new_input = ''.join(reversed(old_input))
    print(f"\nThe reversed number is {new_input} and the original number is {old_input}")
    if old_input == new_input:
        print("So this is True")
    else:
        print("So this is False")


num_check()
