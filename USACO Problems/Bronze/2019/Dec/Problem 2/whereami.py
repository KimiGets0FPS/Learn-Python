import sys

sys.stdin = open("whereami.in", "r")
sys.stdout = open("whereami.out", "w")

input()

mailbox = list(input())
unique = set(mailbox)
count = 0
for i in range(len(mailbox)):
    ...
# print(set(mailbox))
print(count)
