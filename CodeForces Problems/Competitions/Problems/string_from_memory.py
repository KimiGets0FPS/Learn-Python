import sys


input = sys.stdin.readline

t = int(input())
s = []
for _ in range(t):
    s.append(''.join(input().split()))


def main():
    for i in range(len(s)):
        days, seen = 0, []
        for j in range(len(s[i])):
            if s[i][j] not in seen:
                if len(seen) >= 3:
                    days += 1
                    seen = [s[i][j]]
                elif len(seen) < 3:
                    seen.append(s[i][j])
        if len(seen) > 0 or len(s[i]) == 1:
            days += 1
        print(days)


main()
