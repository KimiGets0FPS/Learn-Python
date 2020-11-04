def new_words(letter_list, num_list):
    """
    >>> new_words(['g', 'e', 'o'], [1, 0, 2])
    'ego'
    >>> new_words(['e', 't', 's', 't'], [1, 0, 2, 3])
    'test'
    >>> new_words(['b', 'e', 't', 'i', 'd', 'a'], [1, 4, 5, 0, 3, 2])
    'edabit'
    """
    i = 0
    output = []
    for _ in letter_list:
        temp = letter_list[num_list[i]]
        i += 1
        output.append(temp)
    return ''.join(output)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
