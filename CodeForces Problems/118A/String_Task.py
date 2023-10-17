def main():
    string = input().lower()
    new_string = ""
    vowels = ["a", "e", "i", "o", "u", "y"]
    for i in range(len(string)):
        if string[i] not in vowels:
            new_string += "." + string[i]
    return new_string


if __name__ == "__main__":
    print(main())
