class Main:
    def __init__(self, nums, i=0):
        self.nums = nums
        self.i = i

    def display(self):
        j = self.i % len(self.nums)  # temp variable j
        modified = self.nums.copy()
        modified[j] = [self.nums[j]]
        # indexes[to_modify[index]] = replacements[index]
        return modified

    # this time using a string
    def display_string(self):
        j = self.i % len(self.nums)  # temp variable j
        for num in self.nums:
            if num == self.nums[j]:
                return ...

    def to_the_right(self):
        self.i += 1
        return self


main = Main([1, 5, 2, 7, 3, 8])
print('\n')
for _ in range(12):
    print(main.display())
    main.to_the_right()
