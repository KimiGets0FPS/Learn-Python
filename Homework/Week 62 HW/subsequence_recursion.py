def subsequence_recursion(word, target, word_i, target_i):
    """
    >>> subsequence_recursion('cathartic', 'hac', 9, 3)
    True
    >>> subsequence_recursion('table', 'bat', 5, 3)
    False
    """
    if target_i == 0:
        return True
    #   ^^^  Eliminated the option of target_i being equal to 0
    elif word_i == 0:
        return False
    if word[word_i-1] == target[target_i-1]:
        return subsequence_recursion(word, target, word_i-1, target_i-1)
    return subsequence_recursion(word, target, word_i-1, target_i)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
