def main(cows, moves):
    if moves:

        # for i in range(len(cows)):
        #     for j in range(moves, i, -1):
        #         if cows[j] == cows[i]:
        #             cows[i] = "."
        count = 0
        for i in range(len(cows)):
            if cows[i] != ".":
                count += 1
        return [count, ''.join(cows)]
    return [len(cows), ''.join(cows)]


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, k = list(map(int, input().split()))
        c = list(input())
        out = main(c, k)
        print(f"{out[0]}\n{out[1]}")
