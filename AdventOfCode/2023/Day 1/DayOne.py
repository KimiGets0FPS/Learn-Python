import sys

sys.stdin = open("DayOne.in", "r")
sys.stdout = open("DayOne.out", "w")

words = []
while True:
    word = sys.stdin.readline()[:-1]
    if not word:
        break
    else:
        words.append(word)


nums = []
for i in range(len(words)):
    number = ""
    for j in range(len(words[i])):
        if 48 <= int(ord(words[i][j])) <= 57:
            number += words[i][j]
    nums.append(number)

new_nums = []
for i in range(len(nums)):
    first, second = int(nums[i][0]) * 10, int(nums[i][-1])
    new_nums.append(first + second)

print(sum(new_nums))
