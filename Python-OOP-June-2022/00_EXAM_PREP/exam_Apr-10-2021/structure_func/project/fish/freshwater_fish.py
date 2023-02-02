from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    SIZE_INCREASE = 3
    INITIAL_SIZE = 3
    HABITAT = 'FreshwaterAquarium'

    def __init__(self, name, species, price):
        super().__init__(name, species, self.INITIAL_SIZE, price)

    def eat(self):
        self.size += self.SIZE_INCREASE
