def num_of_occurrence():
    new_dict = {}
    user_input = input("Enter a group of numbers (seperated by spaces): ")
    original_list = user_input.split(" ")
    for num in range(len(original_list)):
        new_dict[int(original_list[num])] = new_dict.get(int(original_list[num]), 0) + 1
    return new_dict


print(num_of_occurrence())
