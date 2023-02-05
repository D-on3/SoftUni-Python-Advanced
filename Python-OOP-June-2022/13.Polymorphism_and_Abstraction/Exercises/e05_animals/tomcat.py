from cat import Cat


class Tomcat(Cat):
    _GENDER = 'Male'

    def __init__(self, name, age):
        super().__init__(name, age, self._GENDER)

    def make_sound(self):
        return "Hiss"