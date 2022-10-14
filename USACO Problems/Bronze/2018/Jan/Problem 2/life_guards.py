import sys


sys.stdin = open('lifeguards.in', 'r')
sys.stdout = open('lifeguards.out', 'w')
nums = []
for i in range(int(input())):
    nums.append(list(map(int, input().split())))

# Solution

nums.sort()
output = 0
for i in range(len(nums)-1):
    new = nums.copy()
    new.pop(i)
    covered = new[-1][1] - new[0][0]
    for j in range(len(new)-1):
        if new[j][1] < new[j+1][0]:
            covered -= new[j+1][0] - new[j][1]
    output = max(output, covered)


print(output)
