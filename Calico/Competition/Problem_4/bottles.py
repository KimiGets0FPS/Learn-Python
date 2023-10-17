def main(time):
    new_time = []
    for i in range(len(time)):
        new_time.append([time[i], i])

    new_time.sort()
    time_required = 0
    acc = 0

    for i in new_time:
        time_required += acc + i[0]
        acc += i[0]
    output = [time_required]

    for i in new_time:
        output.append(i[1] + 1)

    return output


if __name__ == "__main__":
    for _ in range(int(input())):
        input()
        result = main(list(map(int, input().split())))
        print(result[0])
        print(' '.join(list(map(str, result[1:]))))
