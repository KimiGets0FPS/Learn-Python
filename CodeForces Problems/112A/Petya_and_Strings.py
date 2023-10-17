def main():
    string_a, string_b = input().lower(), input().lower()
    length = len(string_a)
    for i in range(length):
        if ord(string_a[i]) > ord(string_b[i]):
            return 1
        elif ord(string_a[i]) < ord(string_b[i]):
            return -1
    return 0


if __name__ == "__main__":
    print(main())
