class Stack():

    def __init__(self, data: list):
        self.data = data

    def push(self, element):
        self.data.append(element)

    def pop(self):
        self.data.pop()
        return self.data.pop

    def top(self):
        # self.data[-1]
        return self.data[-1]


    def is_empty(self):
        if len(self.data) == 0:
            return False
        return True

    def __str__(self):
        self.to_repr = ""
        for el in reversed(self.data):
            self.to_repr += f"{el}, "

        return self.to_repr
