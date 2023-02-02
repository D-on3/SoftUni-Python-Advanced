# class reverse_iter:
#     def __init__(self, iterable):
#         self.iterable = list(iterable)
#
#     def __iter__(self):
#         return iter(self.iterable[::-1])


class reverse_iter:
    def __init__(self, iterable):
        self.iterable = list(iterable)
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < -len(self.iterable):
            raise StopIteration

        value_to_return = self.iterable[self.index]
        self.index -= 1
        return value_to_return


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)

# for item in reverse_iter({1, 2, 3, 4}):
#     print(item)
