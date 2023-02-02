class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        num_to_return = self.start
        if self.count == 0:
            raise StopIteration
        self.start += self.step
        self.count -= 1
        return num_to_return


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)
