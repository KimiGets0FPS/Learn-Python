import sys


input = sys.stdin.readline

t = int(input())
nums = []
for i in range(t):
    nums.append(int(input()))


def main():
    for num in range(len(nums)):
        if nums[num] == 1:
            print('0')
        else:
            div_num = int(nums[num] // 10)
            if div_num == 0:
                powered = 1
            else:
                powered = 10 ** len(str(div_num))
            print(f"{nums[num] - powered}")


main()
