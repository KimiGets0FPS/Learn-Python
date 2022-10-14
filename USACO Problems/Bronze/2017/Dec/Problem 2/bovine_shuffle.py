import sys


sys.stdin = open('shuffle.in', 'r')
sys.stdout = open('shuffle.out', 'w')
n = int(input())
swap = list(map(int, input().split()))
cow_id = list(map(int, input().split()))
# Solution

output = []
for i in range(3):
    temp = list('0'*n)
    for j in range(len(cow_id)):
        for x in range(len(swap)):
            temp[x] = cow_id[swap[x]-1]
    cow_id = temp
    output = temp

print(i for i in output)
