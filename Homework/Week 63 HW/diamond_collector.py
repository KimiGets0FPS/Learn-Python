# I/O input
n, k = map(int, input().split())
num = []
for i in range(n):
    num.append(int(input()))

output = 0
for i in range(len(num)):  # assume nums[i] is the smallest diamond in the result
    count = 0
    for j in range(len(num)):
        if 0 <= num[j] - num[i] <= k:
            count += 1
    if count > output:
        output = count

print(output)
