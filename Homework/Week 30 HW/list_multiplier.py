def list_multiply(thing_list):
    """
    >>> list_multiply(['Hi', 'Hey', 'HeHe'])
    [['Hi', 'Hi', 'Hi'], ['Hey', 'Hey', 'Hey'], ['HeHe', 'HeHe', 'HeHe']]
    >>> list_multiply(['A', 'B', 'C', 'D'])
    [['A', 'A', 'A', 'A'], ['B', 'B', 'B', 'B'], ['C', 'C', 'C', 'C'], ['D', 'D', 'D', 'D']]
    >>> list_multiply([1, 2, 4, 3, 5])
    [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [4, 4, 4, 4, 4], [3, 3, 3, 3, 3], [5, 5, 5, 5, 5]]
    """
    output = []
    for element in thing_list:
        the_thing_that_im_going_to_put_into_the_output = []  # XD
        for _ in thing_list:
            the_thing_that_im_going_to_put_into_the_output.append(element)
        output.append(the_thing_that_im_going_to_put_into_the_output)
    return output


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
