fin = open('lifeguards.in', 'r')
nums = []
for i in range(int(fin.readline())):
    nums.append(list(map(int, fin.readline().split())))

# Solution

# creating every non-repeating possibility for the lifeguards to be fired.
lifeguard = sorted(nums)
output = 0
for i in range(len(lifeguard)-1):
    new = lifeguard.copy()
    new.pop(i)
    covered = new[-1][1] - new[0][0]
    for j in range(len(new)-1):
        if new[j][1] < new[j+1][0]:
            covered -= new[j+1][0] - new[j][1]
    output = max(output, covered)

print(output)

with open('lifeguards.out', 'w') as out:
    print(output, file=out)
