def neutralise_things(compare_1, compare_2):
    """
    >>> neutralise_things('+-+', '+--')
    '+-0'
    >>> neutralise_things('--++--', '++--++')
    '000000'
    >>> neutralise_things('-+-+-+', '-+-+-+')
    '-+-+-+'
    >>> neutralise_things('-++-', '-+-+')
    '-+00'
    """
    thing_1 = list(compare_1)
    thing_2 = list(compare_2)
    i = 0  # 'i' is going to be for the main structure here.
    output = []
    for _ in thing_1:
        if thing_1[i] == thing_2[i]:
            if thing_1[i] == '-':
                output.append('-')
            else:
                output.append('+')
        else:
            output.append('0')
        i += 1
    return ''.join(output)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
