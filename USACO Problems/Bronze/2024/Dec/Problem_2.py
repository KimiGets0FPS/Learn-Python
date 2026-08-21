def main():
    n, q = map(int, input().split())
    coords = [[[False for _ in range(n)] for _ in range(n)] for _ in range(n)]

    count = 0
    for i in range(q):
        x, y, z = map(int, input().split())
        if not coords[x][y][z]:
            coords[x][y][z] = True

            count += solution(n, coords, x, y, z)

        print(count)

def solution(n, coords, x, y, z):
    output = 0

    j = 0
    for i in range(n):
        if not coords[i][y][z]:
            break
        j += 1

    if j == n:
        output += 1


    j = 0
    for i in range(n):
        if not coords[x][i][z]:
            break
        j += 1

    if j == n:
        output += 1

    j = 0
    for i in range(n):
        if not coords[x][y][i]:
            break
        j += 1

    if j == n:
        output += 1

    return output


if __name__ == '__main__':
    main()
