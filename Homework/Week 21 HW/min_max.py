import math


class Min_Max:
    def min(self, num_list):
        i = 0
        smallest_num = math.inf
        for num in num_list:
            if num is num_list[i]:
                i += 1
            else:
                previous_num = num_list[i-1]
                if num < previous_num:
                    smallest_num = num
                else:
                    pass
        return smallest_num

    def max(self, num_list):
        for num in num_list:
            pass


do = Min_Max()
print(do.min(num_list=[1, 2, 4, 2, 5, 63535, 644]))
print(do.max(num_list=[1, 2, 4, 2, 5, 63535, 644]))
