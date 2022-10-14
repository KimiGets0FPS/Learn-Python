def diagonal_difference(arr):
    sum_1 = 0
    for i in range(len(arr[0])):
        sum_1 += arr[i][i]

    sum_2 = 0
    count = 0
    for i in range(len(arr[0])-1, -1, -1):
        print(arr[i][count])
        sum_2 += arr[i][count]
        count += 1

    print(sum_1, sum_2)
    return abs(sum_1 - sum_2)


if __name__ == "__main__":
    n = int(input())
    array = []
    for _ in range(n):
        array.append(list(map(int, input().split())))
    print(diagonal_difference(array))
