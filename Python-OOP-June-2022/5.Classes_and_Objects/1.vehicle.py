# Create a class called Vehicle. Upon initialization, it should receive max_speed
# (integer, optional; 150 by default) and mileage (number).
# Create an instance variable called gadgets - an empty list by default.


class Vehicle:
    def __init__(self, mileage, max_speed=150):
        self.max_speed = max_speed
        self.mileage = mileage
        self.gadgets = []


car = Vehicle(20)
print(car.max_speed)
print(car.mileage)
print(car.gadgets)
car.gadgets.append('Hudly Wireless')
print(car.gadgets)
