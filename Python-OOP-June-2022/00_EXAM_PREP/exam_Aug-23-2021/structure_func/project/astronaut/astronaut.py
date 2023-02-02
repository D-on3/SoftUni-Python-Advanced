from abc import ABC, abstractmethod


class Astronaut(ABC):
    DEFAULT_BREATH_UNITS = 10
    INITIAL_OXYGEN = 0

    @abstractmethod
    def __init__(self, name, oxygen):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    def breathe(self):
        self.oxygen -= self.DEFAULT_BREATH_UNITS

    def increase_oxygen(self, amount):
        self.oxygen += amount

    @property
    def get_info(self):
        bag_items = 'none'
        if self.backpack:
            bag_items = ', '.join(self.backpack)

        result = f'\nName: {self.name}' \
                 f'\nOxygen: {self.oxygen}' \
                 f'\nBackpack items: {bag_items}'

        return result


