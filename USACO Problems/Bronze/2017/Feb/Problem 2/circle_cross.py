fin = open('circlecross.in', 'r')
fences = ''.join(fin.readline().split())
print(fences)

# Solution

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Since there are only 325 (yes only) possible combinations, I'm just going to create those here

ind = {}

for i in range(len(letters)):
    ind[letters[i]] = []

for i in range(len(fences)):
    ind[fences[i]] = ind.get(fences[i], ind[fences[i]].append(i))
print(ind)

output = 0
for i in range(len(letters) - 1):
    for j in range(i + 1, len(letters)):
        if ind[letters[i]][0] < ind[letters[j]][0] < ind[letters[i]][1] < ind[letters[j]][1] or \
                ind[letters[j]][0] < ind[letters[i]][0] < ind[letters[j]][1] < ind[letters[i]][1]:
            output += 1

print(output)

with open('circlecross.out', 'w') as out:
    print(output, file=out)
