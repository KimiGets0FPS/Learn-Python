# File Input
fin = open("diamond.in", "r")

n, k = map(int, fin.readline().split())
nums = []
for i in range(n):
    nums.append(int(fin.readline()))

# Two Pointers Technique
nums = sorted(nums)
high, low = 0, 0
count = 0
while high != len(nums):
    if nums[high] - nums[low] <= k:
        count = max(count, high-low+1)
        high += 1
    else:
        low += 1

with open("diamond.out", "w") as out:
    print(count, file=out)
