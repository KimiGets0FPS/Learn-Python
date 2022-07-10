import sys


sys.stdin = open('speeding.in', 'r')
sys.stdout = open('speeding.out', 'w')
n, m = list(map(int, input().split()))
lv = []
for i in range(n):
    lv.append(list(map(int, input().split())))
info = []
for i in range(m):
    info.append(list(map(int, input().split())))

# Solution

speed_limit = []
for i in range(len(lv)):
    for j in range(lv[i][0]):
        speed_limit.append(lv[i][1])

bessie = []
for i in range(len(info)):
    for j in range(info[i][0]):
        bessie.append(info[i][1])

output = 0
for i in range(100):
    output = max(output, bessie[i]-speed_limit[i])

print(output)
