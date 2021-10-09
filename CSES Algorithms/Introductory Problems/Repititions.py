DNA = input()
output = 0
for i in range(len(DNA)):
    count = 1
    for j in range(i+1, len(DNA)):
        if DNA[i] != DNA[j]:
            break
        else:
            count += 1
    output = max(output, count)

print(output)
