def main(words):
    max_len = len(words[0])
    for i in range(1, len(words)):
        if len(words[i]) > max_len:
            max_len = len(words[i])
    output = ["*" * (max_len + 2)]
    for i in range(len(words)):
        output.append(f"*{words[i]}{' ' * (max_len - len(words[i]))}*")
    output.append("*" * (max_len + 2))
    return output


if __name__ == "__main__":
    for _ in range(int(input())):
        for line in main(input().split()):
            print(line)
