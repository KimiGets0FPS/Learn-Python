def count_num_in_list(num_list, num):
    i = 0
    index_nums = []
    for number in num_list:
        if number == num:
            index_nums.append(i)
        i += 1
    return index_nums


numbers = [1, 3, 5, 3, 8, 9, 3]  # Edit the my_list of numbers
print(count_num_in_list(numbers, 9))  # Edit the second number two
