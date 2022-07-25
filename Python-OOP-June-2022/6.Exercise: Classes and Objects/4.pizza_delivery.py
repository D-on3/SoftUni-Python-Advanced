class PizzaDelivery:

    def __init__(self, name, price, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredients: str, quantity: int, price_per_quantity: float):

        if ingredients in self.ingredients:
            for product, price in self.ingredients.items():
                self.price += (abs(quantity - self.ingredients[ingredients]) * price_per_quantity)
        else:
            self.ingredients[ingredients] = quantity

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float):
        if not self.ordered:
            if ingredient not in self.ingredients:
                pass

    def make_order(self):

        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

        self.represent_list_all_items = ''

        for key, value in self.ingredients.items():
            self.represent_list_all_items += f"{key}: {value}, "

        self.ordered = True
        return f"You've ordered pizza {self.name} prepared with {self.represent_list_all_items} and the price will be {self.price}lv."


margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
margarita.add_extra('mozzarella', 1, 0.5)
margarita.add_extra('cheese', 1, 1)
margarita.remove_ingredient('cheese', 1, 1)
print(margarita.remove_ingredient('bacon', 1, 2.5))
print(margarita.remove_ingredient('tomatoes', 2, 0.5))
margarita.remove_ingredient('cheese', 2, 1)
print(margarita.make_order())
print(margarita.add_extra('cheese', 1, 1))
