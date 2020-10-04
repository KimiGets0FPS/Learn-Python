def additional_homework_2():
    user_input = input("Enter a word and I'll tell you if the word is palindrome or not: ")
    reversed_us_in = "".join(reversed(user_input))
    if user_input == reversed_us_in:
        print(f"The word {user_input} is a palindrome word")
    else:
        print(f"The word {user_input} is not a palindrome  word")
    """This homework is about palindrome!"""


additional_homework_2()
