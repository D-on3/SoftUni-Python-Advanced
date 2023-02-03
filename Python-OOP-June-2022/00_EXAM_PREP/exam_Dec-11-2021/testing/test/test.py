from project.team import Team

import unittest


class TeamTests(unittest.TestCase):
    TEAM_MEMBERS = {'Ana': 15, 'Beti': 20, 'Misho': 8}
    OTHER_MEMBERS = {'Pesho': 17, 'Gosho': 22, 'Sasho': 18, 'Maria': 21}

    def setUp(self) -> None:
        self.team = Team('red')
        self.other = Team('blue')

    def test__init__when_name_is_invalid__expect_error(self):
        error_message = "Team Name can contain only letters!"
        wrong_name = 'abc1'

        with self.assertRaises(ValueError) as error:
            team = Team(wrong_name)
        self.assertIsNotNone(error)
        self.assertEqual(error_message, str(error.exception))

    def test__init__when_name_is_valid__expect_new_instance(self):
        name = 'pink'
        team = Team('pink')
        self.assertEqual(name, team.name)
        self.assertEqual({}, team.members)

    def test__init__when_name_is_valid_and_members__expect_new_instance(self):
        name = 'pinko'
        team = Team(name)
        members = {'Ana': 1}
        team.members = members
        self.assertEqual(name, team.name)
        self.assertEqual(members, team.members)

    def test_add_member__expect_correct_result(self):
        actual = self.team.add_member(**self.TEAM_MEMBERS)
        expected = f"Successfully added: Ana, Beti, Misho"

        actual_dupl = self.team.add_member(**{'Ana': 10})
        expected_dupl = f"Successfully added: "

        self.other.add_member(**self.OTHER_MEMBERS)
        other_dupl = self.other.add_member(**{'Pesho': 9, 'Petko': 10})
        other_expected_dupl = f"Successfully added: Petko"

        self.assertEqual(expected, actual)
        self.assertEqual(expected_dupl, actual_dupl)
        self.assertEqual(self.TEAM_MEMBERS, self.team.members)
        self.assertEqual(other_expected_dupl, other_dupl)
        self.assertEqual({'Pesho': 17, 'Gosho': 22, 'Sasho': 18, 'Maria': 21, 'Petko': 10}, self.other.members)

    def test_remove_member_when_name_not_in_members__expect_message(self):
        name = 'Ilina'
        error_message = f"Member with name {name} does not exist"
        self.team.add_member(**self.TEAM_MEMBERS)
        actual = self.team.remove_member(name)

        self.assertEqual(error_message, actual)
        self.assertEqual(self.TEAM_MEMBERS, self.team.members)

    def test_remove_member_when_name_in_members__expect_remove_name(self):
        name = 'Misho'
        message = f"Member {name} removed"
        self.team.add_member(**self.TEAM_MEMBERS)
        actual = self.team.remove_member(name)

        self.assertEqual(message, actual)
        self.assertEqual({'Ana': 15, 'Beti': 20}, self.team.members)

    def test__gt__expect_bool(self):
        self.team.add_member(**self.TEAM_MEMBERS)
        self.other.add_member(**self.OTHER_MEMBERS)
        first = len(self.team) > len(self.other)
        second = len(self.other) > len(self.team)
        expected = self.team > self.other
        expected2 = self.other > self.team
        self.assertEqual(expected, first)
        self.assertEqual(expected2, second)

    def test__len__(self):
        expected = len(self.TEAM_MEMBERS)
        self.team.add_member(**self.TEAM_MEMBERS)
        actual = len(self.team.members)

        self.assertEqual(expected, actual)

    def test__add__when_team_has_not_members__expect_correct_result(self):
        self.team.add_member(**{})
        self.other.add_member(**self.OTHER_MEMBERS)

        actual = self.team + self.other
        new_team_name_expected = f"{self.team.name}{self.other.name}"
        new_team_expected = Team(new_team_name_expected)
        new_team_expected.add_member(**self.team.members)
        new_team_expected.add_member(**self.other.members)

        new_team_result = f'''Team name: {new_team_name_expected}
Member: Gosho - 22-years old
Member: Maria - 21-years old
Member: Sasho - 18-years old
Member: Pesho - 17-years old'''

        self.assertEqual(new_team_result, actual.__str__())
        self.assertEqual(new_team_name_expected, actual.name)
        self.assertEqual(new_team_expected.members, actual.members)

    def test__add__when_other_team_has_not_members__expect_correct_result(self):
        self.team.add_member(**self.TEAM_MEMBERS)
        self.other.add_member(**{})

        actual = self.team + self.other
        new_team_name_expected = f"{self.team.name}{self.other.name}"
        new_team_expected = Team(new_team_name_expected)
        new_team_expected.add_member(**self.team.members)
        new_team_expected.add_member(**self.other.members)

        new_team_result = f'''Team name: {new_team_name_expected}
Member: Beti - 20-years old
Member: Ana - 15-years old
Member: Misho - 8-years old'''

        self.assertEqual(new_team_result, actual.__str__())
        self.assertEqual(new_team_name_expected, actual.name)
        self.assertEqual(new_team_expected.members, actual.members)

    def test__add__when_teams_have_members__expect_correct_result(self):
        self.team.add_member(**self.TEAM_MEMBERS)
        self.other.add_member(**self.OTHER_MEMBERS)

        actual = self.team + self.other
        new_team_name_expected = f"{self.team.name}{self.other.name}"
        new_team_expected = Team(new_team_name_expected)
        new_team_expected.add_member(**self.team.members)
        new_team_expected.add_member(**self.other.members)

        new_team_result = f'''Team name: {new_team_name_expected}
Member: Gosho - 22-years old
Member: Maria - 21-years old
Member: Beti - 20-years old
Member: Sasho - 18-years old
Member: Pesho - 17-years old
Member: Ana - 15-years old
Member: Misho - 8-years old'''

        self.assertEqual(new_team_result, actual.__str__())
        self.assertEqual(new_team_name_expected, actual.name)
        self.assertEqual(new_team_expected.members, actual.members)

    def test__str__with_without_members__expect_correct_result(self):
        actual = str(self.team)
        self.other.add_member(**self.OTHER_MEMBERS)
        actual_with_members = str(self.other)

        expected = 'Team name: red'
        expected_with_members = '''Team name: blue
Member: Gosho - 22-years old
Member: Maria - 21-years old
Member: Sasho - 18-years old
Member: Pesho - 17-years old'''

        self.assertEqual(actual, expected)
        self.assertEqual(actual_with_members, expected_with_members)


if __name__ == '__main__':
    unittest.main()
