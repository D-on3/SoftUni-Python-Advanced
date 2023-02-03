from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    SIZE_INCREASE = 2
    INITIAL_SIZE = 5
    HABITAT = 'SaltwaterAquarium'

    def __init__(self, name, species, price):
        super().__init__(name, species, self.INITIAL_SIZE, price)

    def eat(self):
        self.size += self.SIZE_INCREASE
