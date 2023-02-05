from project.plantation import Plantation

import unittest


class PlantationTests(unittest.TestCase):
    SIZE = 5
    PLANTS = {'Ana': ['tulip'], 'Beti': ['tulip2']}
    WORKERS = ['Ana', 'Beti']

    def setUp(self) -> None:
        self.plantation = Plantation(self.SIZE)

    def test__init__expect_correct_result(self):
        self.assertEqual(self.SIZE, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test__init_when_size_is_negative__expect_error(self):
        size = -5
        with self.assertRaises(ValueError) as error:
            plant = Plantation(size)

        self.assertIsNotNone(error)
        self.assertEqual("Size must be positive number!", str(error.exception))

    def test_hire_worker_when_worker_not_in_workers__expect_extended_workers(self):
        worker = 'Ana'
        actual = self.plantation.hire_worker(worker)
        expected = f"{worker} successfully hired."
        self.assertEqual(['Ana'], self.plantation.workers)
        self.assertEqual(expected, actual)

    def test_hire_worker_when_worker_in_workers__expect_error(self):
        worker = 'Ana'
        self.plantation.hire_worker(worker)

        with self.assertRaises(ValueError) as error:
            self.plantation.hire_worker(worker)

        self.assertIsNotNone(error)
        self.assertEqual("Worker already hired!", str(error.exception))
        self.assertEqual(['Ana'], self.plantation.workers)

    def test__len__expect_correct_result(self):
        plantation = Plantation(self.SIZE)
        plantation.plants = self.PLANTS
        plantation.workers = self.WORKERS

        expected = 0
        for plants_planted in self.PLANTS.values():
            expected += len(plants_planted)

        actual = plantation.__len__()
        self.assertEqual(expected, actual)
        self.assertEqual(self.PLANTS, plantation.plants)

    def test_planting_when_worker_not_in_workers_expect_error(self):
        plantation = Plantation(self.SIZE)
        plantation.plants = self.PLANTS
        plantation.workers = self.WORKERS

        worker = 'Test'
        plant = 'flower'

        with self.assertRaises(ValueError) as error:
            plantation.planting(worker, plant)
        self.assertIsNotNone(error)
        self.assertEqual(f"Worker with name {worker} is not hired!", str(error.exception))
        self.assertEqual(self.PLANTS, plantation.plants)
        self.assertEqual(self.WORKERS, plantation.workers)

    def test_planting_when_plantation_is_full__expect_error(self):
        self.SIZE = 2
        plantation = Plantation(self.SIZE)
        plantation.plants = self.PLANTS
        plantation.workers = self.WORKERS

        worker = 'Ana'
        plant = 'flower'

        with self.assertRaises(ValueError) as error:
            plantation.planting(worker, plant)
        self.assertIsNotNone(error)
        self.assertEqual("The plantation is full!", str(error.exception))
        self.assertEqual(self.PLANTS, plantation.plants)
        self.assertEqual(self.WORKERS, plantation.workers)
        self.assertEqual(self.SIZE, plantation.size)

    def test_planting_when_worker_is_valid_and_free_space__expect_adding_plant_to_the_worker(self):
        self.SIZE = 30
        plantation = Plantation(self.SIZE)
        plantation.plants = self.PLANTS
        plantation.workers = self.WORKERS

        worker = 'Ana'
        plant = 'flower'

        actual = plantation.planting(worker, plant)
        expected = f"{worker} planted {plant}."
        self.assertEqual(expected, actual)
        self.assertEqual({'Ana': ['tulip', 'flower'], 'Beti': ['tulip2']}, plantation.plants)

    def test_planting_when_worker_not_in_plants_dict_and_free_space__expect_adding_worker_plant(self):
        self.SIZE = 30
        plantation2 = Plantation(self.SIZE)
        plantation2.plants = {'Ana': ['tulip'], 'Beti': ['tulip2']}
        plantation2.workers = ['Ana', 'Beti', 'Misho']

        worker = 'Misho'
        plant = 'flower'

        actual = plantation2.planting(worker, plant)
        expected = f"{worker} planted it's first {plant}."
        self.assertEqual(expected, actual)
        self.assertEqual({'Ana': ['tulip'], 'Beti': ['tulip2'], 'Misho': ['flower']}, plantation2.plants)

    def test__str__when_all_valid__expect_correct_result(self):
        plantation = Plantation(30)
        plantation.plants = {'Ana': ['tulip'], 'Beti': ['tulip2']}
        plantation.workers = ['Ana', 'Beti']

        expected = '''Plantation size: 30
Ana, Beti
Ana planted: tulip
Beti planted: tulip2'''

        actual = str(plantation)
        self.assertEqual(expected, actual)

    def test__str__when_no_workers__expect_correct_result(self):
        plantation = Plantation(30)
        plantation.plants = {'Ana': ['tulip'], 'Beti': ['tulip2']}
        plantation.workers = []

        expected = '''Plantation size: 30

Ana planted: tulip
Beti planted: tulip2'''
        actual = str(plantation)
        self.assertEqual(expected, actual)

    def test__str__when_no_plants__expect_correct_result(self):
        plantation = Plantation(30)
        plantation.plants = {}
        plantation.workers = ['Ana', 'Beti']

        expected = '''Plantation size: 30
Ana, Beti'''

        actual = str(plantation)
        self.assertEqual(expected, actual)

    def test__str__when_no_plants_and_workers__expect_correct_result(self):
        plantation = Plantation(30)
        plantation.plants = {}
        plantation.workers = []

        expected = 'Plantation size: 30\n'

        actual = str(plantation)
        self.assertEqual(expected, actual)

    def test__repr__when_no_workers__expect_result(self):
        plantation = Plantation(30)
        plantation.workers = []
        actual = repr(plantation)
        expected = '''Size: 30
Workers: '''
        self.assertEqual(expected, actual)

    def test__repr_when_workers__expect_result(self):
        plantation = Plantation(30)
        plantation.workers = ['Ana', 'Beti']
        actual = repr(plantation)
        expected = '''Size: 30
Workers: Ana, Beti'''
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
