import os


def positive(num1, num2, num3):
    print("\n==Positive==\n")
    product = num1 * num2
    i = 1
    nums = []
    while product >= i:
        if product % i == 0:
            nums.append([i, product / i])
        i += 1

    answer = []
    for i in range(len(nums)):
        if nums[i][0] + nums[i][1] == num3:
            answer = nums[i]
    if answer:
        return answer
    return "No Solution"


def negative(num1, num2, num3):
    print("\n==Negative==\n")
    product = abs(num1 * num2)
    i = 1
    nums = []
    while product >= i:
        if product % i == 0:
            nums.append([i, product / i])
        i += 1

    answer = []
    for i in range(len(nums)):
        if nums[i][0] - nums[i][1] == num3:
            answer = [-nums[i][1], nums[i][0]]
        elif nums[i][1] - nums[i][0] == num3:
            answer = [nums[i][1], -nums[i][0]]
    if answer:
        return answer
    return "No Solution"


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    while True:
        num1 = int(input("Number 1 (first number): "))
        num2 = int(input("Number 2 (second number): "))
        num3 = int(input("Number 3 (sum): "))
        # product = num1 * num2
        pos_neg = True
        div_err = False

        if num1 <= 0 and num2 > 0 and num3 < 0:
            pos_neg = True
        elif (num1 >= 0 and num2 > 0 and num3 > 0) or (num1 <= 0 and num2 < 0 and num3 < 0):
            pos_neg = False
        if num2 == 0:
            print("Zero Division Error")
            div_err = True

        if not div_err:
            if pos_neg:
                print(negative(num1, num2, num3))
            if not pos_neg:
                print(positive(abs(num1), abs(num2), abs(num3)))
            input("Press Enter to continue: ")
        clear()


print(main())
clear()
