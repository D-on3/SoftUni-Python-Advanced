from cat import Cat


class Kitten(Cat):
    _GENDER = 'Female'

    def __init__(self, name, age):
        super().__init__(name, age, self._GENDER)

    def make_sound(self):
        return "Meow"
