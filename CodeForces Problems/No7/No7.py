num = int(input()) - 1

while True:
    flag = False
    for i in str(num):
        if i == "7":
            flag = True
            break
    if flag:
        num -= 1
    else:
        break
print(num)