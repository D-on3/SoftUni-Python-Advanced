class dictionary_iter:
    def __init__(self, dict_values):
        self.dict_values = list(dict_values.items())
        self.index = 0


    # def __iter__(self):
    #     return ((key, value) for key, value in self.dict_values.items())

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.dict_values):
            raise StopIteration
        item = self.dict_values[self.index]
        self.index += 1
        return item




result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
