def fizz_buzz():
    user_input = int(input("Give me any integer: "))
    if user_input % 3 == 0:
        print("Fizz")
    elif user_input % 5 == 0:
        print("Buzz")
    elif user_input % 3 == 0 and user_input % 5 == 0:
        print("FizzBuzz")
    else:
        print(f"The number {user_input} is not qualified :(")


fizz_buzz()
