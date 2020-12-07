class NumberIterator:
    def __init__(self, start_num, end_num):
        self.start_num = int(start_num)
        self.end_num = int(end_num)
        self.current_num = self.start_num

    def __iter__(self):
        self.current_num = self.start_num
        self.next = self.start_num
        return self

    def __next__(self):
        self.current_num = self.next
        if self.current_num > self.end_num:
            self.current_num = self.start_num
        self.next += 1
        return self.current_num


c1v = NumberIterator(0, 3)
c1i = iter(c1v)
print(f'{next(c1v)}, {next(c1v)}, {next(c1v)}, {next(c1v)}, {next(c1v)}')
c2v = NumberIterator(5, 7)
c2i = iter(c2v)
print(f'{next(c2v)}, {next(c2v)}, {next(c2v)}, {next(c2v)}')
