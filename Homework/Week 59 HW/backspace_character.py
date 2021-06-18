def backspace_character(s: str, t: str) -> bool:
    """
    >>> backspace_character('ab#c', 'ad#c')
    True
    >>> backspace_character('ab##', 'c#d#')
    True
    >>> backspace_character('a##c', '#a#c')
    True
    >>> backspace_character('a#c', 'b')
    False
    >>> backspace_character('', '')
    True
    >>> backspace_character('#abc', 'abc')
    True
    """
    list_s = []
    for i in range(len(s)):
        if s[i] == '#':
            if list_s:
                list_s.pop()
        # if s[i] == '#' and list_s:
        #     list_s.pop()
        else:
            list_s.append(s[i])
    list_t = []
    for i in range(len(t)):
        if t[i] == '#':
            if list_t:
                list_t.pop()
        # if t[i] == '#' and list_t:
        #     list_t.pop()
        else:
            list_t.append(t[i])
    return list_s == list_t


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
