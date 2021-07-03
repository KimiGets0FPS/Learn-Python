def palindrome_recursion(word):
    """
    >>> palindrome_recursion('lol')
    True
    >>> palindrome_recursion('yes')
    False
    >>> palindrome_recursion('')
    True
    """
    if len(word) > 1:
        letters = list(word)
        if letters[0] == letters[-1]:
            letters.pop(0)
            letters.pop(-1)
            palindrome_recursion(''.join(letters))
        else:
            return False
    return True


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
