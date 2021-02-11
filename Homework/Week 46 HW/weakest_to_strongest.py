def weakest_to_strongest(matrix, limit):
    """
    >>> weakest_to_strongest([[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]], 3)
    [2, 0, 3]
    >>> weakest_to_strongest([[1,0,0,0], [1,1,1,1], [1,0,0,0], [1,0,0,0]], 2)
    [0, 2]
    """
    dictionary = {}
    for i in range(len(matrix)):
        dictionary[i] = sum(matrix[i])
    return sorted(dictionary, key=dictionary.get)[:limit]
    # Time Complexity = O(n)
    # Space Complexity = O(n**2)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
