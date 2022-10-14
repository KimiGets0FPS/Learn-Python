import sys
import math


sys.stdin = open('balancing.in', 'r')
sys.stdout = open('balancing.out', 'w')

n, b = list(map(int, input().split()))
nums = []
for _ in range(n):
    nums.append(list(map(int, input().split())))

x, y = [math.inf, 0], [math.inf, 0]
for i in range(n):
    x[0], x[1], y[0], y[1] = min(x[0], nums[i][0]), max(x[1], nums[i][0]), min(y[0], nums[i][1]), max(y[1], nums[i][1])

top_left = [x[0], y[-1]]
bottom_right = [x[-1], y[0]]

c_y = y[-1] - 1
output = math.inf
while c_y > y[0]:
    c_x = x[0] + 1
    while c_x < x[-1]:
        quad_1, quad_2, quad_3, quad_4 = 0, 0, 0, 0
        for i in range(n):
            if nums[i][0] > c_x and nums[i][1] > c_y:
                quad_1 += 1
            elif nums[i][0] < c_x and nums[i][1] > c_y:
                quad_2 += 1
            elif nums[i][0] < c_x and nums[i][1] < c_y:
                quad_3 += 1
            elif nums[i][0] > c_x and nums[i][1] < c_y:
                quad_4 += 1
        c_x += 2
        output = min(output, max([quad_1, quad_2, quad_3, quad_4]))
    c_y -= 2

print(output)
