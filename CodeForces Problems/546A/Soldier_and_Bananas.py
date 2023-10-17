def main():
    k, n, w = list(map(int, input().split()))
    cost = 0
    for i in range(w):
        cost += (k*(i+1))
    if n >= cost:
        return 0
    return cost-n


if __name__ == "__main__":
    print(main())
