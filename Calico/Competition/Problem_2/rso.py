def main(year, name):
    trademarked = ["California", "Cal", "Berkeley"]
    if len(name) > 50:
        return "INVALID"
    if year < 2010:
        return "VALID"
    if name.split(" ")[0].title() in trademarked:
        return "INVALID"
    return "VALID"


if __name__ == "__main__":
    for _ in range(int(input())):
        year = int(input())
        name = input()
        print(main(year, name))
