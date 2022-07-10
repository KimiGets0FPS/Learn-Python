# Link: https://leetcode.com/problems/candy/


def candy(ratings):
    """
    >>> candy([1, 0, 2])
    5
    >>> candy([1, 2, 2])
    4
    """
    output = [1] * len(ratings)
    # Look behind
    prev_r = ratings[0]
    for i in range(1, len(ratings)):
        if ratings[i] <= prev_r:
            if output[i-1] != 1:
                output[i] = output[i-1] - 1
            else:
                output[i] = 1
        elif ratings[i] > prev_r:
            output[i] = output[i-1] + 1
        prev_r = ratings[i]
    # Look Ahead
    current = 1
    next_r = ratings[current]
    prev_r = ratings[0]
    for i in range(len(ratings)-1):
        if current != 1:
            next_r = ratings[current]
            current += 1
        if ratings[i] <= next_r:
            if prev_r <= ratings[i]:
                if output[i+1] != 1:
                    output[i] = output[i+1] - 1
                else:
                    output[i] = 1
            else:
                output[i] = output[i+1] + 1
        elif ratings[i] > next_r:
            output[i] = output[i+1] + 1
        prev_r = ratings[i]
    return output


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
