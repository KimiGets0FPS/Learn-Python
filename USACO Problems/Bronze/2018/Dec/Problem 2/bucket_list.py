fin = open('blist.in', 'r')
n = int(''.join(fin.readline().split()))
cows = []
for i in range(n):
    cows.append(list(map(int, fin.readline().split())))

# Cows[i] = starting time, ending time, buckets

# Solution

print(cows)
output = 0

max_time = 0
for i in range(len(cows)):
    max_time = max(max_time, cows[i][1])

for i in range(max_time):
    current = 0
    for j in range(len(cows)):
        if cows[j][0] <= i+1 <= cows[j][1]:
            current += cows[j][2]
    output = max(output, current)

print(output)

print(output, file=open('blist.out', 'w'))
