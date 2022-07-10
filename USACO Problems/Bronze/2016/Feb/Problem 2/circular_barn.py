import math
fin = open("cbarn.in", 'r')
n = int(fin.readline())
r = []
for i in range(n):
    r.append(int(''.join(fin.readline().split())))  # Wow! so good at programming

# Solution
print(r)

output = math.inf
for i in range(len(r)):
    m = 0
    current = 0
    # First iterative
    for j in range(i, len(r)):
        current += r[j] * m
        m += 1
    # Second iterative loop to i
    for j in range(i):
        current += r[j] * m
        m += 1
    output = min(output, current)

print(output)


print(output, file=open("cbarn.out", 'w'))
