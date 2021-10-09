# Based on the problem, but the opposite solution
fin = open('shuffle_challenge.in', 'r')
n = int(fin.readline())
swap = list(map(int, fin.readline().split()))
cows = list(map(int, fin.readline().split()))

# Solution
output = []
for i in range(3):
    temp = list('0'*n)
    for j in range(len(cows)):
        for x in range(len(swap)):
            temp[x] = cows[swap[x]-1]
    cows = temp
    output = temp

print(output)


with open('shuffle_challenge.out', 'w') as out:
    for i in range(len(output)):
        print(output[i], file=out)
