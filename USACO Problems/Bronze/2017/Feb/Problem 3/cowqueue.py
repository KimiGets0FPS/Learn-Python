import sys


sys.stdin = open("cowqueue.in", 'r')
sys.stdout = open('cowqeue.out', 'w')

num = int(input())
cows = []
for i in range(num):
    cows.append(list(map(int, input().split())))

# Solution

cows = sorted(cows)  # Sort by starting time
print(cows)
output = 0  # Current time and output
for i in range(len(cows)):
    if output >= int(cows[i][0]):
        output += int(cows[i][1])
    else:
        output = int(cows[i][0]) + int(cows[i][1])


print(output)

