def parentheses_clusters(parentheses: str) -> list[str]:
    """
    >>> parentheses_clusters('()()()')
    ['()', '()', '()']
    >>> parentheses_clusters('((()))')
    ['((()))']
    >>> parentheses_clusters('((()))(())()()(()())')
    ['((()))', '(())', '()', '()', '(()())']
    >>> parentheses_clusters('((())())(()(()()))')
    ['((())())', '(()(()()))']
    """
    string = ''
    count = 0
    output = []
    for i in range(len(parentheses)):
        string += parentheses[i]
        if parentheses[i] == '(':
            count += 1
        elif parentheses[i] == ')':
            count -= 1
        if count == 0:
            output.append(string)
            string = ''
    return output


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
