from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if not self.aquarium_type_is_valid(aquarium_type):
            return "Invalid aquarium type."
        new_aquarium = self.create_aquarium(aquarium_type, aquarium_name)
        self.aquariums.append(new_aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if not self.decoration_is_valid(decoration_type):
            return "Invalid decoration type."

        new_decoration = self.create_decoration(decoration_type)
        self.decorations_repository.add(new_decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        decoration = self.__find_decoration_by_type(decoration_type)
        if not decoration:
            return f"There isn't a decoration of type {decoration_type}."

        aquarium = self.__find_aquarium_by_name(aquarium_name)
        if aquarium:
            aquarium.add_decoration(decoration)
            self.decorations_repository.remove(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if not self.fish_is_valid(fish_type):
            return f"There isn't a fish of type {fish_type}."
        fish = self.create_fish(fish_type, fish_name, fish_species, price)
        aquarium = self.__find_aquarium_by_name(aquarium_name)
        if fish.habitat != aquarium.aquarium_type:
            return "Water not suitable."
        return aquarium.add_fish(fish)

    def feed_fish(self, aquarium_name: str):
        aquarium = self.__find_aquarium_by_name(aquarium_name)
        if aquarium:
            aquarium.feed()
            return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = self.__find_aquarium_by_name(aquarium_name)
        if aquarium:
            value = aquarium.aquarium_value
            return f"The value of Aquarium {aquarium_name} is {value}."

    def report(self):
        result = '\n'.join([str(aquarium) for aquarium in self.aquariums])
        return result

    @staticmethod
    def aquarium_type_is_valid(aquarium_type):
        return aquarium_type in ("FreshwaterAquarium", "SaltwaterAquarium")

    @staticmethod
    def create_aquarium(type_fish, name):
        if type_fish == "FreshwaterAquarium":
            return FreshwaterAquarium(name)
        else:
            return SaltwaterAquarium(name)

    @staticmethod
    def decoration_is_valid(type_decoration):
        return type_decoration in ("Ornament", "Plant")

    @staticmethod
    def create_decoration(decoration_type):
        if decoration_type == "Ornament":
            return Ornament()
        else:
            return Plant()

    def __find_decoration_by_type(self, decoration_type):
        for decoration in self.decorations_repository.decorations:
            if decoration.decoration_type == decoration_type:
                return decoration

    def __find_aquarium_by_name(self, name):
        for a in self.aquariums:
            if a.name == name:
                return a

    @staticmethod
    def fish_is_valid(fish_type):
        return fish_type in ("FreshwaterFish", "SaltwaterFish")

    @staticmethod
    def create_fish(fish_type, fish_name, fish_species, price):
        if fish_type == "FreshwaterFish":
            return FreshwaterFish(fish_name, fish_species, price)
        else:
            return SaltwaterFish(fish_name, fish_species, price)
