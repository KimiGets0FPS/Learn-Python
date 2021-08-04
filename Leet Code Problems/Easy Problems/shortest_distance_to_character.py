# TODO: SUBMIT THIS PROBLEM
# LINK: https://leetcode.com/problems/shortest-distance-to-a-character/


def shortest_distance_to_a_character(string: str, target: str) -> list[int]:
    """
    >>> shortest_distance_to_a_character("loveleetcode", "e")
    [3, 2, 1, 0, 1, 0, 0, 4, 3, 2, 1, 0]
    """
    count = 0
    output = []
    for i in range(len(string)-1, -1, -1):
        if string[i] == target:
            count = 0
            output.append(count)
        else:
            count += 1
            output.append(count)
    return output[::-1]


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
