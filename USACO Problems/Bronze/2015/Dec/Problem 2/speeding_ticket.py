fin = open('speeding.in', 'r')
n, m = list(map(int, fin.readline().split()))
lv = []
for i in range(n):
    lv.append(list(map(int, fin.readline().split())))
info = []
for i in range(m):
    info.append(list(map(int, fin.readline().split())))

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

with open('speeding.out', 'w') as out:
    print(output, file=out)
