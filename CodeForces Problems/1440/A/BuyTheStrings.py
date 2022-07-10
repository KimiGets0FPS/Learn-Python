import sys

read = sys.stdin.readline
write = sys.stdout.write


def main(nums, binary):
    n, c0, c1, h = nums[0], nums[1], nums[2], nums[3]
    output = 0
    for bi in range(n):
        if binary[bi] == 0:
            if c1 + h < c0:
                output += c1
                output += h
            else:
                output += c0
        elif binary[bi] == 1:
            if c0 + h < c1:
                output += c0
                output += h
            else:
                output += c1
    return output


for i in range(int(read())):
    nu = list(map(int, input().split()))
    b = list(map(int, list(input())))
    print(main(nu, b))
