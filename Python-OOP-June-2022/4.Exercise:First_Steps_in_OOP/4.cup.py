class Cup:

    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, quantity_added):
        self.quantity_added = quantity_added
        if (self.size - self.quantity) >= quantity_added:
            self.quantity += quantity_added
            return self.quantity

    def status(self):
        return self.size - self.quantity


cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())
