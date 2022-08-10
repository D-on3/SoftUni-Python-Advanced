class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel: float, horse_power: int):
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION
        self.fuel = fuel
        self.horse_power = horse_power

    def drive(self,kilometers):
        for_the_travel = kilometers * self.fuel_consumption
        if for_the_travel <= self.fuel:
            self.fuel -= for_the_travel

        return self.fuel