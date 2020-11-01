def wash_them_hands(wash_day, many_months):
    """
    >>> wash_them_hands(8, 7)
    '588 min(s) and 0 sec(s)'
    >>> wash_them_hands(7, 9)
    '661 min(s) and 30 sec(s)'
    """
    wash_hand_sec = 21
    days_month = 30
    total = wash_day*many_months*days_month*wash_hand_sec
    min_output = total//60
    sec_output = total % 60
    return '{} min(s) and {} sec(s)'.format(min_output, sec_output)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
