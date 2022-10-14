import sys


sys.stdin = open("gymnastics.in", "r")
sys.stdout = open("gymnastics.out", "w")

k, n = map(int, input().split())
nums = []
for i in range(k):
    nums.append(list(map(int, input().split())))

# solution

# Number -> Index
# Index -> Number
indexes = []
for i in range(len(nums)):
    temp = [0] * n
    for j in range(len(nums[i])):
        temp[nums[i][j]-1] = j
    indexes.append(temp)

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
