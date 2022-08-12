class Shop:

    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}

    @classmethod
    def small_shop(cls, name, type):
        return cls(name, type, 10)

    def add_items(self, items_name):
        if self.capacity > sum(self.items.values()):
            if items_name not in self.items:
                self.items[items_name] = 0
            self.items[items_name] += 1
