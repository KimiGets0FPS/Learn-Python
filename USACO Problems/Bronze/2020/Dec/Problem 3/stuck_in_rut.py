import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
cows = []
for i in range(n):
    cows.append(input().split())

print(f"{cows}")
