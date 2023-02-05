from project.vehicle import Vehicle

import unittest


class VehicleTest(unittest.TestCase):
    FUEL = 50
    HORSE_POWER = 100
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def setUp(self) -> None:
        self.vehicle = Vehicle(self.FUEL, self.HORSE_POWER)

    def test__init__expect_to_create_instance(self):
        self.assertEqual(self.FUEL, self.vehicle.fuel)
        self.assertEqual(self.HORSE_POWER, self.vehicle.horse_power)
        self.assertEqual(self.FUEL, self.vehicle.capacity)
        self.assertEqual(self.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_drive__when_fuel_is_less_than_needed_fuel__expect_exception(self):
        distance = 50
        with self.assertRaises(Exception) as context:
            self.vehicle.drive(distance)

        self.assertIsNotNone(context)
        self.assertEqual("Not enough fuel", str(context.exception))

    def test_drive__when_fuel_is_enough__expect_fuel_to_decrease(self):
        distance = 10
        self.vehicle.drive(distance)
        expected_fuel = self.FUEL - (self.DEFAULT_FUEL_CONSUMPTION * distance)
        self.assertEqual(expected_fuel, self.vehicle.fuel)

    def test_refuel__when_total_fuel_not_within_capacity__expect_exception(self):
        fuel = 10
        with self.assertRaises(Exception) as context:
            self.vehicle.refuel(fuel)

        self.assertIsNotNone(context)
        self.assertEqual("Too much fuel", str(context.exception))

    def test_refuel__when_total_fuel_within_capacity__expect_fuel_to_increase(self):
        fuel = 10
        distance = 20
        self.vehicle.drive(distance) # fuel left 25
        self.vehicle.refuel(fuel) # 35
        expected = self.FUEL - (self.DEFAULT_FUEL_CONSUMPTION * distance) + fuel
        self.assertEqual(expected, self.vehicle.fuel)

    def test__str__expect_correct_result(self):
        actual = self.vehicle.__str__()
        expected = f"The vehicle has {self.HORSE_POWER} " \
               f"horse power with {self.FUEL} fuel left and {self.DEFAULT_FUEL_CONSUMPTION} fuel consumption"
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()