def num_of_occurrence():
    new_dict = {}
    user_input = input("Enter a group of numbers: ")
    original_list = user_input.split(" ")
    for num in range(len(original_list)-1):
        if original_list[num].isspace:
            original_list.pop(num)
        elif original_list[num] in new_dict:
            previous_count = original_list[num]
            previous_count += 1
            new_dict[original_list[num]] = previous_count
        else:
            new_dict[num] = 1
    return new_dict


print(num_of_occurrence())

# TODO: FINISH EDITING THIS PROBLEM
