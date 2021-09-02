nums = [1, 2, 3, 4]
output = []
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        temp = (nums[i], nums[j])
        output.append(temp)
print(output)
