# Problem: http://www.usaco.org/index.php?page=viewproblem2&cpid=737
# IDK how to solve because I'm bad.
fin = open("art.in", 'r')
wl = int(fin.readline())

painting = []
for i in range(wl-1):
    painting.append(list(map(int, fin.readline().split())))

print(painting)


print(..., file=open("art.out", 'w'))
