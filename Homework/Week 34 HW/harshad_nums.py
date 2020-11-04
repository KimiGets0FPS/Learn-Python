def harshad_nums(numbers):
    """
    >>> harshad_nums(481)
    True
    >>> harshad_nums(89)
    False
    >>> harshad_nums(516)
    True
    >>> harshad_nums(200)
    True
    """
    temp_list = []
    numbers = str(numbers)
    different_num = list(numbers)
    for number in different_num:
        temp_list.append(int(number))
    new_number = sum(temp_list)
    numbers = int(numbers)
    if numbers % new_number == 0:
        return True
    return False


def math_way(more_numbers):
    """
    >>> math_way(481)
    True
    >>> math_way(89)
    False
    >>> math_way(516)
    True
    >>> math_way(200)
    True
    """
    temp = more_numbers
    sums = 0
    while temp > 0:
        sums += temp % 10  # Gets the remainder thing
        temp //= 10  # Returns a full value; no decimal numbers
    if more_numbers%sums == 0:
        return True
    return False


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
