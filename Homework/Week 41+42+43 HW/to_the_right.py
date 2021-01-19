class Main:
    def __init__(self, nums, i=0):
        self.nums = nums
        self.i = i

    def display(self):
        return self.nums

    def to_the_right(self):
        if self.i > len(self.nums):
            self.i = 0
            self.nums.append(self.nums[-1])
            self.nums.pop(-2)
        elif self.i == 0:
            ...
        elif self.i != 0:
            self.nums.insert(self.i, [self.nums[self.i]])
            self.nums.pop(self.i-1)
        self.i += 1
        return self


ttr = Main([1, 2, 3])

print(ttr.display())
ttr.to_the_right()
print(ttr.display())
ttr.to_the_right()
print(ttr.display())
ttr.to_the_right()
print(ttr.display())
