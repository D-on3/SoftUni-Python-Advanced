class Student:
    kind = 'human'

    def __init__(self,name):
        self.name = name


    #Changes permanent on evry other instance of the class
    @classmethod
    def change_kind(cls):
        cls.kind = "ULTRA"

        