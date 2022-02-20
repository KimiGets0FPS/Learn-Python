import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    while True:
        print("\n----Press Enter to exit anytime----\n")
        choice = input(f"Choices (select number):\n1.) 2 inputs\nChoice: ")
        if not choice:
            break
        if int(choice) == 1:
            while True:
                set_1 = list(map(int, input("First set (separated with space): ").split(" ")))
                if not set_1:
                    break
                set_2 = list(map(int, input("Second set (separated with space): ").split(" ")))
                if not set_2:
                    break
                print(set_1, set_2)
                print(f"Slope: {(set_1[1]-set_2[1])/(set_1[0]-set_2[0])}")
    return "Thanks you for using this calculator!"


if __name__ == '__main__':
    print(main())
