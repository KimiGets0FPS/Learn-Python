def missing_num_in_array(array):
    """
    >>> missing_num_in_array([0, 2, 3])
    1
    >>> missing_num_in_array([1, 2, 3])
    0
    >>> missing_num_in_array([0, 1, 2])
    3
    """
    expected_num = 0
    for _ in range(len(array)):
        if expected_num not in array:
            break
        expected_num += 1
    return expected_num
    # Time Complexity = O(n)
    # Space Complexity = O(n)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
