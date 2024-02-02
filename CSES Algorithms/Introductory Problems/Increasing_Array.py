input()
nums = list(map(int, input().split()))


count = 0
for i in range(1, len(nums)):
    if nums[i-1] > nums[i]:
        count += (nums[i-1] - nums[i])
        nums[i] = nums[i-1]

print(count)
