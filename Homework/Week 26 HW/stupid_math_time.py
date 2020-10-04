def stupid_math_time(num_1, num_2):
    if type(num_1) is str and type(num_2) is str:
        num_1 = int(num_1)
        num_2 = int(num_2)
        return num_1 + num_2
    elif type(num_1) is int and type(num_2) is int:
        return f"{num_1}{num_2}"
    else:
        return None


print(stupid_math_time("100", "50"))
print(stupid_math_time(100, 50))
print(stupid_math_time("100", 50))
