def key_and_values(input_dict):
    """
    >>> key_and_values({ 'z':'q', 'w':'f' })
    { 'q':'z', 'f':'w' }
    >>> key_and_values({ 'a': 1, 'b':2, 'c':3 })
    {1:'a', 2:'b', 3:'c'}
    """
    for _ in input_dict:
        pass


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
