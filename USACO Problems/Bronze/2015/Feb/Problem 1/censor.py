import sys


sys.stdin = open('censor.in', 'r')
sys.stdout = open('censor.out', 'w')

word = list(input())
censored = input()


def main():
    output = []
    for i in range(len(word)):
        output.append(word[i])
        if len(output) >= len(censored) and ''.join(output[len(output)-len(censored):]) == censored:
            for _ in range(len(censored)):
                output.pop()

    print(''.join(output))


main()


