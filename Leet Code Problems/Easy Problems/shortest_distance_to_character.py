# TODO: FINISH THIS PROBLEM
# LINK: https://leetcode.com/problems/shortest-distance-to-a-character/


def shortest_distance_to_a_character(string: str, target: str) -> list[int]:
    """
    >>> shortest_distance_to_a_character("loveleetcode", "e")
    [3, 2, 1, 0, 1, 0, 0, 4, 3, 2, 1, 0]
    """
    output = []
    temp = []
    no_occ_ind = 0
    for i in range(len(string)):
        no_occ_ind += 1
        if string[i] == target:
            no_occ_ind = 0
        output.append(no_occ_ind)
    return output


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
