count = input()
nums = input().split()

# Solution

output = {}
for i in range(len(nums)):
    output[nums[i]] = output.get(nums[i], 0) + 1

print(len(output))
