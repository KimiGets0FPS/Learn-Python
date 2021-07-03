def prime_nums_are_hehe(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


print(prime_nums_are_hehe(7))
