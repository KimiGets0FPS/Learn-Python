import random


def main():
    num = random.randint(1, int(input("Maximum number you want: ")))
    while True:
        guess = int(input("Your guess: "))
        if guess > num:
            print("Too high!")
        elif guess < num:
            print("Too low!")
        else:
            print("You got it!")


if __name__ == "__main__":
    while True:
        main()
        if input("Play again (Y/N)?").lower() == "n":
            break
