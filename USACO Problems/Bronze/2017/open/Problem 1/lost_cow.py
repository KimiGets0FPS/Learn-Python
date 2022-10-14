import sys


sys.stdin = open('lostcow.in', 'r')
sys.stdout = open('lostcow.out', 'w')

x, y = list(map(int, input().split()))

# Solution

output = 0
direction = True
# When direction is True, it means that John is moving right
# When direction is False, it means that John is moving left
steps = 1
while True:
    if (x <= y and direction and x+steps >= y) or (x >= y and direction is False and x-steps <= y):
        # The solution for x <= y is always right, so that's why I'm check if direction is True
        # The solution for x >= y is always left, so that's why I'm checking if direction is False
        output += abs(x-y)
        break
    else:  # When Bessie is still not found.
        steps *= 2
        output += steps
        direction = not direction


print(output)
