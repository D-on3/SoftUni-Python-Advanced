class Student:
    kind = "human"


    def __init__(self,name):
        self.name = name
# overriding the kind
    @classmethod
    def change_kind(cls):
        cls.kind = "asd"


