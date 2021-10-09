num = int(input())
nums = list(map(int, input().split()))

moves = 0
for i in range(1, len(nums)):
    if nums[i] < nums[i-1]:
        temp = nums[i-1] - nums[i]
        moves += temp
        nums[i] = temp

print(moves)
