from project2 import Food


class Fruit(Food):
    def __init__(self, name,expiration_date):
        super().__init__(self, expiration_date)
        self.name = name




#     def __str__(self):
#         return f"Product : {self.name} - Exp.Date {self.expiration_date}"
#
# apple = Fruit('Apple',"2/11/2012")
# print(apple)
