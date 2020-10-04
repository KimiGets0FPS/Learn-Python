def tower_of_hanoi(num):
    return 2 ** num - 1  # algorithm is 2 ** number - 1


run = tower_of_hanoi(5)
# print(f"There are {run} steps.")


def hello(num_list, num):
    i = 0
    index_nums = []
    for number in num_list:
        if number == num:
            index_nums.append(i)
        i += 1
    return index_nums


numbers = [1, 3, 5, 3, 8, 9, 3]  # Edit the list of numbers
print(hello(numbers, 9))  # Edit the second number two
