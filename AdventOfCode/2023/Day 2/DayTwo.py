import sys


sys.stdin = open("DayTwo.in", "r")
sys.stdout = open("DayTwo.out", "w")


def get_input():
    while True:
        game = sys.stdin.readline()[:-1]
        if game:
            print(game)
            for i in range(len(game)):
                if game[i] == ":" or game[i] == ";":
                    ...
        else:
            break



def main():
    get_input()


def solution() -> bool:
    ...


if __name__ == "__main__":
    main()
