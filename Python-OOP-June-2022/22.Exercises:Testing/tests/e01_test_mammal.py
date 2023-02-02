from project.mammal import Mammal

import unittest


class MammalTest(unittest.TestCase):
    NAME = "TestName"
    TYPE = "TestType"
    SOUND = "TestSound"
    KINGDOM = "animals"

    def setUp(self) -> None:
        self.mammal = Mammal(self.NAME, self.TYPE, self.SOUND)

    def test__init__expect_to_create_an_instance(self):
        self.assertEqual(self.NAME, self.mammal.name)
        self.assertEqual(self.TYPE, self.mammal.type)
        self.assertEqual(self.SOUND, self.mammal.sound)
        self.assertEqual(self.KINGDOM, self.mammal._Mammal__kingdom)

    def test_make_sound__expect_correct_result(self):
        actual = self.mammal.make_sound()
        expected = f"{self.NAME} makes {self.SOUND}"
        self.assertEqual(expected, actual)

    def test_get_kingdom__expect_return_kingdom(self):
        actual = self.mammal.get_kingdom()
        expected = self.KINGDOM
        self.assertEqual(expected, actual)

    def test_info__expect_correct_info(self):
        actual = self.mammal.info()
        expected = f"{self.NAME} is of type {self.TYPE}"
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
