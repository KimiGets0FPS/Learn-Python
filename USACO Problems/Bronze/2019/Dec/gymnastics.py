fin = open("gymnastics.in", "r")
k, n = map(int, fin.readline().split())
nums = []
for i in range(k):
    nums.append(list(map(int, fin.readline().split())))
print(nums)

# solution

# Number -> Index
# Index -> Number
indexes = []
for i in range(len(nums)):
    temp = [0] * n
    for j in range(len(nums[i])):
        temp[nums[i][j]-1] = j
    indexes.append(temp)
print(indexes)

output = 0
for i in range(len(nums[0])-1):
    for j in range(i+1, len(nums[0])):
        flag = True
        for x in range(len(indexes)):
            if indexes[x][nums[0][i]-1] > indexes[x][nums[0][j]-1]:
                flag = False
                break
        if flag:
            output += 1

print(output)

with open('gymnastics.out', 'w') as out:
    print(output, file=out)
