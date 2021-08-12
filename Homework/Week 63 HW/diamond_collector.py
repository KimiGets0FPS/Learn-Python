# I/O input
n, k = map(int, input().split())
num = []
for i in range(n):
    num.append(int(input()))

output = []
for i in range(len(num)):
    count = 0
    for j in range(len(num)):
        if num[j] - num[i] <= k and num[i] <= num[j]:
            count += 1
    output.append(count)

print(max(output))
