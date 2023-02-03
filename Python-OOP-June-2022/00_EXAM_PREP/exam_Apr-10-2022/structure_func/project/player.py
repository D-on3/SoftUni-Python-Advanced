class Player:
    DEFAULT_STAMINA = 100
    STAMINA_MAX = 100
    STAMINA_MIN = 0
    PLAYERS_INFO = set()

    def __init__(self, name,age, stamina=100):
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name not valid!")
        if value in self.PLAYERS_INFO:
            raise Exception(f"Name {value} is already used!")
        self.__name = value
        self.PLAYERS_INFO.add(value)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if value < self.STAMINA_MIN or value > self.STAMINA_MAX:
            raise ValueError("Stamina not valid!")
        self.__stamina = value

    @property
    def need_sustenance(self):
        return self.stamina < self.STAMINA_MAX

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"