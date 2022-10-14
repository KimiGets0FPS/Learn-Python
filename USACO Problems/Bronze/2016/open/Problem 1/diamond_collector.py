import sys


sys.stdin = open("diamond.in", "r")
sys.stdout = open('diamond.out', 'w')

n, k = map(int, input().split())
nums = []
for i in range(n):
    nums.append(int(input()))

# Brute force method
output = 0
for i in range(len(nums)):
    count = 0
    for j in range(len(nums)):
        if 0 <= nums[j] - nums[i] <= k:
            count += 1
    if count > output:
        output = count

print(output)
