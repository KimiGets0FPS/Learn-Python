encodings_int = [2, 10, 16, 64]
encodings_str = [16, 64]
print(int("10", 2))
I = input
one = I()
two = I()
# one_stuff = []
if one.isdigit():
    one_stuff = [int(one, i) for i in encodings_int]
else:
    one_stuff = [int(one, i) for i in encodings_str]
print(one_stuff)
