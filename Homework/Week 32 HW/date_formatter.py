def date_format_mode(date):
    """
    >>> date_format_mode('11/12/2019')
    '20191211'
    >>> date_format_mode('12/31/2019')
    '20193112'
    >>> date_format_mode('01/15/2019')
    '20191501'
    >>> date_format_mode('12/13/1234')
    '12341312'
    """
    random_name = date.split("/")
    # return random_name # This is just a test
    random_name[0], random_name[2] = random_name[2], random_name[0]
    return ''.join(random_name)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
