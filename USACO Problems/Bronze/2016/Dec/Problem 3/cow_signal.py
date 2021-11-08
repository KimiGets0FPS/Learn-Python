fin = open('cowsignal.in', 'r')
m, n, k = list(map(int, fin.readline().split()))
signal = []
for i in range(m):
    signal.append(fin.readline().split())

print(signal)

# Solution
output = []
for i in range(len(signal)):
    temp = ''
    for j in range(len(signal[i][0])):
        temp += signal[i][0][j] * k
    output.append([temp]*k)


with open('cowsignal.out', 'w') as out:
    for i in output:
        for j in i:
            out.write(j + '\n')
            print(j)

# O(n^2) Time complexity
# O(n) Space complexity
