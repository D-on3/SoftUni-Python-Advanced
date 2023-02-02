from project.astronaut.astronaut import Astronaut

class Biologist(Astronaut):
    DEFAULT_BREATH_UNITS = 5
    INITIAL_OXYGEN = 70

    def __init__(self, name):
        super().__init__(name, self.INITIAL_OXYGEN)