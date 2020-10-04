def dice(dices):
    """Do not roll doubles"""
    if dices[0][0] == dices[0][1] or dices[1][0] == dices[1][1] or dices[2][0] == dices[2][1]:
        return 0
    else:
        return dices[0][0] + dices[0][1] + dices[1][0] + dices[1][1] + dices[2][0] + dices[2][1]


print(dice([(1, 2), (3, 4), (5, 6)]))
print(dice([(1, 1), (5, 6), (6, 4)]))
print(dice([(4, 5), (4, 5), (4, 5)]))
