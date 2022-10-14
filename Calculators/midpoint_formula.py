# import math


def main():
    while True:
        e1, e2 = list(map(float, input("Coords 1: ").split()))
        e3, e4 = list(map(float, input("Coords 2: ").split()))
        print(f"MidPoint: ({(e1+e3)/2}, {(e2+e4)/2})")


if __name__ == "__main__":
    main()
