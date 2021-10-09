num = int(input())
nums = list(map(int, input().split()))
nums.sort()
missing = -1
for i in range(num-1):
    if i+1 != nums[i]:
        missing = i+1
        break
if missing == -1:
    print(nums[-1]+1)
else:
    print(missing)
