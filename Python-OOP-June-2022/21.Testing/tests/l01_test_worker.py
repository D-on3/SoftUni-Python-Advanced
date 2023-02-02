from lab.l01_worker import Worker

import unittest


class WorkerTest(unittest.TestCase):
    NAME = 'Test Name'
    SALARY = 1000
    ENERGY = 5

    def setUp(self) -> None:
        self.worker = Worker(self.NAME, self.SALARY, self.ENERGY)

    def test_worker_init__when_valid_props_expect_to_be_correct_initialized(self):
        self.assertEqual(self.NAME, self.worker.name)
        self.assertEqual(self.SALARY, self.worker.salary)
        self.assertEqual(self.ENERGY, self.worker.energy)
        # self.assertEqual(0, self.worker.money)

    def test_worker_rest__expect_energy_to_be_incremented(self):
        self.worker.rest()
        self.assertEqual(self.ENERGY + 1, self.worker.energy)

    def test_work__when_energy_is_zero__expect_exception(self):
        worker = Worker(self.NAME, self.SALARY, 0)

        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertIsNotNone(ex)
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_work__when_energy_is_greater_that_0__expect_money_to_be_increased_by_salary(self):
        self.worker.work()
        self.worker.work()
        self.assertEqual(self.SALARY * 2, self.worker.money)

    def test_work__when_energy_is_greater_that_0__expect_energy_to_be_decreased_by_1(self):
        self.worker.work()
        self.assertEqual(self.ENERGY - 1, self.worker.energy)

    def test_worker_get_info__expect_correct_result(self):
        actual_info = self.worker.get_info()
        expected_info = f'{self.NAME} has saved {0} money.'
        self.assertEqual(expected_info, actual_info)


if __name__ == '__main__':
    unittest.main()
