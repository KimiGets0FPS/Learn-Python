import os
import time


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


while True:
    nums = input("Enter y-values here: ")
    if nums:
        nums = list(map(float, nums.split()))
        diff_1 = []
        for i in range(len(nums)-1):
            diff_1.append(nums[i+1]-nums[i])
        common = diff_1[1]-diff_1[0]
        print(diff_1)
        for i in range(len(diff_1)-1):
            if common != diff_1[i+1]-diff_1[i]:
                print("Not a Quadratic Equation")
                common = False
                break
        if common:
            print("Quadratic Equation")
        input("Press Enter to continue...")

    else:
        print("Thanks for using this calculator!")
        time.sleep(2)
    clear()
