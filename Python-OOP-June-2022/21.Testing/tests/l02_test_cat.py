from lab.l02_cat import Cat

import unittest


class CatTests(unittest.TestCase):
    NAME = 'Tom'

    def setUp(self) -> None:
        self.cat = Cat(self.NAME)

    def test_eat__expect_size_to_be_increased(self):  # Cat's size is increased after eating
        self.cat.eat()
        self.assertEqual(1, self.cat.size)

    def test_eat__expect_fed_to_be_True(self):  # Cat is fed after eating
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_eat__when_fed_is_True__expect_exception(self):  # Cat cannot eat if already fed, raises an error
        self.cat.eat()

        with self.assertRaises(Exception) as ex_context:
            self.cat.eat()

        self.assertIsNotNone(ex_context)
        self.assertEqual('Already fed.', str(ex_context.exception))

    def test_sleep__when_not_fed__except_exception(self):  # Cat cannot fall asleep if not fed, raises an error

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertIsNotNone(ex)
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_sleep__expect_sleepy_to_be_False(self):  # Cat is not sleepy after sleeping
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    unittest.main()
