def main(velocity: float, distance: float) -> str:
    if distance / velocity <= 1:
        return "SWERVE"
    elif distance / velocity <= 5:
        return "BRAKE"
    return "SAFE"


if __name__ == "__main__":
    for _ in range(int(input())):
        v, x = list(map(float, input().split(":")))
        print(main(v, x))
