from abc import abstractmethod, ABC


class ADuck():

    def __str__(self):
        return "I am a duck"


class FlyingDuck(ABC, ADuck):
    @abstractmethod
    def fly(self):
        pass


class QuackingDuck(ABC, ADuck):

    @abstractmethod
    def quack(self):
        pass


class WalkingDuck(ABC, ADuck):
    @abstractmethod
    def walk(self):
        pass


class RubberDuck(QuackingDuck):

    def quack(self):
        return "Squeek"
    #
    # def walk(self):
    #     """Rubber duck can walk only if you move it"""
    #     return 'I cannot walk by myself'

    # def fly(self):
    #     """Rubber duck can fly only if you throw it"""
    #     return 'I cannot fly by myself'


class RobotDuck(FlyingDuck, WalkingDuck, QuackingDuck):
    def __init__(self):
        self.height = 50

    def quack(self):
        return 'Robotic quacking'

    def walk(self):
        return 'Robotic walking'

    def fly(self):
        return f"I can only fly to specific height of {self.height} m."


class WoodenDuck(ADuck):
    pass


wooden_d = WoodenDuck()
print(f'{wooden_d.__class__.__name__}: {wooden_d}')
robot_d = RobotDuck()
rubber_d = RubberDuck()
print(f'{robot_d.__class__.__name__}: {robot_d.fly()}')
print(f'{robot_d.__class__.__name__}: {robot_d.walk()}')
print(f'{rubber_d.__class__.__name__}: {robot_d.quack()}')
