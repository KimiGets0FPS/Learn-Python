def find_duplicate(array):
    """
    >>> find_duplicate([1, 2, 3, 2, 1])
    True
    """
    keep = []
    for i in array:
        if i not in keep:
            return True
        keep.append(i)
    return False
    # Time complexity = O(n)
    # Space complexity = O(2n-i) --> 2n - how many times it had to run.


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
