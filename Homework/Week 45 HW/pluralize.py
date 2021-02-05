def pluralize(words: list) -> list:
    """
    >>> pluralize(["cow", "pig", "cow", "cow"])
    ['cows', 'pig']
    >>> pluralize(["table", "table", "table"])
    ['tables']
    """
    output = []
    for i in words:
        if words.count(i) >= 2:
            if i + 's' not in output:
                output.append(i + 's')
        else:
            output.append(i)
    return output


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
