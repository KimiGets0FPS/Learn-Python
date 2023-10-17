def top_k_frequent(nums: list[int], target: int) -> list[int]:
    """
    >>> top_k_frequent([1,1,1,2,2,3], 2)
    >>> top_k_frequent([1], 1)
    """
    count = {}
    for i in nums:
        count.get(i, 0) + 1
    temp = []
    for i in count.items():
        temp.append(i)
    output = []
    for i in range(target):
        output.append(max(temp))
        temp.remove(max(temp))
    return output


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
