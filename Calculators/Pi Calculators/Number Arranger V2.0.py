def minimum(number_list):
    y = number_list[0]
    for x in number_list:
        if x < y:
            y = x
    return y
def maximum(number_list):
    y = number_list[0]
    for x in number_list:
        if x > y:
            y = x
    return y
def play():
    list = []
    while True:
        user_input = int(input("Choose a number to be sorted!(0 to stop) "))
        if user_input == 0:
            max_value = maximum(list)
            min_value = minimum(list)
            print ("The biggest number in the list is ", max_value)
            print ("The smallest number in the list is ", min_value)
            break
        else:
            list.append(user_input)
play()
