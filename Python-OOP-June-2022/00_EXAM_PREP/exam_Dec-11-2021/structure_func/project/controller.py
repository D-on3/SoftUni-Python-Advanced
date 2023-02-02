from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []  # all cars obj
        self.drivers = []  # all drivers obj
        self.races = []  # all races obj

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type in ('MuscleCar', 'SportsCar'):
            car = self.__find_car_by_model(model, self.cars)
            if car:
                raise Exception(f"Car {model} is already created!")

            if car_type == 'MuscleCar':
                new_car = MuscleCar(model, speed_limit)
            else:
                new_car = SportsCar(model, speed_limit)
            self.cars.append(new_car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        driver = self.__find_obj_by_name(driver_name, self.drivers)
        if driver:
            raise Exception(f"Driver {driver_name} is already created!")
        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        race = self.__find_obj_by_name(race_name, self.races)
        if race:
            raise Exception(f"Race {race_name} is already created!")
        new_race = Race(race_name)
        self.races.append(new_race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.__find_obj_by_name(driver_name, self.drivers)
        new_car = self.__find_car_by_car_type(car_type)

        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")
        if new_car is None:
            raise Exception(f"Car {car_type} could not be found!")
        old_car = driver.car
        driver.car = new_car
        new_car.is_taken = True
        if old_car:
            old_car.is_taken = False
            return f"Driver {driver_name} changed his car from {old_car.model} to {new_car.model}."
        return f"Driver {driver_name} chose the car {new_car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        driver = self.__find_obj_by_name(driver_name, self.drivers)
        race = self.__find_obj_by_name(race_name, self.races)

        if race is None:
            raise Exception(f"Race {race_name} could not be found!")
        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")
        if driver.car is None:
            raise Exception(f"Driver {driver.name} could not participate in the race!")

        race_driver = self.__find_obj_by_name(driver_name, race.drivers)
        if race_driver:
            return f"Driver {driver_name} is already added in {race.name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = self.__find_obj_by_name(race_name, self.races)

        if race is None:
            raise Exception(f"Race {race_name} could not be found!")
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")
        sorted_participants = sorted(race.drivers, key=lambda x: -x.car.speed_limit)
        result = ''
        for winner in sorted_participants[:3]:
            winner.number_of_wins += 1
            result += f"Driver {winner.name} wins the {race_name} race with a speed of {winner.car.speed_limit}.\n"

        return result.strip()

    @staticmethod
    def __find_car_by_model(model, car_list):
        for car in car_list:
            if car.model == model:
                return car
        return None

    @staticmethod
    def __find_obj_by_name(name, obj_list):
        for obj in obj_list:
            if obj.name == name:
                return obj
        return None

    def __find_car_by_car_type(self, car_type):
        for car in self.cars[::-1]:
            if car.car_type == car_type and not car.is_taken:
                return car
        return None
