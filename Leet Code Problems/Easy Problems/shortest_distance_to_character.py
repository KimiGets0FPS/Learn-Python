# TODO: FINISH THIS PROBLEM
# LINK: https://leetcode.com/problems/shortest-distance-to-a-character/


def shortest_distance_to_a_character(string: str, target: str) -> list[int]:
    """
    >>> shortest_distance_to_a_character("loveleetcode", "e")
    [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
    """
    output = []
    latest_occ = 0
    for i in range(len(string)):
        if string[i] == target:
            output.append(abs(latest_occ-i))
            latest_occ = 0
        else:
            output.append(latest_occ)
            latest_occ += 1
    return output


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
