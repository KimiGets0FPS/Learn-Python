import math
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def _mad(m, n):
    diff = []
    for i in range(len(n)):
        diff.append(abs(m - n[i]))
    mad = sum(diff) / len(diff)
    return mad


def _variance(m, n):
    diff = []
    for i in range(len(n)):
        diff.append((m - n[i]) ** 2)
    var = sum(diff) / (len(diff))
    return var


def _quartiles(n: list[int]) -> list[int]:
    if len(n) % 2 == 0:
        median = (n[int(len(n)/2)] + n[int(len(n)/2-1)]) / 2
        p1 = n[:int(len(n)/2-1)]
        p2 = n[int(len(n)/2):]

    else:
        median = n[int(len(n)//2)]
        p1 = n[:int(len(n)//2)]
        p2 = n[int(len(n)//2):]

    if len(p1) % 2 == 0 and len(p2) % 2 == 0:  # Both because I have issues
        q1 = (p1[int(len(p1)/2)] + p1[int(len(p1)/2-1)]) / 2
        q3 = (p2[int(len(p2)/2)] + p2[int(len(p2)/2-1)]) / 2
    else:
        q1 = p1[int(len(p1)//2)]
        q3 = p2[int(len(p2)//2)]

    return [q1, median, q3]


def main():
    while True:
        nums = list(map(int, input("Enter a list of numbers (separated by spaces): ").split()))

        nums.sort()

        # Sorted, Length, and Range
        print(f"Sorted: {nums}\nLength: {len(nums)}, Range: {nums[-1] - nums[0]}")

        # Finding the 3 Quartiles
        print(f"Min: {nums[0]}, Q1: {_quartiles(nums)[0]}, Median: {_quartiles(nums)[1]}, Q3: {_quartiles(nums)[2]}, "
              f"Max: {nums[-1]}")

        # Mean
        mean = sum(nums) / (len(nums))
        print(f"Mean (average): {mean}")

        # MAD
        print(f"MAD: {_mad(mean, nums)}")

        # Variant and Standard Deviation
        print(f"Variance: {_variance(mean, nums)}, Standard Deviation: {math.sqrt(_variance(mean, nums))}")

        if input("Modification: "):
            while True:
                modifier = input("Enter a modifier (plus, minus, etc.): ")
                if modifier:
                    while True:
                        number = input(f"Enter Number (modifier: {modifier}): ")
                        if number:
                            number = float(number)
                            clear()
                            if modifier == "+":
                                print(f"Mean: {mean + number}\n"
                                      f"Median: {_quartiles(nums)[1] + number}\n"
                                      f"Range: {nums[-1] - nums[0]}\n"
                                      f"Standard Deviation: {math.sqrt(_variance(mean, nums))}"
                                      )

                            elif modifier == "-":
                                print(f"Mean: {mean - number}\n"
                                      f"Median: {_quartiles(nums)[1] - number}\n"
                                      f"Range: {nums[-1] - nums[0]}\n"
                                      f"Standard Deviation: {math.sqrt(_variance(mean, nums))}"
                                      )

                            elif modifier == "*":
                                print(f"Mean: {mean * number}\n"
                                      f"Median: {_quartiles(nums)[1] * number}\n"
                                      f"Range: {(nums[-1] - nums[0]) * number}\n"
                                      f"Standard Deviation: {(math.sqrt(_variance(mean, nums))) * number}"
                                      )

                            elif modifier == "/":
                                print(f"Mean: {mean / number}\n"
                                      f"Median: {_quartiles(nums)[1] / number}\n"
                                      f"Range: {(nums[-1] - nums[0]) / number}\n"
                                      f"Standard Deviation: {(math.sqrt(_variance(mean, nums))) / number}")
                            input("Press Enter to Continue...")
                            clear()

                        else:
                            clear()
                            break

                else:
                    clear()
                    break

        input("Press Enter to Continue...")
        clear()


if __name__ == "__main__":
    clear()
    main()
