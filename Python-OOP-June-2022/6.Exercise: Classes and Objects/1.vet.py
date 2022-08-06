

class Vet:
    animals = []
    space = 5

    def __init__(self, name):
        self.name = name
        self.animals = []

    def register_animal(self, animal_name):
        if Vet.space >= len(Vet.animals):
            self.animals.append(animal_name)
            Vet.animals.append(animal_name)
            return f"{animal_name} registered in the clinic"
        return "Not enough space"

    def unregister_animal(self, animal_name):
        if animal_name in Vet.animals and animal_name in self.animals:
            Vet.animals.remove(animal_name)
            self.animals.remove(animal_name)
            return f"{animal_name} unregistered successfully"
        return f"{animal_name} not in the clinic"

    def info(self):
        return f"{self.name} has {len(self.animals)} animals. {Vet.space - len(Vet.animals)} space left in clinic"


peter = Vet("Peter")
george = Vet("George")
print(peter.register_animal("Tom"))
print(george.register_animal("Cory"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))
print(george.register_animal("Kay"))

print(george.unregister_animal("Cory"))
print(peter.register_animal("Silky"))
print(peter.unregister_animal("Molly"))
print(peter.unregister_animal("Tom"))
print(peter.info())
print(george.info())


import unittest
from unittest import TestCase


class Tests(unittest.TestCase):
    def test_init(self):
        vet = Vet("Bob")
        Vet.animals = []
        Vet.space = 5
        self.assertEqual(vet.name, "Bob")
        self.assertEqual(vet.animals, [])
        self.assertEqual(Vet.animals, [])
        self.assertEqual(Vet.space, 5)

    def test_register_successfull(self):
        vet = Vet("Bob")
        Vet.animals = []
        Vet.space = 5
        vet2 = Vet("Peter")
        res = vet.register_animal("Doggy")
        self.assertEqual(res, "Doggy registered in the clinic")
        self.assertEqual(vet.animals, ["Doggy"])
        self.assertEqual(vet.animals, ["Doggy"])
        self.assertEqual(vet2.animals, [])

    def test_register_unsuccessfull(self):
        vet = Vet("Bob")
        Vet.animals = []
        Vet.space = 5
        for i in range(6):
            vet.register_animal(str(i))
        res = vet.register_animal("Doggy")
        self.assertEqual(res, "Not enough space")
        self.assertEqual(len(Vet.animals), 5)
        self.assertEqual(len(vet.animals), 5)

    def test_unregister_successfull(self):
        vet = Vet("Bob")
        Vet.animals = []
        Vet.space = 5
        vet.register_animal("Kitty")
        res = vet.unregister_animal("Kitty")
        self.assertEqual(res, "Kitty unregistered successfully")
        self.assertEqual(vet.animals, [])
        self.assertEqual(Vet.animals, [])


if __name__ == "__main__":
    unittest.main()