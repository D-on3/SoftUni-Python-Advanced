from project.hero import Hero

import unittest


class HeroTest(unittest.TestCase):
    USERNAME = 'testusername'
    LEVEL = 1
    HEALTH = 100
    DAMAGE = 10


    def setUp(self) -> None:
        self.hero = Hero(self.USERNAME, self.LEVEL, self.HEALTH, self.DAMAGE)
        self.enemy = Hero('enemytest', 1, 100, 10)

    def test__init__expect_to_create_instance(self):
        self.assertEqual(self.USERNAME, self.hero.username)
        self.assertEqual(self.LEVEL, self.hero.level)
        self.assertEqual(self.HEALTH, self.hero.health)
        self.assertEqual(self.DAMAGE, self.hero.damage)

    def test_battle__when_enemy_has_the_same_username_expect_exception(self):
        enemy_hero = Hero(self.USERNAME, 1, 10, 10)
        enemy_hero.username = self.USERNAME
        with self.assertRaises(Exception) as context:
            self.hero.battle(enemy_hero)

        self.assertIsNotNone(context)
        self.assertEqual("You cannot fight yourself", str(context.exception))

    def test_battle__when_health_is_negative_or_0__expect_exception(self):
        self.hero.health = 0

        with self.assertRaises(ValueError) as context:
            self.hero.battle(self.enemy)

        self.assertIsNotNone(context)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(context.exception))

    def test_battle__when_enemy_health_is_negative_or_0__expect_exception(self):
        enemy_hero = Hero('enemytest', 1, 0, 10)

        with self.assertRaises(ValueError) as context:
            self.hero.battle(enemy_hero)

        self.assertIsNotNone(context)
        self.assertEqual(f"You cannot fight {enemy_hero.username}. He needs to rest", str(context.exception))

    def test_battle__when_hero_and_enemy_both_health_is_negative_or_0__expect_return_Draw(self):
        self.hero.damage = 100
        self.enemy.damage = 100

        actual = self.hero.battle(self.enemy)
        expected_health = self.HEALTH - (self.enemy.level * self.enemy.damage)
        expected = 'Draw'
        self.assertEqual(expected, actual)
        self.assertEqual(expected_health, self.hero.health)
        self.assertEqual(expected_health, self.enemy.health)

    def test_battle__when_hero_wins_and_enemy_health_is_negative_or_0__expect_return_You_win(self):
        self.enemy.health = 10
        actual = self.hero.battle(self.enemy)
        expected = "You win"
        self.assertEqual(expected, actual)
        self.assertEqual(2, self.hero.level)
        self.assertEqual(95, self.hero.health)
        self.assertEqual(15, self.hero.damage)

    def test_battle__when_hero_lose__expect_return_You_lose(self):
        self.hero.health = 10
        actual = self.hero.battle(self.enemy)
        expected = "You lose"
        self.assertEqual(expected, actual)
        self.assertEqual(2, self.enemy.level)
        self.assertEqual(95, self.enemy.health)
        self.assertEqual(15, self.enemy.damage)

    def test__str__expect_correct_result(self):
        actual = self.hero.__str__()
        expected = f"Hero {self.USERNAME}: {self.LEVEL} lvl\n" \
                   f"Health: {self.HEALTH}\n" \
                   f"Damage: {self.DAMAGE}\n"
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
