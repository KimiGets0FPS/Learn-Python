import string


fin = open('blocks.in', 'r')
n = int(fin.readline())

words = []
for i in range(n):
    words.append(fin.readline().split())

print(words)

# Solution

letters = dict.fromkeys(string.ascii_lowercase, 0)

# output = []
for i in range(len(words)):
    count = 0
    for j in range(len(words[i])):
        for x in range(len(words[i][j])):
            letters[words[i][j][x]] += 1

print(letters)

for i in letters:
    print(f"{letters[i]}", file=open('blocks.out', 'a'))
