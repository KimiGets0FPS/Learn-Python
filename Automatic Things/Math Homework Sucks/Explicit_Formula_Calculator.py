numbers = list(map(int, input("Give a list of numbers: ").split()))

previous = 0
flag = True
for i in range(1, len(numbers)):
    if i != 1:  # Yes screw OOP
        if numbers[i-1] / numbers[i] != previous:
            flag = False
            break
    else:
        previous = numbers[i-1] / numbers[i]

if flag:
    print(f"Geometric thing, {numbers[0]}")
else:
    print(f"Arithmetic thing, {}")
