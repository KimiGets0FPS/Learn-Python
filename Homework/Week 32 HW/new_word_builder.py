def new_words(letter_list, num_list):
    """
    >>> new_words(["g", "e", "o"], [1, 0, 2])
    'ego'
    >>> new_words(["e", "t", "s", "t"], [3, 0, 2, 1])
    'test'
    """
    original_num = 0
    output = []
    if len(letter_list) == len(num_list):
        for _ in letter_list, num_list:
            letter_list[original_num] = letter_list[num_list[original_num]]
            original_num += 1
            output.append(letter_list)
        return output
    return 'letter list does not equal to number list.'


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
