class Animal:
    def __init__(self, species):
        self.species = species


class SoundMakingAnimal(Animal):
    def __init__(self, animal_type, sound):
        super().__init__(animal_type)
        self.sound = sound

    def get_sound(self):
        return self.sound


def animal_sound(animals: list[SoundMakingAnimal]):
    for animal in animals:
        print(animal.get_sound())


animals = [
    SoundMakingAnimal('cat', 'meow'),
    SoundMakingAnimal('dog', 'woof-woof'),
    SoundMakingAnimal('chicken', 'pi-pi-pi'),
]
animal_sound(animals)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
