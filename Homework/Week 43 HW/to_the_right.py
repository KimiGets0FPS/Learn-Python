class Main:
    def __init__(self, nums, i=0):
        self.nums = nums
        self.i = i

    def display(self):
        return self.nums

    def to_the_right(self):
        if self.i == 0 or self.i >= len(self.nums):
            # resetting the value of i
            if self.i > len(self.nums):
                self.i = 0
                self.nums.pop(-1)
            self.nums.insert(1, [self.nums[0]])
            self.nums.pop(0)
            # modifying the previous number
            self.nums.insert(-1, len(self.nums))
            self.nums.pop(-1)

        # for all of the other i values
        elif self.i != 0 and self.i < len(self.nums):
            self.nums.insert(self.i, [self.i+1])
            self.nums.pop(self.i+1)
            # modifying the previous number
            self.nums.insert(self.i-1, self.i)
            self.nums.pop(self.i)
        self.i += 1
        return self


ttr = Main([1, 2, 3])

# [1, 2, 3]
print(ttr.display())
# [[1], 2, 3]
ttr.to_the_right()
print(ttr.display())
# [1, [2], 3]
ttr.to_the_right()
print(ttr.display())
# [1, 2, [3]]
ttr.to_the_right()
print(ttr.display())
# [[1], 2, 3]
ttr.to_the_right()
print(ttr.display())
