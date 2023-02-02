from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        if food_type in ('Bread', 'Cake'):
            if self.__find_food_by_name(name):
                raise Exception(f"{food_type} {name} is already in the menu!")
            new_food = self.create_food(food_type, name, price)
            self.food_menu.append(new_food)
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        if drink_type in ('Tea', 'Water'):
            # if any(d.name == name for d in self.drinks_menu)
            if self.__find_drink_by_name(name):
                raise Exception(f"{drink_type} {name} is already in the menu!")
            new_drink = self.create_drink(drink_type, name, portion, brand)
            self.drinks_menu.append(new_drink)
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if table_type in ('InsideTable', 'OutsideTable'):
            if self.__find_table_by_number(table_number):
                raise Exception(f"Table {table_number} is already in the bakery!")
            new_table = self.create_table(table_type, table_number, capacity)
            self.tables_repository.append(new_table)
            return f"Added table number {table_number} in the bakery"

    def __find_free_table(self, people):
        for table in self.tables_repository:
            if not table.is_reserved and table.capacity >= people:
                return table

    def reserve_table(self, number_of_people: int):
        table = self.__find_free_table(number_of_people)
        if table:
            table.reserve(number_of_people)
            return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number, *food_names):
        table = self.__find_table_by_number(table_number)
        if table is None:
            return f"Could not find table {table_number}"

        ordered_food = f"Table {table_number} ordered:\n"
        non_existing_food = f"{self.name} does not have in the menu:\n"

        for food_name in food_names:
            food = self.__find_food_by_name(food_name)
            if food:
                ordered_food += f"{repr(food)}\n"
                table.order_food(food)
            else:
                non_existing_food += f"{food_name}\n"

        output = ordered_food + non_existing_food
        return output.strip()

    def order_drink(self, table_number, *drinks_names):
        table = self.__find_table_by_number(table_number)
        if table is None:
            return f"Could not find table {table_number}"

        ordered_drinks = f"Table {table_number} ordered:\n"
        non_existing_drinks = f"{self.name} does not have in the menu:\n"

        for drink_name in drinks_names:
            drink = self.__find_drink_by_name(drink_name)

            if drink is not None:
                ordered_drinks += f"{repr(drink)}\n"
                table.order_drink(drink)
            else:
                non_existing_drinks += f"{drink_name}\n"

        output = ordered_drinks + non_existing_drinks
        return output.strip()

    def leave_table(self, table_number: int):
        table = self.__find_table_by_number(table_number)
        if table:
            bill = table.get_bill()
            result = f"Table: {table_number}" + '\n'
            result += f"Bill: {bill:.2f}"
            self.total_income += bill
            table.clear()
            return result

    def get_free_tables_info(self):
        result = ''
        for table in self.tables_repository:
            if not table.is_reserved:
                result += table.free_table_info() + '\n'
        return result.strip()

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"

    @staticmethod
    def create_food(food_type, name, price):
        if food_type == 'Bread':
            return Bread(name, price)
        elif food_type == 'Cake':
            return Cake(name, price)

    @staticmethod
    def create_drink(drink_type, name, portion, brand):
        if drink_type == 'Tea':
            return Tea(name, portion, brand)
        elif drink_type == 'Water':
            return Water(name, portion, brand)

    @staticmethod
    def create_table(table_type, table_number, capacity):
        if table_type == 'InsideTable':
            return InsideTable(table_number, capacity)
        elif table_type == 'OutsideTable':
            return OutsideTable(table_number, capacity)

    def __find_food_by_name(self, name):
        for food in self.food_menu:
            if food.name == name:
                return food
        return None

    def __find_drink_by_name(self, name):
        for drink in self.drinks_menu:
            if drink.name == name:
                return drink
        return None

    def __find_table_by_number(self, number):
        for table in self.tables_repository:
            if table.table_number == number:
                return table
        return None

    # def __get_table_by_number(self, table_number: int) -> Table:
    #     try:
    #         found_table = next(table for table in self.tables_repository if table.table_number == table_number)
    #         return found_table
    #
