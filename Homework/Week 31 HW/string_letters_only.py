def string_and_letters_only(input_list):
    """
    >>> string_and_letters_only(['John', '', 'Amanda', 5, 'ajdfjkagfguiadshfiuadsh5'])
    ['John', 'Amanda']
    """
    output = []
    for element in input_list:
        if isinstance(element, str) and element.isalpha():
            output.append(element)
    return output


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
