def main():
    matrix = []
    for _ in range(5):
        matrix.append(list(map(int, input().split())))
    return solution(matrix)


def solution(matrix):
    # target index: [2, 2]
    if matrix[2][2] == 1:
        return 0
    count = 0
    # locate
    location = []
    for i in range(len(matrix)):
        flag = False
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                location = [i+1, j+1]
                flag = True
                break
        if flag:
            break
    if location[0] > 2:
        count += (location[0]-3)
    else:
        count += (2-location[0])
    if location[1] > 2:
        count += (location[1]-3)
    else:
        count += (2-location[1])
    return count


if __name__ == "__main__":
    print(main())
