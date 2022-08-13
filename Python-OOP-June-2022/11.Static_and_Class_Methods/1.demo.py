class Person:
    def __init__(self,name):
        self.name = name

    @staticmethod
    def is_adult(age):
        return age >= 18