import sys
from threading import Timer


input = sys.stdin.readline


def main(letters, price):
    char_prices = []
    for i in range(len(letters)):
        char_prices.append(ord(letters[i])-96)
    char_prices.sort()
    output, acc, i = '', 0, 0
    left = {}
    while i < len(char_prices):
        if char_prices[i] + acc > price:
            break
        else:
            acc += char_prices[i]
            output += chr(char_prices[i]+96)
        i += 1

    a_output = ''
    for i in range(len(output)):
        left[output[i]] = left.get(output[i], 0) + 1

    for i in range(len(letters)):
        left[letters[i]] = left.get(letters[i], 0)
        if letters[i] in output and left[letters[i]] > 0:
            a_output += letters[i]
            left[letters[i]] -= 1
    return a_output


t = int(input())

for _ in range(t):
    le = ''.join(input().split())
    timeout = 0.01
    t = Timer(timeout, print)
    t.start()
    pr = int(input())
    t.cancel()
    print(main(le, pr))
