import sys

sys.stdin = open("shell.in", "r")
sys.stdout = open("shell.out", "w")

times = int(input())
nums = []
for i in range(times):
    num = input().split()
    nums.append(num)

output = 0
possibility = 1
for i in range(times):
    count = 0
    original = [1, 2, 3]
    for j in range(len(nums)):
        v1, v2, v3 = int(nums[j][0])-1, int(nums[j][1])-1, int(nums[j][2])  # swap 1; swap 2; guess
        # swap
        original[v1], original[v2] = original[v2], original[v1]
        # checking if the guess is right
        if original[v3-1] == possibility:
            count += 1
    if count > output:
        output = count
    possibility += 1

print(output)
