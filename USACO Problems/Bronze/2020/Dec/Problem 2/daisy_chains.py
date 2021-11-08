amount = int(input())
nums = []
for i in input().split(" "):
    nums.append(int(i))

summed = amount
count = 1
current = []
for i in range(len(nums)):
    temp = i
    current.append(nums[i])
    for j in range(len(nums)):
        for x in range(count):
            if temp + 1 == j:
                current.append(nums[j])
                temp += 1
                if sum(current) / len(current) in current:
                    summed += 1
    count += 1
    current = []

print(summed)
