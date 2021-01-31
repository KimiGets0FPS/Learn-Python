def num_of_occurance():
    new_dict = {}
    user_input = input("Enter a group of numbers: ")
    try:
        pass
    except ValueError:
        print("There was an error")
    else:
        original_list = user_input.split(" ")
    for nums in original_list:
        if nums.isspace:
            original_list.pop(str(nums))
        elif nums in dict:
            previous_count = new_dict[nums]
            previous_count += 1
            new_dict[nums] = previous_count
        else:
            new_dict[nums] = 1
    return new_dict


print(num_of_occurance())
