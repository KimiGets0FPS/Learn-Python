def main():
    print(solution("sadbutsad", "sad"))


def solution(haystack, needle):
    if len(needle) >= len(haystack):
        if needle == haystack:
            return 0
        return -1
    for i in range(len(haystack)-len(needle)+1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1


if __name__ == '__main__':
    main()
