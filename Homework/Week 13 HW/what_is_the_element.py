def additional_homework_7():
    user_input = input("Enter any word you want: ")
    new_string = ""
    for letters in user_input:
        if letters.isupper() is True:
            new_string += (letters.lower())
        elif letters.islower() is True:
            new_string += (letters.upper())
        elif letters.isspace() is True:
            new_string += letters
        elif letters.isdigit() is True:
            new_string += letters
    print(f"The new string is {new_string}")


additional_homework_7()
