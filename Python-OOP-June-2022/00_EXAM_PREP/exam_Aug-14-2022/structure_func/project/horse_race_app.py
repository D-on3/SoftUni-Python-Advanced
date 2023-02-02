from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    def __init__(self):
        self.horses = []  # obj
        self.jockeys = []  # obj
        self.horse_races = []  # obj

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type in ("Appaloosa", "Thoroughbred"):
            if self.__find_horse_by_name(horse_name):
                raise Exception(f"Horse {horse_name} has been already added!")
            new_horse = self.create_horse(horse_type, horse_name, horse_speed)
            self.horses.append(new_horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if self.__find_jockey_by_name(jockey_name):
            raise Exception(f"Jockey {jockey_name} has been already added!")
        new_jockey = self.create_jockey(jockey_name, age)
        self.jockeys.append(new_jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if any(horse_race.race_type == race_type for horse_race in self.horse_races):
            raise Exception(f"Race {race_type} has been already created!")
        new_race = HorseRace(race_type)
        self.horse_races.append(new_race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.__find_jockey_by_name(jockey_name)
        horse = self.__find_free_horse_by_type(horse_type)

        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if horse is None:
            raise Exception(f"Horse breed {horse_type} could not be found!")
        if jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."

        horse.is_taken = True
        jockey.horse = horse
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        jockey = self.__find_jockey_by_name(jockey_name)
        race = self.__find_race_by_type(race_type)

        if not race:
            raise Exception(f"Race {race_type} could not be found!")
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
        if any(jockey.name == jockey_name for jockey in race.jockeys):
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        horse_race = self.__find_race_by_type(race_type)
        if not horse_race:
            raise Exception(f"Race {race_type} could not be found!")
        if len(horse_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner = sorted(self.jockeys, key=lambda x: -x.horse.speed)[0]
        return f"The winner of the {race_type} race, with a speed of {winner.horse.speed}km/h is {winner.name}! Winner's horse: {winner.horse.name}."

    @staticmethod
    def create_horse(horse_type: str, horse_name: str, horse_speed: int):
        if horse_type == "Appaloosa":
            return Appaloosa(horse_name, horse_speed)
        elif horse_type == "Thoroughbred":
            return Thoroughbred(horse_name, horse_speed)

    @staticmethod
    def create_jockey(jockey_name, age):
        return Jockey(jockey_name, age)

    def __find_horse_by_name(self, name):
        for horse in self.horses:
            if horse.name == name:
                return horse

    def __find_jockey_by_name(self, name):
        for jockey in self.jockeys:
            if jockey.name == name:
                return jockey

    def __find_free_horse_by_type(self, horse_type):
        for horse in self.horses[::-1]:
            if horse.horse_type == horse_type and not horse.is_taken:
                return horse

    def __find_race_by_type(self, race_type):
        for race in self.horse_races:
            if race.race_type == race_type:
                return race
