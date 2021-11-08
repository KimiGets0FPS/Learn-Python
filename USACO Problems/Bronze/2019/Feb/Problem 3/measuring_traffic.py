import math


fin = open('traffic.in', 'r')
miles = int(fin.readline())
road_seg = []
for i in range(miles):
    road_seg.append(fin.readline().split())
    
print(road_seg)

# Solution

output = [0, 0, 0, 0]

current_a, current_b = 0, math.inf
in_a, in_b = 0, 0
# Current_a and in_a is minimum amount of cars
# Current_b and in_b is maximum amount of cars
for i in range(len(road_seg)):
    if road_seg[i][0] == 'on':
        in_a += int(road_seg[i][1])
        in_b += int(road_seg[i][2])

    elif road_seg[i][0] == 'off':
        in_a -= int(road_seg[i][2])
        in_b -= int(road_seg[i][1])

    elif road_seg[i][0] == 'none':
        current_a = max(current_a, int(road_seg[i][1]) - in_b)
        current_b = min(current_b, int(road_seg[i][2]) - in_a)

output[0] = current_a
output[1] = current_b


first, second = output[0], output[1]
for i in range(len(road_seg)):
    if road_seg[i][0] == 'on':
        first += int(road_seg[i][1])
        second += int(road_seg[i][2])

    elif road_seg[i][0] == 'off':
        first -= int(road_seg[i][2])
        second -= int(road_seg[i][1])

    elif road_seg[i][0] == 'none':
        first = max(first, int(road_seg[i][1]))
        second = min(second, int(road_seg[i][2]))

output[2] = first
output[3] = second

for i in range(len(output)):
    if output[i] < 0:
        output[i] = 0
print(output)


print(f"{output[0]} {output[1]}\n{output[2]} {output[3]}", file=open("traffic.out", 'w'))
