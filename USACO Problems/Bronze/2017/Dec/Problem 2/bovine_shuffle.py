fin = open('shuffle.in', 'r')
n = int(fin.readline())
swap = list(map(int, fin.readline().split()))
cow_id = list(map(int, fin.readline().split()))
# Solution

output = []
for i in range(3):
    temp = list('0'*n)
    for j in range(len(cow_id)):
        for x in range(len(swap)):
            temp[x] = cow_id[swap[x]-1]
    cow_id = temp
    output = temp

print(output)

with open('shuffle.out', 'w') as out:
    for i in range(len(output)):
        print(output[i], file=out)
