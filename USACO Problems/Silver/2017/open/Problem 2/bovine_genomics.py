import sys


sys.stdin = open('cownomics.in', 'r')
sys.stdout = open('cownomics.out', 'w')

n, m = list(map(int, input().split()))
s_cow, p_cow = [], []
for _ in range(n):
    s_cow.append(input())
for _ in range(n):
    p_cow.append(input())


def main():
    output = 0
    for q in range(m-2):
        for w in range(q+1, m-1):
            for e in range(w+1, m):
                flag = True
                s_s, s_p = set(), set()
                for r in range(n):
                    s_s.add(s_cow[r][q]+s_cow[r][w]+s_cow[r][e])
                    s_p.add(p_cow[r][q]+p_cow[r][w]+p_cow[r][e])
                for r in s_s:
                    if r in s_p:
                        flag = False
                        break
                if flag:
                    output += 1
    print(output)


main()
