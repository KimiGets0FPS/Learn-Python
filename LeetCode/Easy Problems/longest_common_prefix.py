def longest_common_prefix(strings: list[str]) -> str:
    """
    >>> longest_common_prefix(['flower', 'flooring', 'float'])
    "flo"
    """
    output = []
    i = 0  # Used because I don't want O(n^3)
    for word in strings:
        for letter in word:
            if len(list(word)) >= len(output):
                output.append(letter)
        i += 1
    return ''.join(output)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
