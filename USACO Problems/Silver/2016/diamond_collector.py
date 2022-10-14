import sys


sys.stdin = open("diamond.in", "r")
sys.stdout = open("diamond.out", "w")
n, k = map(int, input().split())
nums = []
for i in range(n):
    nums.append(int(input()))

# Two Pointers Technique

nums = sorted(nums)
high, low = 0, 0
output = 0
while high != len(nums):
    if nums[high] - nums[low] <= k:
        count = max(output, high-low+1)
        high += 1
    else:
        low += 1

print(output)
