from abc import ABC, abstractmethod


class BaseDecoration(ABC):
    COMFORT = 0
    PRICE = 0

    @abstractmethod
    def __init__(self, comfort, price):
        self.comfort = comfort
        self.price = price

    @property
    def decoration_type(self):
        return self.__class__.__name__