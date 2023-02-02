from project.decoration.base_decoration import BaseDecoration


class Ornament(BaseDecoration):

    COMFORT = 1
    PRICE = 5

    def __init__(self):
        super().__init__(self.COMFORT, self.PRICE)

# o = Ornament()
# print(o.price, o.comfort)
# print(o.decoration_type)
