def main(ferry, starting, destination, roads, docks, price, current):  # Recursive backtacking??
    if current == starting:
        return price
    flag = False
    for i in range(len(roads)):
        ...
    if flag:
        for i in range(len(roads)):
            ...


if __name__ == "__main__":
    for _ in range(int(input())):
        n, f, s, d = input().split()
        road = []
        dock = []
        for _ in range(n):
            segment = input().split()
            if segment[0] == "ROAD":
                road.append([segment[1], segment[2]])
            else:
                dock.append(segment[1])
        cost = main(f, s, d, road, dock, price=-1, current=s)
        if cost == -1:
            print("Just stay home")
        if cost == 0:
            print("The trip's free!")
        elif cost >= 0:
            print(f"Bring {cost} for the trip.")
        input()  # Blank Line
