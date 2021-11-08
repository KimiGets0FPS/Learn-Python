DNA = input()
output = 0
current = DNA[0]
count = 1
for i in range(1, len(DNA)):
    if current != DNA[i]:
        current = DNA[i]
        output = max(output, count)
        count = 1
    else:
        count += 1
        output = max(output, count)


print(max(output, count))
