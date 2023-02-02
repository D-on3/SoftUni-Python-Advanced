from abc import ABC, abstractmethod


class Horse(ABC):
    MAX_SPEED = None
    TYPE_VALUE = None

    @abstractmethod
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.is_taken = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 4:
            raise ValueError(f"Horse name {value} is less than 4 symbols!")
        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
       if value > self.MAX_SPEED:
           raise ValueError(f"Horse speed is too high!")
       self.__speed = value

    def train(self):
        self.__speed += self.TYPE_VALUE
        if self.__speed > self.MAX_SPEED:
            self.__speed = self.MAX_SPEED

    @property
    def horse_type(self):
        return self.__class__.__name__
