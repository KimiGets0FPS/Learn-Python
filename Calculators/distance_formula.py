import math


def main():
    while True:
        e1, e2 = list(map(float, input("First set of coordinates: ").split()))
        e3, e4 = list(map(float, input("Second set of coordinates: ").split()))

        print(f"Distance: {math.sqrt(((e1-e3)**2) + ((e2-e4)**2))}")


if __name__ == "__main__":
    main()
