import sys
import math


read = sys.stdin.read
write = sys.stdout.write


def main(room, table1, table2):
    horizontal = math.inf
    vertical = math.inf
    if table1[2] - table1[0] + table2[0] <= room[0]:
        horizontal = min(table2[0] - table1[0], table2[0] - (room[0] - table1[2]))

    if table1[3] - table1[1] + table2[1] <= room[1]:
        vertical = min(table2[1] - table1[1], table2[1] - (room[1] - table1[3]))

    ans = min(horizontal, vertical)
    if ans < 0:
        ans = 0
    return ans if ans != math.inf else -1


for i in range(int(input())):
    size_of_room = list(map(int, input().split()))
    t1 = list(map(int, input().split()))
    t2 = list(map(int, input().split()))
    print(main(size_of_room, t1, t2))
    
