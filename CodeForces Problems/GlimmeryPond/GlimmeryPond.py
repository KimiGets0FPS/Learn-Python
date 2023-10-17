def main():
    n, m, k = input().split()
    n, m, k = int(n), int(m), int(k)
    pond = []
    for i in range(n):
        pond.append(list(map(int, input().split())))
    
    for i in range(n):
        for j in range(m):
            if j + k > m:
                break
            the_sum = 0
            for x in range(k):
                for y in range(k):
                    the_sum += pond[i+x][j+y]
            if the_sum % 2 == 0:
                return "true"
        if i + k > n:
            break
    return "false"

if __name__ == "__main__":
    print(main())
