def factorial_recursion(times: int) -> int:
    if times > 1:
        return times * factorial_recursion(times-1)
    return times


if __name__ == '__main__':
    print(factorial_recursion(10))
