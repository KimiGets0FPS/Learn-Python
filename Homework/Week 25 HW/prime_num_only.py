def prime_numbers_only(limit):
    for num in range(2, limit):
        if num % 2 == 0:
            print(num)


prime_numbers_only(100)
