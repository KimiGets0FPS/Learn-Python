import sys


sys.stdin = open("guess.in", 'r')
sys.stdout = open("guess.out", 'w')
nums = int(input())

animals = []
for i in range(nums):
    animals.append(set(input().split()[2:]))

output = 0
for i in range(nums):
    for j in range(i+1, nums):
        output = max(output, len(animals[i].intersection(animals[j]))+1)

print(output)
