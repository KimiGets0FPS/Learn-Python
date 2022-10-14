import sys


input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
print(f"{len(set(list(map(int, input().split()))))}")
