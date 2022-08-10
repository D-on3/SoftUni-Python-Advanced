from project.worker import Worker


class Vet(Worker):
    def __init__(elf, name, age, salary):
        super().__init__(name, age, salary)

