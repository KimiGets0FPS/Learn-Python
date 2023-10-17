def main(w, o, b, cow, cbo, cbw):
    # COW: Orange to White || White to Orange
    # CBO: Brown to Orange || Orange to Brown
    # CBW: Brown to White || White to Brown
    find_min = []
    count = 0
    # Fing White
    find_min.append((o * cow) + (b * cbw))
    find_min.append((b*cbo) + ((b+o) * cow))
    find_min.append((o*cbo) + ((b+o) * cbw))

    # Find Orange
    find_min.append((w * cow) + (b * cbo))
    find_min.append((b*cbw) + ((b+w) * cow))
    find_min.append((w*cbw) + ((b+w) * cbo))

    # Find Brown
    find_min.append((w*cbw) + (o*cbo))
    find_min.append((w*cow) + ((w+o) * cbo))
    find_min.append((o*cow) + ((w+o) * cbw))

    return min(find_min)


if __name__ == "__main__":
    for _ in range(int(input())):
        w, o, b, cow, cbo, cbw = list(map(int, input().split()))
        print(main(w, o, b, cow, cbo, cbw))
