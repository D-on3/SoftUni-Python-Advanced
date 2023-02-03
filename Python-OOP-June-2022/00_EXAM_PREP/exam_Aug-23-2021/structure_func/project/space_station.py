from collections import deque

from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository



class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.successful_missions = 0
        self.not_completed_missions = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        if astronaut_type not in ("Biologist", "Geodesist", "Meteorologist"):
            raise Exception("Astronaut type is not valid!")
        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."
        new_astronaut = self.create_astronaut(astronaut_type, name)
        self.astronaut_repository.add(new_astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."

        new_planet = Planet(name)
        new_planet.items = items.split(', ')
        self.planet_repository.add(new_planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)
        if astronaut is None:
            raise Exception(f"Astronaut {name} doesn't exist!")
        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)

        if planet is None:
            raise Exception("Invalid planet name!")
        sorted_astronauts = deque(
            [astronaut for astronaut in list(filter(lambda x: x.oxygen > 30,
                                                    sorted(self.astronaut_repository.astronauts,
                                                           key=lambda x: -x.oxygen)))[:5]])
        if not sorted_astronauts:
            raise Exception("You need at least one astronaut to explore the planet!")

        landed_astronauts = set()
        while sorted_astronauts and planet.items:
            astronaut = sorted_astronauts.popleft()

            while astronaut.oxygen > 0 and planet.items:
                landed_astronauts.add(astronaut)
                current_item = planet.items.pop()
                astronaut.backpack.append(current_item)
                astronaut.breathe()

        if not planet.items and landed_astronauts:
            self.successful_missions += 1
            return f"Planet: {planet.name} was explored. {len(landed_astronauts)} astronauts participated in collecting items."
        self.not_completed_missions += 1
        return "Mission is not completed."

    def report(self):

        result = f"{self.successful_missions} successful missions!\n\
{self.not_completed_missions} missions were not completed!\n\
Astronauts' info:"
        for astronaut in self.astronaut_repository.astronauts:
            result += astronaut.get_info
        return result.strip()

    @staticmethod
    def create_astronaut(astronaut_type, name):
        if astronaut_type == 'Biologist':
            return Biologist(name)
        elif astronaut_type == "Geodesist":
            return Geodesist(name)
        elif astronaut_type == "Meteorologist":
            return Meteorologist(name)
