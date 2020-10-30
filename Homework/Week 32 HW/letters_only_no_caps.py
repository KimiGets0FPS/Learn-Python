def letters_only(user_input):
    """
    >>> letters_only("PYTHON")
    False
    >>> letters_only("pyt hon")
    True
    >>> letters_only("python")
    True
    >>> letters_only("A1B2C3")
    False
    >>> letters_only(123)
    False
    >>> letters_only("")
    False
    """
    # Return True or False
    if isinstance(user_input, str):
        if len(user_input) == 0:
            return False
        for letter in list(user_input):
            if not letter.isalpha():
                if not letter.isspace():
                    return False
            if letter.isupper():
                return False
        return True
    return False


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
