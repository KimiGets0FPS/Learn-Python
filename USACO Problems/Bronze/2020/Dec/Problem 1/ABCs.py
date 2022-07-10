import sys

write = sys.stdout.write

nums = list(map(int, sys.stdin.readline().split()))

nums.sort()
a, b, c = nums[0], nums[1], nums[-1]-nums[0]-nums[1]
print(f"{a} {b} {c}")
