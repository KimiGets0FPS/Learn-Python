def defanging_ip_address(address: str) -> str:
    """
    >>> defanging_ip_address('123.456.789')
    '123[.]456[.]789'
    """
    output = ''
    for i in address:
        if i == '.':
            output += '[.]'
        else:
            output += f'{i}'
    return output


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
