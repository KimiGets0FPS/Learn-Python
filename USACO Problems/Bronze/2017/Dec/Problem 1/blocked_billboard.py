import sys

sys.stdin = open("billboard.in", 'r')
dimensions = []
for i in range(3):
    nums = list(map(int, input().split()))
    dimensions += [[[nums[0], nums[1]], [nums[2], nums[3]]]]

r1 = dimensions[0]
r2 = dimensions[1]
truck = dimensions[2]


def if_intersect(sq, tr):
    if not ((sq[0] >= tr[2] or sq[2] <= tr[0]) or (sq[1] >= tr[2] or sq[3] <= tr[1])):
        return True
    return False


def inter_area(sq, tr):
    if if_intersect(sq, tr):
        result = (min(sq[2], tr[2]) - max(sq[0], tr[0])) * (min(sq[3], tr[3]) - max(sq[1], tr[1]))
        if result > 0:
            return result
    return 0


print((((r1[1][0] - r1[0][0]) * (r1[1][1] - r1[0][1])) +
       ((r2[1][0] - r2[0][0]) * (r2[1][1] - r2[0][1])) -
       (inter_area([r1[0][0], r1[0][1], r1[1][0], r1[1][1]], [truck[0][0], truck[0][1], truck[1][0], truck[1][1]]) +
        inter_area([r2[0][0], r2[0][1], r2[1][0], r2[1][1]], [truck[0][0], truck[0][1], truck[1][0], truck[1][1]]))),
      file=open("billboard.out", 'w'))
