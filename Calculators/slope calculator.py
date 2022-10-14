import os
import time


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def find_common_factor(num1: int, num2: int) -> int:
    m = max(num1, num2)
    output = 0
    for i in range(m+1):
        if num1 % i == 0 and num2 % i == 0:
            output = i
    return output if output != 0 or output != 1 else None


def two_points(point_1: list[int], point_2: list[int]):
    # Special case if y1 - y2 == 0
    if point_1[1] - point_2[1] == 0 or point_2[1] - point_1[1] == 0:
        return 0
    if point_1[0] - point_2[0] == 0:
        return "Answer Undefined/Infinity"
    return (point_1[1] - point_2[1]) / (point_1[0] - point_2[0])


def main():
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
            slope = two_points(set_1, set_2)
            if slope == "Answer Undefined/Infinity":
                print("Answer Undefined/Infinity")
            else:
                print(f"Slope: {slope}")
                y_intercept = (slope*set_1[0])/set_1[1]
                if slope == 0:
                    print(f"y-intercept: {set_1[1]}")
                else:
                    print(f"y-intercept: {y_intercept}")

                equation = f"y = {slope}x + {y_intercept}"
                print(f"Equation: {equation}")
                input("Press enter to continue...")
        clear()
    time.sleep(2)
    return "Thanks you for using this calculator!"


if __name__ == '__main__':
    print(main())
