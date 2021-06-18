def nums_reverse_recursion(num):
    if num > 10:
        return int(str(num % 10) + str(nums_reverse_recursion(num//10)))
    return num


if __name__ == '__main__':
    print(nums_reverse_recursion(25))
