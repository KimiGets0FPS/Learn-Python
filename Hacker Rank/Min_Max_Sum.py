def min_max(arr):
    arr.sort()
    return f"{sum(arr[0:4])} {sum(arr[1:5])}"


if __name__ == "__main__":
    print(min_max(list(map(int, input().split()))))
