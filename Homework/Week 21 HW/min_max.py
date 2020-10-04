class Min_Max:
    def Min(self, num_list):
        i = 0
        smallest_num = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        for num in num_list:
            if num is num_list[i]:
                i += 1
            else:
                previuos_num = num_list[i-1]
                if num < previuos_num:
                    smallest_num = num
                else:
                    pass
        return smallest_num

    def Max(self, num_list):
        for num in num_list:
            pass


do = Min_Max()
print(do.Min(num_list=[1, 2, 4, 2, 5, 63535, 644]))
