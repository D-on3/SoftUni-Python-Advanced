class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.index = 0

    # def __iter__(self):
    #     return (n for n in range(self.count, -1, -1))
    def __iter__(self):
        return self

    def __next__(self):
        num_to_return = self.count
        if self.count < 0:
            raise StopIteration
        self.count -= 1
        return num_to_return


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")

iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")
