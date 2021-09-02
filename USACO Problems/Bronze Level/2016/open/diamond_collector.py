fin = open("diamond.in", "r")

n, k = map(int, fin.readline().split())
nums = []
for i in range(n):
    nums.append(int(fin.readline()))

# Brute force method
output = 0
for i in range(len(nums)):
    count = 0
    for j in range(len(nums)):
        if 0 <= nums[j] - nums[i] <= k:
            count += 1
    if count > output:
        output = count

with open("diamond.out", "w") as out:
    print(output, file=out)
