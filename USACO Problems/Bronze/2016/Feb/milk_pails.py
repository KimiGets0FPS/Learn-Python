fin = open("pails.in", "r")

x, y, m = list(map(int, open('pails.in', 'r').readline().split()))

# Compete Search Method
# Brute Force

output = 0
c1, c2 = [], []
m1, m2 = 1, 1
while x*m1 <= m:
    c1.append(x*m1)
    m1 += 1
print(c1)

while y*m2 <= m:
    c2.append(y*m2)
    m2 += 1
print(c2)

for i in c1:
    for j in c2:
        if output < i + j <= m:
            output = i + j


with open("pails.out", "w") as out:
    print(output, file=out)
