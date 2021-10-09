start = int(input())
output = [str(start)]
while True:
    if start == 1:
        break
    if start % 2 == 0:
        start /= 2
    elif start % 2 != 0:
        start = (start * 3) + 1
    output.append(str(int(start)))

print(' '.join(output))
