from abc import ABC, abstractmethod

from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink


class Table(ABC):
    MIN_TABLE_NUM = None
    MAX_TABLE_NUM = None
    TABLES_TYPE = None

    @abstractmethod
    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        if not self.MIN_TABLE_NUM <= value <= self.MAX_TABLE_NUM:
            raise ValueError(
                f"{self.TABLES_TYPE} table's number must be between {self.MIN_TABLE_NUM} and {self.MAX_TABLE_NUM} inclusive!")
        self.__table_number = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Capacity has to be greater than 0!")
        self.__capacity = value

    def reserve(self, number_of_people):
        # if not self.is_reserved and self.capacity >= number_of_people:
        self.number_of_people = number_of_people
        self.is_reserved = True

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        bill = sum([f.price for f in self.food_orders])
        bill += sum([d.price for d in self.drink_orders])
        return bill

    def clear(self):
        self.food_orders.clear()
        self.drink_orders.clear()
        self.number_of_people = 0
        self.is_reserved = False

    @property
    def table_type(self):
        return self.__class__.__name__

    def free_table_info(self):
        if not self.is_reserved:
            result = f"Table: {self.table_number}" \
                     f"\nType: {self.table_type}" \
                     f"\nCapacity: {self.capacity}"
            return result
