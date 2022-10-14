import sys

sys.stdin = open("lineup.in", "r")
# sys.stdout = open("lineup.out", "w")

n = int(input())
r = {}
for i in range(n):
    cow_set = input().split()
    current = [cow_set[0], cow_set[-1]]
    current.sort()
    r[current[0]] = r.get(current[0], [])
    r[current[0]].append(current[1])

cows = ["Beatrice", "Belinda", "Bella", "Bessie", "Betsy", "Blue", "Buttercup", "Sue"]

rules = {}
for i in range(len(cows)):
    for j in r.keys():
        if cows[i] == j:
            rules[j] = rules.get(j, r[j])

for i in rules.keys():
    rules[i].sort()

for i in rules.keys():
    ...

print(rules)
print(cows)
