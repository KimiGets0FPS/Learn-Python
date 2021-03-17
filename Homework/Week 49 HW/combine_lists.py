def combine_lists(n1: list[int], n2: list[int]) -> list[int]:
    """
    >>> combine_lists([1, 2, 3], [2, 5, 6, 7])
    [1, 2, 2, 3, 5, 6, 7]
    >>> combine_lists([1, 2, 3, 4], [2, 5])
    [1, 2, 2, 3, 4, 5]
    >>> combine_lists([], [])
    []
    >>> combine_lists([1, 2, 3], [1, 2, 3])
    [1, 1, 2, 2, 3, 3]
    """
    # Criteria: Combine 2 lists without errors
    output = []
    i, j = 0, 0  # n1 nums, n2 nums
    val1 = len(n1)
    val2 = len(n2)
    while val1 > i or val2 > j:
        if val1 > i and val2 > j:  # both lists
            if n1[i] >= n2[j]:
                output.append(n2[j])
                j += 1
            elif n2[j] > n1[i]:
                output.append(n1[i])
                i += 1
        elif val1 > i:  # ONLY n1 nums
            output.append(n1[i])
            i += 1
        else:  # ONLY n2 nums
            output.append(n2[j])
            j += 1
    return output
    # Time Complexity: O(n)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
