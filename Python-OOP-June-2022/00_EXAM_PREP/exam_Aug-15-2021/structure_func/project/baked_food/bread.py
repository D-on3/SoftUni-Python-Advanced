from project.baked_food.baked_food import BakedFood


class Bread(BakedFood):
    DEFAULT_PORTION = 200

    def __init__(self, name, price):
        super().__init__(name, self.DEFAULT_PORTION, price)
