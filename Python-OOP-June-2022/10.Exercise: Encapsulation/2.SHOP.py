class Shop:

    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}

    @classmethod
    def small_show(cls, name, type):
        return cls(name, type, 10)

    def add_item(self, item_name):
        if self.capacity > sum(self.items.values()):
            if item_name not in self.items:
                self.items[item_name] += 1
                return f"{item_name} added to the shop"
            return "Not enough capacity in the shop"

    def remove_item(self, item_name, amount):
        if item_name in self.items and self.items[item_name] >= amount:
            self.items[item_name] -= amount
            if self.items[item_name] == 0:
                del self.items[item_name]
            return f"{amount} {item_name} remove from the shop"
        return f"Cannot remove {amount} {item_name}"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"
