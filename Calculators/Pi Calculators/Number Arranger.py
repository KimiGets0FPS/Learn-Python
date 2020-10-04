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
def max_min():
    list = []
    while True:
        user_input = int(input("Choose your number(0 to stop): "))
        if user_input > 0:
            list.append(user_input)
        else:
            break
    min_value = minimum(list)
    print("The smallest number on this list is: ", min_value)
    max_value = maximum(list)
    print ("The biggest number on this list is: ", max_value)
#######################################################################################################################################################################
#######################################################################################################################################################################
def stats(numbers):
    numbers.sort()
    return (numbers[0],numbers[-1])
def number_sort():
    list = []
    while True:
        user_input = int(input("What number do you want?(Enter 0 to stop)"))
        if user_input > 0:
            list.append(user_input)
        else:
            min,max = stats(list)
            print (list)
            break 
#######################################################################################################################################################################
#######################################################################################################################################################################
def olivers_code_V2():
    new_list = []
    while True:
        user_input = input("Please enter a number: ")
        b = user_input.split() 
    for c in range(len(b)):
        b[c] = int(b[c])
    small = b[0]
    while b != []:
        for x in range(len(b)):
            if small > b[x]:
                small = b[x]
    new_list = new_list + [small]
    b.remove(small)
    print (n)
#######################################################################################################################################################################
#######################################################################################################################################################################           
# Running the code
max_min()
number_sort()
olivers_code_V2()
