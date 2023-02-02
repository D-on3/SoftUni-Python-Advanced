from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAX_SPEED = 120
    TYPE_VALUE = 2

    def __init__(self, name, speed):
        super().__init__(name, speed)