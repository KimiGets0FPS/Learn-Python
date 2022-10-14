from itertools import permutations
import sys


sys.stdin = open('triangles.in', 'r')
sys.stdout = open('triangles.out', 'w')
nums = []
for i in range(int(input())):
    nums.append(list(map(int, input().split())))

# Solution

# Finding all 3 points of a triangle

points = list(permutations(nums, 3))  # creating 3 points for a triangle

output = 0
for i in points:
    if i[0][1] == i[1][1] and i[1][0] == i[2][0]:  # checking if x and y axis are parallel
        output = max(output, abs(
            (i[0][0] * (i[1][1] - i[2][1])) + (i[1][0] * (i[2][1] - i[0][1])) + (i[2][0] * (i[0][1] - i[1][1]))
        ))  # Ax(By − Cy) + Bx(Cy − Ay) + Cx(Ay − By) -> area of triangle from a graph (searched online)

print(output)
