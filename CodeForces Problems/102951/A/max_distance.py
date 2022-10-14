import sys
import itertools


input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

for i in range(n):
    for num in itertools.combinations([x[i], y[i]], 2):
        ...

