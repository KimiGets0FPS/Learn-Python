import sys


fin = open('cownomics.in', 'r')
sys.stdout = open('cownomics.out', 'w')
n, m = list(map(int, fin.readline().split()))
spotty = []
for i in range(n):
    spotty.append(fin.readline()[0:-1])
plain = []
for i in range(n):
    plain.append(fin.readline()[0:-1])
# print(n, m)


# solution
output = 0
for i in range(m):  # looping spotty cow genes
    flag = True
    for j in range(n):  # looping through each spotty cow
        for x in range(n):  # looping plain
            if spotty[j][i] == plain[x][i]:
                flag = False
                break
    if flag:
        output += 1

print(output)
