import sys

sys.stdin = open('square.in', 'r')
sys.stdout = open('square.out', 'w')

r1 = list(map(int, input().split()))
r2 = list(map(int, input().split()))

print(max((max(r1[2], r2[2]) - min(r1[0], r2[0])), (max(r1[3], r2[3])) - min(r1[1], r2[1]))**2)
