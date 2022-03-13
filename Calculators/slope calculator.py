import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def find_common_factor(num1: int, num2: int) -> int:
    m = max(num1, num2)
    output = 0
    for i in range(m+1):
        if num1 % i == 0 and num2 % i == 0:
            output = i
    return output if output != 0 or output != 1 else None


def two_points(point_1: list[int], point_2: list[int]) -> str:
    # Special case if y1 - y2 == 0
    if point_1[1] - point_2[1] == 0 or point_2[1] - point_1[1] == 0:
        return "Slope: 0 (Zero Division Error)"
    return f"Slope: {(point_1[1] - point_2[1]) / (point_1[0] - point_2[0])}"


def main():
    while True:
        print("\n----Press Enter to exit anytime----\n")
        choice = input(f"Choices (select number):\n1.) 2 points\n2.) \nChoice: ")
        if not choice:
            break
        if int(choice) == 1:
            while True:
                set_1 = list(map(int, input("First set (separated with space): ").split(" ")))
                if not set_1:
                    print("Must give input!")
                    break
                set_2 = list(map(int, input("Second set (separated with space): ").split(" ")))
                if not set_2:
                    print("Must give input!")
                    break
                else:
                    print(two_points(set_1, set_2))
        clear()

    return "Thanks you for using this calculator!"


if __name__ == '__main__':
    print(main())
