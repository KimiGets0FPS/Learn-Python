fin = open("cowqueue.in", 'r')
num = int(fin.readline())
cows = []
for i in range(num):
    cows.append(list(map(int, fin.readline().split())))

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

print(output, file=open("cowqueue.out", 'w'))
