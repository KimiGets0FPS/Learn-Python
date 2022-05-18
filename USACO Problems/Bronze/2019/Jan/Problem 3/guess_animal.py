# TODO: Unfinished


fin = open("guess.in", 'r')
num_an = int(fin.readline())

animals = {}  # name: [{characteristics}]
for i in range(num_an):
    s = fin.readline().split()
    animals[s[0]] = s[2:]

output = 0
for i in animals:
    # loop the animals
    count = 1  # The unique guess that Bessie uses to get right
    for j in animals[i]:
        for x in animals:
            if_common = False
            if i != x:
                # Find common characteristics
                for y in animals[x]:
                    # Looping through characteristics
                    if j == y:
                        if_common = True
                        break
        if if_common:
            count += 1
    output = max(output, count)

print(output)

print(output, file=open("guess.out", 'w'))
