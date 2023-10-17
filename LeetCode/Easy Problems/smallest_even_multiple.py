def main():
    print(solution(5))
    print(solution(6))
    print(solution(10))


def solution(n):
    if n % 2 == 0:
        return n
    return n*2


if __name__ == "__main__":
    main()
