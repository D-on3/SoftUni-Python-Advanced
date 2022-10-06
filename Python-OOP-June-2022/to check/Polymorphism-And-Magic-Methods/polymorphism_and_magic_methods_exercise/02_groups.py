class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __add__(self, other):
        new_person = Person(self.name, other.surname)
        return new_person

    def __str__(self):
        return f"{self.name} {self.surname}"


class Group:
    def __init__(self, name, people):
        self.name = name
        self.people = people

    def __add__(self, other):
        new_group = Group(self.name+other.name, self.people+other.people)
        return new_group

    def __len__(self):
        return len(self.people)

    def __str__(self):
        members = ", ".join(f"{str(p.name)} {str(p.surname)}" for p in self.people)
        return f"Group {self.name} with members {members}"

    def __getitem__(self, index):
        return f"Person {index}: {self.people[index].name} {self.people[index].surname}"


p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2+p3

first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])
third_group = first_group+second_group

print(len(first_group))
print(second_group)
print(third_group[0])

for person in third_group:
    print(person)

# import unittest
#
#
# class TestGroups(unittest.TestCase):
#     def setUp(self):
#         self.p0 = Person('Aliko', 'Dangote')
#         self.p1 = Person('Bill', 'Gates')
#         self.p2 = Person('Warren', 'Buffet')
#         self.p3 = Person('Elon', 'Musk')
#
#     def test_person_init(self):
#         self.assertEqual(self.p0.name, 'Aliko')
#         self.assertEqual(self.p0.surname, 'Dangote')
#
#     def test_person_str(self):
#         self.assertEqual(str(self.p1), 'Bill Gates')
#
#     def test_person_add(self):
#         self.assertEqual(str(self.p2+self.p3), 'Warren Musk')
#
#     def test_group_init(self):
#         first_group = Group('__VIP__', [self.p0, self.p1, self.p2])
#         self.assertEqual(first_group.name, '__VIP__')
#         self.assertEqual(first_group.people, [self.p0, self.p1, self.p2])
#
#     def test_group_str(self):
#         first_group = Group('__VIP__', [self.p0, self.p1, self.p2])
#         self.assertEqual(str(first_group), "Group __VIP__ with members Aliko Dangote, Bill Gates, Warren Buffet")
#
#     def test_group_len(self):
#         first_group = Group('__VIP__', [self.p0, self.p1, self.p2])
#         self.assertEqual(len(first_group), 3)
#
#
# if __name__ == "__main__":
#     unittest.main()
