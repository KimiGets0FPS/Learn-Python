def main():
    test_cases = int(input())

    for _ in range(test_cases):
        print(solution(int(input())))

def solution(n):
    output = 0

    if n < 45:
        return output
    if n < 49:
        return output - 45 + 1 + n
    output += 5

    if n < 445:
        return output
    if n < 499:
        return output - 445 + 1 + n
    output += 55

    if n < 4445:
        return output
    if n < 4999:
        return output - 4445 + 1 + n
    output += 555

    if n < 44445:
        return output
    if n < 49999:
        return output - 44445 + 1 + n
    output += 5555

    if n < 444445:
        return output
    if n < 499999:
        return output - 444445 + 1 + n
    output += 55555

    if n < 4444445:
        return output
    if n < 4999999:
        return output - 4444445 + 1 + n
    output += 555555

    if n < 44444445:
        return output
    if n < 49999999:
        return output - 44444445 + 1 + n
    output += 5555555

    if n < 444444445:
        return output
    if n < 499999999:
        return output - 444444445 + 1 + n
    output += 55555555

    if n < 4444444445:
        return output
    if n < 4999999999:
        return output - 4444444445 + 1 + n


if __name__ == '__main__':
    main()