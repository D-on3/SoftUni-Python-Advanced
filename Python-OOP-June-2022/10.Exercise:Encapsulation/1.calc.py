from functools import reduce

class Calculator:
    @staticmethod
    def add(*args):
        return reduce(lambda x, y: x + y, args)

    @staticmethod
    def multiply(*args):
        return reduce(lambda x, y: x * y, args)


    @staticmethod
    def devide(*args):
        return reduce(lambda x, y: x / y, args)

    @staticmethod
    def substract(*args):
        return reduce(lambda x,y: x-y , args)


