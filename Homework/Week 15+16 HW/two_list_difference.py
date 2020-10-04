def two_list_difference():
    user_input_1 = input("Give me a list of numbers ")
    set_1 = user_input_1.split(" ")
    user_input_2 = input("Give me another list of numbers ")
    set_2 = user_input_2.split(" ")
    intersect_set = set()
    new_set = set()
    for nums in set_1:
        if nums.isspace():
            set_1.remove(nums)
        elif nums in set_2:
            intersect_set.add(nums)
        else:
            new_set.add(nums)

    print(f"This is the new set: {new_set}")
    print(f"And this is the intersecting set: {intersect_set}")


two_list_difference()
