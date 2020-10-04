def odd_even(word):
    """
    >>> odd_even("Hello")
    False
    >>> odd_even("BlaBlaBla")
    False
    >>> odd_even("Word")
    True
    """
    if len(word) % 2 == 0:
        return True
    return False


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
