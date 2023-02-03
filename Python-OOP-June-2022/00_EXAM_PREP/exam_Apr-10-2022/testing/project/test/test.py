from project.movie import Movie

import unittest


class MovieTests(unittest.TestCase):
    NAME = 'Test Movie'
    YEAR = 2022
    RATING = 7

    def setUp(self) -> None:
        self.movie = Movie(self.NAME, self.YEAR, self.RATING)

    def test_init(self):
        self.assertEqual(self.NAME, self.movie.name)
        self.assertEqual(self.YEAR, self.movie.year)
        self.assertEqual(self.RATING, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_name_setter__when_empty_str__expect_error(self):
        with self.assertRaises(ValueError) as error:
            self.movie.name = ''
        self.assertIsNotNone(error)
        self.assertEqual("Name cannot be an empty string!", str(error.exception))

    def test_year_setter__when_year_less_than_1887__expect_error(self):
        with self.assertRaises(ValueError) as error:
            self.movie.year = 1800
        self.assertIsNotNone(error)
        self.assertEqual("Year is not valid!", str(error.exception))

    def test_add_actor__when_actor_not_in_actors_list__expect_append_to_the_list(self):
        first = 'Ana'
        second = 'Svilen'
        self.movie.add_actor(first)
        self.movie.add_actor(second)
        self.assertEqual([first, second], self.movie.actors)

    def test_add_actor__when_actor_in_actors_list__expect_error_message(self):
        self.movie.add_actor('Ana')
        first = 'Ana'
        expected = f"{first} is already added in the list of actors!"
        actual = self.movie.add_actor(first)
        self.assertEqual(expected, actual)
        self.assertEqual(['Ana'], self.movie.actors)

    def test__gt__compare_movies__expect_message(self):
        other = Movie('Other Test', 1997, 6)

        first_result = self.movie > other  # True - f'"{self.movie.name}" is better than "{other.name}"'
        second_result = other > self.movie  # False - f'"{self.movie.name}" is better than "{other.name}"'

        expected = f'"{self.movie.name}" is better than "{other.name}"'

        self.assertEqual(expected, first_result)
        self.assertEqual(expected, second_result)

    def test__repr__(self):
        actors = ['Ana', 'Svilen']
        self.movie.add_actor('Ana')
        self.movie.add_actor('Svilen')
        actual = repr(self.movie)
        expected = f"Name: {self.NAME}\n" \
                   f"Year of Release: {self.YEAR}\n" \
                   f"Rating: {self.RATING:.2f}\n" \
                   f"Cast: {', '.join(actors)}"
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
