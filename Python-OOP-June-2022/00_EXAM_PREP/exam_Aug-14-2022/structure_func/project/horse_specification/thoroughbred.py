from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAX_SPEED = 140
    TYPE_VALUE = 3

    def __init__(self, name, speed):
        super().__init__(name, speed)