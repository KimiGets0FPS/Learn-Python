def num_letters(list_words):
    """
    >>> num_letters(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    ['Monday', 'Friday', 'Sunday']
    """
    return_val = []
    for word in list_words:
        if len(word) == 6:
            return_val.append(word)
    return return_val


def lambda_fun_fun(list_words):
    """
    >>> lambda_fun_fun(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    ['Monday', 'Friday', 'Sunday']
    """
    return_val = []
    for letters in filter(lambda word: len(word) == 6, list_words):
        return_val.append(letters)
    return return_val


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
