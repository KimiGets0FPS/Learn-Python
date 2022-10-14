import string
import sys


sys.stdin = open('blocks.in', 'r')
sys.stdout = open('blocks.out', 'w')
n = int(input())

words = []
for i in range(n):
    words.append(input().split())

print(words)

# Solution

letters = dict.fromkeys(string.ascii_lowercase, 0)

# output = []
for i in range(len(words)):
    count = 0
    for j in range(len(words[i])):
        for x in range(len(words[i][j])):
            letters[words[i][j][x]] += 1

print(i for i in letters)
