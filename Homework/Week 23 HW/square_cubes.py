def square_cube(num_1, num_2):
    if num_1**0.5 == num_2**(1/3):
        return True
    else:
        return False


print(square_cube(4, 8))
print(square_cube(16, 48))
print(square_cube(9, 27))
