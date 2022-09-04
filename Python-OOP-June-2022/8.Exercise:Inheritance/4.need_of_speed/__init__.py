from project.family_car import FamilyCar
from project.vehicle import Vehicle
from project.car import Car
from project.cross_motorcycle import CrossMotorcycle
from project.family_car import FamilyCar
from project.motorcycle import Motorcycle
from project.sport_car import SportsCar
from project.race_motorcycle import RaceMotorcycle



vehicle = Vehicle(50, 150)
print(Vehicle.DEFAULT_FUEL_CONSUMPTION)
print(FamilyCar.DEFAULT_FUEL_CONSUMPTION)
print(vehicle.fuel)
print(vehicle.horse_power)
print(vehicle.fuel_consumption)
vehicle.drive(100)
print(vehicle.fuel)
family_car = FamilyCar(150, 150)
family_car.drive(50)
print(family_car.fuel)
family_car.drive(50)
print(family_car.fuel)
print(family_car.__class__.__bases__[0].__name__)

