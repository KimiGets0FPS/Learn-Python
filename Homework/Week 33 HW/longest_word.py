def longest_word(words):
    """
    >>> longest_word("hello my name is Kimi")
    'hello'
    >>> longest_word("reeeeee my name is kiiiiimmmmmiiiiiiii rerererererererererere")
    'rerererererererererere'
    """
    length = 0
    # temp_var = ''
    output = ''
    for word in words.split():
        if len(word) > length:
            length = len(word)
            output = word

    return output


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
