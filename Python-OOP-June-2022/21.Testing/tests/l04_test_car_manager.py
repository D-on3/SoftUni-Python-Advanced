from lab.l04_car_manager import Car

import unittest


class CarTests(unittest.TestCase):
    MAKE = 'Peugeot'
    MODEL = '306'
    FUEL_CONSUMPTION = 5
    FUEL_CAPACITY = 50

    def setUp(self) -> None:
        self.car = Car(self.MAKE, self.MODEL, self.FUEL_CONSUMPTION, self.FUEL_CAPACITY)

    # test car props
    def test_car_make_setter__when_empty_str__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.car.make = None
        self.assertIsNotNone(context)
        self.assertEqual('Make cannot be null or empty!', str(context.exception))

    def test_car_model_setter__when_empty_str__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.car.model = None
        self.assertIsNotNone(context)
        self.assertEqual('Model cannot be null or empty!', str(context.exception))

    def test_car_fuel_consumption__when_less_or_equal_to_0__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_consumption = 0
        self.assertIsNotNone(context)
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(context.exception))

    def test_car_fuel_capacity__when_less_or_equal_to_0__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_capacity = 0
        self.assertIsNotNone(context)
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(context.exception))

    def test_car_fuel_amount__when_less_than_0__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_amount = -3
        self.assertIsNotNone(context)
        self.assertEqual("Fuel amount cannot be negative!", str(context.exception))

    # test refuel method
    def test_refuel_when_fuel_is_less_or_equal_to_0__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.car.refuel(0)
        self.assertIsNotNone(context)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(context.exception))

    def test_refuel_when_fuel_greater_than_0_and_total_amount_within_capacity__expect_fuel_amount_to_increase(self):
        self.car.refuel(20)
        self.assertEqual(20, self.car.fuel_amount)

    def test_refuel_when_fuel_greater_than_0_and_total_amount_over_capacity__expect_fuel_amount_to_be_equal_to_capacity(
            self):
        self.car.refuel(120)
        self.assertEqual(self.car.fuel_capacity, self.car.fuel_amount)

    # test drive method

    def test_car_drive__if_needed_fuel_greater_than_total_fuel__expect_exception(self):
        distance = 800
        self.car.refuel(5)
        with self.assertRaises(Exception) as context:
            self.car.drive(distance)

        self.assertIsNotNone(context)
        self.assertEqual("You don't have enough fuel to drive!", str(context.exception))

    def test_car_drive__if_needed_fuel_less_or_equal_to_total_fuel__expect_correct_result(self):
        distance = 500
        self.car.refuel(30)
        self.car.drive(distance)
        self.assertEqual(5, self.car.fuel_amount)


if __name__ == '__main__':
    unittest.main()
