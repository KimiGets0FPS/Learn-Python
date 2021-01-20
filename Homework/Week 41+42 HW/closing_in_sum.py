def closing_in_sum(number):
    """
    >>> closing_in_sum(12321)
    36
    >>> closing_in_sum(1039)
    22
    """
    output = 0
    # INDEX
    first_number = 0  # Whatever this number is, it's going to be multiplied by 100.
    second_number = -1  # This number will stay the same.
    number_list = list(str(number))
    if len(number_list) % 2 != 0:
        output += int(number_list[len(number_list)//2])
    for _ in range(len(number_list)//2):
        number_list[first_number] = int(number_list[first_number])
        number_list[second_number] = int(number_list[second_number])
        number_list[first_number] *= 10
        number_list[first_number] += number_list[second_number]
        output += number_list[first_number]
        first_number += 1
        second_number -= 1
    return output


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
