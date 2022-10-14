import sys


sys.stdin = open('cowsignal.in', 'r')
sys.stdout = open('cowsignal.out', 'w')

m, n, k = list(map(int, input().split()))
signal = []
for i in range(m):
    signal.append(input().split())

print(signal)

# Solution
output = []
for i in range(len(signal)):
    temp = ''
    for j in range(len(signal[i][0])):
        temp += signal[i][0][j] * k
    output.append([temp]*k)


for i in output:
    for j in i:
        print(j)
