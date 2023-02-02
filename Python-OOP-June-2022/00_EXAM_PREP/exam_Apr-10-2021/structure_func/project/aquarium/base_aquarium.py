from abc import ABC, abstractmethod

from project.decoration.base_decoration import BaseDecoration
from project.fish.base_fish import BaseFish


class BaseAquarium(ABC):

    INITIAL_CAPACITY = 0

    @abstractmethod
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    def calculate_comfort(self):
        return sum(decoration.comfort for decoration in self.decorations)

    def add_fish(self, fish: BaseFish):
        if fish.fish_type in ('FreshwaterFish', 'SaltwaterFish'):
            if len(self.fish) >= self.capacity:
                return 'Not enough capacity.'
            self.fish.append(fish)
            return f'Successfully added {fish.fish_type} to {self.name}.'

    def remove_fish(self, fish: BaseFish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration: BaseDecoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        fishes = ' '.join([fish.name for fish in self.fish]) if self.fish else 'none'

        result = f'''{self.name}:
Fish: {fishes}
Decorations: {len(self.decorations)}
Comfort: {self.calculate_comfort()}'''

        return result

    @property
    def aquarium_type(self):
        return self.__class__.__name__

    @property
    def aquarium_value(self):
        result = sum(decoration.price for decoration in self.decorations)
        result += sum(fish.price for fish in self.fish)

        return f'{result:.2f}'

