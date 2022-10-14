import sys


input = sys.stdin.readline
print = sys.stdout.write

num = int(input())
nums = list(map(int, input().split()))


def main(i, s1, s2):
    if i == num:
        return abs(s1-s2)
    return min(main(i+1, s1+nums[i], s2), main(i+1, s1, s2+nums[i]))


print(f"{main(0, 0, 0)}")
