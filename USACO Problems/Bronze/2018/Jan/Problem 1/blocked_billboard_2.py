import sys

sys.stdin = open("billboard.in", 'r')
sys.stdout = open("billboard.out", 'w')

r1 = list(map(int, input().split()))
r2 = list(map(int, input().split()))

x1, y1, x2, y2 = r1[0], r1[1], r1[2], r1[3]
x3, y3, x4, y4 = r2[0], r2[1], r2[2], r2[3]

if x3 <= x1 and x2 <= x4:
    if y3 < y2 < y4:
        y2 = y3
    if y4 > y1 > y3:
        y1 = y4

if y3 <= y1 and y2 <= y4:
    if x3 < x2 < x4:
        x2 = x3
    if x4 > x1 > x3:
        x1 = x4


print((x2-x1)*(y2-y1))
