def max_word_in_sentences(sentences: list[str]) -> int:
    """
    >>> max_word_in_sentences(["alice and bob love leetcode", "i think so too", "this is great thanks very much"])
    6
    >>> max_word_in_sentences(["please wait", "continue to fight", "continue to win"])
    3
    """
    output = 0
    for i in sentences:
        output = max(output, len(i.split()))
    return output


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
